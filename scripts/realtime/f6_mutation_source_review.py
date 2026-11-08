#!/usr/bin/env python3
"""F6 source-level mutation/worker review queue for all 17 intermediate repos.

This pass is conservative by design: source-derived candidates and approximate
scope/group hints are *not* proof of 100% API coverage or approved ACLs.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import re

import yaml

GROUP = re.compile(r'\\bMapGroup\\s*\\(\\s*"([^"]+)"', re.S)
ROUTE = re.compile(r'\\bMap(Get|Post|Put|Patch|Delete|Methods)\\s*\\(\\s*"([^"]+)"', re.S)
SCOPE = re.compile(r'\\bRequire(?:Any)?Scope\\s*\\(([^)]{1,250})\\)')
AUTH = re.compile(r'\\bRequireAuthorization\\s*\\(')
SAVE = re.compile(r'\\b(?:SaveChanges(?:Async)?|Execute(?:Update|Delete)(?:Async)?|INSERT\\s+INTO|UPDATE\\s+\\w|DELETE\\s+FROM)\\b', re.I)
MUTATING = {"POST", "PUT", "PATCH", "DELETE"}
COLUMNS = [
    "repo", "serviceId", "kind", "sourceFile", "sourceLine", "verb",
    "routeSegment", "groupCandidates", "candidateAbsoluteRoute",
    "ownerByRepository", "scopeHintsFromFile", "authHintFromFile",
    "persistedMutationHintsFromFile", "sourceEvidence",
    "scopeReviewed", "fullRouteReviewed", "audienceReviewed",
    "outboxCoverageReviewed", "frontendConsumerReviewed", "recoveryTestReviewed",
    "formalStatus", "requiredAction"
]


def join(group: str, route: str) -> str:
    if not group:
        return "UNRESOLVED_GROUP/" + route.lstrip("/")
    return "/" + "/".join(
        piece.strip("/") for piece in (group, route) if piece.strip("/"))


def inspect(text: str, segment: str, verb: str, line_index: int) -> dict:
    groups = list(dict.fromkeys(GROUP.findall(text)))
    # If many groups are declared in a file, do not invent exact association.
    absolute = join(groups[0], segment) if len(groups) == 1 else "UNRESOLVED_GROUP/" + segment.lstrip("/")
    return {
        "sourceLine": line_index,
        "routeSegment": segment,
        "groupCandidates": ";".join(groups[:20]),
        "candidateAbsoluteRoute": absolute,
        "scopeHintsFromFile": ";".join(dict.fromkeys(
            g.group(1).replace("\n", " ").strip() for g in SCOPE.finditer(text)))[:900],
        "authHintFromFile": "AUTH_PRESENT_UNASSOCIATED" if AUTH.search(text)
            else "NO_DIRECT_AUTH_DECLARATION_FOUND",
        "persistedMutationHintsFromFile": "PERSISTENCE_CALL_FOUND_IN_FILE" if SAVE.search(text)
            else "PERSISTENCE_CALL_NOT_FOUND_IN_FILE",
        "sourceEvidence": "route source file, line and inferred group; NOT security validation",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default="F0Results/working")
    parser.add_argument("--manifest", default="docs/realtime/release-manifest.yaml")
    parser.add_argument("--output", default="F0Results")
    args = parser.parse_args()
    meta = yaml.safe_load(Path(args.manifest).read_text())
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    rows: list[dict] = []
    missing_repos = []
    counts = Counter()
    repos = meta["repositories"]
    assert len(repos) == 17
    for record in repos:
        name = record["name"]
        repopath = Path(args.workspace) / name.split("/")[-1]
        if not repopath.exists():
            missing_repos.append(name)
            continue
        service = str(record["id"])
        for source in sorted(repopath.rglob("*.cs")):
            if "src" not in source.parts and "Dhole.ApiGateway" not in source.parts:
                continue
            if any(p in {"obj", "bin", "node_modules", ".git"} for p in source.parts):
                continue
            text = source.read_text(encoding="utf-8-sig", errors="replace")
            rel = str(source.relative_to(repopath))
            scopes = inspect(text, "", "", 0)
            for match in ROUTE.finditer(text):
                verb = match.group(1).upper()
                if verb not in MUTATING and verb != "METHODS":
                    continue
                part = match.group(2)
                line = text.count("\n", 0, match.start()) + 1
                hints = inspect(text, part, verb, line)
                rows.append({
                    "repo": name, "serviceId": service, "kind": "MUTABLE_HTTP_CANDIDATE",
                    "sourceFile": rel, "verb": verb, **hints,
                    "ownerByRepository": service,
                    "scopeReviewed": "NO", "fullRouteReviewed": "NO",
                    "audienceReviewed": "NO", "outboxCoverageReviewed": "NO",
                    "frontendConsumerReviewed": "NO", "recoveryTestReviewed": "NO",
                    "formalStatus": "UNVERIFIED",
                    "requiredAction": "Reviewer must link verb/path, transaction, explicit scope, audience, authorized GET, view and test"
                })
                counts[service] += 1
            # Reuse worker candidates from F0 rather than broadening with file
            # names like *Job.cs which may be only DTOs. Keep candidates honest.
    existing = output / "F0-worker-candidates.csv"
    if existing.exists():
        with existing.open(newline="", encoding="utf-8") as f:
            for worker in csv.DictReader(f):
                rows.append({
                    "repo": worker["repo"],
                    "serviceId": next((str(x["id"]) for x in repos if x["name"] == worker["repo"]), "UNKNOWN"),
                    "kind": "WORKER_HANDLER_CANDIDATE",
                    "sourceFile": worker["file"], "sourceLine": "",
                    "verb": "", "routeSegment": "", "groupCandidates": "",
                    "candidateAbsoluteRoute": "",
                    "ownerByRepository": worker["repo"],
                    "scopeHintsFromFile": "N/A", "authHintFromFile": "N/A",
                    "persistedMutationHintsFromFile": "SEE_WORKER_SOURCE",
                    "sourceEvidence": "worker candidate identified by F0 scanner; verify whether it mutates",
                    "scopeReviewed": "NO", "fullRouteReviewed": "NO",
                    "audienceReviewed": "NO", "outboxCoverageReviewed": "NO",
                    "frontendConsumerReviewed": "NO", "recoveryTestReviewed": "NO",
                    "formalStatus": "UNVERIFIED", "requiredAction": "Review worker mutation, idempotency, event publication and consuming view",
                })
                counts["workers"] += 1
    if missing_repos:
        raise SystemExit(f"Missing cloned intermediate repositories: {missing_repos}")
    rows.sort(key=lambda r: (r["repo"], r["sourceFile"], str(r["sourceLine"])))
    with (output / "F6-source-mutation-review.csv").open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        writer.writerows(rows)
    report = {
        "releaseId": "rt-20261107-01",
        "phase": "F6",
        "repoCount": len(repos),
        "serviceCount": 13,
        "sourceRows": len(rows),
        "workerCandidates": counts["workers"],
        "mutableHttpCandidates": len(rows) - counts["workers"],
        "sourceCountsByService": {k: v for k, v in sorted(counts.items()) if k != "workers"},
        "unverifiedCandidates": len(rows),
        "fullyVerifiedCandidates": 0,
        "formalF6Approved": False,
        "sourceInventoryIsNotRuntimeAuthorizationProof": True,
        "readOnly": True,
        "notes": "Scope/group inference is file-level and not an attestation. C# dynamic routes may be absent."
    }
    (output / "F6-source-review-report.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8")
    assert len(rows) > 0 and report["fullyVerifiedCandidates"] == 0
    print(f"F6_SOURCE_REVIEW_QUEUE repos=17 candidates={len(rows)} "
          f"mutable={report['mutableHttpCandidates']} workers={counts['workers']} "
          "all UNVERIFIED, no formal gate")


if __name__ == "__main__":
    main()
