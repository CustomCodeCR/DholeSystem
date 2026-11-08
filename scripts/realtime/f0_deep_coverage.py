#!/usr/bin/env python3
"""Additive F0 gap scan for mutation conventions missed by literal MapPost regex.

This is an *unverified* candidate queue. Not an endpoint count attestation or
an excuse to approve the formal F0/F6 gate. It never changes cloned repos.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
import json
from pathlib import Path
import re

import yaml

CALL = re.compile(r'\bMap(?:Post|Put|Patch|Delete|Methods)\s*\(', re.S)
LITERAL = re.compile(r'\bMap(?:Post|Put|Patch|Delete|Methods)\s*\(\s*"[^"]+"', re.S)
ATTR = re.compile(r'\[\s*Http(?:Post|Put|Patch|Delete)\b', re.I)
PROTO = re.compile(r'\b(?:MapGraphQL|MapGrpcService|AddGraphQLServer)\s*[<(]', re.I)
WORKER = re.compile(r'\bclass\s+([A-Za-z]\w*)[^{;]*:\s*[^{;]*\b(?:BackgroundService|IHostedService)\b', re.S)
ENDPOINT_REGISTRATION = re.compile(r'\bMapControllers\s*\(', re.S)
MAX_CONTEXT = 100

FIELDS = ["repo", "serviceId", "sourceFile", "line", "kind", "sourceHint",
          "status", "requiredReview"]


def inspect_source(name: str, ident: str, root: Path) -> list[dict]:
    rows: list[dict] = []
    search_root = root / "src"
    if not search_root.is_dir():
        search_root = root / "Dhole.ApiGateway"
    if not search_root.is_dir():
        return rows
    for path in sorted(search_root.rglob("*.cs")):
        if any(p in {"bin", "obj", ".git", "node_modules"} for p in path.parts):
            continue
        source = path.read_text(encoding="utf-8-sig", errors="replace")
        relative = path.relative_to(root).as_posix()
        literal_starts = {m.start() for m in LITERAL.finditer(source)}
        categories = (
            ("DYNAMIC_MUTABLE_ROUTE", CALL,
             "Nonliteral route/MapMethods: resolve HTTP verbs, path, ACL and Outbox"),
            ("ASP_CONTROLLER_MUTATION", ATTR,
             "Resolve controller route attribute, action, permissions and Outbox"),
            ("GRAPHQL_GRPC_PROTOCOL", PROTO,
             "Resolve schema/method mutations and dedicated transport policy"),
            ("HOSTED_WORKER_CLASS", WORKER,
             "Review durable worker side effects, idempotency and audience"),
            ("CONTROLLER_DISCOVERY", ENDPOINT_REGISTRATION,
             "Find actual MVC controllers and authorize each mutable action"),
        )
        for kind, pattern, review in categories:
            for hit in pattern.finditer(source):
                if kind == "DYNAMIC_MUTABLE_ROUTE" and hit.start() in literal_starts:
                    continue
                line = source.count("\n", 0, hit.start()) + 1
                hint = source[hit.start():hit.start()+MAX_CONTEXT].splitlines()[0]
                rows.append({
                    "repo": name, "serviceId": ident,
                    "sourceFile": relative, "line": line,
                    "kind": kind, "sourceHint": hint,
                    "status": "UNVERIFIED",
                    "requiredReview": review
                })
    return rows


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--workspace", default="F0Results/working")
    parser.add_argument("--manifest", default="docs/realtime/release-manifest.yaml")
    parser.add_argument("--output", default="F0Results")
    args = parser.parse_args()
    manifest = yaml.safe_load(Path(args.manifest).read_text())
    assert manifest["releaseId"] == "rt-20261107-01"
    assert len(manifest["repositories"]) == 17
    rows: list[dict] = []
    for repo in manifest["repositories"]:
        name = repo["name"]
        root = Path(args.workspace) / name.split("/")[-1]
        if not root.is_dir():
            raise RuntimeError("Missing checked-out intermediate repo " + name)
        rows += inspect_source(name, repo["id"], root)
    counts = Counter(row["kind"] for row in rows)
    output = Path(args.output)
    output.mkdir(parents=True, exist_ok=True)
    with (output/"F0-additional-source-gaps.csv").open("w", newline="", encoding="utf-8") as stream:
        csv_writer = csv.DictWriter(stream, fieldnames=FIELDS)
        csv_writer.writeheader()
        csv_writer.writerows(rows)
    report = {
        "releaseId": "rt-20261107-01",
        "repositoriesScanned": 17,
        "additionalSignaturesFound": len(rows),
        "countsBySignature": dict(sorted(counts.items())),
        "sourceCandidatesAutoApproved": 0,
        "reviewStatus": "UNVERIFIED",
        "includesPotentialDuplicatesOf580ExistingCandidates": True,
        "noDeployment": True,
        "noBranchWrites": True,
        "notes": "This triage extends the previous 510 literal routes + 70 worker files. "
                 "It may overlap or contain false positives. Do NOT add counts as distinct mutations.",
    }
    (output/"F0-additional-source-gaps.json").write_text(json.dumps(report, indent=2)+"\n")
    print("F0_DEEP_SOURCE_GAPS: 17 repos, additional signatures=" + str(len(rows))
          + ", categories=" + str(dict(counts))
          + ", approved=0; NOT a deduplicated new endpoint count")


if __name__ == "__main__":
    main()
