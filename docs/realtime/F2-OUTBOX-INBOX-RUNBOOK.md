# F2 — Outbox/Inbox y Redis Streams: piloto CRM (candidato aislado)

**Plan:** CODEX_DHOLE_REALTIME_PLAN_POR_FASES_MEDIBLES.md v2.1.0  
**Release:** `rt-20261107-01`  
**Rama:** `feature/dhole-realtime-universal-rt-20261107-01`  
**Estado:** `EN_PROGRESO_PRELIMINAR`, **NO aprobado**; F0/F1 aún sin gate formal aprobado.

## Componentes

- `DholeCRMService/src/Dhole.Crm.Infrastructure/Persistence/Migrations/20261108130000_AddRealtimeDurabilityPilot.cs`: nuevas tablas **separadas** `crm.crm_realtime_outbox`, `crm.crm_realtime_inbox`; la outbox de recordatorios CRM NO cambia. Índices parciales Pending/Leased/DeadLetter y restricción por estado.
- `CrmRealtimeOutboxWriter.AppendAsync`: exige una transacción EF Core explícita existente, valida un envelope mínimo CRM y realiza INSERT dentro de la misma transacción. No publica Redis desde REST ni hace commit propio. Integración de mutaciones REST reales a F6.01 (NO implementada en F2).
- `CrmRealtimeOutboxProcessor`: selecciona hasta 100 filas mediante `FOR UPDATE SKIP LOCKED`, emite un lease por lote con token y 60s, envía XADD tras commit, guarda stream ID, reintenta con exponencial + jitter, y pasa a `DeadLetter` tras 5 intentos. Si falla PostgreSQL antes del marcado como publicado, la fila con lease caducado es reprocesable; puede haber redelivery sin efectos de negocio debido a Inbox.
- `CrmRealtimeInboxStore`: usa PK `(event_id, consumer_name)` en la misma transacción que el efecto de proyección. En duplicado retorna false, nunca aplica dos veces. ACK Redis posterior al commit de base de datos.
- `CrmRealtimeInboxConsumer`: consumidor **solo para pruebas de F2**, no registrado como worker de producción. Relee pending del mismo consumer ID, luego `>`. Reclamación de PEL de otros IDs/instancias y DLQ de mensajes malformados pendientes de completar y probar.
- `CrmRealtimeOutboxWorker`: registrado, inactivo salvo que **ambos** flags estén activos: `Features:UniversalRealtimeEnabled=true` y `Realtime:Outbox:Enabled=true`. Sin flags añadidos a configuración desplegada, por lo que ambos son `false`. Ninguna ruta REST fue conectada al nuevo writer todavía.

## Identidad y particionamiento

- Piloto: `dhole.crm.realtime.v1`. Las columnas `stream_name` y `event_id` se persisten en PostgreSQL, y la entrada Redis lleva `event_id`, `event_type`, `payload_json`.
- Idempotencia: lógica de negocio / proyección guardada por `(event_id, consumer_name)`. XADD at-least-once; nunca afirmar exactly-once en transporte.
- En F6 podrán asignarse streams por dominio si volumen/retención lo requiere, con reglas de orden agregado y versionado. No usar un stream único como supuesto de escala a futuro.

## Operación y seguridad

- **No activar** en producción ni staging hasta batch completo de 17 repos. No abrir PR por fase ni promover paquetes NuGet aislados.
- Retención PostgreSQL: mantener Outbox Published y Inbox al menos el horizonte máximo de reconciliación (a definir con p95/p99, volumen y offline real). No purgar sin copia y evidencia de consumidores al día.
- Redis infraestructura en staging/producción: confirmar `appendonly yes`, `appendfsync everysec` (y alternativa de mayor durabilidad según RPO acordado), volumen persistente y restauración probada. El Compose existente y la configuración runtime deben auditarse antes de cambiarse; **no se ha verificado AOF real**.
- **No usar XTRIM MAXLEN arbitrario**: definir MINID/retención temporal + margen mayor a offline/PELs/lag. Alarmar si oldest pending supera SLO; definir umbrales contra medición real.
- Métricas publicadas en `Meter("Dhole.Crm.Realtime.Outbox")`: `realtime_outbox_published`, `realtime_outbox_retried`, `realtime_outbox_deadletter`. Exportador de observabilidad pendiente.
- Seguridad: no loggear envelope/secretos, limitar payload a mínimos; `AudienceRef` requiere resolución posterior de grupos autorizados en F3.

## Diagnóstico SQL solo lectura

```sql
SELECT status, COUNT(*) AS messages, MAX(attempt_count) AS max_attempts,
       MIN(created_at) AS oldest_at
FROM crm.crm_realtime_outbox
GROUP BY status ORDER BY status;
SELECT event_id, attempt_count, last_error, created_at
FROM crm.crm_realtime_outbox
WHERE status='DeadLetter' ORDER BY created_at LIMIT 100;
SELECT consumer_name, COUNT(*) AS handled FROM crm.crm_realtime_inbox GROUP BY consumer_name;
```

## Recuperación supervisada ante pérdida de Redis

1. Mantener los dos flags OFF durante incidentes y comprobar PITR/backup PostgreSQL y salud Redis. Identificar ventana de publicación perdida y consumidores afectados con evidencias.
2. Validar la ventana y retención de `Published` contra stream IDs/PEL antes de cualquier replay, sin borrar/editar datos de negocio.
3. **Solo con procedimiento aprobado**, reencolar los eventos de la ventana identificada. Ejemplo transaccional restringido por ventana y stream, **no ejecutar automáticamente**:

```sql
BEGIN;
UPDATE crm.crm_realtime_outbox
SET status='Pending', attempt_count=0, next_attempt_at=now(),
    lease_token=NULL, lease_until=NULL, stream_id=NULL, last_error='operator_replay_after_redis_loss'
WHERE stream_name='dhole.crm.realtime.v1'
  AND status='Published'
  AND published_at >= :window_start
  AND published_at < :window_end;
-- Revisar recuento esperado y evidencia de aprobación antes de COMMIT.
ROLLBACK;
```

4. Verificar que `eventId` permanece estable, el Inbox impide dobles efectos y los GET REST reconcilian.
5. Para DLQ, triage de causa, aprobación y replay por IDs explícitos; nunca reencolar masivamente sin autorización.

## Gate F2 (sin aprobación)

Pruebas requeridas: 1.000 commits → 1.000 eventos lógicos, duplicados idempotentes, caídas post-commit/pre-XADD/post-XADD/pre-ACK, Redis detenido/restaurado, verificación de AOF/backup, saturación y DLQ; ninguna escritura REST falla por websocket/redis. El workflow candidato `.github/workflows/realtime-f2-durability.yml` crea PostgreSQL 17/Redis 7 efímeros e incluye integración base. Una simulación de Redis indisponible **no equivale** a un reinicio real validado. Las pruebas pendientes NO se cuentan como aprobadas.

**Rollback:** flags OFF, mantener REST y datos de Outbox/Inbox; revertir binarios solo con imagen versionada de batch. La migración es aditiva y no permite `Down` destructivo automático. No eliminar tablas para retroceder la funcionalidad.
