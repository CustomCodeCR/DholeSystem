#!/usr/bin/env bash
set -euo pipefail

MODE="sync"
if [[ "${1:-}" == "--check" ]]; then
  MODE="check"
fi

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
BASE_ENV="${DHOLE_BASE_ENV:-/opt/dhole/.env}"
ENV_DIR="${SYNC_ENV_DIR:-${RUNNER_TEMP:-/tmp}/dhole-nightly-sync-env}"
SYNC_TMP="${SYNC_TMP:-${RUNNER_TEMP:-/tmp}/dhole-nightly-sync}"
STAGING_PROJECT="dhole-staging-infra"
STAGING_NETWORK="dhole-staging"
PRODUCTION_NETWORK="dhole"
SYNC_NETWORK="dhole-nightly-db-sync"

mkdir -p "$ENV_DIR" "$SYNC_TMP"
bash "$ROOT_DIR/deploy/prepare-environments.sh" "$BASE_ENV" "$ENV_DIR"
PROD_ENV="$ENV_DIR/.env.production"
STAGING_ENV="$ENV_DIR/.env.staging"

read_env() {
  local file="$1"
  local key="$2"
  local value
  value="$(grep -m1 "^${key}=" "$file" | cut -d= -f2- | tr -d '\r' || true)"
  value="${value%\"}"
  value="${value#\"}"
  value="${value%\'}"
  value="${value#\'}"
  printf '%s' "$value"
}

require_value() {
  local name="$1"
  local value="$2"
  if [[ -z "$value" ]]; then
    echo "Required value is empty: $name" >&2
    exit 1
  fi
}

ensure_staging_infra() {
  docker network inspect "$STAGING_NETWORK" >/dev/null 2>&1 || docker network create "$STAGING_NETWORK" >/dev/null
  docker compose \
    --env-file "$STAGING_ENV" \
    -f "$ROOT_DIR/deploy/docker-compose.staging-infra.yml" \
    -p "$STAGING_PROJECT" \
    up -d postgres mongo >/dev/null
}

staging_container() {
  local service="$1"
  docker compose \
    --env-file "$STAGING_ENV" \
    -f "$ROOT_DIR/deploy/docker-compose.staging-infra.yml" \
    -p "$STAGING_PROJECT" \
    ps -q "$service"
}

production_container() {
  local service="$1"
  local staging_id="$2"
  local candidates=()

  mapfile -t candidates < <(
    docker ps \
      --filter status=running \
      --filter "network=${PRODUCTION_NETWORK}" \
      --filter "label=com.docker.compose.service=${service}" \
      --format '{{.ID}}' \
      | grep -v -F "$staging_id" || true
  )

  if [[ "${#candidates[@]}" -eq 0 ]]; then
    mapfile -t candidates < <(
      docker ps --filter status=running --format '{{.ID}}|{{.Names}}|{{.Networks}}|{{.Label "com.docker.compose.service"}}' \
        | awk -F'|' -v svc="$service" -v staging="$staging_id" '
            $1 != staging && $3 ~ /(^|,)dhole(,|$)/ && ($4 == svc || $2 ~ svc) { print $1 }
          '
    )
  fi

  if [[ "${#candidates[@]}" -ne 1 ]]; then
    echo "Could not resolve exactly one production ${service} container." >&2
    echo "Candidates: ${candidates[*]:-none}" >&2
    docker ps --format 'table {{.ID}}\t{{.Names}}\t{{.Networks}}\t{{.Label "com.docker.compose.project"}}\t{{.Label "com.docker.compose.service"}}' >&2
    exit 1
  fi

  printf '%s' "${candidates[0]}"
}

wait_for_postgres() {
  local container_id="$1"
  local user="$2"
  for attempt in $(seq 1 30); do
    if docker exec "$container_id" pg_isready -U "$user" >/dev/null 2>&1; then
      return 0
    fi
    if [[ "$attempt" == "30" ]]; then
      docker logs --tail 200 "$container_id" || true
      return 1
    fi
    sleep 2
  done
}

postgres_db_exists() {
  local container_id="$1"
  local user="$2"
  local db="$3"
  docker exec "$container_id" psql -U "$user" -d postgres -tAc \
    "SELECT 1 FROM pg_database WHERE datname = '$db'" \
    | tr -d '[:space:]'
}

sync_postgres_db() {
  local db="$1"
  local dump_file="$SYNC_TMP/${db}.sql"

  echo "PostgreSQL: merging missing rows for database '$db'"

  docker exec "$PROD_POSTGRES_ID" pg_dump \
    -U "$POSTGRES_USER" \
    -d "$db" \
    --data-only \
    --column-inserts \
    --rows-per-insert=100 \
    --on-conflict-do-nothing \
    --disable-triggers \
    --exclude-table-data='*."__EFMigrationsHistory"' \
    --exclude-table-data='*.sessions' \
    --exclude-table-data='*.session' \
    --exclude-table-data='*.refresh_tokens' \
    --exclude-table-data='*.refresh_token' \
    --exclude-table-data='*.outbox_messages' \
    --exclude-table-data='*.outboxmessages' \
    --exclude-table-data='*.inbox_messages' \
    --exclude-table-data='*.inboxmessages' \
    > "$dump_file"

  # Production sequence positions must never lower staging sequence positions.
  # The sequence values are repaired after the insert-only merge.
  sed -i '/^SELECT pg_catalog.setval/d' "$dump_file"

  docker exec -i "$STAGING_POSTGRES_ID" psql \
    -v ON_ERROR_STOP=1 \
    -U "$POSTGRES_USER" \
    -d "$db" \
    < "$dump_file" >/dev/null

  rm -f "$dump_file"

  docker exec -i "$STAGING_POSTGRES_ID" psql \
    -v ON_ERROR_STOP=1 \
    -U "$POSTGRES_USER" \
    -d "$db" >/dev/null <<'SQL'
DO $$
DECLARE
  r record;
  max_value bigint;
  current_value bigint;
BEGIN
  FOR r IN
    SELECT
      n.nspname AS schema_name,
      c.relname AS table_name,
      a.attname AS column_name,
      pg_get_serial_sequence(format('%I.%I', n.nspname, c.relname), a.attname) AS sequence_name
    FROM pg_class c
    JOIN pg_namespace n ON n.oid = c.relnamespace
    JOIN pg_attribute a ON a.attrelid = c.oid
    WHERE c.relkind = 'r'
      AND a.attnum > 0
      AND NOT a.attisdropped
      AND n.nspname NOT IN ('pg_catalog', 'information_schema')
      AND pg_get_serial_sequence(format('%I.%I', n.nspname, c.relname), a.attname) IS NOT NULL
  LOOP
    EXECUTE format(
      'SELECT max(%I)::bigint FROM %I.%I',
      r.column_name,
      r.schema_name,
      r.table_name
    ) INTO max_value;

    IF max_value IS NULL THEN
      CONTINUE;
    END IF;

    EXECUTE format('SELECT last_value::bigint FROM %s', r.sequence_name)
      INTO current_value;

    PERFORM pg_catalog.setval(
      r.sequence_name::regclass,
      GREATEST(COALESCE(current_value, 0), max_value),
      true
    );
  END LOOP;
END
$$;
SQL
}

sync_mongo() {
  if [[ -z "$PROD_MONGO_ID" || -z "$STAGING_MONGO_ID" ]]; then
    echo "MongoDB: production or staging container not found; skipping." >&2
    return 0
  fi

  echo "MongoDB: merging documents that do not exist in staging"

  docker network inspect "$SYNC_NETWORK" >/dev/null 2>&1 || docker network create "$SYNC_NETWORK" >/dev/null
  docker network connect --alias prod-mongo "$SYNC_NETWORK" "$PROD_MONGO_ID" 2>/dev/null || true
  docker network connect --alias staging-mongo "$SYNC_NETWORK" "$STAGING_MONGO_ID" 2>/dev/null || true

  cleanup_mongo_network() {
    docker network disconnect "$SYNC_NETWORK" "$PROD_MONGO_ID" >/dev/null 2>&1 || true
    docker network disconnect "$SYNC_NETWORK" "$STAGING_MONGO_ID" >/dev/null 2>&1 || true
    docker network rm "$SYNC_NETWORK" >/dev/null 2>&1 || true
  }
  trap cleanup_mongo_network RETURN

  docker run --rm -i \
    --network "$SYNC_NETWORK" \
    -e MONGO_USER="$MONGO_USER" \
    -e MONGO_PASSWORD="$MONGO_PASSWORD" \
    mongo:8 \
    mongosh --quiet --nodb <<'JS'
const user = encodeURIComponent(process.env.MONGO_USER || '');
const pass = encodeURIComponent(process.env.MONGO_PASSWORD || '');
if (!user || !pass) throw new Error('Mongo credentials are missing');

const source = new Mongo(`mongodb://${user}:${pass}@prod-mongo:27017/?authSource=admin`);
const target = new Mongo(`mongodb://${user}:${pass}@staging-mongo:27017/?authSource=admin`);

const systemDatabases = new Set(['admin', 'config', 'local']);
const unsafeCollection = /(^|[_-])(sessions?|refresh[_-]?tokens?|outbox(?:messages)?|inbox(?:messages)?)([_-]|$)/i;
const idKey = (value) => EJSON.stringify(value, { relaxed: false });

const databases = source.getDB('admin').runCommand({ listDatabases: 1, nameOnly: true }).databases
  .map((item) => item.name)
  .filter((name) => !systemDatabases.has(name));

for (const dbName of databases) {
  const sourceDb = source.getDB(dbName);
  const targetDb = target.getDB(dbName);
  const collections = sourceDb.getCollectionInfos({ type: 'collection' });

  for (const info of collections) {
    const collectionName = info.name;
    if (collectionName.startsWith('system.') || unsafeCollection.test(collectionName)) {
      print(`MongoDB: skipping operational collection ${dbName}.${collectionName}`);
      continue;
    }
    if (info.options && info.options.timeseries) {
      print(`MongoDB: skipping time-series collection ${dbName}.${collectionName}`);
      continue;
    }

    const sourceCollection = sourceDb.getCollection(collectionName);
    const targetCollection = targetDb.getCollection(collectionName);
    const cursor = sourceCollection.find({}).batchSize(100);
    let batch = [];
    let inserted = 0;

    const flush = () => {
      if (batch.length === 0) return;
      const ids = batch.map((doc) => doc._id);
      const existing = new Set(
        targetCollection.find({ _id: { $in: ids } }, { _id: 1 }).toArray()
          .map((doc) => idKey(doc._id))
      );
      const missing = batch.filter((doc) => !existing.has(idKey(doc._id)));
      if (missing.length > 0) {
        const result = targetCollection.insertMany(missing, { ordered: false });
        inserted += Object.keys(result.insertedIds || {}).length;
      }
      batch = [];
    };

    while (cursor.hasNext()) {
      batch.push(cursor.next());
      if (batch.length >= 100) flush();
    }
    flush();
    print(`MongoDB: ${dbName}.${collectionName} inserted ${inserted} missing document(s)`);
  }
}
JS

  cleanup_mongo_network
  trap - RETURN
}

ensure_staging_infra

POSTGRES_USER="$(read_env "$PROD_ENV" POSTGRES_USER)"
MONGO_USER="$(read_env "$PROD_ENV" MONGO_USER)"
MONGO_PASSWORD="$(read_env "$PROD_ENV" MONGO_PASSWORD)"
require_value POSTGRES_USER "$POSTGRES_USER"

STAGING_POSTGRES_ID="$(staging_container postgres)"
STAGING_MONGO_ID="$(staging_container mongo)"
require_value STAGING_POSTGRES_ID "$STAGING_POSTGRES_ID"

PROD_POSTGRES_ID="$(production_container postgres "$STAGING_POSTGRES_ID")"
PROD_MONGO_ID=""
if [[ -n "$STAGING_MONGO_ID" ]]; then
  PROD_MONGO_ID="$(production_container mongo "$STAGING_MONGO_ID" || true)"
fi

wait_for_postgres "$PROD_POSTGRES_ID" "$POSTGRES_USER"
wait_for_postgres "$STAGING_POSTGRES_ID" "$POSTGRES_USER"

mapfile -t POSTGRES_DATABASES < <(
  awk -F= '
    $1 ~ /^[A-Z0-9_]+_DB$/ && $1 != "POSTGRES_DB" && $1 != "MONGO_DB" {
      value = substr($0, index($0, "=") + 1)
      gsub(/^['"'"']|['"'"']$/, "", value)
      if (length(value) > 0) print value
    }
  ' "$PROD_ENV" | sort -u
)

if [[ "${#POSTGRES_DATABASES[@]}" -eq 0 ]]; then
  echo "No service PostgreSQL databases were discovered from *_DB variables." >&2
  exit 1
fi

echo "Production PostgreSQL container: $PROD_POSTGRES_ID"
echo "Staging PostgreSQL container: $STAGING_POSTGRES_ID"
echo "Production MongoDB container: ${PROD_MONGO_ID:-not found}"
echo "Staging MongoDB container: ${STAGING_MONGO_ID:-not found}"
echo "PostgreSQL databases: ${POSTGRES_DATABASES[*]}"

if [[ "$MODE" == "check" ]]; then
  for db in "${POSTGRES_DATABASES[@]}"; do
    prod_exists="$(postgres_db_exists "$PROD_POSTGRES_ID" "$POSTGRES_USER" "$db")"
    staging_exists="$(postgres_db_exists "$STAGING_POSTGRES_ID" "$POSTGRES_USER" "$db")"
    echo "Check PostgreSQL $db: prod=${prod_exists:-0}, staging=${staging_exists:-0}"
  done
  echo "Check completed. No production data was written to staging."
  exit 0
fi

for db in "${POSTGRES_DATABASES[@]}"; do
  prod_exists="$(postgres_db_exists "$PROD_POSTGRES_ID" "$POSTGRES_USER" "$db")"
  staging_exists="$(postgres_db_exists "$STAGING_POSTGRES_ID" "$POSTGRES_USER" "$db")"

  if [[ "$prod_exists" != "1" ]]; then
    echo "PostgreSQL: skipping '$db' because it does not exist in production."
    continue
  fi

  if [[ "$staging_exists" != "1" ]]; then
    echo "PostgreSQL: staging database '$db' does not exist. Refusing to clone its schema automatically." >&2
    echo "Deploy the corresponding staging service/migrations first, then rerun the sync." >&2
    exit 1
  fi

  sync_postgres_db "$db"
done

if [[ -n "$PROD_MONGO_ID" && -n "$STAGING_MONGO_ID" && -n "$MONGO_USER" && -n "$MONGO_PASSWORD" ]]; then
  sync_mongo
else
  echo "MongoDB sync skipped because the container or credentials are unavailable."
fi

echo "Nightly production -> staging missing-data merge completed successfully."
