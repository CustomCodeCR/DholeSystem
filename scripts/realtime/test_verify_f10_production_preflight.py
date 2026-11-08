import copy
import unittest
from verify_f10_production_preflight import verify, REQUIRED


class F10ProductionGuardTests(unittest.TestCase):
    def setUp(self):
        self.payload = {
            "schemaVersion": 1, "releaseId": "rt-20261107-01",
            "targetBranch": "master", "productionDeploymentExecuted": False,
            **{name: True for name in REQUIRED},
        }

    def test_complete_staging_approval_allows_deployment(self):
        self.assertTrue(verify(self.payload, "master", "CustomCodeCR/DholeSystem"))

    def test_any_missing_gate_blocks(self):
        for name in REQUIRED:
            data = copy.deepcopy(self.payload)
            data[name] = False
            with self.subTest(name=name), self.assertRaises(ValueError):
                verify(data, "master", "CustomCodeCR/DholeSystem")

    def test_wrong_branch_blocks(self):
        with self.assertRaises(ValueError):
            verify(self.payload, "develop", "CustomCodeCR/DholeSystem")

    def test_wrong_repo_blocks(self):
        with self.assertRaises(ValueError):
            verify(self.payload, "master", "CustomCodeCR/Other")

    def test_claiming_deployed_before_deploy_blocks(self):
        data = copy.deepcopy(self.payload)
        data["productionDeploymentExecuted"] = True
        with self.assertRaises(ValueError):
            verify(data, "master", "CustomCodeCR/DholeSystem")


if __name__ == "__main__":
    unittest.main()
