#!/usr/bin/env python3
"""Fail-closed audit of candidate F6 modules and coordinated SemVer.

Does not run migrations, change Git refs, approve gates, or deploy.
"""
from __future__ import annotations

import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
RELEASE = "rt-20261107-01"
BRANCH = "feature/dhole-realtime-universal-rt-20261107-01"
EXPECTED = {
    "S01": ("CustomCodeCR/DholeCRMService", "1.5.0", 15),
    "S02": ("CustomCodeCR/DholePricingService", "1.6.0", 3),
    "S03": ("CustomCodeCR/DholeNotificationsService", "1.3.0", 3),
}
FLAGS = (
    "DHOLE_REALTIME_BATCH_ENABLED",
    "DHOLE_REALTIME_BATCH_APPROVED",
    "DHOLE_REALTIME_GATEWAY_ENABLED",
    "DHOLE_REALTIME_BRIDGE_ENABLED",
    "DHOLE_REALTIME_PRICING_BRIDGE_ENABLED",
    "DHOLE_REALTIME_CRM_OUTBOX_ENABLED",
    "DHOLE_REALTIME_PRICING_OUTBOX_ENABLED",
)


def verify() -> None:
    manifest = yaml.safe_load((ROOT / "docs/realtime/release-manifest.yaml").read_text())
    registry = yaml.safe_load((ROOT / "docs/realtime/service-registry.yaml").read_text())
    metadata = json.loads((ROOT / "version.json").read_text())
    compose = (ROOT / "deploy/docker-compose.services.yml").read_text()
    assert manifest["releaseId"] == registry["releaseId"] == metadata["releaseId"] == RELEASE
    assert manifest["planVersion"] == registry["planVersion"] == "2.1.0"
    assert manifest["batchVersion"]["proposedGlobalRelease"] == metadata["version"] == "1.13.0"
    assert manifest["batchVersion"]["proposedOnly"] is True
    assert manifest["batchStatus"] == "BUILDING"
    policy = manifest["branchPolicy"]
    assert policy["intermediate"] == BRANCH
    assert policy["featureFlagsDefaultOff"] and policy["forbidDirectTargetWrites"]
    assert policy["productionDeploymentAuthorized"] is False
    promotion = manifest["promotion"]
    assert promotion["frozen"] is False and promotion["approvalF0"] is False
    assert promotion["approvalF1ToF8"] is False
    assert promotion["developPRs"] == [] and promotion["masterPRs"] == []
    assert promotion["stagingDeployed"] is False and promotion["productionDeployed"] is False
    assert len(manifest["repositories"]) == 17
    assert len(registry["services"]) == registry["serviceCountExpected"] == 13
    assert registry["serviceCountAuditedCompletely"] == 0
    repositories = {item["id"]: item for item in manifest["repositories"]}
    services = {item["id"]: item for item in registry["services"]}
    for ident, (name, version, minimum) in EXPECTED.items():
        component = repositories[ident]
        service = services[ident]
        assert component["name"] == service["repo"] == name, ident
        assert component["intermediateBranch"] == BRANCH
        assert component["releaseComponentVersion"] == service["candidateReleaseVersion"] == version
        assert service["candidateIntegrationTestsPassed"] >= minimum
        assert service["fullEndpointAndWorkerMappingVerified"] is False
        assert service["f6FormalApproved"] is False
        assert component["flags"]["realtime"] is False
        assert component["developBatchPR"] is None and component["masterBatchPR"] is None
        assert "candidateF6" in " ".join(component), ident
    for ident, service in services.items():
        assert service["branchPrepared"] is True
        if ident not in EXPECTED:
            assert service["coverage"] == "BLOQUEADA", ident
    for name in FLAGS:
        assert ("${" + name + ":-false}") in compose, name
        assert ("${" + name + ":-true}") not in compose, name
    assert "Realtime__PricingBridgeEnabled" in compose
    assert "Realtime__BatchApproved" in compose
    assert "Realtime__Outbox__Enabled" in compose
    print("PASS F6_CANDIDATE_REGISTRY: 3 partial modules, 17 repositories, "
          "13 registered services, flags OFF, no promotion, global 1.13.0 candidate")


if __name__ == "__main__":
    verify()
