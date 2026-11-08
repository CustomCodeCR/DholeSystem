#!/usr/bin/env python3
"""F6 staged AOF migration REHEARSAL on GitHub-hosted disposable Redis only.

Tests migration *from* appendonly=no with real existing RDB data. Does not
connect to dhole-staging or change a live container; formal infra gate stays OFF.
"""
from __future__ import annotations
import json
import os
from pathlib import Path
import subprocess
import time
from datetime import datetime, timezone
import redis


def docker(*args: str) -> None:
    subprocess.run(["docker", *args], check=True, timeout=90, stdout=subprocess.DEVNULL)


def check(name: str, volume: str) -> None:
    assert os.environ.get("GITHUB_ACTIONS") == "true"
    assert os.environ.get("RUNNER_ENVIRONMENT") == "github-hosted"
    assert os.environ.get("F6_AOF_REHEARSAL") == "true"
    assert name.startswith("dhole-f6-aof-rehearsal-")
    assert volume.startswith("dhole-f6-aof-rehearsal-volume-")


def connect() -> redis.Redis:
    r = redis.Redis(host="127.0.0.1", port=16390, decode_responses=True,
                    socket_timeout=2, socket_connect_timeout=2)
    for i in range(60):
        try:
            if r.ping():
                return r
        except redis.RedisError:
            time.sleep(0.3)
    raise RuntimeError("Ephemeral Redis not ready")


def launch(name: str, volume: str, aof: bool) -> redis.Redis:
    docker("run", "-d", "--name", name, "-p", "127.0.0.1:16390:6379",
           "-v", volume + ":/data", "redis:7-alpine", "redis-server",
           "--appendonly", "yes" if aof else "no",
           "--appendfsync", "everysec")
    return connect()


def restart(name: str, volume: str, aof: bool) -> redis.Redis:
    docker("stop", "-t", "15", name)
    docker("rm", name)
    return launch(name, volume, aof)


def verify(r: redis.Redis, expected_ids: set[str]) -> None:
    records = [data["event_id"] for _, data in r.xrange("dhole.f6.aof.rehearsal")]
    assert len(records) == len(expected_ids), "Lost Redis stream entries"
    assert set(records) == expected_ids, "Redis stream changed across AOF migration"
    assert r.get("dhole.f6.aof.rehearsal:control") == "safe"
    assert int(r.info("persistence")["aof_enabled"]) == 1
    assert r.info("persistence")["aof_last_write_status"] == "ok"


def main() -> None:
    name = "dhole-f6-aof-rehearsal-" + os.environ["GITHUB_RUN_ID"]
    volume = "dhole-f6-aof-rehearsal-volume-" + os.environ["GITHUB_RUN_ID"]
    check(name, volume)
    ids = {f"test-event-{i:04d}" for i in range(100)}
    try:
        docker("volume", "create", volume)
        r = launch(name, volume, False)
        assert r.config_get("appendonly")["appendonly"] == "no"
        with r.pipeline(transaction=False) as pipe:
            for eid in sorted(ids):
                pipe.xadd("dhole.f6.aof.rehearsal", {"event_id": eid})
            pipe.set("dhole.f6.aof.rehearsal:control", "safe")
            pipe.execute()
        assert r.save() is True, "RDB baseline must be created before migration"
        assert r.info("persistence")["rdb_last_bgsave_status"] == "ok"
        # Redis 7 MUST convert the *running* dataset into a multi-part AOF
        # BEFORE restarting with appendonly=yes. Switching the compose command
        # directly on an RDB-only volume can start from an empty AOF and lose
        # the existing Streams; the initial red test caught this.
        assert r.config_set("appendonly", "yes"), "AOF runtime transition rejected"
        for retry in range(120):
            state = r.info("persistence")
            if (int(state["aof_enabled"]) == 1
                    and int(state["aof_rewrite_in_progress"]) == 0
                    and state["aof_last_bgrewrite_status"] == "ok"
                    and int(state["aof_current_size"]) > 0
                    and state["aof_last_write_status"] == "ok"):
                break
            time.sleep(0.25)
        else:
            raise RuntimeError("AOF initial rewrite never became durable; refuse restart")
        verify(r, ids)
        # Only now can the Compose command be switched to appendonly=yes.
        r = restart(name, volume, True)
        verify(r, ids)
        # Verify newly appended changes survive a second container replacement.
        r.xadd("dhole.f6.aof.rehearsal", {"event_id": "post-aof-commit"})
        r = restart(name, volume, True)
        verify(r, ids | {"post-aof-commit"})
        result = {
            "releaseId": "rt-20261107-01",
            "phase": "F6",
            "environment": "GITHUB_HOSTED_EPHEMERAL",
            "preMigrationAofEnabled": False,
            "postMigrationAofEnabled": True,
            "onlineAofConversionBeforeContainerReplacement": True,
            "persistentEventsBefore": 100,
            "persistentEventsAfter": 101,
            "containerReplacements": 2,
            "redisAofWriteOk": True,
            "realStagingRedisTouched": False,
            "stagingBackupRestoreVerified": False,
            "formalF6Approved": False,
            "status": "CI_REHEARSAL_PASS",
            "testedAtUtc": datetime.now(timezone.utc).isoformat(),
        }
        output = Path("F6Results/aof-off-to-on-rehearsal.json")
        output.parent.mkdir(exist_ok=True)
        output.write_text(json.dumps(result, indent=2) + "\n")
        print("AOF_MIGRATION_REHEARSAL_PASS: 100 old events + 1 post-AOF event retained")
    finally:
        subprocess.run(["docker", "rm", "-f", name], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, timeout=40)
        subprocess.run(["docker", "volume", "rm", volume], stdout=subprocess.DEVNULL,
                       stderr=subprocess.DEVNULL, timeout=40)


if __name__ == "__main__":
    main()
