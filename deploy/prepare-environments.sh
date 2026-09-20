#!/usr/bin/env bash
set -euo pipefail

PROD_SOURCE="${1:-/opt/dhole/.env}"
TARGET_DIR="${2:-/opt/dhole}"
STAGING_SOURCE="${DHOLE_STAGING_ENV_SOURCE:-/opt/dhole/.env.staging}"
HERMES_ENV_SOURCE="${DHOLE_HERMES_ENV_SOURCE:-/opt/dhole/.env.hermes}"

PROD_ENV="$TARGET_DIR/.env.production"
STAGING_ENV="$TARGET_DIR/.env.staging"

if [[ ! -r "$PROD_SOURCE" ]]; then
  echo "Production environment file not found: $PROD_SOURCE" >&2
  exit 1
fi

if [[ ! -r "$STAGING_SOURCE" ]]; then
  echo "Staging environment file not found: $STAGING_SOURCE" >&2
  exit 1
fi

if [[ ! -r "$HERMES_ENV_SOURCE" ]]; then
  echo "Creating persistent Hermes runtime configuration at $HERMES_ENV_SOURCE"
  umask 077
  mkdir -p "$(dirname "$HERMES_ENV_SOURCE")"
  {
    printf 'HERMES_API_SERVER_KEY=%s\n' "$(openssl rand -hex 32)"
    printf 'HERMES_API_SERVER_MODEL_NAME=hermes-agent\n'
    printf 'HERMES_OLLAMA_MODEL=mistral-nemo:12b\n'
  } > "$HERMES_ENV_SOURCE"
  chmod 600 "$HERMES_ENV_SOURCE"
fi

mkdir -p "$TARGET_DIR"
cp "$PROD_SOURCE" "$PROD_ENV"
cp "$STAGING_SOURCE" "$STAGING_ENV"

append_if_missing() {
  local file="$1"
  local key="$2"
  local value="$3"

  if ! grep -q "^$key=" "$file"; then
    printf '%s=%s\n' "$key" "$value" >> "$file"
  fi
}

read_env_value() {
  local file="$1"
  local key="$2"
  grep -m1 "^$key=" "$file" | cut -d= -f2- | tr -d '\r' || true
}

prepare_runtime_env() {
  local file="$1"
  local postgres_user postgres_password

  postgres_user="$(read_env_value "$file" POSTGRES_USER)"
  postgres_password="$(read_env_value "$file" POSTGRES_PASSWORD)"

  if [[ -z "$postgres_user" || -z "$postgres_password" ]]; then
    echo "POSTGRES_USER and POSTGRES_PASSWORD are required in $file" >&2
    exit 1
  fi

  append_if_missing "$file" CONTENT_POSTGRES_CONNECTION "Host=postgres;Port=5432;Database=dhole_content;Username=$postgres_user;Password=$postgres_password"
  append_if_missing "$file" AGENT_POSTGRES_CONNECTION_STRING "Host=postgres;Port=5432;Database=dhole_agent;Username=$postgres_user;Password=$postgres_password"
  append_if_missing "$file" CONTENT_REDIS_CONNECTION "redis:6379"
  append_if_missing "$file" AGENT_REDIS_CONNECTION_STRING "redis:6379"
  append_if_missing "$file" HERMES_GATEWAY_URL "http://hermes-agent:8642"

  printf '\n# Hermes runtime\n' >> "$file"
  while IFS= read -r line || [[ -n "$line" ]]; do
    [[ -z "$line" || "$line" == \#* ]] && continue
    local key="${line%%=*}"
    local value="${line#*=}"
    append_if_missing "$file" "$key" "$value"
  done < "$HERMES_ENV_SOURCE"
}

prepare_runtime_env "$PROD_ENV"
prepare_runtime_env "$STAGING_ENV"

chmod 600 "$PROD_ENV" "$STAGING_ENV"

printf 'Loaded production env from %s and staging env from %s.\n' "$PROD_SOURCE" "$STAGING_SOURCE"
printf 'Merged Hermes/Ollama runtime environment from %s.\n' "$HERMES_ENV_SOURCE"
printf 'Runtime copies: %s and %s\n' "$PROD_ENV" "$STAGING_ENV"
