#!/usr/bin/env python3
"""F7 C04/C05/C11 candidate chaos on a dedicated Docker Redis AOF volume.

Use ONLY from the GitHub-hosted isolated workflow. Never targets staging/prod,
does not require service credentials, and never approves the formal F7 gate.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import subprocess
import time
import uuid

import redis

RELEASE = "rt-20261107-01"


def require_isolation(container: str) -> None:
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise RuntimeError("Refuse live environments: only GitHub-hosted CI")
    if os.environ.get("RUNNER_ENVIRONMENT") != "github-hosted":
        raise RuntimeError("Refuse self-hosted runner or staging")
    if os.environ.get("F7_ISOLATED_CHAOS") != "true":
        raise RuntimeError("Missing explicit CI isolation opt-in")
    if not container.startswith("dhole-f7-ephemeral-"):
        raise RuntimeError("Refuse unmanaged Redis container")


def docker(*args: str) -> None:
    subprocess.run(["docker", *args], check=True, timeout=90, stdout=subprocess.DEVNULL)


def connect(port: int) -> redis.Redis:
    client = redis.Redis(host="127.0.0.1", port=port, socket_connect_timeout=2,
                         socket_timeout=2, decode_responses=True)
    for _ in range(60):
        try:
            if client.ping():
                return client
        except redis.RedisError:
            time.sleep(0.25)
    raise RuntimeError("Ephemeral Redis did not become ready")


def append_only_ready(r: redis.Redis) -> None:
    aof = r.config_get("appendonly")
    assert aof.get("appendonly") == "yes", f"AOF not active: {aof}"
    info = r.info("persistence")
    assert info["aof_enabled"] == 1, "AOF disabled"
    assert info["aof_last_write_status"] == "ok", "AOF write error"


def test_c04(r: redis.Redis, port: int, container: str, volume: str) -> tuple[redis.Redis, dict]:
    name = "dhole.f7.c04.redis-streams.ci"
    events = [str(uuid.uuid4()) for _ in range(10)]
    with r.pipeline(transaction=False) as batch:
        for event_id in events:
            batch.xadd(name, {"event_id": event_id, "release": RELEASE})
        batch.execute()
    before = {fields["event_id"] for _, fields in r.xrange(name)}
    assert before == set(events)
    append_only_ready(r)
    # A clean stop includes a final fsync. This proves normal persisted-restart
    # continuity, NOT disaster durability/backup of staging.
    docker("stop", "-t", "15", container)
    docker("rm", container)
    docker("run", "-d", "--name", container, "-p", f"127.0.0.1:{port}:6379",
           "-v", f"{volume}:/data", "redis:7-alpine",
           "redis-server", "--appendonly", "yes", "--appendfsync", "everysec")
    r = connect(port)
    append_only_ready(r)
    after = {fields["event_id"] for _, fields in r.xrange(name)}
    assert after == before, "C04: lost Redis stream event after restart"
    return r, {"candidate": "PASS", "restartIterations": 1, "eventsRetained": len(after),
               "fault": "Redis Docker container replaced with same private AOF volume"}


def test_c05(r: redis.Redis) -> dict:
    name, group = "dhole.f7.c05.unacked.ci", "realtime-isolated-bridge"
    r.xgroup_create(name, group, id="0-0", mkstream=True)
    seen = []
    for i in range(10):
        event_id = str(uuid.uuid4())
        r.xadd(name, {"event_id": event_id, "iteration": str(i)})
        claimed = r.xreadgroup(group, "gateway-died", {name: ">"}, count=1)
        assert len(claimed) == 1 and claimed[0][1][0][1]["event_id"] == event_id
        stream_id = claimed[0][1][0][0]
        # A consumer fails before ACK: exact pending entry is recovered, and
        # the consumer applies the effect only under Inbox SET NX identity.
        replay = r.xautoclaim(name, group, "gateway-recovered",
                              min_idle_time=0, start_id="0-0", count=100)
        matches = [(eid, values) for eid, values in replay[1]
                   if values.get("event_id") == event_id]
        assert len(matches) == 1 and matches[0][0] == stream_id
        inbox_key = f"dhole.f7.c05.inbox:{event_id}"
        assert r.set(inbox_key, "committed", nx=True) is True
        assert r.set(inbox_key, "committed", nx=True) is None, "duplicate side effect"
        assert r.xack(name, group, stream_id) == 1
        seen.append(event_id)
    assert len(set(seen)) == 10
    assert r.xpending(name, group)["pending"] == 0
    return {"candidate": "PASS", "iterations": 10, "acked": 10,
            "inboxDuplicateSideEffects": 0, "fault": "Crash-before-ACK / XAUTOCLAIM replay"}


def test_c11(r: redis.Redis) -> dict:
    name, group = "dhole.f7.c11.backlog.ci", "gateway-isolated-consumers"
    count = 1200
    r.xgroup_create(name, group, id="0-0", mkstream=True)
    event_ids = [str(uuid.uuid4()) for _ in range(count)]
    with r.pipeline(transaction=False) as batch:
        for eid in event_ids:
            batch.xadd(name, {"event_id": eid, "release": RELEASE})
        batch.execute()
    assert r.xlen(name) == count
    assert r.xpending(name, group)["pending"] == 0
    # Producer keeps adding; consumer is unavailable. Recovery must drain every
    # event exactly once without losing the backlog under batched processing.
    consumed: set[str] = set()
    total = 0
    for _ in range(30):
        frames = r.xreadgroup(group, "recovery", {name: ">"}, count=100)
        if not frames:
            break
        for stream, messages in frames:
            assert stream == name
            for stream_id, fields in messages:
                eid = fields["event_id"]
                assert eid not in consumed, "Duplicate effect during recovery"
                consumed.add(eid)
                total += r.xack(name, group, stream_id)
    assert len(consumed) == count and consumed == set(event_ids)
    assert total == count and r.xpending(name, group)["pending"] == 0
    return {"candidate": "PASS", "events": count, "acked": total,
            "missing": 0, "duplicateEffects": 0,
            "fault": "1200 events produced while consumer paused, then replayed"}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--container", required=True)
    parser.add_argument("--volume", required=True)
    parser.add_argument("--port", type=int, default=16389)
    parser.add_argument("--output", default="F7Results/isolated-redis-chaos.json")
    args = parser.parse_args()
    require_isolation(args.container)
    assert args.volume.startswith("dhole-f7-ephemeral-volume-")
    r = connect(args.port)
    append_only_ready(r)
    r, c04 = test_c04(r, args.port, args.container, args.volume)
    c05 = test_c05(r)
    c11 = test_c11(r)
    result = {
        "releaseId": RELEASE,
        "phase": "F7",
        "scope": "CI_EPHEMERAL_DOCKER_ONLY",
        "formalStagingEvidence": False,
        "f6FormalGatePassed": False,
        "f7FormalGatePassed": False,
        "collectedAtUtc": datetime.now(timezone.utc).isoformat(),
        "scenarios": {"C04": c04, "C05": c05, "C11": c11}
    }
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("F7_CI_EPHEMERAL_PASS C04=10 persisted events, 1 AOF restart; C05=10 Inbox ACK retries "
          "C11=1200 backlog drained; staging NOT checked; formal F7 0/14")


if __name__ == "__main__":
    main()
