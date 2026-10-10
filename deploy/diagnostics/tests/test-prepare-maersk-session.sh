#!/usr/bin/env bash
set -euo pipefail
root="$(cd "$(dirname "$0")/.." && pwd)"
sandbox="$(mktemp -d)"
trap 'rm -rf "$sandbox"' EXIT
mkdir -p "$sandbox/bin"
cat > "$sandbox/env" <<'ENV'
AGENT_POSTGRES_CONNECTION_STRING=Host=postgres;Port=5432;Database=dhole_agent;Username=fixture;Password=DO_NOT_PRINT
ENV
cat > "$sandbox/bin/docker" <<'MOCK'
#!/usr/bin/env bash
set -euo pipefail
printf '%s\n' "$*" >> "$FAKE_DOCKER_LOG"
case "$1" in
  ps) echo worker1 ;;
  inspect)
    case "$*" in
      *Mounts*) echo dhole-staging_agent-browser-profiles ;;
      *) echo 'Unexpected inspection' >&2; exit 1 ;;
    esac ;;
  run)
    if [[ "$*" == *" psql "* ]]; then
      printf '0\n'
    elif [[ "$*" == *"readonly"* ]]; then
      echo existing_profile=PRESENT
    else
      echo 'Unsafe write-side operation in dry-run' >&2; exit 1
    fi ;;
  *) echo 'Unexpected command' >&2; exit 1 ;;
esac
MOCK
chmod +x "$sandbox/bin/docker"
export FAKE_DOCKER_LOG="$sandbox/docker.log"
export MAERSK_DIAGNOSTIC_ENV_OVERRIDE="$sandbox/env"
export PATH="$sandbox/bin:$PATH"
bash -n "$root/prepare-maersk-session.sh"
bash "$root/prepare-maersk-session.sh" staging --dry-run > "$sandbox/out"
grep -q 'DRY_RUN: no service, profile, or database changes.' "$sandbox/out"
grep -q 'existing_profile=PRESENT' "$sandbox/out"
if grep -q 'DO_NOT_PRINT' "$sandbox/out"; then echo 'Leaked credential' >&2; exit 1; fi
if grep -qE '^stop |^start ' "$FAKE_DOCKER_LOG"; then
  echo 'Dry-run attempted to stop/start a container' >&2; exit 1
fi
if bash "$root/prepare-maersk-session.sh" staging --apply INVALID >/dev/null 2>&1; then
  echo 'Applied without confirmation' >&2; exit 1
fi
echo 'Maersk controlled session dry-run tests passed.'
