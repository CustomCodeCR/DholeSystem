#!/usr/bin/env python3
"""F6/F9: non-mutating, fail-closed inspection of actual staging persistence.

Only reads exact dhole-staging-infra Redis/PostgreSQL Compose services.
Never executes CONFIG SET/BGSAVE/SAVE, Docker Compose up or a production command.
No secrets, raw Redis values, host paths or container configuration are logged.
"""
from __future__ import annotations
import json
import subprocess
import sys
from pathlib import Path

PROJECT = "dhole-staging-infra"
REDIS_VOLUME = "dhole-staging-infra_dhole-staging-redis"
POSTGRES_VOLUME = "dhole-staging-infra_dhole-staging-postgres"


class NotReady(RuntimeError):
    pass


def run(*args: str) -> str:
    try:
        p = subprocess.run(args, capture_output=True, text=True, timeout=18, check=False)
    except (FileNotFoundError, subprocess.TimeoutExpired) as exc:
        raise NotReady("Docker introspection unavailable") from exc
    if p.returncode:
        raise NotReady("Staging Docker introspection failed")
    return p.stdout.strip()


def single(service: str) -> str:
    ids = run("docker", "ps", "-q",
              "--filter", f"label=com.docker.compose.project={PROJECT}",
              "--filter", f"label=com.docker.compose.service={service}").splitlines()
    if len(ids) != 1 or not ids[0]:
        raise NotReady(f"Expected exactly one running {service} in the staging infra project")
    return ids[0]


def identify(container: str, service: str, volume: str, destination: str) -> dict:
    data = json.loads(run("docker", "inspect", "--format",
                          "{{json .}}", container))
    labels = data.get("Config", {}).get("Labels") or {}
    if labels.get("com.docker.compose.project") != PROJECT or (
        labels.get("com.docker.compose.service") != service
    ):
        raise NotReady("Unexpected Docker project/service identity")
    mounts = [v for v in data.get("Mounts", []) if v.get("Destination") == destination]
    if len(mounts) != 1 or mounts[0].get("Type") != "volume" or (
        mounts[0].get("Name") != volume or mounts[0].get("RW") is not True
    ):
        raise NotReady("Persistent staging volume identity not verified")
    return data


def persistence(raw: str) -> dict[str, str]:
    return dict(row.strip().split(":", 1) for row in raw.splitlines()
                if ":" in row and not row.startswith("#"))


def redis_ready(values: dict[str, str], command: list[str]) -> bool:
    return (
        values.get("aof_enabled") == "1"
        and values.get("aof_last_write_status") == "ok"
        and values.get("aof_last_bgrewrite_status") == "ok"
        and values.get("aof_rewrite_in_progress") == "0"
        and values.get("aof_rewrite_scheduled", "0") == "0"
        and values.get("aof_current_size", "0").isdigit()
        and int(values["aof_current_size"]) > 0
        and "--appendonly" in command
        and command.index("--appendonly") + 1 < len(command)
        and command[command.index("--appendonly") + 1] == "yes"
    )


def collect() -> dict:
    redis = single("redis")
    postgres = single("postgres")
    redis_meta = identify(redis, "redis", REDIS_VOLUME, "/data")
    identify(postgres, "postgres", POSTGRES_VOLUME, "/var/lib/postgresql/data")
    p = persistence(run("docker", "exec", redis, "redis-cli", "--raw",
                        "INFO", "persistence"))
    cmd = redis_meta.get("Config", {}).get("Cmd") or []
    live_aof = p.get("aof_enabled") == "1"
    configured_aof = ("--appendonly" in cmd
                      and cmd.index("--appendonly") + 1 < len(cmd)
                      and cmd[cmd.index("--appendonly") + 1] == "yes")
    good = redis_ready(p, cmd)
    return {
        "releaseId": "rt-20261107-01",
        "environment": "staging",
        "readOnly": True,
        "productionTouched": False,
        "exactStagingRedisAndPostgresVolumes": True,
        "redisRuntimeAofEnabled": live_aof,
        "redisContainerCommandAppendonlyYes": configured_aof,
        "redisAofWriteOk": p.get("aof_last_write_status") == "ok",
        "redisAofInitialRewriteComplete": (p.get("aof_last_bgrewrite_status") == "ok"
                                             and p.get("aof_rewrite_in_progress") == "0"),
        "redisAofReadyForSafeCompose": good,
        "offHostBackupRestoreVerified": False,
        "stagingF7ChaosVerified": False,
        "formalF9Ready": False,
        "unverifiedDependency": "Backup restoration and 14/14 formal chaos require separate evidence",
    }


def main() -> int:
    try:
        report = collect()
    except (NotReady, ValueError, KeyError, IndexError, TypeError,
            json.JSONDecodeError) as exc:
        print(f"F6_STAGING_READONLY_BLOCKED: {exc}", file=sys.stderr)
        return 2
    path = Path("F6Results/staging-live-readonly-preflight.json")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print("F6_STAGING_READONLY:", {key: value for key, value in report.items()
                                    if isinstance(value, bool)})
    if not report["redisAofReadyForSafeCompose"]:
        print("F6_STAGING_AOF_BLOCKED: running Redis is not AOF-ready; "
              "do not redeploy RDB-only volume with AOF command", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
