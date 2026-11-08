#!/usr/bin/env python3
"""F10 production deployment preflight; fail closed until F9 is verified.

Read-only; no network, no credentials. Designed to run as the FIRST
post-checkout step of DholeSystem's automatic master production workflow.
"""
import argparse
import json
import os
from pathlib import Path
import sys

RELEASE = "rt-20261107-01"
REQUIRED = (
    "productionRequestedByUser",
    "f0ToF8FormalApproved",
    "all17DevelopPrsMerged",
    "all17ComponentVersionsVerified",
    "finalShasFrozenAndCiGreen",
    "f9StagingAll14ChaosPassed",
    "f9StagingRedisAofAndRestorationVerified",
    "f9RollbackDrillVerified",
    "f9ApprovalGranted",
    "f10SameReleaseShaProven",
    "f10ProductionDeploymentAuthorized",
)


def verify(data, git_ref, repository):
    if data.get("schemaVersion") != 1 or data.get("releaseId") != RELEASE:
        raise ValueError("Missing or mismatched realtime production release attestation")
    if data.get("targetBranch") != "master" or git_ref != "master":
        raise ValueError("Production deployment is permitted only from master")
    if repository != "CustomCodeCR/DholeSystem":
        raise ValueError("Unexpected GitHub repository for production approval")
    missing = [field for field in REQUIRED if data.get(field) is not True]
    if missing:
        raise ValueError("F10 refuses deployment: unapproved gates: " + ", ".join(missing))
    if data.get("productionDeploymentExecuted") is not False:
        raise ValueError("Deployment outcome must be recorded after, not before, deployment")
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--policy", default="docs/realtime/f10-production-approval.json")
    args = ap.parse_args()
    try:
        data = json.loads(Path(args.policy).read_text(encoding="utf-8"))
        verify(data, os.getenv("GITHUB_REF_NAME", ""),
               os.getenv("GITHUB_REPOSITORY", ""))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print("F10_PRODUCTION_PREFLIGHT_BLOCKED:", exc, file=sys.stderr)
        return 2
    print("F10_PRODUCTION_PREFLIGHT_APPROVED: F9 evidence and 17-repo release attested")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
