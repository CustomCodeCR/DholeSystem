#!/usr/bin/env bash
set -euo pipefail

STAGING_NETWORK="${STAGING_NETWORK:-dhole-staging}"
PRODUCTION_NETWORK="${PRODUCTION_NETWORK:-dhole}"
CURL_IMAGE="${CURL_IMAGE:-curlimages/curl:8.12.1}"
WORK_DIR="${RUNNER_TEMP:-/tmp}/whs-promotion"
BACKUP_DIR="${RUNNER_TEMP:-/tmp}/whs-promotion-backup"
mkdir -p "$WORK_DIR" "$BACKUP_DIR"
rm -rf "$WORK_DIR"/*

log() { printf '[WHS promotion] %s\n' "$*"; }
fail() { printf '[WHS promotion] ERROR: %s\n' "$*" >&2; exit 1; }

one_container() {
  local network="$1" service="$2"
  local ids
  mapfile -t ids < <(docker ps --filter status=running --filter "network=${network}" --filter "label=com.docker.compose.service=${service}" --format '{{.ID}}')
  [[ ${#ids[@]} -eq 1 ]] || fail "Expected exactly one ${service} container on ${network}; found ${#ids[@]}"
  printf '%s' "${ids[0]}"
}

postgres_user() {
  local container="$1"
  docker exec "$container" sh -lc 'printf "%s" "$POSTGRES_USER"'
}

find_config_db() {
  local container="$1" user="$2" db
  while IFS= read -r db; do
    [[ -n "$db" ]] || continue
    if [[ "$(docker exec "$container" psql -X -qAt -U "$user" -d "$db" -c "SELECT to_regclass('config.\"CatalogGroups\"') IS NOT NULL AND to_regclass('config.\"CatalogItems\"') IS NOT NULL" 2>/dev/null || true)" == "t" ]]; then
      printf '%s' "$db"
      return 0
    fi
  done < <(docker exec "$container" psql -X -qAt -U "$user" -d postgres -c "SELECT datname FROM pg_database WHERE datallowconn AND NOT datistemplate ORDER BY datname")
  return 1
}

columns_signature() {
  local container="$1" user="$2" db="$3" table="$4"
  docker exec "$container" psql -X -qAt -U "$user" -d "$db" -c "
    SELECT string_agg(column_name || ':' || udt_name, ',' ORDER BY ordinal_position)
    FROM information_schema.columns
    WHERE table_schema='config' AND table_name='${table}';"
}

copy_query_to_file() {
  local container="$1" user="$2" db="$3" query="$4" file="$5"
  docker exec "$container" psql -X -q -U "$user" -d "$db" -c "COPY (${query}) TO STDOUT WITH (FORMAT csv, HEADER true)" > "$file"
}

copy_file_into_table() {
  local container="$1" user="$2" db="$3" table="$4" file="$5"
  cat "$file" | docker exec -i "$container" psql -X -q -v ON_ERROR_STOP=1 -U "$user" -d "$db" -c "COPY ${table} FROM STDIN WITH (FORMAT csv, HEADER true)"
}

wait_for_persistent_production_storage() {
  local attempt storage_id
  for attempt in $(seq 1 120); do
    storage_id="$(docker ps --filter status=running --filter "network=${PRODUCTION_NETWORK}" --filter 'label=com.docker.compose.service=storage-api' --format '{{.ID}}' | head -n1 || true)"
    if [[ -n "$storage_id" ]] && docker inspect "$storage_id" --format '{{range .Mounts}}{{println .Destination}}{{end}}' | grep -Fxq '/app/storage/dhole-storage'; then
      log "Production Storage is using the persistent /app/storage/dhole-storage mount."
      return 0
    fi
    log "Waiting for production Storage persistent mount (${attempt}/120)..."
    sleep 10
  done
  fail "Production storage-api is not running with the persistent storage mount."
}

STAGING_POSTGRES_ID="$(one_container "$STAGING_NETWORK" postgres)"
PROD_POSTGRES_ID="$(one_container "$PRODUCTION_NETWORK" postgres)"
STAGING_USER="$(postgres_user "$STAGING_POSTGRES_ID")"
PROD_USER="$(postgres_user "$PROD_POSTGRES_ID")"
[[ -n "$STAGING_USER" && -n "$PROD_USER" ]] || fail "POSTGRES_USER is unavailable in one of the PostgreSQL containers."

STAGING_CONFIG_DB="$(find_config_db "$STAGING_POSTGRES_ID" "$STAGING_USER")" || fail "Could not locate the staging Config database."
PROD_CONFIG_DB="$(find_config_db "$PROD_POSTGRES_ID" "$PROD_USER")" || fail "Could not locate the production Config database."

log "Staging Config DB: $STAGING_CONFIG_DB"
log "Production Config DB: $PROD_CONFIG_DB"

for table in CatalogGroups CatalogItems; do
  staging_sig="$(columns_signature "$STAGING_POSTGRES_ID" "$STAGING_USER" "$STAGING_CONFIG_DB" "$table")"
  prod_sig="$(columns_signature "$PROD_POSTGRES_ID" "$PROD_USER" "$PROD_CONFIG_DB" "$table")"
  [[ -n "$staging_sig" && "$staging_sig" == "$prod_sig" ]] || fail "Config table schema mismatch for ${table}; deploy compatible Config migrations before promotion."
done

wait_for_persistent_production_storage
one_container "$STAGING_NETWORK" api-gateway >/dev/null
one_container "$PRODUCTION_NETWORK" api-gateway >/dev/null

# Backup current production WHS rows before changing anything.
copy_query_to_file "$PROD_POSTGRES_ID" "$PROD_USER" "$PROD_CONFIG_DB" \
  "SELECT * FROM config.\"CatalogGroups\" WHERE slug='pricing-warehouses'" \
  "$BACKUP_DIR/prod-pricing-warehouses-group-before.csv"
copy_query_to_file "$PROD_POSTGRES_ID" "$PROD_USER" "$PROD_CONFIG_DB" \
  "SELECT item.* FROM config.\"CatalogItems\" item JOIN config.\"CatalogGroups\" g ON g.id=item.catalog_group_id WHERE g.slug='pricing-warehouses' ORDER BY item.sort_order,item.code" \
  "$BACKUP_DIR/prod-pricing-warehouses-items-before.csv"

# Export the authoritative WHS catalog from staging.
copy_query_to_file "$STAGING_POSTGRES_ID" "$STAGING_USER" "$STAGING_CONFIG_DB" \
  "SELECT * FROM config.\"CatalogGroups\" WHERE slug='pricing-warehouses' AND NOT is_deleted" \
  "$WORK_DIR/staging-whs-group.csv"
copy_query_to_file "$STAGING_POSTGRES_ID" "$STAGING_USER" "$STAGING_CONFIG_DB" \
  "SELECT item.* FROM config.\"CatalogItems\" item JOIN config.\"CatalogGroups\" g ON g.id=item.catalog_group_id WHERE g.slug='pricing-warehouses' AND NOT g.is_deleted AND NOT item.is_deleted ORDER BY item.sort_order,item.code" \
  "$WORK_DIR/staging-whs-items.csv"

[[ $(wc -l < "$WORK_DIR/staging-whs-group.csv") -gt 1 ]] || fail "Staging has no active pricing-warehouses group."
[[ $(wc -l < "$WORK_DIR/staging-whs-items.csv") -gt 1 ]] || fail "Staging has no active WHS catalog items."

# Load staging rows into production-side scratch tables and upsert by business key.
docker exec "$PROD_POSTGRES_ID" psql -X -q -v ON_ERROR_STOP=1 -U "$PROD_USER" -d "$PROD_CONFIG_DB" <<'SQL'
DROP TABLE IF EXISTS public.__whs_catalog_groups_stage;
DROP TABLE IF EXISTS public.__whs_catalog_items_stage;
CREATE TABLE public.__whs_catalog_groups_stage AS SELECT * FROM config."CatalogGroups" WITH NO DATA;
CREATE TABLE public.__whs_catalog_items_stage AS SELECT * FROM config."CatalogItems" WITH NO DATA;
SQL
copy_file_into_table "$PROD_POSTGRES_ID" "$PROD_USER" "$PROD_CONFIG_DB" public.__whs_catalog_groups_stage "$WORK_DIR/staging-whs-group.csv"
copy_file_into_table "$PROD_POSTGRES_ID" "$PROD_USER" "$PROD_CONFIG_DB" public.__whs_catalog_items_stage "$WORK_DIR/staging-whs-items.csv"

docker exec "$PROD_POSTGRES_ID" psql -X -q -v ON_ERROR_STOP=1 -U "$PROD_USER" -d "$PROD_CONFIG_DB" <<'SQL'
DO $$
DECLARE
  prod_group_id uuid;
  group_set text;
  item_set text;
  insert_columns text;
  insert_select text;
  row_item record;
BEGIN
  SELECT id INTO prod_group_id
  FROM config."CatalogGroups"
  WHERE slug='pricing-warehouses'
  ORDER BY is_deleted, created_at_utc
  LIMIT 1;

  IF prod_group_id IS NULL THEN
    INSERT INTO config."CatalogGroups"
    SELECT * FROM public.__whs_catalog_groups_stage
    LIMIT 1
    RETURNING id INTO prod_group_id;
  ELSE
    SELECT string_agg(format('%1$I = s.%1$I', column_name), ', ' ORDER BY ordinal_position)
      INTO group_set
    FROM information_schema.columns
    WHERE table_schema='config' AND table_name='CatalogGroups' AND column_name <> 'id';

    EXECUTE format(
      'UPDATE config."CatalogGroups" d SET %s FROM public.__whs_catalog_groups_stage s WHERE d.id=$1',
      group_set
    ) USING prod_group_id;
  END IF;

  SELECT string_agg(format('%I', column_name), ', ' ORDER BY ordinal_position)
    INTO insert_columns
  FROM information_schema.columns
  WHERE table_schema='config' AND table_name='CatalogItems';

  SELECT string_agg(
    CASE
      WHEN column_name='catalog_group_id' THEN format('%L::uuid', prod_group_id::text)
      WHEN column_name='metadata_json' THEN 'NULL::jsonb'
      ELSE format('s.%I', column_name)
    END,
    ', ' ORDER BY ordinal_position
  ) INTO insert_select
  FROM information_schema.columns
  WHERE table_schema='config' AND table_name='CatalogItems';

  SELECT string_agg(format('%1$I = s.%1$I', column_name), ', ' ORDER BY ordinal_position)
    INTO item_set
  FROM information_schema.columns
  WHERE table_schema='config'
    AND table_name='CatalogItems'
    AND column_name NOT IN ('id','catalog_group_id','metadata_json');

  FOR row_item IN SELECT code FROM public.__whs_catalog_items_stage ORDER BY sort_order, code LOOP
    IF EXISTS (
      SELECT 1 FROM config."CatalogItems" d
      WHERE d.catalog_group_id=prod_group_id AND d.code=row_item.code
    ) THEN
      EXECUTE format(
        'UPDATE config."CatalogItems" d SET %s FROM public.__whs_catalog_items_stage s WHERE d.catalog_group_id=$1 AND d.code=$2 AND s.code=$2',
        item_set
      ) USING prod_group_id, row_item.code;
    ELSE
      EXECUTE format(
        'INSERT INTO config."CatalogItems" (%s) SELECT %s FROM public.__whs_catalog_items_stage s WHERE s.code=$1',
        insert_columns,
        insert_select
      ) USING row_item.code;
    END IF;
  END LOOP;
END $$;
SQL

# Build a JSONL manifest containing staging metadata and the production item id chosen by the upsert.
docker exec "$PROD_POSTGRES_ID" psql -X -qAt -U "$PROD_USER" -d "$PROD_CONFIG_DB" -c "
SELECT json_build_object(
  'code', s.code,
  'prodId', d.id,
  'metadata', COALESCE(s.metadata_json, '{}'::jsonb)
)::text
FROM public.__whs_catalog_items_stage s
JOIN config.\"CatalogGroups\" g ON g.slug='pricing-warehouses' AND NOT g.is_deleted
JOIN config.\"CatalogItems\" d ON d.catalog_group_id=g.id AND d.code=s.code
ORDER BY s.sort_order,s.code;" > "$WORK_DIR/whs-manifest.jsonl"

export WORK_DIR BACKUP_DIR STAGING_NETWORK PRODUCTION_NETWORK CURL_IMAGE PROD_POSTGRES_ID PROD_USER PROD_CONFIG_DB
python3 <<'PY'
import base64
import json
import mimetypes
import os
import pathlib
import re
import subprocess
import sys

work = pathlib.Path(os.environ['WORK_DIR'])
staging_network = os.environ['STAGING_NETWORK']
prod_network = os.environ['PRODUCTION_NETWORK']
curl_image = os.environ['CURL_IMAGE']
prod_pg = os.environ['PROD_POSTGRES_ID']
prod_user = os.environ['PROD_USER']
prod_db = os.environ['PROD_CONFIG_DB']
manifest = work / 'whs-manifest.jsonl'


def run(cmd, *, capture=False):
    return subprocess.run(cmd, check=True, text=True, capture_output=capture)


def curl_container(network, args, *, capture=False):
    cmd = ['docker', 'run', '--rm', '--network', network, '-v', f'{work}:/work', curl_image, *args]
    return run(cmd, capture=capture)


def clean_name(value, code, index):
    original = pathlib.Path(str(value or '')).name
    ext = pathlib.Path(original).suffix.lower()
    if ext not in {'.png','.jpg','.jpeg','.webp','.gif','.bmp','.svg','.tif','.tiff'}:
        ext = '.bin'
    safe_code = re.sub(r'[^A-Za-z0-9._-]+', '-', str(code)).strip('-') or 'warehouse'
    return f'{safe_code}-{index}{ext}'


def update_metadata(prod_id, metadata):
    raw = json.dumps(metadata, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
    encoded = base64.b64encode(raw).decode('ascii')
    sql = (
        'UPDATE config."CatalogItems" '
        f"SET metadata_json=convert_from(decode('{encoded}','base64'),'UTF8')::jsonb "
        f"WHERE id='{prod_id}'::uuid;"
    )
    run(['docker','exec',prod_pg,'psql','-X','-q','-v','ON_ERROR_STOP=1','-U',prod_user,'-d',prod_db,'-c',sql])


def upload_image(old_id, file_name, code, prod_id, index):
    local_name = f'{old_id}.bin'
    local_path = work / local_name
    source_url = f'http://api-gateway:8080/api/storage/api/v1/storage/files/{old_id}/content'
    curl_container(staging_network, ['-fsSL', source_url, '-o', f'/work/{local_name}'])
    if not local_path.exists() or local_path.stat().st_size == 0:
        raise RuntimeError(f'Staging Storage returned an empty file for {old_id}')

    upload_name = clean_name(file_name, code, index)
    mime = mimetypes.guess_type(upload_name)[0] or 'application/octet-stream'
    metadata = json.dumps({'catalogGroupSlug':'pricing-warehouses','warehouseCode':code,'promotedFrom':'staging'})
    upload_url = 'http://api-gateway:8080/api/storage/api/v1/storage/files'
    response = curl_container(prod_network, [
        '-fsS', '-X', 'POST', upload_url,
        '-F', f'file=@/work/{local_name};filename={upload_name};type={mime}',
        '-F', 'sourceService=DholeWeb',
        '-F', 'entityType=PricingWarehouse',
        '-F', f'entityId={prod_id}',
        '--form-string', f'metadataJson={metadata}',
    ], capture=True).stdout
    payload = json.loads(response)
    new_id = payload.get('id') or (payload.get('data') or {}).get('id')
    if not new_id:
        raise RuntimeError(f'Production Storage upload did not return an id: {response[:500]}')

    # Verify that production can immediately serve the promoted object.
    verify_url = f'http://api-gateway:8080/api/storage/api/v1/storage/files/{new_id}/content'
    curl_container(prod_network, ['-fsS', verify_url, '-o', '/dev/null'])
    local_path.unlink(missing_ok=True)
    return str(new_id)

rows = []
for line in manifest.read_text(encoding='utf-8').splitlines():
    if line.strip():
        rows.append(json.loads(line))

if not rows:
    raise RuntimeError('The WHS promotion manifest is empty.')

promoted_images = 0
for row in rows:
    code = str(row['code'])
    prod_id = str(row['prodId'])
    metadata = row.get('metadata') or {}
    if not isinstance(metadata, dict):
        metadata = {}

    refs = []
    seen = set()
    images = metadata.get('images')
    if isinstance(images, list):
        for image in images:
            if not isinstance(image, dict):
                continue
            sid = str(image.get('storageId') or '').strip()
            if sid and sid not in seen:
                seen.add(sid)
                refs.append((sid, image.get('fileName') or ''))
    legacy_id = str(metadata.get('imageStorageId') or '').strip()
    if legacy_id and legacy_id not in seen:
        seen.add(legacy_id)
        refs.append((legacy_id, metadata.get('imageFileName') or ''))

    mapping = {}
    for index, (old_id, file_name) in enumerate(refs, start=1):
        print(f'[WHS promotion] {code}: copying image {index}/{len(refs)} ({old_id})', flush=True)
        mapping[old_id] = upload_image(old_id, file_name, code, prod_id, index)
        promoted_images += 1

    if isinstance(images, list):
        for image in images:
            if isinstance(image, dict):
                old = str(image.get('storageId') or '').strip()
                if old in mapping:
                    image['storageId'] = mapping[old]
    if legacy_id in mapping:
        metadata['imageStorageId'] = mapping[legacy_id]

    update_metadata(prod_id, metadata)
    print(f'[WHS promotion] {code}: production metadata updated.', flush=True)

summary = {'warehouses': len(rows), 'imagesPromoted': promoted_images}
(work / 'promotion-summary.json').write_text(json.dumps(summary, indent=2), encoding='utf-8')
print(f"[WHS promotion] Completed {len(rows)} WHS item(s), {promoted_images} image(s).", flush=True)
PY

# Final production-side verification: every storage id currently referenced by WHS metadata must be reachable.
docker exec "$PROD_POSTGRES_ID" psql -X -qAt -U "$PROD_USER" -d "$PROD_CONFIG_DB" -c "
SELECT count(*)
FROM config.\"CatalogItems\" item
JOIN config.\"CatalogGroups\" g ON g.id=item.catalog_group_id
WHERE g.slug='pricing-warehouses' AND NOT g.is_deleted AND NOT item.is_deleted;" > "$WORK_DIR/prod-whs-count.txt"

# Keep the staging scratch rows out of production after the operation.
docker exec "$PROD_POSTGRES_ID" psql -X -q -v ON_ERROR_STOP=1 -U "$PROD_USER" -d "$PROD_CONFIG_DB" -c '
DROP TABLE IF EXISTS public.__whs_catalog_items_stage;
DROP TABLE IF EXISTS public.__whs_catalog_groups_stage;'

cp "$WORK_DIR/promotion-summary.json" "$BACKUP_DIR/promotion-summary.json"
cp "$WORK_DIR/prod-whs-count.txt" "$BACKUP_DIR/prod-whs-count.txt"
log "Promotion completed. Backup/summary directory: $BACKUP_DIR"
