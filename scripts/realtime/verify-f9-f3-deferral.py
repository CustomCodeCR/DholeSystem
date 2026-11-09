#!/usr/bin/env python3
"""F9 code-review waiver for F3 external staging attestation ONLY.

Does not turn F3 formal gate green, authorize merge, activate a Hub, deploy,
or weaken JWT, resource-owner ACL, Redis durability or F6/F7/F8 CI guards.
"""
from __future__ import annotations
import argparse
from datetime import date
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[2]
RELEASE = "rt-20261107-01"
CI_RUN = "https://github.com/CustomCodeCR/DholeApiGateway/actions/runs/42538863927"
TESTED_SHA = "de1b57e987ddb6be83f58f53152ce3ee72ce46f2"
FALSE_CONTROLS = (
    "runtimeUniversalRealtimeEnabled",
    "f9MergeAuthorized",
    "f10ProductionAuthorized",
    "f3FormalApprovalUnchanged",
)
TRUE_CONTROLS = (
    "f9ReviewMayProceed",
    "requireRealStagingBeforeFeatureActivation",
    "requireAllOtherReleaseGates",
    "preserveRedisAofAndBackupChecks",
    "preserveOriginAndJwtChecks",
    "preserveBranchProtection",
)


def verify_review(data: dict, now: date, evidence_text: str) -> None:
    if data.get("schemaVersion") != 1 or data.get("releaseId") != RELEASE:
        raise ValueError("Unexpected release identity")
    if data.get("scope") != "F9_CODE_REVIEW_ONLY":
        raise ValueError("F3 exception cannot cover merge or deployment")
    if not re.fullmatch(r"F9-F3-TRANSPORT-REVIEW-\d{8}", data.get("exceptionId", "")):
        raise ValueError("Invalid audit exception ID")
    if date.fromisoformat(data["expiresOn"]) < now:
        raise ValueError("F3 review exception expired")
    proof = data["proof"]
    if proof.get("gatewayRepo") != "CustomCodeCR/DholeApiGateway":
        raise ValueError("Unexpected Gateway")
    if proof.get("gatewayCiRun") != CI_RUN or proof.get("gatewayTestedCommit") != TESTED_SHA:
        raise ValueError("F3 isolation test must be pinned to the validated CI run and SHA")
    if proof.get("isolatedTraefikTlsWssPassed") is not True or proof.get("ownerRestAclSyntheticPassed") is not True:
        raise ValueError("Required isolated TLS/WSS and ACL evidence absent")
    if proof.get("syntheticAuthorizedUsers") != 2 or proof.get("syntheticDeniedUsers") != 1:
        raise ValueError("Isolated authentication/authorization scenario count incorrect")
    if proof.get("realStagingGatewayUniversalWssVerified") is not False or proof.get("realStagingOwnerAclVerified") is not False:
        raise ValueError("Staging cannot be claimed verified by this exception")
    controls = data["compensatingControls"]
    for key in FALSE_CONTROLS:
        if controls.get(key) is not False:
            raise ValueError(f"Forbidden review waiver control: {key}")
    for key in TRUE_CONTROLS:
        if controls.get(key) is not True:
            raise ValueError(f"Required compensating control missing: {key}")
    signoff = data["signoff"]
    if signoff.get("requestedByUser") is not True or signoff.get("formalAcceptance") is not False:
        raise ValueError("Exception is not a formal signoff")
    # The real gate must remain NOT approved. We never rewrite its evidence.
    match = re.search(r"(?m)^  F3:\s*\n(.*?)(?=^  F4:|\Z)", evidence_text, re.S | re.M)
    if not match or not re.search(r"(?m)^    approval: false\s*$", match.group(1)):
        raise ValueError("F3 formal gate is missing or was modified")
    if CI_RUN not in (ROOT / "docs/realtime/test-evidence/F3-TRAEFIK-WSS-CI-42538238853.md").read_text():
        raise ValueError("Gateway isolated WSS evidence document not found")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--review-only", action="store_true")
    parser.add_argument("--exception", default="docs/realtime/f9-f3-staging-deferral.json")
    args = parser.parse_args()
    if not args.review_only:
        print("F9_EXCEPTION_DENIED: review-only is the only supported mode; no merge/deploy", file=sys.stderr)
        return 2
    try:
        data = json.loads(Path(args.exception).read_text(encoding="utf-8"))
        evidence = (ROOT / "docs/realtime/gate-evidence.f0-f4.yaml").read_text(encoding="utf-8")
        verify_review(data, date.today(), evidence)
    except (OSError, ValueError, KeyError, TypeError, json.JSONDecodeError) as exc:
        print("F9_F3_REVIEW_EXCEPTION_BLOCKED:", exc, file=sys.stderr)
        return 2
    print("F9_F3_REVIEW_READY: isolated WSS evidence accepted for review ONLY; F3 staging unverified; merge/activation/deploy blocked")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
