#!/usr/bin/env python3
"""Positive/negative F8 PR checks. All fixtures disposable; no target refs."""
from __future__ import annotations

import importlib.util
from pathlib import Path
import shutil
import tempfile
import unittest

import yaml

ROOT = Path(__file__).resolve().parents[2]
SAMPLE = ROOT / "scaffolds/dhole-future-service"
REGISTRY = ROOT / "docs/realtime/service-registry.yaml"
POLICY = ROOT / "scripts/realtime/verify-f8-future-service.py"
spec = importlib.util.spec_from_file_location("future_policy", POLICY)
assert spec is not None and spec.loader is not None
policy = importlib.util.module_from_spec(spec)
spec.loader.exec_module(policy)


class FuturePolicyTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory(prefix="dhole-f8-")
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name) / "service"
        shutil.copytree(SAMPLE, self.root)
        self.manifest = self.root / "realtime.manifest.yaml"
        self.program = self.root / "src/Dhole.FutureSample.Api/Program.cs"
        self.worker = self.root / "src/Dhole.FutureSample.Api/OutboxWorker.cs"

    def check(self) -> list[str]:
        return policy.validate(self.root, registry=REGISTRY)

    def change_manifest(self, callback) -> None:
        data = yaml.safe_load(self.manifest.read_text())
        callback(data)
        self.manifest.write_text(yaml.safe_dump(data, sort_keys=False))

    def test_positive_complete_sample_passes_with_registry(self):
        self.assertEqual(self.check(), [])
        discovered, workers, problems = policy.source_inventory(self.root)
        self.assertEqual(len(discovered), 2)
        self.assertEqual(len(workers), 1)
        self.assertEqual(problems, [])

    def test_negative_new_unmapped_mutation_fails(self):
        self.program.write_text(self.program.read_text() +
            '\norders.MapDelete("/{id:guid}", () => Results.NoContent());\n')
        self.assertTrue(any("Unmapped mutable route" in v for v in self.check()))

    def test_negative_new_worker_without_manifest_fails(self):
        source = self.root / "src/Dhole.FutureSample.Api/NewInvoiceWorker.cs"
        source.write_text("public class NewInvoiceWorker : BackgroundService { }")
        self.assertTrue(any("Unmapped background worker" in v for v in self.check()))

    def test_negative_dynamic_mapmethods_is_not_silently_ignored(self):
        self.program.write_text(self.program.read_text() +
            '\norders.MapMethods("/private", new[] {"POST","DELETE"}, () => Results.Ok());\n')
        errors = self.check()
        self.assertTrue(any("MapMethods" in v for v in errors))

    def test_negative_missing_integration_test_file_fails(self):
        self.change_manifest(lambda d: d["mutations"][0].update(
            integrationTest="tests/does-not-exist.py"))
        self.assertTrue(any("Missing test source integrationTest" in v for v in self.check()))

    def test_negative_missing_authorization_scope_fails(self):
        self.change_manifest(lambda d: d["mutations"][0].update(scope=""))
        self.assertTrue(any("Missing mutation scope" in v for v in self.check()))

    def test_negative_missing_outbox_opt_in_fails(self):
        self.change_manifest(lambda d: d["outbox"].update(sameTransactionAsMutation=False))
        self.assertTrue(any("sameTransactionAsMutation" in v for v in self.check()))

    def test_negative_false_exemption_does_not_bypass(self):
        self.program.write_text(self.program.read_text() +
            '\norders.MapDelete("/cancel", () => Results.Ok());\n')
        self.change_manifest(lambda d: d["exceptions"].append({
            "source":"src/Dhole.FutureSample.Api/Program.cs",
            "verb":"DELETE", "routeLiteral":"/cancel",
            "approved":False, "signedAdr":"docs/ADRs/9999.md",
            "approvedBy":"unknown"
        }))
        errors=self.check()
        self.assertTrue(any("Unmapped mutable route" in v for v in errors))
        self.assertTrue(any("Unapproved exception" in v for v in errors))

    def test_negative_rogue_hub_is_forbidden(self):
        self.program.write_text(self.program.read_text() +
            '\napp.MapHub<AnotherHub>("/hubs/new");\n')
        self.assertTrue(any("new Hub is prohibited" in v for v in self.check()))

    def test_negative_stale_manifest_entry_fails(self):
        self.program.write_text(self.program.read_text().replace(
            'orders.MapPatch("/{id:guid}"', 'orders.MapPatch("/v2/{id:guid}"'))
        errors = self.check()
        self.assertTrue(any("Stale/imaginary route" in v for v in errors))
        self.assertTrue(any("Unmapped mutable route" in v for v in errors))

    def test_negative_mismatched_registry_fails(self):
        self.change_manifest(lambda d: d["service"].update(repo="CustomCodeCR/UnregisteredOther"))
        self.assertTrue(any("central registry" in v for v in self.check()))

    def test_negative_unauthorized_second_hub_fails(self):
        self.change_manifest(lambda d: d.update(hub="DholeFutureSample"))
        self.assertTrue(any("Only central" in v for v in self.check()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
