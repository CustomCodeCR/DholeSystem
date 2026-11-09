import unittest
from verify_prod_redis_aof import evaluate, parse_persistence


class ProductionAofReadOnlyTests(unittest.TestCase):
    def setUp(self):
        self.container = {
            "Name": "/redis",
            "Config": {"Cmd": ["redis-server", "--appendonly", "yes",
                               "--appendfsync", "everysec"]},
            "Mounts": [{"Destination": "/data", "Type": "volume",
                        "RW": True, "Name": "redis-data"}],
        }
        self.info = {"aof_enabled": "1", "aof_last_write_status": "ok",
                     "aof_last_bgrewrite_status": "ok",
                     "aof_rewrite_in_progress": "0"}

    def test_healthy(self):
        data = evaluate(self.container, self.info)
        self.assertTrue(data["runtimeHealthy"])
        self.assertTrue(data["redisStartupAppendonlyArgumentVerified"])
        self.assertFalse(data["backupRestorationVerified"])

    def test_aof_disabled(self):
        self.assertFalse(evaluate(self.container,
                                 {**self.info, "aof_enabled": "0"})["runtimeHealthy"])

    def test_write_failure(self):
        self.assertFalse(evaluate(
            self.container, {**self.info, "aof_last_write_status": "err"})["runtimeHealthy"])

    def test_rewrite_running(self):
        self.assertFalse(evaluate(
            self.container, {**self.info, "aof_rewrite_in_progress": "1"})["runtimeHealthy"])

    def test_wrong_container(self):
        self.assertFalse(evaluate(
            {**self.container, "Name": "/dhole-staging-infra-redis-1"},
            self.info)["runtimeHealthy"])

    def test_no_persistent_volume(self):
        self.assertFalse(evaluate(
            {**self.container, "Mounts": []}, self.info)["runtimeHealthy"])

    def test_restart_not_proven_when_runtime_aof_set_dynamically(self):
        container = {**self.container, "Config": {"Cmd": ["redis-server"]}}
        data = evaluate(container, self.info)
        self.assertTrue(data["runtimeHealthy"])
        self.assertFalse(data["redisStartupAppendonlyArgumentVerified"])
        self.assertFalse(data["aofSurvivesRecreationVerified"])

    def test_parse_does_not_echo_payload(self):
        parsed = parse_persistence("# Persistence\n" +
                "aof_enabled:1\n" + "aof_last_write_status:ok\n")
        self.assertEqual(parsed["aof_enabled"], "1")


if __name__ == "__main__":
    unittest.main()
