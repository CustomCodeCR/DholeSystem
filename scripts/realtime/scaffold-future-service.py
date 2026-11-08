#!/usr/bin/env python3
"""Generate an isolated Dhole service candidate, with zero Git/deploy writes.

The generated registration *proposal* is not a central registry approval.
Register the real repo in DholeSystem via reviewed batch PR and install its CI.
"""
from __future__ import annotations

import argparse
from pathlib import Path
import re
import shutil
import sys

import yaml

ROOT = Path(__file__).resolve().parents[2]
TEMPLATE = ROOT / "scaffolds/dhole-future-service"
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)$")
SERVICE = re.compile(r"^Dhole[A-Z][A-Za-z0-9]*Service$")
DOMAIN = re.compile(r"^[a-z][a-z0-9]{2,25}$")
ID = re.compile(r"^S(?:1[4-9]|[2-9]\d|\d{3,})$")

def scaffold(*, name: str, domain: str, service_id: str, owner: str,
             version: str, target: Path) -> None:
    if not SERVICE.fullmatch(name):
        raise ValueError("name must be Dhole<PascalCase>Service")
    if not DOMAIN.fullmatch(domain):
        raise ValueError("domain must be lowercase alphanumeric, 3-26 chars")
    if not ID.fullmatch(service_id):
        raise ValueError("service-id S14 or higher; existing S01-S13 are reserved")
    if not SEMVER.fullmatch(version):
        raise ValueError("version must be SemVer X.Y.Z")
    if not owner or len(owner) < 4 or not re.fullmatch("[A-Za-z0-9_.-]+", owner):
        raise ValueError("owner must name an accountable team or maintainer")
    if target.exists():
        raise ValueError("destination exists, refusing overwrite")
    relative = name.removeprefix("Dhole").removesuffix("Service")
    replacements = (
        ("Dhole.FutureSample.Api", "Dhole." + relative + ".Api"),
        ("FutureSample.IntegrationHarness", relative + ".IntegrationHarness"),
        ("DholeFutureSample", name),
        ("FuturePlatformTeam", owner),
        ("dhole.future-sample.realtime.v1", "dhole." + domain + ".realtime.v1"),
        ("future-sample", domain),
        ("future.order", domain + ".order"),
        ("future:", domain + ":"),
        ("future.", domain + "."),
        ("S14", service_id),
        ('version: "1.13.0"', 'version: "' + version + '"'),
        ("<Version>1.13.0</Version>", "<Version>" + version + "</Version>"),
    )
    shutil.copytree(TEMPLATE, target)
    for file in target.rglob("*"):
        if file.is_file() and file.suffix.lower() in {".cs", ".csproj", ".sql", ".py", ".yaml", ".md"}:
            body = file.read_text(encoding="utf-8")
            for old, new in replacements:
                body = body.replace(old, new)
            file.write_text(body, encoding="utf-8")
    for old, new in (("Dhole.FutureSample.Api", "Dhole." + relative + ".Api"),
                     ("FutureSample.IntegrationHarness", relative + ".IntegrationHarness")):
        for directory in sorted([p for p in target.rglob("*") if p.is_dir() and p.name == old],
                                key=lambda x: len(x.parts), reverse=True):
            directory.rename(directory.with_name(new))
        for file in sorted([p for p in target.rglob("*") if p.is_file() and old in p.name],
                           key=lambda x: len(x.parts), reverse=True):
            file.rename(file.with_name(file.name.replace(old, new)))
    # Future repo must receive the same immutable policy source via its own
    # feature branch. Cross-repository registry verification is STILL REQUIRED.
    verifier = ROOT / "scripts/realtime/verify-f8-future-service.py"
    dest = target / "scripts/realtime/verify-f8-future-service.py"
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(verifier, dest)
    registry_proposal = {
        "futureServices": [{
            "id": service_id, "repo": "CustomCodeCR/" + name,
            "name": name, "stream": "dhole." + domain + ".realtime.v1",
            "hub": "DholeApiGateway", "manifest": "realtime.manifest.yaml",
            "status": "REGISTER_IN_DHOLE_SYSTEM_BATCH_PR",
            "candidateOnly": True, "deploymentApproved": False
        }]
    }
    (target / "central-registry.PROPOSAL.yaml").write_text(
        "# PROPOSAL ONLY. Merge into DholeSystem registry only after review.\n"
        + yaml.safe_dump(registry_proposal, sort_keys=False), encoding="utf-8")
    (target / ".github/workflows").mkdir(parents=True, exist_ok=True)
    (target / ".github/workflows/realtime-future-enforcement.yml").write_text(
        (ROOT / "scaffolds/realtime-future-enforcement.yml").read_text(encoding="utf-8"),
        encoding="utf-8")
    (target / ".github/PULL_REQUEST_TEMPLATE.md").write_text(
        (ROOT / "scaffolds/realtime-future-PR-template.md").read_text(encoding="utf-8"),
        encoding="utf-8")
    print("F8 scaffold written: " + str(target))
    print("Review central-registry.PROPOSAL.yaml in DholeSystem; neither Git nor production changed.")

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--name", required=True)
    parser.add_argument("--domain", required=True)
    parser.add_argument("--service-id", required=True)
    parser.add_argument("--owner", required=True)
    parser.add_argument("--version", required=True)
    parser.add_argument("--out", required=True)
    args = parser.parse_args()
    try:
        scaffold(name=args.name, domain=args.domain, service_id=args.service_id,
                 owner=args.owner, version=args.version, target=Path(args.out))
        return 0
    except (ValueError, OSError) as exc:
        print("F8_SCAFFOLD_REFUSED: " + str(exc), file=sys.stderr)
        return 1

if __name__ == "__main__":
    raise SystemExit(main())
