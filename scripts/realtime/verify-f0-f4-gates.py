#!/usr/bin/env python3
"""Fail-closed F0-F4 release gate.

This script never deploys or alters refs. CI runs --assert-blocked while an
incomplete batch is under development. F9 must instead run --require-all
against signed, real operational evidence verified separately.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

PRE = ("F0", "F1", "F2", "F3", "F4")

REQUIREMENTS: dict[str, list[tuple[str, object]]] = {
    "F0": [
        ("repositoryCountInspected", 17),
        ("sourceDiscoveryExecuted", True),
        ("missingEndpointsOrJobsExplicitlyRegistered", True),
        ("srMOwnerConfirmed", True),
        ("systemFullOwnershipConfirmed", True),
        ("allMutableEndpointsAndWorkersReviewedAndMapped", True),
        ("realStagingProxyJwtRedisAofVerified", True),
        ("realStagingRestP95P99Measured", True),
        ("runtimeInstanceTopologyVerified", True),
        ("targetBranchPolicyVerifiedByCi", True),
        ("nativeProtectedBranchesVerified", True)
    ],
    "F1": [
        ("buildSuccess", True),
        ("unitTestsFailed", 0),
        ("unitTestsSkipped", 0),
        ("crmF2WireCompatibilityTested", True),
        ("contractSchemaEvolutionTested", True),
        ("namespaceAdditiveNoBreakingChange", True)
    ],
    "F2": [
        ("buildSuccess", True),
        ("integrationTestsFailed", 0),
        ("integrationTestsSkipped", 0),
        ("committedBusinessOperations", 1000),
        ("persistedLogicalEvents", 1000),
        ("duplicateSideEffects", 0),
        ("pilotHttpTestServerMutationSucceedsUnderSimulatedRedisOutage", True),
        ("realProductionCrmRestHandlersCovered", True),
        ("redisStreamLossRecoverySimulatedWithRealPostgresRedis", True),
        ("deadLetterAndRetryVerified", True),
        ("realStagingRedisOutageAndRestoreVerified", True),
        ("realStagingBackupRetentionAndAlertsVerified", True)
    ],
    "F3": [
        ("buildSuccess", True),
        ("gatewayTestsFailed", 0),
        ("gatewayTestsSkipped", 0),
        ("negativeAuthorizationScenarios", 30),
        ("twoAuthorizedUsersReceive", True),
        ("deniedUserDoesNotReceive", True),
        ("twoIsolatedGatewayInstancesCi", True),
        ("restartedGatewayConsumesDurableRedisCursorCi", True),
        ("wssTlsThroughRealStagingProxyVerified", True),
        ("ownerRestAuthorizationRealStagingVerified", True),
        ("productionJwtRevocationVerified", True),
        ("realStagingInstanceTopologyVerified", True)
    ],
    "F4": [
        ("buildSuccess", True),
        ("managerTestsFailed", 0),
        ("frontendTypecheckPass", True),
        ("chromiumListenerGrowth", 0),
        ("chromiumSocketGrowth", 0),
        ("simulatedReconnects", 30),
        ("simulatedInitialConnectionFailures", 30),
        ("crmPricingPilotRestReconciledInBrowserFixture", True),
        ("dirtyFormsProtected", True),
        ("offlineAutoMutations", 0),
        ("expiredTokenIsolated", True),
        ("realStagingTwoUsersTwoTabsReconcileVerified", True),
        ("realStagingOfflineWssRestRecoveryVerified", True)
    ]
}

MINIMUM: dict[str, list[tuple[str, int]]] = {
    "F1": [("unitTestsPassed", 20)],
    "F2": [("integrationTestsPassed", 11)],
    "F3": [("gatewayTestsPassed", 100)],
    "F4": [("managerTestsPassed", 12),
           ("frontendRegressionTestsPassed", 91),
           ("chromiumRealVueCycles", 100)]
}

def run(evidence: dict) -> dict:
    if evidence.get("releaseId") != "rt-20261107-01" or evidence.get("planVersion") != "2.1.0":
        raise ValueError("Unexpected releaseId or planVersion")
    if evidence.get("promotionApproved") is not False or evidence.get("productionDeploymentAuthorized") is not False:
        raise ValueError("Premature promotion or production authorization in F0-F4 evidence")
    phases = evidence.get("phaseGates", {})
    if set(phases) != set(PRE):
        raise ValueError("Must declare exactly F0, F1, F2, F3, F4")
    result: dict = {"releaseId": evidence["releaseId"], "phases": {},
                    "allGatesApproved": False}
    previous = True
    for phase in PRE:
        entry = phases[phase]
        failed = []
        for field, expected in REQUIREMENTS[phase]:
            observed = entry.get(field)
            if type(observed) is not type(expected) or observed != expected:
                failed.append({"field": field, "required": expected,
                               "observed": observed})
        for field, minimum in MINIMUM.get(phase, []):
            observed = entry.get(field)
            if type(observed) is not int or observed < minimum:
                failed.append({"field": field, "minimum": minimum,
                               "observed": observed})
        if not previous:
            failed.append({"field": "previousPhaseGateApproved",
                           "required": True, "observed": False})
        eligible = not failed
        if entry.get("approval") is True and not eligible:
            raise ValueError(f"{phase} declares APPROVED with outstanding blockers")
        result["phases"][phase] = {
            "criteriaSatisfied": eligible,
            "declaredApproved": entry.get("approval") is True,
            "missing": failed,
            "status": "APPROVED" if eligible and entry.get("approval") is True
                      else "BLOCKED",
            "testedRun": entry.get("testedRun") or entry.get("technicalAuditRun")
        }
        previous = eligible and entry.get("approval") is True
    result["allGatesApproved"] = previous
    return result

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--evidence", default="docs/realtime/gate-evidence.f0-f4.yaml")
    parser.add_argument("--output", default="GateResults/F0-F4-gates.json")
    modes = parser.add_mutually_exclusive_group(required=True)
    modes.add_argument("--report-only", action="store_true")
    modes.add_argument("--require-all", action="store_true")
    modes.add_argument("--assert-blocked", action="store_true")
    args = parser.parse_args()
    data = yaml.safe_load(Path(args.evidence).read_text(encoding="utf8"))
    report = run(data)
    target = Path(args.output)
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(report, indent=2) + "\n", encoding="utf8")
    for name, item in report["phases"].items():
        print(f"{name}: {item['status']} — {len(item['missing'])} blockers")
        for miss in item["missing"]:
            print("  " + miss["field"])
    if args.require_all:
        return 0 if report["allGatesApproved"] else 1
    if args.assert_blocked:
        return 0 if all(x["status"] == "BLOCKED" for x in report["phases"].values()) else 1
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, TypeError, KeyError) as ex:
        print(f"GATE_REGISTRY_INVALID: {ex}", file=sys.stderr)
        sys.exit(2)
