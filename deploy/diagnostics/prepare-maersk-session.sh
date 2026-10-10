#!/usr/bin/env bash
# Manual and controlled Chromium session replacement for the Maersk credential.
# No PostgreSQL update, no environment, IP or account rotation.
# Never runs scheduled searches or attempts to solve CAPTCHA.
set -euo pipefail
set +x
if [ "$#" -lt 1 ] || [ "$#" -gt 3 ]; then
  echo 'Usage: prepare-maersk-session.sh <staging|production> [--dry-run|--apply] [REPLACE_CHROMIUM_SESSION]' >&2
  exit 2
fi
env_name="$1"
operation="--dry-run"
if [ "$#" -ge 2 ]; then operation="$2"; fi
case "$operation" in --dry-run|--apply) ;; *) exit 2 ;; esac
case "$env_name" in
 staging) project="dhole-staging"; network="dhole-staging"; envfile="/opt/dhole/.env.staging" ;;
 production) project="dhole"; network="dhole"; envfile="/opt/dhole/.env" ;;
 *) echo 'Invalid environment' >&2; exit 2 ;;
esac
# Dry-run tests may use an isolated fixture. Apply always uses the real env.
if [ "$operation" = "--dry-run" ] && [ -n "${MAERSK_DIAGNOSTIC_ENV_OVERRIDE:-}" ]; then
  envfile="$MAERSK_DIAGNOSTIC_ENV_OVERRIDE"
fi
if [ "$operation" = "--apply" ] && [ "$#" -ne 3 ]; then
  echo 'To apply, provide explicit REPLACE_CHROMIUM_SESSION confirmation' >&2; exit 2
fi
if [ "$operation" = "--apply" ] && [ "$3" != REPLACE_CHROMIUM_SESSION ]; then
  echo 'Confirmation mismatch; nothing changed' >&2; exit 2
fi
command -v docker >/dev/null || exit 2
test -r "$envfile" || { echo 'Runtime environment missing'; exit 1; }
provider="MAERSK"
credential="70ccf773c95a4ed899058df77cd1c126"
ids="$(docker ps -q --filter "label=com.docker.compose.project=$project" --filter label=com.docker.compose.service=dhole-agent-workers)"
num_ids="$(printf '%s\n' "$ids" | sed '/^$/d' | wc -l)"
[ "$num_ids" -eq 1 ] || { echo 'A single running Agent worker is required; no change made' >&2; exit 1; }
worker="$ids"
volume="$(docker inspect --format '{{range .Mounts}}{{if eq .Destination "/data/browser-profiles"}}{{.Name}}{{end}}{{end}}' "$worker")"
[ -n "$volume" ] || { echo 'Persistent Chromium volume not mounted; aborting' >&2; exit 1; }
case "$volume" in
  dhole_agent-browser-profiles|dhole-staging_agent-browser-profiles) ;;
  *) echo 'Unexpected profile volume; nothing changed' >&2; exit 1 ;;
esac
expected_volume="$project"
expected_volume="$expected_volume""_agent-browser-profiles"
[ "$volume" = "$expected_volume" ] || { echo 'Environment/volume mismatch; aborting' >&2; exit 1; }

# These are metadata-only reads. The SQL client cannot write to PostgreSQL.
envval() { grep -E "^$1=" "$envfile" | tail -n1 | cut -d= -f2- | tr -d '\r' || true; }
conn="$(envval AGENT_POSTGRES_CONNECTION_STRING)"
if [ -z "$conn" ]; then
  pguser="$(envval POSTGRES_USER)"
  pgpass="$(envval POSTGRES_PASSWORD)"
  [ -n "$pguser" ] && [ -n "$pgpass" ] || { echo 'Database credentials missing; aborting' >&2; exit 1; }
  conn="Host=postgres;Port=5432;Database=dhole_agent;Username=$pguser;Password=$pgpass"
fi
value() { printf '%s' "$conn" | tr ';' '\n' | sed -n "s/^$1=//p" | head -n1; }
dbhost="$(value Host)"
dbport="$(value Port)"
dbname="$(value Database)"
dbuser="$(value Username)"
dbpass="$(value Password)"
[[ "$dbname" =~ ^[a-zA-Z0-9_]+$ ]] || { echo 'Unsafe DB name; aborting' >&2; exit 1; }
if [ -z "$dbuser" ] || [ -z "$dbpass" ]; then echo 'Invalid DB configuration' >&2; exit 1; fi
run_count="$(docker run --rm --network "$network" -e PGPASSWORD="$dbpass" \
 -e PGOPTIONS='-c default_transaction_read_only=on' postgres:16-alpine \
 psql -X -v ON_ERROR_STOP=1 -At -h "$dbhost" -p "$dbport" -U "$dbuser" -d "$dbname" \
 -c 'SELECT COUNT(*) FROM agent."AgentExecutions" WHERE status = '"'Running'"';')"
[[ "$run_count" =~ ^[0-9]+$ ]] || { echo 'Cannot confirm queue idle; aborting' >&2; exit 1; }
echo "environment=$env_name mode=$operation active_executions=$run_count"
if [ "$run_count" -ne 0 ]; then
  echo 'Worker is handling an execution. No session changes allowed.' >&2
  exit 1
fi

# Check presence without modifying the profile.
docker run --rm --network none -e CREDENTIAL="$credential" \
 --mount "type=volume,src=$volume,dst=/profiles,readonly" \
 --entrypoint /bin/sh postgres:16-alpine -ec '
  original="/profiles/MAERSK/$CREDENTIAL"
  if [ -L "$original" ]; then echo "Symlinked profile refused" >&2; exit 1; fi
  if [ -d "$original" ]; then
    echo "existing_profile=PRESENT"
  else
    echo "existing_profile=ABSENT"
  fi
'
if [ "$operation" = "--dry-run" ]; then
  echo 'DRY_RUN: no service, profile, or database changes.'
  exit 0
fi

# Do not archive a provider-restricted session automatically. This command
# must be operator-initiated; all CAPTCHA verification remains manual.
# Gracefully stop only the existing worker to exclude concurrent file access.
stopped=0
restart_worker() {
  if [ "$stopped" -eq 1 ]; then
    if docker start "$worker" >/dev/null; then
      echo 'Agent worker restarted using original container, image and DB.'
    else
      echo 'ALERT: worker did not restart; intervention required' >&2
    fi
  fi
}
trap restart_worker EXIT
docker stop --time 60 "$worker" >/dev/null
stopped=1
backup_tag="$(date -u +%Y%m%dT%H%M%SZ)"
docker run --rm --network none -e CREDENTIAL="$credential" -e BACKUP_TAG="$backup_tag" \
 --mount "type=volume,src=$volume,dst=/profiles" \
 --entrypoint /bin/sh postgres:16-alpine -ec '
  set -eu
  original="/profiles/MAERSK/$CREDENTIAL"
  if [ ! -d "$original" ]; then
    echo "The original persistent profile is absent; no session replaced." >&2
    exit 1
  fi
  if [ -L "$original" ]; then echo "Symlink refused" >&2; exit 1; fi
  backup="$original.manual-backup-$BACKUP_TAG"
  if [ -e "$backup" ]; then echo "Backup path exists; aborting" >&2; exit 1; fi
  old_uid="$(stat -c %u "$original")"
  old_gid="$(stat -c %g "$original")"
  mv "$original" "$backup"
  if ! mkdir "$original"; then
    mv "$backup" "$original"
    echo "Unable to create fresh profile; original restored" >&2
    exit 1
  fi
  chmod 0700 "$original"
  chown "$old_uid:$old_gid" "$original"
  echo "CHROMIUM_PROFILE_ARCHIVED=$backup"
  echo "FRESH_CHROMIUM_PROFILE=$original"
'
echo 'The next authorized login will use a fresh Chromium profile.'
echo 'The old profile remains on the same persistent Docker volume; the PostgreSQL database and existing execution statuses are unchanged.'
echo 'If Maersk requires CAPTCHA or additional verification, authenticate through the normal interactive flow; do not run automated searches until allowed.'
