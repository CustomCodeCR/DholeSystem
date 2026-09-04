#!/usr/bin/env bash
set -euo pipefail

PG_CONTAINER=postgres
DB=dhole_pricing
timestamp="$(date -u +%Y%m%dT%H%M%SZ)"
backup_dir="/var/lib/postgresql/data/dhole-reset-backups/pricing-${timestamp}"
counts_file="${RUNNER_TEMP:-/tmp}/pricing-retained-${timestamp}.txt"

run_sql() {
  local sql="$1"
  docker exec "$PG_CONTAINER" sh -lc 'PGPASSWORD="${POSTGRES_PASSWORD:-}" psql -v ON_ERROR_STOP=1 -U "${POSTGRES_USER:-postgres}" -d "$1" -c "$2"' sh "$DB" "$sql"
}

count_table() {
  local table="$1"
  docker exec "$PG_CONTAINER" sh -lc 'PGPASSWORD="${POSTGRES_PASSWORD:-}" psql -v ON_ERROR_STOP=1 -U "${POSTGRES_USER:-postgres}" -d "$1" -At -c "SELECT COUNT(*) FROM $2;"' sh "$DB" "$table"
}

RESET_SQL='TRUNCATE TABLE
  pricing."RateComparisonDetails",
  pricing."RateComparisons",
  pricing."RateRevisions",
  pricing."RateContainerAllocations",
  pricing."RateDetails",
  pricing."RateServices",
  pricing."RateHeaders",
  pricing."RateRequests",
  pricing."PricingImportFromExtractionJobs",
  pricing."LogisticsNewsRateImpacts",
  pricing."LogisticsNews",
  pricing."OwnLclConsolidationPricingLines",
  pricing."OwnLclConsolidations",
  pricing."OwnLclHistoricalRates",
  pricing.inbox_messages,
  pricing.outbox_messages
RESTART IDENTITY;'

echo '=== Verify pricing tables exist before any mutation ==='
for table in \
  'pricing."ImportFclRates"' \
  'pricing."Costs"' \
  'pricing."CostServices"' \
  'pricing."CostIncoterms"' \
  'pricing."CarrierFreeDayRules"' \
  'pricing."LclRateSources"' \
  'pricing."RateTermItems"' \
  'pricing."RateTermBlocks"' \
  'pricing."RateTermBlockItems"' \
  'pricing."RateTermBlockServices"' \
  'pricing."RateHeaders"' \
  'pricing."OwnLclHistoricalRates"'; do
  count_table "$table" >/dev/null
  echo "TABLE_OK|$table"
done

echo '=== Pause Pricing containers ==='
mapfile -t pricing_containers < <(docker network inspect dhole --format '{{range .Containers}}{{.Name}}{{"\n"}}{{end}}' | grep -E '^dhole-pricing-' | sort || true)
paused=()
cleanup_pause() {
  if [ "${#paused[@]}" -gt 0 ]; then
    docker unpause "${paused[@]}" >/dev/null 2>&1 || true
  fi
}
trap cleanup_pause EXIT
for c in "${pricing_containers[@]}"; do
  [ -n "$c" ] || continue
  docker pause "$c" >/dev/null
  paused+=("$c")
done
echo "PAUSED_CONTAINERS=${#paused[@]}"

echo '=== Full dhole_pricing backup ==='
docker exec "$PG_CONTAINER" sh -lc 'mkdir -p "$1" && chmod 700 "$1"' sh "$backup_dir"
backup_file="$backup_dir/dhole_pricing.dump"
docker exec "$PG_CONTAINER" sh -lc 'set -eu; PGPASSWORD="${POSTGRES_PASSWORD:-}" pg_dump -U "${POSTGRES_USER:-postgres}" -Fc --no-owner --no-privileges -f "$2" "$1"; test -s "$2"; test "$(head -c 5 "$2")" = PGDMP' sh "$DB" "$backup_file"
docker exec "$PG_CONTAINER" sh -lc 'sha256sum "$1/dhole_pricing.dump" > "$1/SHA256SUMS" && chmod 600 "$1"/*' sh "$backup_dir"
echo "BACKUP_OK|postgres:$backup_file|$(docker exec "$PG_CONTAINER" stat -c%s "$backup_file")"

echo '=== Snapshot retained Pricing master/import tables ==='
: > "$counts_file"
for table in \
  'pricing."ImportFclRates"' \
  'pricing."Costs"' \
  'pricing."CostServices"' \
  'pricing."CostIncoterms"' \
  'pricing."CarrierFreeDayRules"' \
  'pricing."LclRateSources"' \
  'pricing."RateTermItems"' \
  'pricing."RateTermBlocks"' \
  'pricing."RateTermBlockItems"' \
  'pricing."RateTermBlockServices"' \
  'public."__EFMigrationsHistory"'; do
  count="$(count_table "$table")"
  printf '%s|%s\n' "$table" "$count" | tee -a "$counts_file"
done

echo '=== Preflight TRUNCATE in rollback transaction ==='
run_sql "BEGIN; $RESET_SQL ROLLBACK;"
echo 'PREFLIGHT_OK'

echo '=== Execute Pricing reset ==='
run_sql "BEGIN; $RESET_SQL COMMIT;"
echo 'TRUNCATE_OK'

echo '=== Verify retained tables unchanged ==='
while IFS='|' read -r table expected; do
  [ -n "$table" ] || continue
  actual="$(count_table "$table")"
  echo "KEEP_CHECK|$table|before=$expected|after=$actual"
  [ "$actual" = "$expected" ]
done < "$counts_file"

echo '=== Verify imported rates remain ==='
imported="$(count_table 'pricing."ImportFclRates"')"
echo "IMPORTED_RATES_RETAINED=$imported"
[ "$imported" -gt 0 ]

echo '=== Verify cleaned tables are empty ==='
for table in \
  'pricing."RateHeaders"' \
  'pricing."RateDetails"' \
  'pricing."RateContainerAllocations"' \
  'pricing."RateServices"' \
  'pricing."RateComparisons"' \
  'pricing."PricingImportFromExtractionJobs"' \
  'pricing."OwnLclConsolidations"' \
  'pricing."OwnLclHistoricalRates"' \
  'pricing.inbox_messages' \
  'pricing.outbox_messages'; do
  count="$(count_table "$table")"
  echo "ZERO_CHECK|$table|$count"
  [ "$count" = 0 ]
done

echo '=== Resume Pricing containers ==='
cleanup_pause
paused=()
trap - EXIT

for c in "${pricing_containers[@]}"; do
  state="$(docker inspect -f '{{.State.Status}}' "$c")"
  health="$(docker inspect -f '{{if .State.Health}}{{.State.Health.Status}}{{else}}none{{end}}' "$c")"
  echo "CONTAINER|$c|$state|$health"
  [ "$state" = running ]
done

echo "PRICING_RESET_COMPLETE|backup=postgres:$backup_file|imported_rates=$imported"
