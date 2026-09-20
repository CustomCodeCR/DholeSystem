#!/usr/bin/env bash
set -euo pipefail

PROD_SOURCE="${1:-/opt/dhole/.env}"
TARGET_DIR="${2:-/opt/dhole}"
STAGING_SOURCE="${DHOLE_STAGING_ENV_SOURCE:-/opt/dhole/.env.staging}"
HERMES_ENV_SOURCE="${DHOLE_HERMES_ENV_SOURCE:-/opt/dhole/.env.hermes}"
HERMES_CONFIG_DIR="${DHOLE_HERMES_CONFIG_DIR:-/opt/dhole/hermes}"

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

merge_optional_env() {
  local target="$1"
  local source="$2"

  [[ -r "$source" ]] || return 0

  while IFS= read -r line || [[ -n "$line" ]]; do
    [[ -z "$line" || "$line" == \#* ]] && continue
    local key="${line%%=*}"
    local value="${line#*=}"
    append_if_missing "$target" "$key" "$value"
  done < "$source"
}

resolve_auth_jwt_secret() {
  local file="$1"
  local project="$2"
  local value candidate container_id

  for candidate in AUTH_JWT_SECRET AUTH_JWT_SECRET_KEY JWT_SECRET JWT_SECRET_KEY; do
    value="$(read_env_value "$file" "$candidate")"
    if [[ -n "$value" ]]; then
      printf '%s' "$value"
      return 0
    fi
  done

  if command -v docker >/dev/null 2>&1; then
    container_id="$(
      docker ps -q         --filter "label=com.docker.compose.project=$project"         --filter "label=com.docker.compose.service=auth-api"         | head -n1 || true
    )"

    if [[ -n "$container_id" ]]; then
      value="$(
        docker inspect -f '{{range .Config.Env}}{{println .}}{{end}}' "$container_id" 2>/dev/null           | sed -n 's/^Auth__Jwt__SecretKey=//p'           | head -n1
      )"
      if [[ -n "$value" ]]; then
        printf '%s' "$value"
        return 0
      fi
    fi
  fi

  return 1
}

prepare_runtime_env() {
  local file="$1"
  local project="$2"
  local postgres_user postgres_password auth_secret hermes_key

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

  merge_optional_env "$file" "$HERMES_ENV_SOURCE"

  append_if_missing "$file" HERMES_API_SERVER_MODEL_NAME "hermes-agent"
  append_if_missing "$file" HERMES_OLLAMA_MODEL "mistral-nemo:12b"
  append_if_missing "$file" HERMES_CONTEXT_LENGTH "65536"

  auth_secret="$(resolve_auth_jwt_secret "$file" "$project" || true)"
  if [[ -n "$auth_secret" ]]; then
    append_if_missing "$file" AUTH_JWT_SECRET "$auth_secret"
  fi

  hermes_key="$(read_env_value "$file" HERMES_API_SERVER_KEY)"
  if [[ -z "$hermes_key" ]]; then
    hermes_key="$(
      printf 'dhole-hermes:%s:%s' "$postgres_user" "$postgres_password"         | sha256sum         | awk '{print $1}'
    )"
    append_if_missing "$file" HERMES_API_SERVER_KEY "$hermes_key"
  fi
}

prepare_runtime_env "$PROD_ENV" "dhole"
prepare_runtime_env "$STAGING_ENV" "dhole-staging"

write_hermes_config() {
  local file="$1"
  local suffix="$2"
  local model context_length config_file

  model="$(read_env_value "$file" HERMES_OLLAMA_MODEL)"
  context_length="$(read_env_value "$file" HERMES_CONTEXT_LENGTH)"
  model="${model:-mistral-nemo:12b}"
  context_length="${context_length:-65536}"

  mkdir -p "$HERMES_CONFIG_DIR"
  config_file="$HERMES_CONFIG_DIR/config.$suffix.yaml"

  cat > "$config_file" <<EOF
model:
  default: $model
  provider: custom
  base_url: http://ollama:11434/v1
  context_length: $context_length
EOF

  chmod 600 "$config_file"
  append_if_missing "$file" HERMES_CONFIG_FILE "$config_file"
}

write_hermes_config "$PROD_ENV" "production"
write_hermes_config "$STAGING_ENV" "staging"

chmod 600 "$PROD_ENV" "$STAGING_ENV"

printf 'Loaded production env from %s and staging env from %s.\n' "$PROD_SOURCE" "$STAGING_SOURCE"
if [[ -r "$HERMES_ENV_SOURCE" ]]; then
  printf 'Merged optional Hermes overrides from %s.\n' "$HERMES_ENV_SOURCE"
else
  printf 'No writable Hermes env file required; runtime Hermes credentials are derived per environment.\n'
fi
printf 'Runtime copies: %s and %s\n' "$PROD_ENV" "$STAGING_ENV"
