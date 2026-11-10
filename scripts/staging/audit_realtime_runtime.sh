#!/usr/bin/env bash
set -euo pipefail
# Read-only staging runtime audit. Never print access tokens, environment
# values, Redis message payloads, database rows or browser identifiers.
echo "STAGING_REALTIME_AUDIT_BEGIN"
tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT

# Public production-shaped hostname is intentionally mapped to staging here.
curl -fsS --retry 3 --retry-delay 2 --max-time 25 \
  https://dhole.customcodecr.com/ -o "$tmp/public-index.html"
curl -fsS --retry 3 --retry-delay 2 --max-time 15 \
  http://127.0.0.1:18081/ -o "$tmp/local-index.html"
python3 - "$tmp/public-index.html" "$tmp/local-index.html" <<'PY'
import re,sys,pathlib
def bundles(path):
    contents=pathlib.Path(path).read_text(encoding="utf-8")
    return sorted(set(re.findall(r"[/]assets/index-[\w-]+\.js", contents)))
public=bundles(sys.argv[1])
local=bundles(sys.argv[2])
print("Public staging entry bundle(s):", ",".join(public) or "MISSING")
print("Local staging entry bundle(s):", ",".join(local) or "MISSING")
if not public or public != local:
    print("ERROR: Public Dhole frontend is not the staging bundle.")
    sys.exit(1)
print("PASS: Public Dhole web uses the staging entry bundle.")
PY

for target in public local; do
  if [[ "$target" == public ]]; then
    origin="https://dhole-api.customcodecr.com"
  else
    origin="http://127.0.0.1:18080"
  fi
  status="$(curl --silent --show-error --max-time 20 --output /dev/null \
    --write-out '%{http_code}' --request POST \
    --header 'Content-Type: text/plain;charset=UTF-8' \
    --header 'Origin: https://dhole.customcodecr.com' \
    "$origin/api/notifications/hub/negotiate?negotiateVersion=1" || true)"
  echo "$target anonymous SignalR negotiation: HTTP $status"
  case "$status" in
    401|403) ;;
    *) echo "ERROR: $target anonymous SignalR negotiate is not an expected authentication denial."; exit 1 ;;
  esac
done

for component in notifications-api config-api config-workers; do
  id="$(docker ps -q \
    --filter "label=com.docker.compose.project=dhole-staging" \
    --filter "label=com.docker.compose.service=$component" | head -n1)"
  if [[ -z "$id" ]]; then echo "ERROR: Missing staging $component"; exit 1; fi
  docker inspect --format '{{json .Config.Env}}' "$id" | \
    python3 -c '
import json,sys
component=sys.argv[1]
values=dict(x.split("=",1) for x in json.load(sys.stdin) if "=" in x)
keys=["Features__UniversalRealtimeEnabled","Realtime__ReleaseId"]
if component=="notifications-api":
    keys+=["Realtime__NotificationsHostEnabled","Realtime__DeploymentTarget"]
else:
    keys+=["Realtime__Outbox__Enabled","Realtime__BatchApproved"]
expected={"Features__UniversalRealtimeEnabled":"true",
          "Realtime__ReleaseId":"rt-20261107-01",
          "Realtime__NotificationsHostEnabled":"true",
          "Realtime__DeploymentTarget":"staging",
          "Realtime__Outbox__Enabled":"true",
          "Realtime__BatchApproved":"true"}
fail=[key for key in keys if values.get(key,"").lower()!=expected[key].lower()]
print(component+": realtime flags "+("PASS" if not fail else "FAIL " + ",".join(fail)))
if fail: sys.exit(1)
' "$component"
done

redis="$(docker ps -q \
  --filter "label=com.docker.compose.project=dhole-staging-infra" \
  --filter "label=com.docker.compose.service=redis" | head -n1)"
if [[ -z "$redis" ]]; then echo "ERROR: Staging Redis container missing"; exit 1; fi
echo "Checking ONLY staging Redis. Event payloads are never printed."
# XINFO GROUPS works even when no events have been published. A missing group
# proves the Notifications consumer has not initialized against staging Redis.
groups="$(docker exec "$redis" redis-cli --raw XINFO GROUPS dhole.config.realtime.v1)"
if ! grep -Fxq 'dhole-notifications-resource-v1' <<<"$groups"; then
  echo "ERROR: Config resource consumer group is missing on staging Redis."
  exit 1
fi
length="$(docker exec "$redis" redis-cli --raw XLEN dhole.config.realtime.v1)"
if [[ ! "$length" =~ ^[0-9]+$ ]]; then
  echo "ERROR: Could not read sanitized Config Redis stream length."
  exit 1
fi
echo "Staging Config stream length: $length (no payloads displayed)"
echo "PASS: Notifications resource group is attached to staging Redis."
# Only Redis XINFO metadata; do not show the stream events or credentials.
printf '%s\n' "$groups" | python3 -c '
import sys
lines=[x.strip() for x in sys.stdin if x.strip()]
records=[dict(zip(lines[i:i+2], lines[i+1:i+2])) for i in []]  # no payload access
pairs=dict(zip(lines[0::2],lines[1::2]))
name=pairs.get("name", "")
print("Config Notifications consumer group:", "PRESENT" if name=="dhole-notifications-resource-v1" else "UNKNOWN")
print("Config consumer active count:", pairs.get("consumers", "?"))
print("Config consumer pending count:", pairs.get("pending", "?"))
print("Config consumer lag count:", pairs.get("lag", "?"))
'
echo "STAGING_REALTIME_AUDIT_PASS"
