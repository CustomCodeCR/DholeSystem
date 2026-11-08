# ADR-0002 — Hub universal en DholeApiGateway con autorización renovada por recurso

**Estado:** CANDIDATO / NO APROBADO · **Plan:** v2.1.0 · **Release:** `rt-20261107-01` · **Fase:** F3

## Decisión candidata

- Alojamiento de `UniversalRealtimeHub` en `DholeApiGateway`, ruta `/hubs/realtime` (no eliminar ni sustituir `DholeNotificationsService/api/notifications/hub`).
- Opt-in obligatorio: `Features:UniversalRealtimeEnabled`, `Realtime:Enabled`, `Realtime:BatchApproved` y `Realtime:ReleaseId=rt-20261107-01`. Todos los flags de configuración de este release están desactivados por defecto.
- Cliente navegador intercambia JWT firmado mediante `POST /hubs/realtime/ticket` autenticado por bearer; responde ticket opaco aleatorio de 43 caracteres, 60s, un uso (`Redis GETDEL`). El JWT jamás va en query string, logs ni eventos. Los nativos pueden usar header Authorization sobre transporte cifrado. `OnMessageReceived` acepta `ticket` solo en la ruta exacta del Hub.
- El Hub acepta `Subscribe(kind,id)` únicamente a tipos explícitos `crm.account` y `pricing.rate` con GUID válido. El `groupName` lo calcula el servidor, no el navegador. Hasta aprobar el ACL real de Pricing, `pricing.rate` sigue como candidato.
- `OwnerRestRealtimeResourceAuthorizer`: hace GET autorizado al dueño (CRM: `/api/crm/accounts/{guid}`, Pricing: `/api/pricing/rates/{guid}`) con el JWT delegado, sobre una base fijada por configuración interna. Solo `200 OK` concede acceso; `401/403/404`, timeouts, 5xx, redirecciones y errores deniegan.
- Antes de **cada emisión** del bridge se reevalúa el permiso; si cambió, se saca la suscripción del registro y del grupo. `OnDisconnectedAsync` limpia la conexión; expiración del token cierra WSS.
- La emisión se dirige a conexiones **con autorización revalidada** mediante `Clients.Client(connectionId)`; nunca `Clients.All` ni `Clients.Group(audienceRef)`. Solo envía `eventId/eventType/aggregateType/aggregateId/aggregateVersion/occurredAtUtc`; ningún `payload` PII. SignalR no efectúa mutaciones REST.
- El bridge lee `dhole.crm.realtime.v1`, con **un consumer group durable y único por instancia Gateway estable**, para que las instancias reciben el mismo evento y atienden solo sus WebSockets locales. `Inbox` PostgreSQL por `(eventId, instanceId)`; ACK Redis **después** de entrega autorizada, registro Inbox y commit. Redelivery puede duplicar notificación, nunca efectos de negocio. `XAUTOCLAIM` recupera pending, registros malformados van a `gateway_deadletter` sin almacenar payload.
- `GET` REST es fuente autoritativa. Los clientes F4 usarán idempotencia `eventId` y reconciliarán por versión, reconnect y poll. Bridge no reemplaza Outbox del productor ni garantiza que el browser haya procesado la notificación.
- Rechazar `Origin` WebSocket no permitido (CORS no protege upgrade WS). Para clientes nativos sin Origin, exigir bearer header válido. No confiar en X-User-Id remitido por el browser.

## Motivación y alternativas

El Gateway ya enruta HTTP/WS y puede centralizar tokens/permisos; Notifications cuenta con Hub específico que se conserva por compatibilidad. No se usa SignalR Redis backplane como cola durable; cada instancia tiene grupo Redis Streams propio para cubrir conexiones locales, sujeto a validación en 2 instancias reales (no solo simuladas). Un servicio Hub dedicado queda como alternativa si las mediciones de F0 revelan riesgo de recursos/aislamiento.

## Precondiciones no satisfechas

1. Cerrar gates F0/F1/F2, cobertura 100% y F6 owner ACL por recurso.
2. Confirmar terminación HTTPS/WSS, Traefik, timeouts e instancias reales. No hay evidencia operativa de `dhole-staging` ni p95/p99.
3. Crear/migrar `realtime.gateway_inbox/gateway_deadletter` en la base Gateway mediante batch F9 y respaldos.
4. Auditar credenciales existentes de JWT: la configuración del Gateway contiene una clave estática de ejemplo en un archivo versionado; verificar origen del secreto real, externalizarlo y rotarlo conforme a seguridad antes de activar F3. No replicar clave aquí.
5. Confirmar revocación de sesiones con Auth, cambios de permisos y autorización de recursos Pricing. Verificar 2 usuarios permitidos, 30 negativos, reinicio de host y topología de 2 instancias en staging real.
6. F4: cliente universal, reconexión, cache y polling. No activar la solución sin batch completo.

## Rollback

Mantener desactivadas todas las flags del Gateway, conservar REST, Hub Notifications y estado Outbox/Inbox. Migraciones aditivas no se eliminan automáticamente; revocación de tickets por TTL Redis. Ningún merge a `develop/master/main` ni despliegue de esta decisión hasta F9/F10 formal.
