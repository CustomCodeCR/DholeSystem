#!/usr/bin/env python3
"""F0/F9 exact-SHA and SemVer release preflight for all Dhole repositories.

Read-only by design. A green candidate audit is NOT F9 approval. The formal
mode fails closed if global versions, repo HEADs, approval or frozen SHAs differ.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import subprocess
import sys
import yaml

RELEASE = "rt-20261107-01"
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:-([0-9A-Za-z.-]+))?$")
SHA = re.compile(r"^[0-9a-f]{40}$")


def parse_version(raw: object) -> tuple[int, int, int]:
    if not isinstance(raw, str):
        raise ValueError("SemVer missing")
    match = SEMVER.fullmatch(raw)
    if not match:
        raise ValueError("Invalid SemVer: " + raw)
    return tuple(int(x) for x in match.groups()[:3])


def inspect(manifest: dict, workspace: Path, formal: bool) -> dict:
    if manifest.get("releaseId") != RELEASE or len(manifest.get("repositories", [])) != 17:
        raise ValueError("Wrong release or incomplete 17-repository manifest")
    expected = manifest["batchVersion"]["proposedGlobalRelease"]
    observed = manifest["batchVersion"]["currentGlobalMaxObserved"]
    if parse_version(expected) <= parse_version(observed):
        raise ValueError("Global candidate must exceed existing ecosystem version")
    results = []
    seen = set()
    problems = []
    for item in manifest["repositories"]:
        name = item["name"]
        if name in seen:
            raise ValueError("Duplicate repository in release manifest: " + name)
        seen.add(name)
        root = workspace / name.rsplit("/", 1)[-1]
        issues = []
        metadata_path = root / "version.json"
        if not metadata_path.is_file():
            issues.append("VERSION_JSON_MISSING")
            metadata = {}
        else:
            try:
                metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            except (json.JSONDecodeError, UnicodeError):
                metadata = {}
                issues.append("VERSION_JSON_INVALID")
        version = metadata.get("version")
        global_version = metadata.get("ecosystemVersion")
        try:
            parse_version(version)
            parse_version(global_version)
        except ValueError:
            issues.append("INVALID_SEMVER")
        if metadata.get("releaseId") != RELEASE:
            issues.append("RELEASE_ID_MISMATCH")
        if version != item.get("releaseComponentVersion"):
            issues.append("COMPONENT_MANIFEST_VERSION_MISMATCH")
        baseline = item.get("currentComponentVersionBaseline")
        if baseline:
            try:
                if parse_version(version) <= parse_version(baseline):
                    issues.append("COMPONENT_VERSION_NOT_ADVANCED")
            except ValueError:
                issues.append("BASELINE_VERSION_INVALID")
        if global_version != expected:
            issues.append("GLOBAL_VERSION_SKEW")
        changelog = root / "CHANGELOG.md"
        if not changelog.is_file() or not isinstance(version, str) or (
            not re.search(r"(?m)^## \[" + re.escape(version) + r"\]", changelog.read_text(encoding="utf-8"))
        ):
            issues.append("CHANGELOG_VERSION_MISSING")
        sha = ""
        if (root / ".git").exists():
            proc = subprocess.run(["git", "-C", str(root), "rev-parse", "HEAD"],
                                  text=True, capture_output=True, timeout=10, check=False)
            if proc.returncode == 0:
                sha = proc.stdout.strip().lower()
        if not SHA.fullmatch(sha):
            issues.append("CHECKOUT_SHA_MISSING")
        if formal and (not item.get("frozenSha") or item["frozenSha"] != sha):
            issues.append("FROZEN_SHA_MISSING_OR_DRIFT")
        results.append({
            "repository": name, "componentVersion": version,
            "ecosystemVersion": global_version, "shaAtAudit": sha,
            "frozenSha": item.get("frozenSha"), "issues": issues,
        })
        problems.extend(f"{name}: {issue}" for issue in issues)
    if formal:
        promotion = manifest.get("promotion", {})
        if promotion.get("frozen") is not True or promotion.get("frozenShaCount") != 17:
            problems.append("BATCH_NOT_FROZEN_17_SHA")
        if promotion.get("approvalF0") is not True or promotion.get("approvalF1ToF8") is not True:
            problems.append("F0_TO_F8_NOT_APPROVED")
        if not manifest.get("branchPolicy", {}).get("featureFlagsDefaultOff"):
            problems.append("UNSAFE_FLAG_DEFAULT")
    return {
        "releaseId": RELEASE,
        "mode": "FORMAL_PRE_F9" if formal else "CANDIDATE_AUDIT",
        "proposedGlobalRelease": expected,
        "repositoriesInspected": len(results),
        "alignedGlobalVersions": sum(x["ecosystemVersion"] == expected for x in results),
        "allComponentVersionsVerified": not any(
            any(t in x["issues"] for t in (
                "INVALID_SEMVER", "RELEASE_ID_MISMATCH",
                "COMPONENT_MANIFEST_VERSION_MISMATCH", "COMPONENT_VERSION_NOT_ADVANCED",
                "CHANGELOG_VERSION_MISSING")) for x in results),
        "issues": problems,
        "entries": results,
        "formalF9Ready": bool(formal and not problems),
        "noRefsChanged": True,
        "noServicesDeployed": True,
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--workspace", default="F0Results/working")
    ap.add_argument("--manifest", default="docs/realtime/release-manifest.yaml")
    ap.add_argument("--output", default="F0Results/F0-release-version-audit.json")
    ap.add_argument("--require-f9-ready", action="store_true")
    args = ap.parse_args()
    try:
        manifest = yaml.safe_load(Path(args.manifest).read_text(encoding="utf-8"))
        result = inspect(manifest, Path(args.workspace), args.require_f9_ready)
    except (ValueError, KeyError, FileNotFoundError, OSError, subprocess.TimeoutExpired) as exc:
        print("RELEASE_VERSION_PRECHECK_ERROR:", exc, file=sys.stderr)
        return 2
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"RELEASE_VERSION_AUDIT: {result['repositoriesInspected']}/17 repos, "
          f"{result['alignedGlobalVersions']}/17 aligned, "
          f"{len(result['issues'])} findings; F9_READY={result['formalF9Ready']}")
    if args.require_f9_ready and result["issues"]:
        for problem in result["issues"]:
            print("F9_BLOCKER:", problem, file=sys.stderr)
        return 1
    # Candidate mode keeps findings visible in an artifact; it NEVER approves F9.
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
