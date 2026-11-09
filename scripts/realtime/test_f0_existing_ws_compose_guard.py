import unittest
from f0_existing_ws_compose_guard import must


class WsReusePolicyTests(unittest.TestCase):
    def test_positive_invariant(self):
        must(True, "existing WS")
    def test_missing_hub_rejected(self):
        with self.assertRaisesRegex(ValueError, "NotificationsHub"):
            must(False, "NotificationsHub")
    def test_missing_aof_rejected(self):
        with self.assertRaisesRegex(ValueError, "Redis AOF"):
            must(False, "Redis AOF")
    def test_disallowed_feature_flag_rejected(self):
        with self.assertRaises(ValueError):
            must(False, "flags default OFF")


if __name__ == "__main__":
    unittest.main()
