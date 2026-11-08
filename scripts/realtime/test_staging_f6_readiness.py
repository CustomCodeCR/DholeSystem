import unittest
from staging_f6_readiness import NotReady, identify, redis_ready, persistence, PROJECT


class F6StagingReadinessTests(unittest.TestCase):
    def setUp(self):
        self.ready = {
            "aof_enabled": "1", "aof_last_write_status": "ok",
            "aof_last_bgrewrite_status": "ok",
            "aof_rewrite_in_progress": "0", "aof_rewrite_scheduled": "0",
            "aof_current_size": "4096",
        }
        self.cmd = ["redis-server", "--appendonly", "yes", "--appendfsync", "everysec"]

    def test_positive(self):
        self.assertTrue(redis_ready(self.ready, self.cmd))

    def test_aof_off(self):
        self.assertFalse(redis_ready({**self.ready, "aof_enabled": "0"}, self.cmd))

    def test_no_runtime_command(self):
        self.assertFalse(redis_ready(self.ready, ["redis-server", "--appendonly", "no"]))

    def test_aof_write_failure(self):
        self.assertFalse(redis_ready({**self.ready, "aof_last_write_status": "err"},
                                     self.cmd))

    def test_pending_rewrite(self):
        self.assertFalse(redis_ready({**self.ready, "aof_rewrite_in_progress": "1"},
                                     self.cmd))

    def test_rdb_only(self):
        self.assertFalse(redis_ready({"aof_enabled": "0", "aof_current_size": "0"},
                                     self.cmd))

    def test_parse_no_secrets(self):
        self.assertEqual(persistence("# Persistence\r\naof_enabled:0\r\n")["aof_enabled"],
                         "0")


if __name__ == "__main__":
    unittest.main()
