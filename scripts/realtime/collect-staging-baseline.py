#!/usr/bin/env python3
"""Read-only F0 baseline collector, executed on an authorized staging runner.

Never retrieves credentials, changes DB/container state, deploys, or contacts
production. No automatic CI status is a replacement for staging evidence.
"""
from __future__ import annotations
import argparse
import json
import os
import statistics
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

def run_command(argv: list[str]) -> dict:
    try:
        p = subprocess.run(argv, capture_output=True, text=True,
                           timeout=12, check=False)
        return {"exitCode": p.returncode,
                "output": p.stdout[:1500] if p.returncode == 0 else ""}
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return {"exitCode": None, "output": ""}

def probe(base_url: str, count: int) -> dict:
    u = urllib.parse.urlsplit(base_url)
    if u.scheme != "https" or not u.hostname or u.username or u.password or u.query:
        raise ValueError("Only explicit HTTPS staging base URL is accepted.")
    if "prod" in u.hostname.lower() or u.hostname.lower() in {"localhost", "127.0.0.1"}:
        raise ValueError("Use an authorized real staging host, not production/localhost.")
    endpoint = urllib.parse.urlunsplit(
        (u.scheme, u.netloc, (u.path.rstrip("/") + "/health"), "", ""))
    latency_ms, status_codes = [], {}
    for _ in range(count):
        request = urllib.request.Request(endpoint, headers={
            "Accept": "application/json", "Cache-Control": "no-store",
            "User-Agent": "Dhole-Realtime-F0-ReadOnly-Gate/1.0"
        }, method="GET")
        start = time.monotonic()
        try:
            with urllib.request.urlopen(request, timeout=8) as response:
                status = response.status
                response.read(512)  # bounded, no sensitive response persisted
        except urllib.error.HTTPError as ex:
            status = ex.code
        except (urllib.error.URLError, TimeoutError):
            status = "network_error"
        elapsed = round((time.monotonic() - start) * 1000, 3)
        latency_ms.append(elapsed)
        status_codes[str(status)] = status_codes.get(str(status), 0) + 1
        time.sleep(0.08)  # intentionally low-frequency, non-load baseline
    ordered = sorted(latency_ms)
    def q(percentile: float) -> float:
        return ordered[max(0, min(len(ordered)-1,
                                  int((len(ordered)*percentile+0.9999))-1))]
    return {"count": count, "statusCounts": status_codes,
            "p50Ms": q(.5), "p95Ms": q(.95), "p99Ms": q(.99),
            "meanMs": round(statistics.mean(ordered), 2),
            "environment": "staging",
            "scope": "public health GET baseline, NOT realtime user-to-user latency"}

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--output", default="F0-runtime-baseline.json")
    ap.add_argument("--samples", type=int, default=100)
    args = ap.parse_args()
    if os.getenv("DHOLE_GATE_ENV") != "staging":
        raise ValueError("DHOLE_GATE_ENV=staging required; refuses production.")
    url = os.getenv("DHOLE_GATE_STAGING_URL")
    if not url:
        raise ValueError("DHOLE_GATE_STAGING_URL explicit HTTPS URL required.")
    if not 30 <= args.samples <= 1000:
        raise ValueError("samples must be between 30 and 1000.")
    result = {
        "releaseId": "rt-20261107-01", "gate": "F0_RUNTIME_BASELINE",
        "observedAtUtc": datetime.now(timezone.utc).isoformat(),
        "readOnly": True, "prodTouched": False,
        "health": probe(url, args.samples),
        "runtimeHostEvidenceRequired": True,
        "runtimeHostEvidenceVerified": False,
        "jwtAndWssTwoUserEvidenceRequired": True,
        "jwtAndWssTwoUserEvidenceVerified": False,
        "redisAofLiveVerified": False,
        "postgresBackupRestoreVerified": False,
        "serviceInstancesVerified": False,
        "status": "PARTIAL_MEASUREMENTS_NOT_ACCEPTED_AS_COMPLETE_GATE"
    }
    # No hostname, private IP, token, cookies or response body written.
    path = Path(args.output)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf8")
    print(f"F0_HEALTH_MEASURED: {result['health']['count']} read-only HTTPS requests, "
          f"p95={result['health']['p95Ms']} ms; runtime/WSS gate still pending.")
    return 0

if __name__ == "__main__":
    try:
        sys.exit(main())
    except (ValueError, OSError) as ex:
        print("F0_BLOCKED: " + str(ex), file=sys.stderr)
        sys.exit(2)
