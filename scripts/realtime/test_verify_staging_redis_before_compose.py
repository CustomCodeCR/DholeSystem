import unittest
from verify_staging_redis_before_compose import (
    inspect_persistence, check_mounts, StagingAofNotReady, VOLUME
)

GOOD = ("aof_enabled:1\n"
        "aof_last_write_status:ok\n"
        "aof_last_bgrewrite_status:ok\n"
        "aof_rewrite_in_progress:0\n"
        "aof_rewrite_scheduled:0\n"
        "aof_current_size:1024\n")


class StagingRedisGuardTests(unittest.TestCase):
    def test_good_ready_aof(self):
        self.assertEqual(inspect_persistence(GOOD)["aof_enabled"], "1")
        check_mounts([{"Destination": "/data", "Type": "volume",
                       "Name": VOLUME, "RW": True}])

    def test_aof_off_fails(self):
        with self.assertRaises(StagingAofNotReady):
            inspect_persistence(GOOD.replace("aof_enabled:1", "aof_enabled:0"))

    def test_aof_write_failure_fails(self):
        with self.assertRaises(StagingAofNotReady):
            inspect_persistence(GOOD.replace("aof_last_write_status:ok",
                                             "aof_last_write_status:err"))

    def test_initial_rewrite_pending_fails(self):
        with self.assertRaises(StagingAofNotReady):
            inspect_persistence(GOOD.replace("aof_rewrite_in_progress:0",
                                             "aof_rewrite_in_progress:1"))

    def test_aof_size_zero_fails(self):
        with self.assertRaises(StagingAofNotReady):
            inspect_persistence(GOOD.replace("aof_current_size:1024",
                                             "aof_current_size:0"))

    def test_wrong_volume_fails(self):
        with self.assertRaises(StagingAofNotReady):
            check_mounts([{"Destination": "/data", "Type": "volume",
                           "Name": "dhole-production_redis", "RW": True}])

    def test_unmounted_or_bind_data_fails(self):
        with self.assertRaises(StagingAofNotReady):
            check_mounts([])
        with self.assertRaises(StagingAofNotReady):
            check_mounts([{"Destination": "/data", "Type": "bind",
                           "Name": VOLUME, "RW": True}])


if __name__ == "__main__":
    unittest.main()
