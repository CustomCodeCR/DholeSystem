import json
from pathlib import Path
import subprocess
import tempfile
import unittest

from f0_release_versions import inspect, parse_version

BRANCH = "feature/dhole-realtime-universal-rt-20261107-01"


class ReleasePreflightTests(unittest.TestCase):
    def test_semver(self):
        self.assertEqual(parse_version("1.13.4"), (1, 13, 4))
        for wrong in ("1.013.4", "1.0", "v1.2.3", "bad"):
            with self.assertRaises(ValueError):
                parse_version(wrong)

    def fixture(self):
        tmp = tempfile.TemporaryDirectory()
        root = Path(tmp.name)
        repositories = []
        for name in ("DholeSystem", "DholeCRMService"):
            repo = root / name
            repo.mkdir()
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            (repo / "version.json").write_text(json.dumps({
                "version": "1.2.1", "ecosystemVersion": "1.13.4",
                "releaseId": "rt-20261107-01",
            }))
            (repo / "CHANGELOG.md").write_text("# Changes\n\n## [1.2.1] - 2026-11-08\n")
            repositories.append({
                "name": f"CustomCodeCR/{name}", "currentComponentVersionBaseline": "1.2.0",
                "releaseComponentVersion": "1.2.1", "frozenSha": None,
            })
        # Pad manifest using same schema with unique codebase names.
        for n in range(15):
            repo = root / f"TestRepo{n}"
            repo.mkdir()
            subprocess.run(["git", "init", "-q", str(repo)], check=True)
            (repo / "version.json").write_text(json.dumps({
                "version": "0.1.1", "ecosystemVersion": "1.13.4",
                "releaseId": "rt-20261107-01",
            }))
            (repo / "CHANGELOG.md").write_text("## [0.1.1] - 2026-11-08\n")
            repositories.append({
                "name": f"CustomCodeCR/TestRepo{n}",
                "currentComponentVersionBaseline": "0.1.0",
                "releaseComponentVersion": "0.1.1",
                "frozenSha": None,
            })
        manifest = {
            "releaseId": "rt-20261107-01", "repositories": repositories,
            "batchVersion": {"proposedGlobalRelease": "1.13.4",
                             "currentGlobalMaxObserved": "1.12.11"},
            "promotion": {"frozen": False, "frozenShaCount": 0,
                          "approvalF0": False, "approvalF1ToF8": False},
            "branchPolicy": {"featureFlagsDefaultOff": True},
        }
        return tmp, root, manifest

    def test_candidate_cannot_approve_f9(self):
        tmp, root, manifest = self.fixture()
        try:
            report = inspect(manifest, root, False)
            self.assertEqual(report["alignedGlobalVersions"], 17)
            self.assertFalse(report["formalF9Ready"])
        finally:
            tmp.cleanup()

    def test_formal_rejects_missing_frozen_sha_and_approvals(self):
        tmp, root, manifest = self.fixture()
        try:
            report = inspect(manifest, root, True)
            self.assertFalse(report["formalF9Ready"])
            self.assertTrue(any("BATCH_NOT_FROZEN" in x for x in report["issues"]))
        finally:
            tmp.cleanup()

    def test_skew_missing_changelog_detected(self):
        tmp, root, manifest = self.fixture()
        try:
            meta = root / "DholeSystem" / "version.json"
            data = json.loads(meta.read_text())
            data["ecosystemVersion"] = "1.13.0"
            meta.write_text(json.dumps(data))
            (root / "DholeSystem" / "CHANGELOG.md").write_text("No matching version")
            report = inspect(manifest, root, False)
            self.assertEqual(report["alignedGlobalVersions"], 16)
            self.assertTrue(any("GLOBAL_VERSION_SKEW" in x for x in report["issues"]))
            self.assertTrue(any("CHANGELOG_VERSION_MISSING" in x for x in report["issues"]))
        finally:
            tmp.cleanup()


if __name__ == "__main__":
    unittest.main()
