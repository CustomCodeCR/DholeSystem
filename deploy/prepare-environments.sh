#!/usr/bin/env bash
set -euo pipefail

PROD_SOURCE="${1:-/opt/dhole/.env}"
TARGET_DIR="${2:-/opt/dhole}"
STAGING_SOURCE="${DHOLE_STAGING_ENV_SOURCE:-${PROD_SOURCE}.staging}"
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

# Compatibility copies for older deployment workflows only.
# Production always originates from /opt/dhole/.env and staging always
# originates from /opt/dhole/.env.staging. Values are never synthesized,
# overridden, or copied from production into staging here.
cp "$PROD_SOURCE" "$PROD_ENV"
cp "$STAGING_SOURCE" "$STAGING_ENV"
chmod 600 "$PROD_ENV" "$STAGING_ENV"

printf 'Prepared compatibility copies from %s (production) and %s (staging).\n' "$PROD_SOURCE" "$STAGING_SOURCE"
