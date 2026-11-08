#!/usr/bin/env python3
"""Fail-closed audit of candidate F6 modules and coordinated SemVer.

Does not run migrations, change Git refs, approve gates, or deploy.
"""
from __future__ import annotations

import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
RELEASE = "rt-20261107-01"
BRANCH = "feature/dhole-realtime-universal-rt-20261107-01"
EXPECTED = {
    "S01": ("CustomCodeCR/DholeCRMService", "1.5.1", 15),
    "S02": ("CustomCodeCR/DholePricingService", "1.6.2", 3),
    "S03": ("CustomCodeCR/DholeNotificationsService", "1.3.1", 3),
    "S04": ("CustomCodeCR/DholeAuthService", "1.3.1", 3),
    "S05": ("CustomCodeCR/DholeConfigService", "1.3.1", 4),
    "S06": ("CustomCodeCR/DholeAuditLogsService", "1.3.1", 3),
    "S07": ("CustomCodeCR/DholeStorageService", "1.3.1", 3),
    "S08": ("CustomCodeCR/DholeDataExtractionService", "1.4.1", 3),
    "S09": ("CustomCodeCR/DholeReportsService", "1.5.1", 3),
    "S10": ("CustomCodeCR/DholeDynamicsConnectorService", "1.3.1", 3),
    "S11": ("CustomCodeCR/DholeAIService", "1.4.1", 3),
    "S12": ("CustomCodeCR/DholeAgentService", "1.3.1", 3),
    "S13": ("CustomCodeCR/DholeContentService", "1.3.1", 5),
}
FLAGS = (
    "DHOLE_REALTIME_BATCH_ENABLED",
    "DHOLE_REALTIME_BATCH_APPROVED",
    "DHOLE_REALTIME_GATEWAY_ENABLED",
    "DHOLE_REALTIME_BRIDGE_ENABLED",
    "DHOLE_REALTIME_PRICING_BRIDGE_ENABLED",
    "DHOLE_REALTIME_CRM_OUTBOX_ENABLED",
    "DHOLE_REALTIME_PRICING_OUTBOX_ENABLED",
    "DHOLE_REALTIME_CONTENT_OUTBOX_ENABLED",
    "DHOLE_REALTIME_AGENT_OUTBOX_ENABLED",
    "DHOLE_REALTIME_UNIVERSAL_SERVICES_BRIDGE_ENABLED",
)


def verify() -> None:
    manifest = yaml.safe_load((ROOT / "docs/realtime/release-manifest.yaml").read_text())
    registry = yaml.safe_load((ROOT / "docs/realtime/service-registry.yaml").read_text())
    metadata = json.loads((ROOT / "version.json").read_text())
    compose = (ROOT / "deploy/docker-compose.services.yml").read_text()
    assert manifest["releaseId"] == registry["releaseId"] == metadata["releaseId"] == RELEASE
    assert manifest["planVersion"] == registry["planVersion"] == "2.1.0"
    # Validate current *candidate* SemVer, not an outdated hard-coded patch.
    version = metadata["version"]
    baseline = manifest["batchVersion"]["currentGlobalMaxObserved"]
    semver = re.compile(r"^(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)$")
    assert semver.fullmatch(version) and semver.fullmatch(baseline)
    assert tuple(map(int, version.split("."))) > tuple(map(int, baseline.split(".")))
    assert manifest["batchVersion"]["proposedGlobalRelease"] == version
    assert metadata["ecosystemVersion"] == version
    doc = next(item for item in manifest["repositories"] if item["id"] == "DOC")
    assert doc["releaseComponentVersion"] == version
    assert ("## [" + version + "]") in (ROOT / "CHANGELOG.md").read_text()
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
        if ident in ("S01", "S02", "S03"):
            assert service["coverage"] == "EN_PROGRESO_GATE_BLOQUEADO", ident
        else:
            assert component["candidateF6TestsPassed"] >= minimum, ident
            assert component["candidateF6FormalGateApproved"] is False
            assert component["candidateF6FullEndpointInventoryVerified"] is False
            assert component["candidateF6StagingWssE2EPassed"] is False
            assert component["candidateF6TestedRun"].startswith(
                "https://github.com/" + name + "/actions/runs/"
            ), ident
            assert service["coverage"] == "IMPLEMENTACION_CANDIDATA_CI_PASS_GATE_BLOQUEADO", ident
            assert service["stagingWssE2EVerified"] is False, ident
    for ident, service in services.items():
        assert service["branchPrepared"] is True
        assert service["f6FormalApproved"] is False, ident
    gw = repositories["GW"]
    assert gw["candidateF604ToF613MappedKinds"] == 19
    assert gw["candidateF604ToF613SecurityTestsPassed"] >= 128
    assert gw["candidateF604ToF613FormalGateApproved"] is False
    # The source coverage CSV is granular and honest about missing end-to-end
    # coverage: no placeholder F0 inventory row may count as a mapped endpoint.
    import csv
    with (ROOT / "docs/realtime/coverage-matrix.csv").open(newline="") as f:
        mapped = list(csv.DictReader(f))
    assert len([row for row in mapped
        if row["status"] == "IMPLEMENTACION_CANDIDATA_GATES_BLOQUEADOS"]) >= 19
    assert len({row["domain_event"] for row in mapped
        if row["status"] == "IMPLEMENTACION_CANDIDATA_GATES_BLOQUEADOS"}) >= 19
    for name in FLAGS:
        assert ("${" + name + ":-false}") in compose, name
        assert ("${" + name + ":-true}") not in compose, name
    assert "Realtime__UniversalServicesBridgeEnabled" in compose
    assert "Gateway__HealthChecks__dynamics:" in compose
    assert "Realtime__PricingBridgeEnabled" in compose
    assert "Realtime__BatchApproved" in compose
    assert "Realtime__Outbox__Enabled" in compose
    print("PASS F6_CANDIDATE_REGISTRY: 13 partial services, 19 scoped kinds, 10 isolated"
          f" streams, 17 repositories, flags OFF, NO FORMAL GATE, global {version} candidate")


if __name__ == "__main__":
    verify()
