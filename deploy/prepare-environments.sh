#!/usr/bin/env bash
set -euo pipefail

PROD_SOURCE="${1:-/opt/dhole/.env}"
TARGET_DIR="${2:-/opt/dhole}"
STAGING_SOURCE="${DHOLE_STAGING_ENV_SOURCE:-/opt/dhole/.env.staging}"

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
chmod 600 "$PROD_ENV" "$STAGING_ENV"

printf 'Loaded production env from %s and staging env from %s.\n' "$PROD_SOURCE" "$STAGING_SOURCE"
printf 'Runtime copies: %s and %s\n' "$PROD_ENV" "$STAGING_ENV"
