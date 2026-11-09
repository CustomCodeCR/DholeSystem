#!/usr/bin/env python3
"""F8 generator positive/negative tests, no Git refs or deployment touched."""
from __future__ import annotations
import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]

def load(filename: str, name: str):
    spec = importlib.util.spec_from_file_location(name, ROOT / "scripts/realtime" / filename)
    assert spec is not None and spec.loader is not None
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module

generator = load("scaffold-future-service.py", "scaffolder")
validator = load("verify-f8-future-service.py", "validator")

class ScaffoldTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix="dhole-f8-generator-")
        self.addCleanup(self.tmp.cleanup)
        self.target = Path(self.tmp.name) / "DholeBillingService"

    def generate(self):
        generator.scaffold(name="DholeBillingService", domain="billing",
                           service_id="S15", owner="PlatformTeam", version="1.14.0",
                           target=self.target)

    def test_positive_generated_service_is_consistent_and_registered_proposal(self):
        self.generate()
        manifest = self.target / "realtime.manifest.yaml"
        source = self.target / "src/Dhole.Billing.Api/Program.cs"
        worker = self.target / "src/Dhole.Billing.Api/OutboxWorker.cs"
        dotnet = self.target / "src/Dhole.Billing.Api/Dhole.Billing.Api.csproj"
        tests = self.target / "tests/Billing.IntegrationHarness/Billing.IntegrationHarness.csproj"
        self.assertTrue(all(x.is_file() for x in (manifest, source, worker, dotnet, tests)))
        self.assertTrue((self.target/".github/workflows/realtime-future-enforcement.yml").is_file())
        registry = self.target / "central-registry.PROPOSAL.yaml"
        self.assertEqual(validator.validate(self.target, registry=registry), [])
        self.assertIn("1.14.0", manifest.read_text())
        self.assertIn("1.14.0", dotnet.read_text())
        self.assertIn("billing.order.changed.v1", worker.read_text())
        self.assertNotIn("future.order.changed.v1", worker.read_text())
        self.assertNotIn("DholeFutureSample", source.read_text())
        self.assertNotIn("DholeFutureSample", manifest.read_text())

    def test_refuses_to_overwrite_existing_checkout(self):
        self.generate()
        self.assertRaises(ValueError, self.generate)

    def test_refuses_existing_legacy_service_identifier(self):
        with self.assertRaises(ValueError):
            generator.scaffold(name="DholeBillingService", domain="billing",
                service_id="S13", owner="PlatformTeam", version="1.14.0",
                target=self.target)

    def test_refuses_invalid_version_and_name(self):
        for name, version in (("DholeBillingService","1.14"),("foo","1.14.0")):
            with self.assertRaises(ValueError):
                generator.scaffold(name=name, domain="billing",service_id="S15",
                    owner="PlatformTeam",version=version,target=self.target)

if __name__ == "__main__":
    unittest.main(verbosity=2)
