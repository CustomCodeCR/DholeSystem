# F6/F9 — Migración segura Redis RDB → AOF para Dhole staging

**Release:** `rt-20261107-01` · **Versión candidata:** `1.13.0`.
**Estado:** ENSAYADA EN CI AISLADO, **NO EJECUTADA EN STAGING**.
**Ámbito:** exclusivamente Redis del proyecto Docker Compose `dhole-staging-infra`.
**Restricción:** ejecutar en la ventana F9 del batch aprobado; no alterar `master`, producción ni Redis staging durante F0–F8.

## Hallazgo de pérdida de datos

El ensayo inicial [#42507114616](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42507114616)
arrancó Redis 7 **con `appendonly yes` sobre un volumen que solo contenía `dump.rdb`**,
sin convertir el dataset activo. Tras ese arranque **faltaron entradas de Redis Streams**.
Por ello está **PROHIBIDO** resolver el problema con únicamente
`docker compose up -d redis` al introducir `--appendonly yes`.

El ensayo corregido [#42507199248](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42507199248),
SHA `d3fc51bc2e235915e16242ab33b76c10c9b987a8`, sí conservó
100 eventos RDB previos y otro posterior a la conversión AOF, a través de dos
recreaciones con el mismo volumen privado. La migración debe convertir el dataset
vivo **antes** del cambio de comando en Compose.

## Precondiciones obligatorias de staging

1. Aprobación y ventana del batch coordinado F9, con SHAs congelados y flags
   realtime OFF. No ejecutar si F6/F7 no cumplen sus pruebas en entorno aislado
   o si los responsables no han autorizado explícitamente los cambios en staging.
2. Identificar inequívocamente el contenedor Redis por etiquetas Docker
   `com.docker.compose.project=dhole-staging-infra` y
   `com.docker.compose.service=redis`; debe existir **exactamente uno**.
   Comprobar que el volumen `/data` es persistente, su nombre es el esperado y
   no corresponde a producción. Nunca usar IDs obtenidos de filtros ambiguos.
3. Inventariar `DBSIZE`, `INFO persistence`, `INFO replication`, `XINFO STREAM`
   por stream, `XPENDING` por consumer group y la cuota libre del volumen.
   Resguardar PostgreSQL Outbox/Inbox y los cursores de Redis.
4. Crear y **verificar un backup fuera del volumen Redis activo** (snapshot RDB y
   copia consistente del volumen, retenida fuera del servidor) antes de cualquier
   comando de escritura. Tener un procedimiento probado de restauración en una
   instancia aislada; no confiar solo en `docker volume ls`.
5. Establecer una breve ventana de quiescencia de productores críticos o un
   watermark de eventos para poder comprobar que ningún evento confirmado
   se pierde durante el cambio. Nunca borrar streams ni reiniciar grupos/cursors.

## Procedimiento aprobado (solo en staging y bajo ventana F9)

Ejecutar desde una sesión operativa identificada, **no** automáticamente mediante
el workflow de auditoría de solo lectura. Los ejemplos usan `$STAGING_REDIS`,
que debe obtenerse del filtro exacto de etiquetas y verificarse contra el
proyecto `dhole-staging-infra`.

1. Antes de cambiar Docker Compose, crear RDB persistente y respaldarlo:

   `docker exec "$STAGING_REDIS" redis-cli SAVE`

   Comprobar `rdb_last_bgsave_status=ok` y que el backup aislado pueda abrirse.
2. **Con el Redis actual todavía encendido y con todos sus datos cargados**:

   `docker exec "$STAGING_REDIS" redis-cli CONFIG SET appendonly yes`

   Esperar a que termine la escritura inicial en segundo plano. No reiniciar
   mientras `aof_rewrite_in_progress=1`, `aof_current_size=0`,
   `aof_last_bgrewrite_status!=ok` o `aof_last_write_status!=ok`.
   Comprobar que `INFO persistence` ahora informa `aof_enabled=1`.
3. Inspeccionar el manifiesto AOF multiparte de Redis 7 y los archivos base/
   incremental dentro de `/data` (sin exponer datos a logs). Comprobar
   el watermark exacto de eventos y preservar la copia RDB de respaldo.
4. Solo cuando se acrediten esas condiciones, aplicar **la misma configuración
   revisada** de `deploy/docker-compose.staging-infra.yml` que declara
   `redis-server --appendonly yes --appendfsync everysec`. Recrear únicamente
   el Redis identificado de staging, nunca el proyecto de producción.
5. Comprobar `aof_enabled=1`, `aof_last_write_status=ok`, misma cantidad y
   los mismos `event_id` de los streams, claves de coordinación, grupos y
   pendientes; verificar que no disminuyan los watermarks confirmados.
6. Ejecutar restore desde backup independiente en una **instancia aislada**,
   recuperar Outbox pendiente por idempotency key y medir acumulación/replay,
   latencias, alertas y permisos de la conexión real. Documentar toda evidencia,
   redacciones, SHAs e identidad de la ventana.

## Abort/rollback

- Ante pérdida de eventos, fallo de fsync, inconsistencia de snapshot o grupos,
  suspender el proceso y **mantener flags realtime OFF**. No efectuar más
  recreaciones sobre un volumen posiblemente incompatible.
- Conservar volumen AOF, RDB original y backup independiente para comparar y
  restaurar en host aislado. No hacer `FLUSHALL`, `XTRIM`, `XGROUP DESTROY` ni
  restaurar un RDB viejo encima de un AOF con eventos posteriores.
- Si una restauración real falla o no puede compararse Outbox/Inbox, F0/F2/F6
  mantienen `approval=false`, F7 permanece `formalApproved=false`; prohibido
  avanzar el release al siguiente gate.

## Trazabilidad y limitaciones

- [CI falla segura #42507114616](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42507114616):
  impide iniciar con AOF sobre RDB sin conversión previa.
- [CI conversión segura #42507199248](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42507199248):
  100+1 eventos conservados con conversión en línea y dos reinicios; solo
  Redis sintético en runner GitHub-hosted.
- [CI caos F7 #42506868019](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42506868019):
  AOF persistente/consumer replay/backlog en Docker privado.
- La última lectura de staging disponible [#42490276695](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42490276695)
  evidenció `aof_enabled=0`. **No** sustituirla por un valor supuesto.
