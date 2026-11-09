#!/usr/bin/env python3
"""F0/F6 fail-closed reconciliation of source signatures against reviewed evidence.

This is a candidate-signature register, NOT a unique count of real business
mutations. Evidence on a different commit SHA cannot approve current source.
The tool does not change refs, staging, flags or formal gate approvals.
"""
from __future__ import annotations

import argparse
from collections import Counter
import csv
from hashlib import sha256
import json
from pathlib import Path
import re
import sys

RELEASE_ID = "rt-20261107-01"
FIELDS = ("sourceKey", "sourceSha", "status", "reviewer", "reviewedAtUtc",
          "resourceOwner", "effectiveRouteOrJob", "authorizationPolicy",
          "eventContract", "audience", "frontendConsumer", "restReconcile",
          "integrationTest", "evidenceUrl", "exceptionReason", "approvedBy",
          "approvalEvidence")
REVIEW_FIELDS = ("reviewer", "reviewedAtUtc", "resourceOwner",
                 "effectiveRouteOrJob", "approvedBy", "approvalEvidence")
IMPLEMENTED_FIELDS = ("authorizationPolicy", "eventContract", "audience",
                      "frontendConsumer", "restReconcile", "integrationTest",
                      "evidenceUrl")
EXEMPT_FIELDS = ("exceptionReason",)
HEX40 = re.compile(r"^[0-9a-f]{40}$")
OUTPUT_FIELDS = ("sourceKey", "sourceSha", "repo", "kind", "sourceFile",
                 "sourceLine", "verb", "routeSegmentOrHint", "origin",
                 "possibleSameFileOverlap", "reviewStatus", "reviewer",
                 "reviewEvidence")


def load_csv(path: Path) -> list[dict]:
    if not path.is_file():
        raise FileNotFoundError("Required F0 input absent: " + str(path))
    with path.open(newline="", encoding="utf-8-sig") as stream:
        reader = csv.DictReader(stream)
        if not reader.fieldnames:
            raise ValueError("CSV header missing: " + str(path))
        return list(reader)


def signature(row: dict, origin: str) -> dict:
    repo = (row.get("repo") or "").strip()
    source_file = (row.get("sourceFile") or "").replace("\\", "/").strip()
    kind = (row.get("kind") or "").strip()
    line = str(row.get("sourceLine") or row.get("line") or "").strip()
    verb = (row.get("verb") or "").strip().upper()
    route = (row.get("routeSegment") or row.get("sourceHint") or "").strip()
    if not repo or not source_file or not kind:
        raise ValueError("Candidate has no repo, sourceFile or kind")
    fingerprint = "\x1f".join((repo, source_file, origin, kind, line, verb, route))
    return {
        "sourceKey": sha256(fingerprint.encode("utf-8")).hexdigest()[:24],
        "sourceSha": "", "repo": repo, "kind": kind,
        "sourceFile": source_file, "sourceLine": line, "verb": verb,
        "routeSegmentOrHint": route, "origin": origin,
        "possibleSameFileOverlap": "NO", "reviewStatus": "UNVERIFIED",
        "reviewer": "", "reviewEvidence": "",
    }


def reconcile(base: list[dict], additional: list[dict],
              heads: list[dict], decisions: list[dict]) -> tuple[list[dict], list[str]]:
    errors: list[str] = []
    sha_by_repo: dict[str, str] = {}
    for head in heads:
        repo = (head.get("repo") or "").strip()
        sha = (head.get("shaAtScan") or "").lower().strip()
        if repo in sha_by_repo:
            errors.append("Duplicate source head: " + repo)
        if not HEX40.fullmatch(sha):
            errors.append("Invalid scan SHA for " + repo)
        sha_by_repo[repo] = sha

    base_files = {(r.get("repo"), r.get("sourceFile")) for r in base}
    collected: dict[str, dict] = {}
    for origin, source_rows in (("F6_PRIMARY", base), ("F0_ADDITIONAL", additional)):
        for source in source_rows:
            try:
                entry = signature(source, origin)
            except ValueError as exc:
                errors.append(str(exc))
                continue
            if entry["sourceKey"] in collected:
                errors.append("Duplicate candidate signature: " + entry["sourceKey"])
                continue
            if entry["repo"] not in sha_by_repo:
                errors.append("No scanned branch SHA for " + entry["repo"])
            entry["sourceSha"] = sha_by_repo.get(entry["repo"], "")
            if origin == "F0_ADDITIONAL" and (entry["repo"], entry["sourceFile"]) in base_files:
                entry["possibleSameFileOverlap"] = "YES_NOT_AUTO_DEDUPLICATED"
            collected[entry["sourceKey"]] = entry

    seen_decisions: set[str] = set()
    for decision in decisions:
        key = (decision.get("sourceKey") or "").strip()
        if key in seen_decisions:
            errors.append("Duplicate review decision for " + key)
            continue
        seen_decisions.add(key)
        entry = collected.get(key)
        if entry is None:
            errors.append("Unknown or stale sourceKey: " + key)
            continue
        sha = (decision.get("sourceSha") or "").lower().strip()
        if sha != entry["sourceSha"] or not HEX40.fullmatch(sha):
            errors.append("STALE_SHA review: " + key)
            continue
        status = (decision.get("status") or "").strip().upper()
        required = REVIEW_FIELDS + (IMPLEMENTED_FIELDS if status == "VALIDATED"
                                    else EXEMPT_FIELDS if status == "EXEMPT" else ())
        if status not in {"VALIDATED", "EXEMPT"}:
            errors.append("Unsupported decision status for " + key)
            continue
        absent = [field for field in required if not (decision.get(field) or "").strip()]
        if absent:
            errors.append("Missing review evidence for " + key + ": " + ", ".join(absent))
            continue
        if not (decision.get("approvalEvidence") or "").startswith("https://"):
            errors.append("Unlinkable approval evidence for " + key)
            continue
        if status == "VALIDATED" and not (decision.get("evidenceUrl") or "").startswith("https://"):
            errors.append("Unlinkable test evidence for " + key)
            continue
        entry["reviewStatus"] = "EVIDENCE_SUBMITTED_" + status
        entry["reviewer"] = decision["reviewer"]
        entry["reviewEvidence"] = decision["approvalEvidence"]

    return sorted(collected.values(),
                  key=lambda e: (e["repo"], e["sourceFile"], e["sourceLine"],
                                 e["sourceKey"])), errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="F0Results")
    parser.add_argument("--decisions", default="docs/realtime/F0-approved-source-decisions.csv")
    parser.add_argument("--output", default="F0Results")
    parser.add_argument("--require-all", action="store_true")
    args = parser.parse_args()
    src, out = Path(args.input), Path(args.output)
    try:
        primary = load_csv(src / "F6-source-mutation-review.csv")
        gaps = load_csv(src / "F0-additional-source-gaps.csv")
        heads = load_csv(src / "F0-branch-heads.csv")
        decisions = load_csv(Path(args.decisions))
        rows, errors = reconcile(primary, gaps, heads, decisions)
    except (FileNotFoundError, ValueError) as exc:
        print("F0_RECONCILIATION_INPUT_ERROR:", exc, file=sys.stderr)
        return 2
    out.mkdir(parents=True, exist_ok=True)
    with (out / "F0-unified-source-review.csv").open("w", newline="", encoding="utf-8") as stream:
        writer = csv.DictWriter(stream, fieldnames=OUTPUT_FIELDS)
        writer.writeheader()
        writer.writerows(rows)
    counts = Counter(r["reviewStatus"] for r in rows)
    unresolved = counts["UNVERIFIED"]
    report = {
        "releaseId": RELEASE_ID,
        "primaryCandidateSignatures": len(primary),
        "additionalCandidateSignatures": len(gaps),
        "consolidatedSourceSignatures": len(rows),
        "mayOverlapAsBusinessMutations": True,
        "sameFileOverlapHints": sum(r["possibleSameFileOverlap"] != "NO" for r in rows),
        "evidenceSubmitted": len(rows) - unresolved,
        "unverifiedSourceSignatures": unresolved,
        "reviewErrors": errors,
        "byRepository": dict(sorted(Counter(r["repo"] for r in rows).items())),
        "formalF0Approved": False,
        "formalF6Approved": False,
        "sourceSignaturesDoNotCertifyRealRuntimeCoverage": True,
        "readonly": True,
    }
    (out / "F0-unified-source-summary.json").write_text(
        json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("F0_SOURCE_RECONCILIATION:", len(rows), "source signatures;",
          unresolved, "unverified;", len(errors), "invalid reviews; formal gates BLOCKED")
    for error in errors:
        print("REVIEW_ERROR:", error, file=sys.stderr)
    if errors or not rows or (args.require_all and unresolved):
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
