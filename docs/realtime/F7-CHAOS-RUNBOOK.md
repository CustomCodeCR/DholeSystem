# F7 — Runbook de contingencia y consistencia transversal (C01–C14)

**Plan** 2.1.0 · **releaseId** `rt-20261107-01` · **estado** PREPARACIÓN TÉCNICA; **F6 no aprobado**.
**Versión global candidata:** 1.13.0. **Ramas:** `feature/dhole-realtime-universal-rt-20261107-01`.
**Última revisión:** 2026-11-08.

## Principio de ejecución

1. Las pruebas automatizadas con `FakeHost`, TestServer y Redis/Postgres de CI son candidatas, **no verificaciones de despliegue**. Un workflow verde de auditoría no concede aprobación de C01–C14.
2. No ejecutar inyecciones sobre `dhole` ni `dhole-staging` con usuarios o datos reales antes de que F6 y su gate secuencial estén aprobados y exista un entorno de integración **aislado** o la ventana de pruebas autorizada del batch. No reiniciar, matar, congelar, cambiar flags o modificar Redis staging/producción durante F0–F8.
3. Un escenario real exige: versión/release SHA de los 17 repos, contexto de cada servicio/proxy/Redis/PostgreSQL, usuario autorizado A/B y usuario C denegado, datos de prueba, hora UTC (commit/evento/UI), conteo de eventos, solicitudes REST, logs anonimizados, versión final de recurso, observación de ACL y resultado del rollback.
4. F7 no sustituye el Gate F6: 13/13 servicios, matriz de cada mutación/worker, pruebas e2e 20+ operaciones y 5+ reconexiones por servicio, además de 0 fugas. C01–C08 necesitan **10 ejecuciones reales por caso**.
5. Mantener `Features:UniversalRealtimeEnabled=false`, `Realtime:BatchApproved=false`, `Realtime:UniversalServicesBridgeEnabled=false` y `VITE_DHOLE_REALTIME_ENABLED=false` fuera de un conjunto efímero dedicado. Nunca activar un solo componente del batch contra el resto sin compatibilidad explícita.

## Registro de ejecución obligatorio

Por escenario guardar `test-evidence/F7/<run-id>/Cxx.json` y `Cxx.md` sin tokens ni datos sensibles. Usar identificadores opacos y timestamps; resultado `VALIDADA` solo con evidencias verificadas por el responsable. Medir p95/p99 desde commit confirmado hasta GET/actualización UI con **>= 1000 eventos por escenario de rendimiento**; para reconexión, al menos 30 iteraciones y p95 <= 10 s tras recuperar REST. Comparar escrituras y eventIds antes/después, no únicamente mensajes recibidos.

| Caso | Inyección segura en entorno autorizado | Observación y aserción exigida |
|---|---|---|
| C01 | Poner navegador A offline 1–5 min, escribir desde B, luego reconectar | Estado offline legible; sin POST inventados; GET converge y no borra formulario sucio |
| C02 | Bloquear inicialmente negociación/ticket WSS para A | Backoff+jitter independiente; REST polling autorizado; luego recuperación con un WebSocket lógico |
| C03 | Reiniciar solo host Hub efímero | Ticket fresco, revalidación de ACL, Subscribe y GET; sin acceso previo revocado |
| C04 | Detener Redis efímero después de transacción confirmada | REST confirma; Outbox retiene todos los commits; al restaurar Streams replay íntegro |
| C05 | Cancelar Bridge de integración justo antes del XACK | XAUTOCLAIM/Inbox evita duplicación lógica; eventual REST converge |
| C06 | Inyectar mensajes repetidos/invertidos con distintos EventId y versiones locales | Idempotencia por EventId y GET autoritativo; 0 estado antiguo aplicado tras reconciliar |
| C07 | Caducar JWT de A y revocar scopes de B entre evento y entrega | 401/403/404 deniegan; desconectar/limpiar caché y grupos; 0 entrega a C |
| C08 | Dos usuarios editan misma entidad; A guarda y B guarda con versión antigua | REST retorna 409/412 o política optimista equivalente; B conserva cambios locales para resolver |
| C09 | Suspender pestaña A con vista activa y modificar desde B | No polling oculto excesivo; al reabrir revalidar ACL y consultar REST actual |
| C10 | Interrumpir REST efímero conservando WS | Mantener último snapshot confirmado y mostrar error; no marcar POST como exitoso |
| C11 | Suspender publicador Outbox y crear backlog sintético acotado | Métrica/alerta, DLQ y runbook; al restaurar drena sin pérdidas ni tormenta de eventos |
| C12 | Logout de A, cambiar a identidad B en la misma pestaña | Cero listeners/sockets A; purga de caché; ningún evento de A en B |
| C13 | Caída simulada de una de dos réplicas Gateway en test cluster | Transporte/restablecimiento por proxy, grupos reautorizados, Inbox/cursor durable y convergencia |
| C14 | Duplicar eventos de Dynamics/email en test queues con idempotency keys | 0 correos extra, 0 cotizaciones/líneas duplicadas, 0 acciones de negocio por notificación UI |

## Gates y fallos conocidos

- **Candidatos aprobados en CI Vue:** C01, C02, C03, C06, C07, C09, C10, C12, todos con sockets/REST simulados; [Web #42505547084](https://github.com/CustomCodeCR/DholeWeb/actions/runs/42505547084) compilación, regresiones, Chromium y 22/22 pruebas del gestor PASS. No cuentan como inyecciones en staging.
- **C04/C05:** la durabilidad Outbox/Inbox y replay se ejercitaron anteriormente en [CRM F2 #42444994037](https://github.com/CustomCodeCR/DholeCRMService/actions/runs/42444994037) con PostgreSQL/Redis de CI. Aún falta comprobar restauración AOF y backup en runtime real.
- **C08:** CRM HTTP TestServer validó 409 de versión obsoleta en [F5 CI #42489760621](https://github.com/CustomCodeCR/DholeCRMService/actions/runs/42489760621), pero no prueba dos navegadores con permisos reales en staging.
- **C13:** Gateway 2 instancias de TestServer y cursor durable se documentaron en [F3 CI #42485284958](https://github.com/CustomCodeCR/DholeApiGateway/actions/runs/42485284958), no equivale a Traefik TLS/WSS multiinstancia.
- **Bloqueo F0/F2 en staging:** Redis `aof_enabled=0` observado en [auditoría #42490276695](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42490276695). No declarar C04/C05 validados mientras la restauración real y snapshots de backup sigan sin prueba.
- **C11 y C14:** no existen inyecciones F7 equivalentes acreditadas; quedan `NO_EJECUTADO`.
- **Formal F7 0/14**. Gate `python scripts/realtime/verify-f7-chaos-gate.py --require-all` **debe fallar** hasta aprobación reproducible de los 14 escenarios. `--assert-candidate-blocked` es solo un control contra falsos positivos.

## Criterio de parada y rollback

Detener escenario ante exposición ACL, escritura duplicada, pérdida de commit, divergencia de negocio o fuga sostenida de conexión/listeners. En entorno autorizado: desactivar flags realtime, mantener REST operativo, asegurar primero integridad Outbox/Inbox y backups, capturar evidencia de recuperación. No reintentar comandos de efectos externos ni POST inciertos sin idempotencyKey y consulta de resultado. **No desplegar a producción** por pasar el runbook; F9/F10 y la autorización separada continúan obligatorios.

## Evidencia candidata nueva (no ejecución formal)

- [F7 Redis aislado CI #42506868019](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42506868019): C04 persistencia AOF de 10 eventos tras 1 reemplazo; C05 diez recuperaciones con `XAUTOCLAIM` e Inbox sintético; C11 backlog de 1.200 eventos drain/ACK. No prueba el grupo Redis/Gateway/Outbox Postgres reales de staging.
- [Dynamics Postgres CI #42507593928](https://github.com/CustomCodeCR/DholeDynamicsConnectorService/actions/runs/42507593928): C14 parcial, un solo trabajo/Outbox ante dedupeKey repetido con esquema SQL real; **falta** correo y terceros.
- [Conversión AOF segura #42507199248](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42507199248): los datos existentes de RDB deben convertirse al AOF **mientras Redis está en línea**, esperar fin de rewrite y comprobar persistencia antes de reconfigurar Compose. Ver `F6-REDIS-AOF-STAGING-MIGRATION.md`. La simple recreación perdida en CI #42507114616 está prohibida.
- Se consideran **12 candidatos con alguna evidencia parcial**, no 12 casos aprobados; C08/C13 no poseen todavía suite F7 dedicada. **14/14 formales continúan pendientes y F8 no está autorizada**.
