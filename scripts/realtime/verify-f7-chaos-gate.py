#!/usr/bin/env python3
"""F7 fail-closed guard: candidate browser simulations are NOT 14/14 staging chaos.

This program never manipulates branches, flags, deployment or evidence approvals.
The required gate remains false until the 14 real scenarios have measurable proof.
"""
from __future__ import annotations
import argparse
from pathlib import Path
import sys
import yaml

ROOT = Path(__file__).resolve().parents[2]
RELEASE = "rt-20261107-01"
IDS = {f"C{i:02d}" for i in range(1, 15)}
WEB_CANDIDATES = {"C01", "C02", "C03", "C06", "C07", "C09", "C10", "C12"}
REDIS_CANDIDATES = {"C04", "C05", "C11"}
DYNAMICS_PARTIAL_CANDIDATES = {"C14"}


def validate() -> tuple[dict, list[str]]:
    evidence = yaml.safe_load((ROOT / "docs/realtime/gate-evidence.f7.yaml").read_text())
    f6 = yaml.safe_load((ROOT / "docs/realtime/gate-evidence.f6.yaml").read_text())
    manifest = yaml.safe_load((ROOT / "docs/realtime/release-manifest.yaml").read_text())
    assert evidence["releaseId"] == f6["releaseId"] == manifest["releaseId"] == RELEASE
    scenarios = evidence["scenarios"]
    assert len(scenarios) == 14, "F7 requires fourteen scenarios, not an arbitrary subset"
    assert {item["id"] for item in scenarios} == IDS, "Missing or duplicate C01-C14 IDs"
    assert evidence["criticalRepetitionsRequired"] >= 10
    assert evidence["formalTargetPassed"] == 14
    assert evidence["browserCandidateCi"]["mockedRuntime"] is True
    assert evidence["noDevelopOrMasterMerge"] and evidence["noProductionDeployment"]
    for item in scenarios:
        expected = (
            "WEB_SIMULADO_CI_PASS" if item["id"] in WEB_CANDIDATES
            else "REDIS_EPHEMERAL_CI_PASS" if item["id"] in REDIS_CANDIDATES
            else "DYNAMICS_POSTGRES_PARTIAL_PASS" if item["id"] in DYNAMICS_PARTIAL_CANDIDATES
            else "NO_EJECUTADO_F7"
        )
        assert item["candidateStatus"] == expected, (
            f"{item['id']} candidate evidence changed without review"
        )
        assert item["realEnvironmentRuns"] == 0 or item["stagingEvidence"], (
            "Synthetic CI must never claim real staging repetitions."
        )

    missing = []
    if not f6["formalApproved"] or not f6["nextPhaseF7Authorized"]:
        missing.append("F6 has not authorized formal F7")
    if not evidence["stagingTestsExecuted"]:
        missing.append("Real staging faults/recovery not exercised")
    for item in scenarios:
        if item["formalStatus"] != "VALIDADA":
            missing.append(f"{item['id']}: real F7 execution/evidence missing")
            continue
        if item["realEnvironmentRuns"] < (10 if item["id"] in {f"C{i:02d}" for i in range(1, 9)} else 1):
            missing.append(f"{item['id']}: repetitions below required minimum")
        if not item["stagingEvidence"]:
            missing.append(f"{item['id']}: no immutable environment evidence")
        if not item["verifiedNoDataLoss"] or not item["verifiedNoAuthorizationLeak"]:
            missing.append(f"{item['id']}: integrity/security not verified")
    if evidence["formalApproved"] is not True:
        missing.append("F7 formal approval absent")
    return evidence, missing


def main() -> int:
    parser = argparse.ArgumentParser()
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--assert-candidate-blocked", action="store_true")
    mode.add_argument("--require-all", action="store_true")
    args = parser.parse_args()
    evidence, missing = validate()
    if args.assert_candidate_blocked:
        assert missing and evidence["formalApproved"] is False
        assert evidence["nextPhaseF8Authorized"] is False
        print(f"F7_CANDIDATE_EVIDENCE_OK: 8 browser, 3 isolated Redis, 1 partial "
              f"Dynamics; 0/14 real staging, {len(missing)} formal blockers")
        print("Formal F7 remains BLOCKED. This job does NOT validate staging chaos.")
        return 0
    if missing or evidence["nextPhaseF8Authorized"] is not True:
        for item in missing:
            print("BLOCKER:", item, file=sys.stderr)
        return 1
    print("F7_FORMAL_GATE_PASS (14/14 with real evidence)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
