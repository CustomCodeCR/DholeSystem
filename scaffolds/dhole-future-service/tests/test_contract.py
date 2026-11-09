import unittest
from pathlib import Path
import yaml

ROOT = Path(__file__).resolve().parents[1]

class FutureContract(unittest.TestCase):
    def test_owner_acl_and_transaction(self):
        code = (ROOT / "src/Dhole.FutureSample.Api/Program.cs").read_text()
        self.assertIn('RequireAuthorization("future.orders.view")', code)
        self.assertEqual(code.count('RequireAuthorization("future.orders.write")'), 2)
        self.assertIn("owner_id=@owner", code)
        self.assertIn("version=@expected", code)
        self.assertEqual(code.count("FutureOutbox.AppendAsync"), 2)
        self.assertEqual(code.count("await tx.CommitAsync(ct)"), 2)
        self.assertNotIn("MapHub", code)

    def test_event_identity_only_and_stream_ack_contract(self):
        code = (ROOT / "src/Dhole.FutureSample.Api/OutboxWorker.cs").read_text()
        self.assertIn("future.order.changed.v1", code)
        self.assertIn("audienceRef", code)
        self.assertIn("StreamAddAsync", code)
        self.assertIn("FOR UPDATE SKIP LOCKED", code)
        self.assertIn("await tx.CommitAsync(stoppingToken)", code)
        self.assertNotIn("clientSecret", code)
        manifest = yaml.safe_load((ROOT/"realtime.manifest.yaml").read_text())
        self.assertEqual(manifest["hub"], "DholeApiGateway")
        self.assertEqual(manifest["eventTransport"], "redis-streams")
        self.assertEqual(len(manifest["mutations"]), 2)

if __name__ == "__main__":
    unittest.main()
