#!/usr/bin/env python3
"""Refuse an unsafe staging Redis restart before Docker Compose can recreate it.

Redis 7 AOF configured in the NEW Compose file does not convert a running
RDB-only dataset by itself. This read-only guard runs BEFORE compose pull/up.
Never inspects production Redis or prints secrets/events/host paths.
"""
from __future__ import annotations

import json
import subprocess
import sys

PROJECT = "dhole-staging-infra"
SERVICE = "redis"
VOLUME = "dhole-staging-infra_dhole-staging-redis"


class StagingAofNotReady(RuntimeError):
    pass


def inspect_persistence(info: str) -> dict[str, str]:
    values = {}
    for raw in info.splitlines():
        if raw.startswith("#") or ":" not in raw:
            continue
        key, value = raw.strip().split(":", 1)
        values[key] = value.strip()
    if values.get("aof_enabled") != "1":
        raise StagingAofNotReady("Staging Redis AOF is OFF; do not recreate RDB-only Redis.")
    if values.get("aof_last_write_status") != "ok":
        raise StagingAofNotReady("Staging Redis AOF last write is not OK.")
    if values.get("aof_last_bgrewrite_status") != "ok":
        raise StagingAofNotReady("Staging Redis initial AOF rewrite not confirmed.")
    if values.get("aof_rewrite_in_progress") != "0":
        raise StagingAofNotReady("Staging Redis AOF rewrite still active.")
    if values.get("aof_rewrite_scheduled") not in ("0", None):
        raise StagingAofNotReady("Staging Redis AOF rewrite scheduled.")
    try:
        if int(values.get("aof_current_size", "0")) < 1:
            raise StagingAofNotReady("Staging Redis AOF file is empty.")
    except ValueError as exc:
        raise StagingAofNotReady("Staging Redis invalid AOF size.") from exc
    return values


def check_mounts(mounts: list[dict]) -> None:
    matches = [entry for entry in mounts if entry.get("Destination") == "/data"]
    if len(matches) != 1 or matches[0].get("Type") != "volume" or (
        matches[0].get("Name") != VOLUME or matches[0].get("RW") is not True
    ):
        raise StagingAofNotReady("Staging Redis data volume identity is not verified.")


def command(*args: str) -> str:
    try:
        result = subprocess.run(
            list(args), text=True, capture_output=True, timeout=15, check=False
        )
    except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
        raise StagingAofNotReady("Docker staging audit command unavailable.") from exc
    if result.returncode != 0:
        raise StagingAofNotReady("Docker staging audit command failed.")
    return result.stdout.strip()


def verify() -> None:
    ids = command(
        "docker", "ps", "-q",
        "--filter", f"label=com.docker.compose.project={PROJECT}",
        "--filter", f"label=com.docker.compose.service={SERVICE}",
    ).splitlines()
    if len(ids) != 1 or not ids[0].strip():
        raise StagingAofNotReady("Exactly one running staging Redis required.")
    container = ids[0].strip()
    labels = json.loads(command(
        "docker", "inspect", "--format", "{{json .Config.Labels}}", container
    ))
    if labels.get("com.docker.compose.project") != PROJECT or (
        labels.get("com.docker.compose.service") != SERVICE
    ):
        raise StagingAofNotReady("Container belongs to an unexpected environment.")
    mounts = json.loads(command(
        "docker", "inspect", "--format", "{{json .Mounts}}", container
    ))
    check_mounts(mounts)
    info = command("docker", "exec", container, "redis-cli", "--raw", "INFO", "persistence")
    inspect_persistence(info)
    print("STAGING_REDIS_AOF_PRE_DEPLOY_PASS: exact staging identity, persistent volume, "
          "enabled/steady-state AOF. This does NOT verify off-host backups/restore.")


def main() -> int:
    try:
        verify()
        return 0
    except (StagingAofNotReady, ValueError, KeyError, TypeError, json.JSONDecodeError) as error:
        # Avoid printing subprocess stderr (may contain secrets).
        print("STAGING_REDIS_PRE_DEPLOY_BLOCKED:", error, file=sys.stderr)
        print("Run the reviewed RDB-to-AOF migration with independently tested backup "
              "before restarting staging Redis. Production is never inspected.",
              file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
