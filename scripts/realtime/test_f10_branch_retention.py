import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
WORKFLOW = ROOT / ".github/workflows/deploy-production.yml"


class F10BranchRetentionTests(unittest.TestCase):
    def test_production_deploy_never_deletes_release_branches(self):
        content = WORKFLOW.read_text(encoding="utf-8")
        self.assertNotIn("git push origin --delete", content)
        self.assertNotIn("git push --force", content)
        self.assertNotIn("git branch -D", content)

    def test_read_only_repository_permission(self):
        content = WORKFLOW.read_text(encoding="utf-8")
        self.assertIn("permissions:\n  contents: read", content)

    def test_f10_preflight_remains_before_prod_mutation(self):
        content = WORKFLOW.read_text(encoding="utf-8")
        self.assertLess(
            content.index("python3 scripts/realtime/verify_f10_production_preflight.py"),
            content.index("bash deploy/prepare-environments.sh"))


if __name__ == "__main__":
    unittest.main()
