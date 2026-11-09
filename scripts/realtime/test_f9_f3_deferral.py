#!/usr/bin/env python3
"""Negative tests ensure a F3 evidence waiver cannot silently become release approval."""
from copy import deepcopy
from datetime import date
from importlib.util import module_from_spec, spec_from_file_location
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[2]
spec = spec_from_file_location("f9_f3_waiver", ROOT / "scripts/realtime/verify-f9-f3-deferral.py")
mod = module_from_spec(spec)
spec.loader.exec_module(mod)


class ScopedF3ReviewExceptionTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.good = json.loads((ROOT / "docs/realtime/f9-f3-staging-deferral.json").read_text())
        cls.gates = (ROOT / "docs/realtime/gate-evidence.f0-f4.yaml").read_text()

    def test_valid_exception_is_review_only(self):
        mod.verify_review(deepcopy(self.good), date(2026, 11, 9), self.gates)

    def test_expired_exception_fails(self):
        data = deepcopy(self.good)
        data["expiresOn"] = "2026-11-08"
        with self.assertRaises(ValueError):
            mod.verify_review(data, date(2026, 11, 9), self.gates)

    def test_wrong_gateway_sha_fails(self):
        data = deepcopy(self.good)
        data["proof"]["gatewayTestedCommit"] = "0" * 40
        with self.assertRaises(ValueError):
            mod.verify_review(data, date(2026, 11, 9), self.gates)

    def test_wrong_ci_run_fails(self):
        data = deepcopy(self.good)
        data["proof"]["gatewayCiRun"] = "https://github.com/CustomCodeCR/DholeApiGateway/actions/runs/1"
        with self.assertRaises(ValueError):
            mod.verify_review(data, date(2026, 11, 9), self.gates)

    def test_scope_merge_fails(self):
        data = deepcopy(self.good)
        data["scope"] = "F9_MERGE_ALLOWED"
        with self.assertRaises(ValueError):
            mod.verify_review(data, date(2026, 11, 9), self.gates)

    def test_runtime_enabled_fails(self):
        data = deepcopy(self.good)
        data["compensatingControls"]["runtimeUniversalRealtimeEnabled"] = True
        with self.assertRaises(ValueError):
            mod.verify_review(data, date(2026, 11, 9), self.gates)

    def test_merge_authorized_fails(self):
        data = deepcopy(self.good)
        data["compensatingControls"]["f9MergeAuthorized"] = True
        with self.assertRaises(ValueError):
            mod.verify_review(data, date(2026, 11, 9), self.gates)

    def test_staging_approval_claim_fails(self):
        data = deepcopy(self.good)
        data["proof"]["realStagingOwnerAclVerified"] = True
        with self.assertRaises(ValueError):
            mod.verify_review(data, date(2026, 11, 9), self.gates)

    def test_formal_f3_gate_cannot_be_rewritten(self):
        with self.assertRaises(ValueError):
            mod.verify_review(deepcopy(self.good), date(2026, 11, 9),
                              self.gates.replace("    approval: false", "    approval: true"))

    def test_signature_replaced_cannot_self_approve(self):
        data = deepcopy(self.good)
        data["signoff"]["formalAcceptance"] = True
        with self.assertRaises(ValueError):
            mod.verify_review(data, date(2026, 11, 9), self.gates)


if __name__ == "__main__":
    unittest.main()
