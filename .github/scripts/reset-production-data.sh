#!/usr/bin/env bash
set -euo pipefail

PG_CONTAINER=postgres
timestamp="$(date -u +%Y%m%dT%H%M%SZ)"
backup_dir="/var/lib/postgresql/data/dhole-reset-backups/data-reset-${timestamp}"
retained_counts="${RUNNER_TEMP:-/tmp}/dhole-retained-counts-${timestamp}.txt"

query_tables() {
  local db="$1"
  docker exec "$PG_CONTAINER" sh -lc 'PGPASSWORD="${POSTGRES_PASSWORD:-}" psql -U "${POSTGRES_USER:-postgres}" -d "$1" -At -c "SELECT schemaname || CHR(46) || relname FROM pg_stat_user_tables ORDER BY schemaname, relname;"' sh "$db"
}

run_sql() {
  local db="$1"
  local sql="$2"
  docker exec "$PG_CONTAINER" sh -lc 'PGPASSWORD="${POSTGRES_PASSWORD:-}" psql -v ON_ERROR_STOP=1 -U "${POSTGRES_USER:-postgres}" -d "$1" -c "$2"' sh "$db" "$sql"
}

count_table() {
  local db="$1"
  local table="$2"
  docker exec "$PG_CONTAINER" sh -lc 'PGPASSWORD="${POSTGRES_PASSWORD:-}" psql -v ON_ERROR_STOP=1 -U "${POSTGRES_USER:-postgres}" -d "$1" -At -c "SELECT COUNT(*) FROM $2;"' sh "$db" "$table"
}

check_exact_tables() {
  local db="$1"
  local expected="$2"
  local actual_file expected_file
  actual_file="$(mktemp)"
  expected_file="$(mktemp)"
  query_tables "$db" | sort > "$actual_file"
  printf '%s\n' "$expected" | sed 's/^[[:space:]]*//;s/[[:space:]]*$//;/^$/d' | sort > "$expected_file"
  if ! diff -u "$expected_file" "$actual_file"; then
    echo "ERROR: table inventory for $db differs from the reviewed whitelist. No data has been deleted."
    rm -f "$actual_file" "$expected_file"
    exit 1
  fi
  rm -f "$actual_file" "$expected_file"
}

echo '=== Verify reviewed table inventory before any mutation ==='
check_exact_tables dhole_ai '
ai.AiConnections
ai.AiEmailAnalysisJobs
ai.AiExecutionAttempts
ai.AiExecutions
ai.AiModels
ai.AiProfileModels
ai.AiProfiles
ai.AiPromptTemplates
ai.inbox_messages
ai.outbox_messages
public.__EFMigrationsHistory'

check_exact_tables dhole_auditlogs '
auditlogs.AuditEvents
auditlogs.inbox_messages
public.__EFMigrationsHistory'

check_exact_tables dhole_auth '
auth.RoleScopes
auth.Roles
auth.Scopes
auth.Sessions
auth.UserRoles
auth.UserScopes
auth.Users
auth.inbox_messages
auth.outbox_messages
public.__EFMigrationsHistory'

check_exact_tables dhole_config '
config.CatalogGroups
config.CatalogItems
config.inbox_messages
config.outbox_messages
public.__EFMigrationsHistory'

check_exact_tables dhole_data_extraction '
data_extraction.ColumnMappingProfiles
data_extraction.ColumnMappingRules
data_extraction.EmailAiAnalysisRequests
data_extraction.EmailAttachments
data_extraction.EmailExtractionJobs
data_extraction.EmailIngestionAccounts
data_extraction.EmailMessages
data_extraction.ExtractionExecutions
data_extraction.ExtractionIssues
data_extraction.PricingExtractionRecords
data_extraction.SourceDocuments
data_extraction.inbox_messages
data_extraction.outbox_messages
public.__EFMigrationsHistory'

check_exact_tables dhole_notifications '
notifications.inbox_messages
notifications.notification_delivery_attempts
notifications.notification_messages
notifications.notification_recipients
notifications.notification_templates
notifications.outbox_messages'

check_exact_tables dhole_pricing '
pricing.CarrierFreeDayRules
pricing.CostIncoterms
pricing.CostServices
pricing.Costs
pricing.ImportFclRates
pricing.LclRateSources
pricing.LogisticsNews
pricing.LogisticsNewsRateImpacts
pricing.OwnLclConsolidationPricingLines
pricing.OwnLclConsolidations
pricing.OwnLclHistoricalRates
pricing.PricingImportFromExtractionJobs
pricing.RateComparisonDetails
pricing.RateComparisons
pricing.RateContainerAllocations
pricing.RateDetails
pricing.RateHeaders
pricing.RateRequests
pricing.RateRevisions
pricing.RateServices
pricing.RateTermBlockItems
pricing.RateTermBlockServices
pricing.RateTermBlocks
pricing.RateTermItems
pricing.inbox_messages
pricing.outbox_messages
public.__EFMigrationsHistory'

check_exact_tables dhole_reports '
public.__EFMigrationsHistory
reports.report_templates'

check_exact_tables dhole_storage '
public.__EFMigrationsHistory
storage.FileReferences
storage.FileVersions
storage.Files
storage.StorageProviders
storage.inbox_messages
storage.outbox_messages'

declare -A RESET_SQL
RESET_SQL[dhole_ai]='TRUNCATE TABLE ai."AiEmailAnalysisJobs", ai."AiExecutionAttempts", ai."AiExecutions", ai.inbox_messages, ai.outbox_messages RESTART IDENTITY;'
RESET_SQL[dhole_auditlogs]='TRUNCATE TABLE auditlogs."AuditEvents", auditlogs.inbox_messages RESTART IDENTITY;'
RESET_SQL[dhole_auth]='TRUNCATE TABLE auth."Sessions", auth.inbox_messages, auth.outbox_messages RESTART IDENTITY;'
RESET_SQL[dhole_config]='TRUNCATE TABLE config.inbox_messages, config.outbox_messages RESTART IDENTITY;'
RESET_SQL[dhole_data_extraction]='TRUNCATE TABLE data_extraction."EmailAiAnalysisRequests", data_extraction."EmailExtractionJobs", data_extraction."EmailAttachments", data_extraction."EmailMessages", data_extraction."ExtractionIssues", data_extraction."PricingExtractionRecords", data_extraction."SourceDocuments", data_extraction."ExtractionExecutions", data_extraction.inbox_messages, data_extraction.outbox_messages RESTART IDENTITY;'
RESET_SQL[dhole_notifications]='TRUNCATE TABLE notifications.notification_delivery_attempts, notifications.notification_recipients, notifications.notification_messages, notifications.inbox_messages, notifications.outbox_messages RESTART IDENTITY;'
RESET_SQL[dhole_pricing]='TRUNCATE TABLE pricing."RateComparisonDetails", pricing."RateComparisons", pricing."RateRevisions", pricing."RateContainerAllocations", pricing."RateDetails", pricing."RateServices", pricing."RateHeaders", pricing."RateRequests", pricing."PricingImportFromExtractionJobs", pricing."LogisticsNewsRateImpacts", pricing."LogisticsNews", pricing."OwnLclConsolidationPricingLines", pricing."OwnLclConsolidations", pricing.inbox_messages, pricing.outbox_messages RESTART IDENTITY;'
RESET_SQL[dhole_storage]='TRUNCATE TABLE storage.inbox_messages, storage.outbox_messages RESTART IDENTITY;'

echo '=== Pause Dhole application containers for a consistent backup/reset point ==='
mapfile -t app_containers < <(docker network inspect dhole --format '{{range .Containers}}{{.Name}}{{"\n"}}{{end}}' | grep -E '^dhole-(ai|api-gateway|auditlogs|auth|config|dataextraction|dhole-web|notifications|pricing|reports|storage)-' | sort || true)
paused=()
cleanup_pause() {
  if [ "${#paused[@]}" -gt 0 ]; then
    docker unpause "${paused[@]}" >/dev/null 2>&1 || true
  fi
}
trap cleanup_pause EXIT
for c in "${app_containers[@]}"; do
  [ -n "$c" ] || continue
  docker pause "$c" >/dev/null
  paused+=("$c")
done
echo "PAUSED_CONTAINERS=${#paused[@]}"

echo '=== Create full compressed backups inside the persistent PostgreSQL volume ==='
docker exec "$PG_CONTAINER" sh -lc 'mkdir -p "$1" && chmod 700 "$1"' sh "$backup_dir"
dbs=(dhole_ai dhole_auditlogs dhole_auth dhole_config dhole_data_extraction dhole_notifications dhole_pricing dhole_reports dhole_storage)
for db in "${dbs[@]}"; do
  file="$backup_dir/${db}.dump"
  docker exec "$PG_CONTAINER" sh -lc 'set -eu; PGPASSWORD="${POSTGRES_PASSWORD:-}" pg_dump -U "${POSTGRES_USER:-postgres}" -Fc --no-owner --no-privileges -f "$2" "$1"; test -s "$2"; test "$(head -c 5 "$2")" = PGDMP' sh "$db" "$file"
  size="$(docker exec "$PG_CONTAINER" stat -c%s "$file")"
  echo "BACKUP_OK|$db|$size"
done
docker exec "$PG_CONTAINER" sh -lc 'sha256sum "$1"/*.dump > "$1/SHA256SUMS" && chmod 600 "$1"/*' sh "$backup_dir"
echo "BACKUP_DIR|postgres:$backup_dir"

echo '=== Snapshot every retained table count before reset ==='
: > "$retained_counts"
while IFS='|' read -r db table; do
  [ -n "$db" ] || continue
  count="$(count_table "$db" "$table")"
  printf '%s|%s|%s\n' "$db" "$table" "$count" | tee -a "$retained_counts"
done <<'EOF'
dhole_ai|ai."AiConnections"
dhole_ai|ai."AiModels"
dhole_ai|ai."AiProfileModels"
dhole_ai|ai."AiProfiles"
dhole_ai|ai."AiPromptTemplates"
dhole_ai|public."__EFMigrationsHistory"
dhole_auditlogs|public."__EFMigrationsHistory"
dhole_auth|auth."RoleScopes"
dhole_auth|auth."Roles"
dhole_auth|auth."Scopes"
dhole_auth|auth."UserRoles"
dhole_auth|auth."UserScopes"
dhole_auth|auth."Users"
dhole_auth|public."__EFMigrationsHistory"
dhole_config|config."CatalogGroups"
dhole_config|config."CatalogItems"
dhole_config|public."__EFMigrationsHistory"
dhole_data_extraction|data_extraction."ColumnMappingProfiles"
dhole_data_extraction|data_extraction."ColumnMappingRules"
dhole_data_extraction|data_extraction."EmailIngestionAccounts"
dhole_data_extraction|public."__EFMigrationsHistory"
dhole_notifications|notifications.notification_templates
dhole_pricing|pricing."CarrierFreeDayRules"
dhole_pricing|pricing."CostIncoterms"
dhole_pricing|pricing."CostServices"
dhole_pricing|pricing."Costs"
dhole_pricing|pricing."ImportFclRates"
dhole_pricing|pricing."LclRateSources"
dhole_pricing|pricing."OwnLclHistoricalRates"
dhole_pricing|pricing."RateTermBlockItems"
dhole_pricing|pricing."RateTermBlockServices"
dhole_pricing|pricing."RateTermBlocks"
dhole_pricing|pricing."RateTermItems"
dhole_pricing|public."__EFMigrationsHistory"
dhole_reports|reports.report_templates
dhole_reports|public."__EFMigrationsHistory"
dhole_storage|storage."FileReferences"
dhole_storage|storage."FileVersions"
dhole_storage|storage."Files"
dhole_storage|storage."StorageProviders"
dhole_storage|public."__EFMigrationsHistory"
EOF
docker cp "$retained_counts" "$PG_CONTAINER:$backup_dir/retained-counts.txt"
docker exec "$PG_CONTAINER" chmod 600 "$backup_dir/retained-counts.txt"

echo '=== Preflight every truncate inside a rolled-back transaction ==='
for db in "${!RESET_SQL[@]}"; do
  run_sql "$db" "BEGIN; ${RESET_SQL[$db]} ROLLBACK;"
  echo "PREFLIGHT_OK|$db"
done

echo '=== Execute reviewed transactional/history reset (NO CASCADE) ==='
for db in dhole_ai dhole_auditlogs dhole_auth dhole_config dhole_data_extraction dhole_notifications dhole_pricing dhole_storage; do
  run_sql "$db" "BEGIN; ${RESET_SQL[$db]} COMMIT;"
  echo "TRUNCATE_OK|$db"
done

echo '=== Verify all retained table counts are unchanged ==='
while IFS='|' read -r db table expected; do
  [ -n "$db" ] || continue
  actual="$(count_table "$db" "$table")"
  echo "KEEP_CHECK|$db|$table|before=$expected|after=$actual"
  if [ "$actual" != "$expected" ]; then
    echo "ERROR: retained table changed: $db $table"
    exit 1
  fi
done < "$retained_counts"

echo '=== Verify representative cleaned tables are empty ==='
for spec in \
  'dhole_ai|ai."AiExecutions"' \
  'dhole_ai|ai.outbox_messages' \
  'dhole_auditlogs|auditlogs."AuditEvents"' \
  'dhole_auth|auth."Sessions"' \
  'dhole_config|config.outbox_messages' \
  'dhole_data_extraction|data_extraction."ExtractionExecutions"' \
  'dhole_data_extraction|data_extraction."PricingExtractionRecords"' \
  'dhole_notifications|notifications.notification_messages' \
  'dhole_pricing|pricing."RateHeaders"' \
  'dhole_pricing|pricing."OwnLclConsolidations"' \
  'dhole_storage|storage.outbox_messages'; do
  db="${spec%%|*}"
  table="${spec#*|}"
  count="$(count_table "$db" "$table")"
  echo "ZERO_CHECK|$db|$table|$count"
  [ "$count" = "0" ]
done

echo '=== Resume Dhole application containers ==='
cleanup_pause
paused=()
trap - EXIT

echo '=== Verify application containers resumed ==='
for c in "${app_containers[@]}"; do
  for attempt in $(seq 1 30); do
    state="$(docker inspect -f '{{.State.Status}}' "$c")"
    health="$(docker inspect -f '{{if .State.Health}}{{.State.Health.Status}}{{else}}none{{end}}' "$c")"
    if [ "$state" = running ] && { [ "$health" = healthy ] || [ "$health" = none ]; }; then
      echo "CONTAINER_OK|$c|$state|$health"
      break
    fi
    if [ "$attempt" -eq 30 ]; then
      echo "CONTAINER_FAILED|$c|$state|$health"
      exit 1
    fi
    sleep 2
  done
done

echo "RESET_COMPLETE|postgres:$backup_dir"
