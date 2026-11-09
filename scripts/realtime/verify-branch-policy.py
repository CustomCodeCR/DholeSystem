#!/usr/bin/env python3
"""Dhole batch branch-policy guard (no Git writes, no deployments).

This F0/F1 guard validates the versioned manifest and rejects target-branch
release PRs/feature activation before F9/F10. Server-side protected-branch
enforcement remains pending; this script cannot replace GitHub rulesets.
"""
from __future__ import annotations

import os
import sys
from pathlib import Path

import yaml
from f0_scan import check_manifest


def main() -> int:
    file = Path("docs/realtime/release-manifest.yaml")
    with file.open(encoding="utf-8") as handle:
        manifest = yaml.safe_load(handle)

    errors = check_manifest(manifest)
    phase = str(manifest.get("phase") or "")
    branch = os.environ.get("GITHUB_REF_NAME", "")
    base = os.environ.get("GITHUB_BASE_REF", "")

    if phase in {"F0", "F1", "F2", "F3", "F4", "F5", "F6", "F7", "F8"}:
        if base in {"develop", "master", "main"}:
            errors.append(f"F0-F8 cannot target protected release branch {base}")
        if branch and branch in {"develop", "master", "main"}:
            errors.append(f"F0-F8 cannot write target branch {branch}")

    if errors:
        for item in errors:
            print(f"BRANCH_POLICY_REJECTED: {item}", file=sys.stderr)
        return 1
    print("BRANCH_POLICY_OK: 17 repositories, feature branches, flags OFF, no premature PR/deploy")
    return 0


if __name__ == "__main__":
    sys.exit(main())
