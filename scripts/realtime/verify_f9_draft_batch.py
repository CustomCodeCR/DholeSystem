#!/usr/bin/env python3
"""F9 draft PR inventory validation, never authorizes promotion."""
import argparse
import re
from pathlib import Path
import sys
import yaml

RELEASE = "rt-20261107-01"


def inspect(manifest, roster):
    if manifest.get("releaseId") != RELEASE or roster.get("releaseId") != RELEASE:
        raise ValueError("Invalid F9 release identity")
    entries = roster.get("pullRequests", [])
    expected = {item["name"] for item in manifest["repositories"]}
    actual = [entry["repository"] for entry in entries]
    if len(entries) != 17 or set(actual) != expected or len(set(actual)) != 17:
        raise ValueError("F9 must contain one and only one draft PR for each of 17 repos")
    if roster.get("targetBranch") != "develop" or roster.get("sourceBranch") != (
        "feature/dhole-realtime-universal-rt-20261107-01"
    ):
        raise ValueError("F9 target/source branch mismatch")
    for entry in entries:
        number = entry["number"]
        expected_url = f"https://github.com/{entry['repository']}/pull/{number}"
        if not isinstance(number, int) or number < 1 or entry["url"] != expected_url:
            raise ValueError("Invalid GitHub F9 PR URL")
        if entry.get("state") != "DRAFT" or entry.get("mergeAuthorized") is not False:
            raise ValueError("A draft is not a release approval")
    if any(roster.get(field) is not False for field in (
        "mergeAuthorized", "formalF9Complete", "sourceGatesF0ToF8Approved",
        "all17FinalShasFrozen", "stagingValidated"
    )):
        raise ValueError("Draft phase must not claim approvals")
    if manifest["promotion"].get("developPRs") != []:
        raise ValueError("No develop PR has been merged or accepted in F9")
    return len(entries)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--manifest", default="docs/realtime/release-manifest.yaml")
    p.add_argument("--roster", default="docs/realtime/f9-draft-prs.yaml")
    args = p.parse_args()
    try:
        count = inspect(yaml.safe_load(Path(args.manifest).read_text()),
                        yaml.safe_load(Path(args.roster).read_text()))
    except (OSError, KeyError, TypeError, ValueError, yaml.YAMLError) as exc:
        print("F9_DRAFT_BATCH_BLOCKED:", exc, file=sys.stderr)
        return 2
    print(f"F9_DRAFT_BATCH_READY_FOR_REVIEW_ONLY: {count} draft PRs; no approval, no merges")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
