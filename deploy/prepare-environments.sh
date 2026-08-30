#!/usr/bin/env bash
set -euo pipefail

BASE_ENV="${1:-/opt/dhole/.env}"
TARGET_DIR="${2:-/opt/dhole}"
PROD_ENV="$TARGET_DIR/.env.production"
STAGING_ENV="$TARGET_DIR/.env.staging"

if [[ ! -r "$BASE_ENV" ]]; then
  echo "Base environment file not found: $BASE_ENV" >&2
  exit 1
fi

mkdir -p "$TARGET_DIR"
cp "$BASE_ENV" "$PROD_ENV"
cp "$BASE_ENV" "$STAGING_ENV"
chmod 600 "$PROD_ENV" "$STAGING_ENV"

set_env() {
  local file="$1"
  local key="$2"
  local value="$3"
  local tmp
  tmp="$(mktemp)"

  awk -v key="$key" -v value="$value" '
    BEGIN { replaced = 0 }
    index($0, key "=") == 1 {
      print key "=" value
      replaced = 1
      next
    }
    { print }
    END {
      if (!replaced) print key "=" value
    }
  ' "$file" > "$tmp"

  cat "$tmp" > "$file"
  rm -f "$tmp"
}

# Production keeps the existing private credentials and data configuration,
# but publishes only through the production Castro Fallas domains.
set_env "$PROD_ENV" ASPNETCORE_ENVIRONMENT Production
set_env "$PROD_ENV" DOTNET_ENVIRONMENT Production
set_env "$PROD_ENV" DHOLE_WEB_HOST sistema.logisticacastrofallas.com
set_env "$PROD_ENV" DHOLE_API_HOST api.logisticacastrofallas.com
set_env "$PROD_ENV" DHOLE_WEB_PUBLIC_URL https://sistema.logisticacastrofallas.com
set_env "$PROD_ENV" DHOLE_API_PUBLIC_URL https://api.logisticacastrofallas.com
set_env "$PROD_ENV" VITE_API_URL https://api.logisticacastrofallas.com
set_env "$PROD_ENV" VITE_FRONTEND_DOMAIN https://sistema.logisticacastrofallas.com
set_env "$PROD_ENV" CORS_WEB_ORIGIN https://sistema.logisticacastrofallas.com

# Staging is isolated by Docker project/network and never consumes or sends
# real email automatically. The private credentials remain server-only.
set_env "$STAGING_ENV" ASPNETCORE_ENVIRONMENT Staging
set_env "$STAGING_ENV" DOTNET_ENVIRONMENT Staging
set_env "$STAGING_ENV" DHOLE_WEB_HOST dhole.customcodecr.com
set_env "$STAGING_ENV" DHOLE_API_HOST dhole-api.customcodecr.com
set_env "$STAGING_ENV" DHOLE_WEB_PUBLIC_URL https://dhole.customcodecr.com
set_env "$STAGING_ENV" DHOLE_API_PUBLIC_URL https://dhole-api.customcodecr.com
set_env "$STAGING_ENV" VITE_API_URL https://dhole-api.customcodecr.com
set_env "$STAGING_ENV" VITE_FRONTEND_DOMAIN https://dhole.customcodecr.com
set_env "$STAGING_ENV" CORS_WEB_ORIGIN https://dhole.customcodecr.com
set_env "$STAGING_ENV" DATA_EXTRACTION_EMAIL_ENABLED false
set_env "$STAGING_ENV" NOTIFICATIONS_EMAIL_ENABLED false

printf 'Prepared %s and %s from server-only base env.\n' "$PROD_ENV" "$STAGING_ENV"
