#!/usr/bin/env python3
"""F6 sequential phase gate. CI candidates may PASS while formal F6 remains BLOCKED.

--assert-blocked checks the repository has not accidentally approved F7.
--require-all blocks PRs into develop/master until real evidence is signed off.
No tool in this file changes Git refs, infrastructure or approval flags.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[2]
BRANCH = "feature/dhole-realtime-universal-rt-20261107-01"
RELEASE = "rt-20261107-01"


def collect() -> tuple[dict, list[str]]:
    gate = yaml.safe_load((ROOT / "docs/realtime/gate-evidence.f6.yaml").read_text())
    registry = yaml.safe_load((ROOT / "docs/realtime/service-registry.yaml").read_text())
    manifest = yaml.safe_load((ROOT / "docs/realtime/release-manifest.yaml").read_text())
    assert gate["releaseId"] == manifest["releaseId"] == registry["releaseId"] == RELEASE
    assert gate["branch"] == manifest["branchPolicy"]["intermediate"] == BRANCH
    assert gate["candidateProducerOrDeliveryMechanisms"] == 13
    assert gate["candidateAdditionalStreams"] == 10
    assert gate["candidateResourceKinds"] == 19
    assert gate["allFeatureFlagsDefaultOff"] is True
    assert gate["noDevelopOrMasterMerge"] and gate["noProductionDeployment"]
    assert len(registry["services"]) == 13 and len(manifest["repositories"]) == 17

    missing = []
    for phase, approved in gate["sequentialGates"].items():
        if approved is not True:
            missing.append(f"{phase}: approval/evidence pending")
    for name, accepted in gate["acceptance"].items():
        if accepted is not True:
            missing.append(f"F6: {name} pending")
    if registry["serviceCountAuditedCompletely"] != 13:
        missing.append("F6: 13/13 full source inventories not formally audited")
    for service in registry["services"]:
        if service.get("f6FormalApproved") is not True:
            missing.append(f"{service['id']}: formal owner approval pending")
    if gate["formalApproved"] is not True:
        missing.append("F6 formal approval not granted")
    return gate, missing


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--assert-blocked", action="store_true")
    mode.add_argument("--require-all", action="store_true")
    args = parser.parse_args()
    gate, missing = collect()
    if args.assert_blocked:
        assert missing and gate["nextPhaseF7Authorized"] is False, (
            "Candidate CI must not silently authorize F7."
        )
        print(f"PASS F6_GUARD_BLOCKED: {len(missing)} formal blockers; F7 prohibited")
        return 0
    if missing or gate["nextPhaseF7Authorized"] is not True:
        for finding in missing:
            print("BLOCKER:", finding, file=sys.stderr)
        print("BLOCKED F6: no PR integration or F7 until gates pass", file=sys.stderr)
        return 1
    print("PASS F6_FORMAL_GATE: verified approvals permit F7")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
