#!/usr/bin/env python3
"""Dhole Realtime F0 read-only source audit. Never merges, writes refs or deploys."""
from __future__ import annotations

import argparse
import csv
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

import yaml

HEX_SHA = re.compile(r"^[0-9a-f]{40}$")
ROUTE = re.compile(r'\bMap(Get|Post|Put|Patch|Delete|Methods)\s*\(\s*"([^"]+)"', re.M | re.S)
GROUP = re.compile(r'\bMapGroup\s*\(\s*"([^"]+)"', re.M | re.S)
WORKER = re.compile(r'\b(BackgroundService|IHostedService|ExecuteAsync|ProcessAsync|IStreamEventHandler|IIntegrationEventHandler|Quartz|Hangfire)\b')
MUTATING = {"POST", "PUT", "PATCH", "DELETE"}
REQUIRED_SERVICES = {f"S{i:02d}" for i in range(1, 14)}
BRANCH_PREFIX = "feature/dhole-realtime-universal-"


def check_manifest(manifest: dict) -> list[str]:
    errors: list[str] = []
    release = manifest.get("releaseId", "")
    policy = manifest.get("branchPolicy", {})
    branch = policy.get("intermediate", "")
    records = manifest.get("repositories", [])
    if release != "rt-20261107-01":
        errors.append("releaseId mismatch")
    if branch != BRANCH_PREFIX + release:
        errors.append("intermediate branch naming mismatch")
    if {r.get("id") for r in records if re.fullmatch(r"S\d\d", str(r.get("id", "")))} != REQUIRED_SERVICES:
        errors.append("missing or duplicated service identifiers S01-S13")
    names = [r.get("name") for r in records]
    if len(names) != len(set(names)) or len(names) != 17:
        errors.append(f"expected 17 unique repositories, got {len(names)}")
    if not policy.get("forbidDirectTargetWrites") or not policy.get("forbidMainChanges") or not policy.get("forbidForcePush"):
        errors.append("immutable target policy absent")
    if policy.get("masterRequiresExplicitAuthorization") is not True:
        errors.append("master authorization gate absent")
    if manifest.get("phase") in ("F0", "F1"):
        promo = manifest.get("promotion", {})
        if promo.get("developPRs") or promo.get("masterPRs"):
            errors.append("premature release PRs")
        if promo.get("stagingDeployed") or promo.get("productionDeployed"):
            errors.append("premature deploy")
        if promo.get("frozen"):
            errors.append("release frozen before F9")
        for r in records:
            if r.get("developBatchPR") or r.get("masterBatchPR"):
                errors.append(f"premature repo PR: {r.get('name')}")
            if (r.get("flags") or {}).get("realtime") is not False:
                errors.append(f"realtime flag not OFF: {r.get('name')}")
    for r in records:
        if not isinstance(r.get("name"), str) or not r["name"].startswith("CustomCodeCR/"):
            errors.append("invalid repo owner")
        if r.get("intermediateBranch") != branch or not r.get("intermediateCreated"):
            errors.append(f"missing intermediate branch: {r.get('name')}")
        for field in ("baseSha", "developBaselineSha", "masterBaselineSha", "initialIntermediateSha"):
            if not HEX_SHA.fullmatch(str(r.get(field) or "")):
                errors.append(f"bad {field}: {r.get('name')}")
    return errors


def run_git(args: list[str], *, cwd: Path | None = None) -> str:
    result = subprocess.run(
        ["git", *args], cwd=cwd, text=True, capture_output=True,
        check=False, timeout=180)
    if result.returncode != 0:
        raise RuntimeError(f"git command failed (exit {result.returncode}): {args[0]}; {result.stderr[:250]}")
    return result.stdout.strip()


def write_csv(path: Path, rows: list[dict], columns: list[str]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=columns, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def scan_service(repo: str, directory: Path) -> tuple[list[dict], list[dict], list[dict]]:
    routes: list[dict] = []
    jobs: list[dict] = []
    frontend: list[dict] = []
    src = directory / "src"
    if not src.is_dir():
        src = directory / "Dhole.ApiGateway"
    if src.is_dir():
        for path in src.rglob("*.cs"):
            if any(piece in ("bin", "obj") for piece in path.parts):
                continue
            text = path.read_text(encoding="utf-8-sig", errors="replace")
            relative = str(path.relative_to(directory))
            group_prefixes = ";".join(GROUP.findall(text)[:12])
            for match in ROUTE.finditer(text):
                verb = match.group(1).upper()
                routes.append({
                    "repo": repo, "file": relative, "verb": verb,
                    "routeSegment": match.group(2), "groupCandidates": group_prefixes,
                    "mutation": str(verb in MUTATING).lower(),
                    "status": "CANDIDATE_REQUIRES_FULL_ROUTE_AUTH_OWNERSHIP_UI_VALIDATION",
                })
            if WORKER.search(text) and (
                re.search(r"(/Workers/|/Streams/|/Outbox/|/Inbox/|Job|Worker|Handler)", relative, re.I)
            ):
                jobs.append({
                    "repo": repo, "file": relative, "kind": "BACKGROUND_OR_EVENT_HANDLER",
                    "status": "CANDIDATE_REQUIRES_MUTATION_AND_UI_IMPACT_REVIEW"
                })
    if repo.endswith("DholeWeb"):
        root = directory / "src"
        if root.is_dir():
            for path in root.rglob("*.ts"):
                if "node_modules" in path.parts:
                    continue
                txt = path.read_text(encoding="utf-8-sig", errors="replace")
                if "fetchClient" in txt or "fetch(" in txt or "axios" in txt:
                    frontend.append({
                        "repo": repo, "file": str(path.relative_to(directory)),
                        "kind": "REST_CLIENT_CANDIDATE", "status": "REQUIRES_VIEW_MAPPING"
                    })
    return routes, jobs, frontend


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--manifest", default="docs/realtime/release-manifest.yaml")
    parser.add_argument("--output", default="F0Results")
    parser.add_argument("--scan", action="store_true", help="Clones only intermediate branches; requires GitHub access")
    args = parser.parse_args()

    with Path(args.manifest).open(encoding="utf-8") as f:
        manifest = yaml.safe_load(f)
    errors = check_manifest(manifest)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    report = {
        "releaseId": manifest.get("releaseId"),
        "source": "GitHub intermediate branch checkout",
        "repoCount": len(manifest.get("repositories", [])),
        "manifestPolicyErrors": errors,
        "fullEndpointCoverageProven": False,
        "runtimeInfrastructureVerified": False,
        "gateF0Approved": False,
        "notes": ["Static extraction is candidate discovery, not evidence of full business coverage."],
    }
    if errors:
        (output / "F0-policy-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
        print("BLOCKED: " + "; ".join(errors), file=sys.stderr)
        return 1
    print("PASS: manifest branch policy and 17-repo registry shape")
    if not args.scan:
        (output / "F0-policy-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
        return 0

    branch = manifest["branchPolicy"]["intermediate"]
    workspace = output / "working"
    workspace.mkdir(parents=True, exist_ok=True)
    rows: list[dict] = []
    routes: list[dict] = []
    jobs: list[dict] = []
    frontend: list[dict] = []
    for record in manifest["repositories"]:
        name = record["name"]
        target = workspace / name.split("/")[-1]
        if target.exists():
            shutil.rmtree(target)
        run_git(["clone", "--depth", "1", "--single-branch", "--branch", branch,
                 f"https://github.com/{name}.git", str(target)])
        sha = run_git(["rev-parse", "HEAD"], cwd=target)
        candidate_sha = record.get("candidateF1HeadSha")
        rows.append({
            "repo": name, "intermediateBranch": branch, "shaAtScan": sha,
            "initialBaselineSha": record["initialIntermediateSha"],
            "matchesInitialBaseline": str(sha == record["initialIntermediateSha"]).lower(),
            "matchesF1CandidateSha": str(sha == candidate_sha).lower() if candidate_sha else "n/a",
            "source": "git clone --depth 1 (read-only)"
        })
        rr, jj, ff = scan_service(name, target)
        routes.extend(rr)
        jobs.extend(jj)
        frontend.extend(ff)
        print(f"SCAN {name} {sha[:12]}: routes={len(rr)} workers={len(jj)} frontend={len(ff)}")
    write_csv(output / "F0-branch-heads.csv", rows,
              ["repo", "intermediateBranch", "shaAtScan", "initialBaselineSha",
               "matchesInitialBaseline", "matchesF1CandidateSha", "source"])
    write_csv(output / "F0-route-candidates.csv", routes,
              ["repo", "file", "verb", "routeSegment", "groupCandidates", "mutation", "status"])
    write_csv(output / "F0-worker-candidates.csv", jobs,
              ["repo", "file", "kind", "status"])
    write_csv(output / "F0-frontend-api-candidates.csv", frontend,
              ["repo", "file", "kind", "status"])

    # Every potential mutation/worker remains explicitly unapproved until its
    # absolute route, owner, auth scope, event, UI consumer and test are mapped.
    # This is a full exception/gap register, NOT a false 100% coverage claim.
    unresolved: list[dict] = []
    for route in routes:
        if route["mutation"] != "true" and route["verb"] != "METHODS":
            continue
        unresolved.append({
            "repository": route["repo"], "sourceFile": route["file"],
            "kind": "MUTABLE_HTTP_CANDIDATE", "verb": route["verb"],
            "routeCandidate": route["routeSegment"],
            "groupCandidates": route["groupCandidates"],
            "resourceOwner": "PENDING_HUMAN_REVIEW",
            "authorizationScope": "PENDING_HUMAN_REVIEW",
            "outboxOrApprovedException": "PENDING_HUMAN_REVIEW",
            "audiencePolicy": "PENDING_HUMAN_REVIEW",
            "frontendConsumer": "PENDING_HUMAN_REVIEW",
            "reconciliationTest": "PENDING_HUMAN_REVIEW",
            "gate": "BLOCKED"
        })
    for job in jobs:
        unresolved.append({
            "repository": job["repo"], "sourceFile": job["file"],
            "kind": "WORKER_HANDLER_CANDIDATE", "verb": "",
            "routeCandidate": "", "groupCandidates": "",
            "resourceOwner": "PENDING_HUMAN_REVIEW",
            "authorizationScope": "PENDING_HUMAN_REVIEW",
            "outboxOrApprovedException": "PENDING_HUMAN_REVIEW",
            "audiencePolicy": "PENDING_HUMAN_REVIEW",
            "frontendConsumer": "PENDING_HUMAN_REVIEW",
            "reconciliationTest": "PENDING_HUMAN_REVIEW",
            "gate": "BLOCKED"
        })
    coverage_fields = ["repository", "sourceFile", "kind", "verb",
                       "routeCandidate", "groupCandidates", "resourceOwner",
                       "authorizationScope", "outboxOrApprovedException",
                       "audiencePolicy", "frontendConsumer",
                       "reconciliationTest", "gate"]
    write_csv(output / "F0-unresolved-gate-items.csv", unresolved, coverage_fields)
    unresolved_by_repo = {
        r["name"]: sum(1 for x in unresolved if x["repository"] == r["name"])
        for r in manifest["repositories"]
    }
    report.update({
        "unresolvedTotal": len(unresolved),
        "unresolvedMutations": sum(x["kind"] == "MUTABLE_HTTP_CANDIDATE"
                                   for x in unresolved),
        "unresolvedWorkers": sum(x["kind"] == "WORKER_HANDLER_CANDIDATE"
                                 for x in unresolved),
        "unresolvedByRepository": unresolved_by_repo,
        "gateF0Approved": False,
        "gateF0Blocker": "Runtime baseline, ownership, auth scopes and complete route/worker mappings missing"
    })
    report.update({
        "reposCloned": len(rows), "routeCandidates": len(routes),
        "mutableRouteCandidates": sum(x["mutation"] == "true" for x in routes),
        "workerCandidates": len(jobs),
        "frontendApiCandidates": len(frontend),
        "status": "SOURCE_DISCOVERY_COMPLETED_GATES_PENDING"
    })
    (output / "F0-policy-report.json").write_text(json.dumps(report, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
