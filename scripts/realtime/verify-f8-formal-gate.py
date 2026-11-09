#!/usr/bin/env python3
"""F8 formal gate: CI candidate evidence never overrides sequential F0-F7."""
from __future__ import annotations

import argparse
from pathlib import Path
import sys

import yaml

ROOT = Path(__file__).resolve().parents[2]
BRANCH = "feature/dhole-realtime-universal-rt-20261107-01"
RELEASE = "rt-20261107-01"
FEATURES = ("positiveNegativeCiPassed", "sampleDotNetPostgresRedisRecoveryCiPassed",
            "sourceEndpointJobManifestCoverageVerified", "futureServiceRegisteredCentral",
            "futureServiceGatewayStreamRoutingVerified", "futureServiceAuthorizedRestAclTested",
            "futureServiceWssAndRestRecoveryVerified", "futurePRRequiredChecksProtected")


def evaluate() -> tuple[dict, list[str]]:
    p = ROOT / "docs/realtime/gate-evidence.f8.yaml"
    f8 = yaml.safe_load(p.read_text())
    f7 = yaml.safe_load((ROOT / "docs/realtime/gate-evidence.f7.yaml").read_text())
    f6 = yaml.safe_load((ROOT / "docs/realtime/gate-evidence.f6.yaml").read_text())
    f0 = yaml.safe_load((ROOT / "docs/realtime/gate-evidence.f0-f4.yaml").read_text())
    registry = yaml.safe_load((ROOT / "docs/realtime/service-registry.yaml").read_text())
    manifest = yaml.safe_load((ROOT / "docs/realtime/release-manifest.yaml").read_text())

    assert all(doc["releaseId"] == RELEASE for doc in (f8, f7, f6, f0, registry, manifest))
    assert f8["releaseBranch"] == manifest["branchPolicy"]["intermediate"] == BRANCH
    assert f8["phase"] == "F8"
    assert f8["hub"] == "DholeApiGateway"
    assert f8["sampleIsDeployable"] is False
    assert registry["futureServices"][0]["candidateOnly"] is True
    assert registry["futureServices"][0]["deploymentApproved"] is False
    assert manifest["batchStatus"] == "BUILDING"
    assert manifest["promotion"]["frozen"] is False
    assert manifest["promotion"]["stagingDeployed"] is False
    assert manifest["promotion"]["productionDeployed"] is False

    missing: list[str] = []
    if any(not gate.get("approval") for gate in f0["phaseGates"].values()):
        missing.append("F0-F4 not formally approved in sequence")
    if not f6["formalApproved"] or not f6["nextPhaseF7Authorized"]:
        missing.append("F6 not formally approved")
    if not f7["formalApproved"] or not f7["nextPhaseF8Authorized"]:
        missing.append("F7 has not authorized F8 (14/14 staging required)")
    if not f8.get("ciEvidence", {}).get("candidateRun"):
        missing.append("F8 CI SHA/run absent")
    if not f8.get("ciEvidence", {}).get("scaffoldAndNegativeTestCount"):
        missing.append("F8 positive/negative PR cases not recorded")
    for k in FEATURES:
        if f8["acceptance"].get(k) is not True:
            missing.append("F8 acceptance missing: " + k)
    if f8["formalApproved"] is not True:
        missing.append("F8 formal sign-off absent")
    if f8["nextPhaseF9Authorized"] is not True:
        missing.append("F9 batch not authorized by F8")
    if registry["futureServicePolicy"]["enforced"] is not True:
        missing.append("Future service registry enforcement not enabled in protected targets")
    if f8.get("targetBranchProtectionVerified") is not True:
        missing.append("Native GitHub develop/master required checks not verified")
    return f8, missing


def main() -> int:
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--assert-candidate-blocked", action="store_true")
    group.add_argument("--require-all", action="store_true")
    args = parser.parse_args()
    data, missing = evaluate()
    if args.assert_candidate_blocked:
        assert data["formalApproved"] is False
        assert data["nextPhaseF9Authorized"] is False
        assert missing, "Candidate CI cannot approve the formal gate"
        print("F8_CANDIDATE_GUARD_PASS: sample prepared, " + str(len(missing))
              + " formal blockers, develop/master unchanged")
        return 0
    if missing:
        for item in missing:
            print("F8_BLOCKER: " + item, file=sys.stderr)
        return 1
    print("F8_FORMAL_APPROVED; sequential F0-F8 and 14/14 F7 have evidence.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
