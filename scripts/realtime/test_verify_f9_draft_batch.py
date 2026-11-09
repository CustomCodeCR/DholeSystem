import copy
import unittest
from verify_f9_draft_batch import inspect


class F9DraftTests(unittest.TestCase):
    def setUp(self):
        self.repositories = [{"name": "CustomCodeCR/Test" + str(n)} for n in range(17)]
        self.manifest = {
            "releaseId": "rt-20261107-01",
            "repositories": self.repositories,
            "promotion": {"developPRs": []},
        }
        self.roster = {
            "releaseId": "rt-20261107-01",
            "sourceBranch": "feature/dhole-realtime-universal-rt-20261107-01",
            "targetBranch": "develop",
            **{k: False for k in (
                "mergeAuthorized", "formalF9Complete", "sourceGatesF0ToF8Approved",
                "globalEcosystemVersionAligned", "all17FinalShasFrozen", "stagingValidated")},
            "pullRequests": [{
                "repository": p["name"], "number": n + 1,
                "url": f"https://github.com/{p['name']}/pull/{n+1}",
                "state": "DRAFT", "mergeAuthorized": False,
            } for n, p in enumerate(self.repositories)],
        }

    def test_exact_17_drafts(self):
        self.assertEqual(inspect(self.manifest, self.roster), 17)

    def test_duplicate_repo_fails(self):
        data = copy.deepcopy(self.roster)
        data["pullRequests"][1]["repository"] = data["pullRequests"][0]["repository"]
        with self.assertRaises(ValueError):
            inspect(self.manifest, data)

    def test_approval_cannot_be_claimed(self):
        data = copy.deepcopy(self.roster)
        data["formalF9Complete"] = True
        with self.assertRaises(ValueError):
            inspect(self.manifest, data)

    def test_version_alignment_alone_does_not_approve_f9(self):
        data = copy.deepcopy(self.roster)
        data["globalEcosystemVersionAligned"] = True
        self.assertEqual(inspect(self.manifest, data), 17)

    def test_wrong_base_fails(self):
        data = copy.deepcopy(self.roster)
        data["targetBranch"] = "master"
        with self.assertRaises(ValueError):
            inspect(self.manifest, data)

    def test_pr_url_cannot_target_other_repo(self):
        data = copy.deepcopy(self.roster)
        data["pullRequests"][0]["url"] = "https://example.com/"
        with self.assertRaises(ValueError):
            inspect(self.manifest, data)


if __name__ == "__main__":
    unittest.main()
