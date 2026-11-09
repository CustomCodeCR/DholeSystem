#!/usr/bin/env python3
"""Read-only inspection of production Redis AOF, with sanitized evidence.

Never calls CONFIG SET, SAVE, BGSAVE, restart, docker compose, or changes flags.
This DOES NOT establish a tested backup restore or prove restart persistence.
"""
from __future__ import annotations

from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess
import sys

CONTAINER = "redis"
RELEASE = "rt-20261107-01"
OUTPUT = Path("F6Results/production-live-readonly-aof.json")


def parse_persistence(raw: str) -> dict[str, str]:
    return dict(line.strip().split(":", 1) for line in raw.splitlines()
                if ":" in line and not line.startswith("#"))


def evaluate(container: dict, info: dict[str, str]) -> dict:
    name = container.get("Name")
    mounts = container.get("Mounts") or []
    command = container.get("Config", {}).get("Cmd") or []
    aof_arg = "--appendonly" in command
    restart_configured = (
        aof_arg and command.index("--appendonly") + 1 < len(command)
        and command[command.index("--appendonly") + 1] == "yes"
    )
    persist_volume = any(m.get("Destination") == "/data"
                         and m.get("Type") == "volume"
                         and m.get("RW") is True for m in mounts)
    status = {
        "releaseId": RELEASE,
        "environment": "production",
        "readOnly": True,
        "productionModified": False,
        "redisContainerIdentityVerified": name == "/" + CONTAINER,
        "redisDataVolumePersistent": persist_volume,
        "redisRuntimeAofEnabled": info.get("aof_enabled") == "1",
        "redisAofWriteHealthy": info.get("aof_last_write_status") == "ok",
        "redisAofRewriteHealthy": info.get("aof_last_bgrewrite_status") == "ok",
        "redisAofRewriteIdle": info.get("aof_rewrite_in_progress") == "0",
        "redisStartupAppendonlyArgumentVerified": bool(restart_configured),
        "backupRestorationVerified": False,
        "aofSurvivesRecreationVerified": False,
    }
    status["runtimeHealthy"] = all(status[key] for key in (
        "redisContainerIdentityVerified", "redisDataVolumePersistent",
        "redisRuntimeAofEnabled", "redisAofWriteHealthy",
        "redisAofRewriteHealthy", "redisAofRewriteIdle"))
    return status


def run(*argv: str) -> str:
    result = subprocess.run(argv, capture_output=True, text=True, timeout=18,
                            check=False)
    if result.returncode != 0:
        raise RuntimeError("Read-only Docker/Redis introspection failed")
    return result.stdout


def main() -> int:
    try:
        data = json.loads(run("docker", "inspect", "--format", "{{json .}}", CONTAINER))
        info = parse_persistence(run("docker", "exec", CONTAINER,
                                     "redis-cli", "--raw", "INFO", "persistence"))
        result = evaluate(data, info)
        result["observedAtUtc"] = datetime.now(timezone.utc).isoformat()
    except (OSError, RuntimeError, subprocess.TimeoutExpired, ValueError,
            json.JSONDecodeError) as exc:
        print("PROD_AOF_READONLY_FAILED: sanitized inspection unavailable", file=sys.stderr)
        return 2
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("PROD_AOF_READONLY:", {key: value for key, value in result.items()
                                 if isinstance(value, bool)})
    if not result["runtimeHealthy"]:
        print("PROD_AOF_NOT_READY: runtime AOF/volume check failed", file=sys.stderr)
        return 1
    if not result["redisStartupAppendonlyArgumentVerified"]:
        print("PROD_AOF_NOTE: startup config not proven by Redis CLI command args")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
