# F3 — Hub central, Gateway y seguridad de entrega

**Plan:** `CODEX_DHOLE_REALTIME_PLAN_POR_FASES_MEDIBLES.md` v2.1.0  
**Batch:** `rt-20261107-01`  
**Host candidato:** `CustomCodeCR/DholeApiGateway`, rama `feature/dhole-realtime-universal-rt-20261107-01`  
**Gate:** `NO_APROBADO`; F0/F1/F2 aún con condiciones pendientes.

## Rutas y contratos

- `/hubs/realtime`: SignalR **WebSockets-only** candidato (F4 deberá gestionar reconexión y fallback REST; F3 requiere verificar WSS/negociación en el proxy real).
- `POST /hubs/realtime/ticket`: autenticación JWT Bearer en header, expide ticket opaco de 60 segundos que se consume atómicamente mediante Redis `GETDEL`. No expone JWT en URL.
- Cliente suscribe con `Subscribe("crm.account", "<guid>")` o `Subscribe("pricing.rate", "<guid>")`; desuscribe con `Unsubscribe(...)`. Los identificadores y nombres de grupo no pueden ser prefijados arbitrariamente.
- Notificación `resourceChanged`: `{eventId,eventType,aggregateType,aggregateId,aggregateVersion,occurredAtUtc}`. Sin `payload` de negocio. Cliente F4 realizará GET REST, reconciliación por versión y deduplicación.

## Autorización de recursos

1. Conexión autenticada con JWT vigente, `sub`/userId válido GUID; se cierra en expiración.
2. En `Subscribe`, permitir solo tipos de recurso explícitos y GUID. `IRealtimeResourceAuthorizer` llama al servicio propietario con el JWT original delegado. CRM: `GET /api/crm/accounts/{guid}` (backend aplica `CrmAccess.CanSeeAccount`); Pricing: `GET /api/pricing/rates/{guid}` (pendiente auditar acceso específico de cotización). Se aprueba **solo HTTP 200** y se falla cerrado ante 401/403/404/5xx/redirects/timeout. URL destino fija desde `Gateway.HealthChecks`, no desde solicitud del usuario.
3. El grupo `dhole:rt:<tipo>:<GUID N>` se genera en servidor; el bridge jamás invoca `Clients.All` ni entrega a un grupo arbitrario.
4. **Cada evento** se reautoriza contra dueño antes de enviarlo a la conexión local. Si cambia permiso, se elimina del registro/grupo. La desconexión elimina suscripciones. Los cambios de Auth no notifican todavía un `disconnect` proactivo; sigue pendiente en F3/F6.
5. `Origin` de browser WebSocket debe coincidir con `Cors.AllowedOrigins` o dominios confiables explicitados; CORS normal no valida WebSockets. Sin Origin solo se aceptan clientes nativos con bearer header.
6. Límite de 25 recursos por conexión por defecto y eventos entrantes máximo 2048 bytes.

## Bridge durable y topología

- Redis Streams: `dhole.crm.realtime.v1` (primera fuente piloto F2), campos `event_id,event_type,payload_json`. F6 extiende otras fuentes tras validar ownership.
- Por cada Gateway **InstanceId único, estable**, consumer group `dhole-rt-gw-v1-<InstanceId>`, consumidor `InstanceId`. Esta topología permite 2+ instancias sin mezclar el registro local de sockets; **probar dos instancias reales** en staging antes de aprobar. No confundir con un SignalR Redis backplane.
- `XAUTOCLAIM` recupera entradas pendientes; si se detecta grupo preexistente, el cursor no se reinicia. Cada evento se valida, consulta Inbox `realtime.gateway_inbox(event_id,instance_id)`, revalida ACL para cada conexión local, envía invalidación, persiste Inbox y solo entonces hace `XACK`.
- Tras caída entre `SendAsync` y commit se puede emitir evento duplicado. `eventId` y reconciliación REST de F4 neutralizan sus efectos, pero SignalR no confirma procesamiento del navegador.
- Si es inválido, se persiste metadato de cuarentena en `realtime.gateway_deadletter` **sin payload**, seguido de ACK. Las cuarentenas requieren alerta, revisión y triaje; no se pierden silenciosamente.
- SQL aditivo (NO autoejecutado): `DholeApiGateway/Dhole.ApiGateway/Realtime/Migrations/20261108140000_AddGatewayRealtimeInbox.sql`. Requiere aprobación/migración separada dentro del batch F9, backup y verificación en Gateway PostgreSQL.

## Feature flags: desactivadas

Para habilitar luego de aprobar **TODO** el release, Gateway exige simultáneamente:

```text
Features__UniversalRealtimeEnabled=false
Realtime__Enabled=false
Realtime__BatchApproved=false
Realtime__ReleaseId=rt-20261107-01
Realtime__BridgeEnabled=false
Realtime__RedisConnectionString=<runtime secret; not committed>
Realtime__InboxPostgresConnectionString=<runtime secret; not committed>
Realtime__InstanceId=<unique stable instance identifier>
```

La configuración del batch candidato añade **defaults false** en `DholeSystem/deploy/docker-compose.services.yml`. El bridge solo inicia si además está activo `Realtime__BridgeEnabled`. **Ningún flag ha sido activado en staging o producción.**

## Pruebas

- `tests/Dhole.ApiGateway.Realtime.Tests/RealtimeF3SecurityTests.cs`: 30 casos negativos de lector denegado, grupos no autorizados, dos sujetos aprobados simulados y reautorización.
- `RealtimeF3TicketTests.cs`: Redis real, ticket un uso y 60 segundos, replay rechazado.
- `RealtimeF3WebSocketIntegrationTests.cs`: TestServer HTTP/WebSockets real en CI con JWT de prueba, dos usuarios autorizados y uno denegado, entrega y revocación por evento con bridge Redis/PostgreSQL. **No confundir TestServer `ws://` con prueba TLS `wss://` a través de Traefik en staging**.
- `.github/workflows/realtime-f3-gateway.yml` ejecuta build y tests .NET 10 en runner efímero con Redis7/Postgres17 y valida SQL.
- Si cualquier test falla, gate F3 sigue **RECHAZADO**; no convertir `SKIPPED` en verde.

## Pendientes y riesgos obligatorios

- Gate F0: inventario completo, proxy/servidores reales y baseline p95/p99; F1 paquete integrado, F2 aislamiento de piloto real.
- Test WSS externo por proxy (TLS, HTTP/1.1 Upgrade, negociación, origen y token), resiliencia en 2 instancias y revocación de sesiones con Auth real; pruebas negativas con identidades reales y 0 fugas.
- Auditoría explícita de scopes `Pricing.rate`, `CRM Castro Fallas` y demás recursos; bridges/consumidores por servicio y audiences correctas en F6.
- Clave JWT estática actualmente versionada en el appsettings histórico de Gateway: evaluar externalización, inventario del secreto realmente utilizado y rotación **sin publicar valores**. No activar mientras no esté verificada la cadena de autenticación efectiva.
- F4: singleton cliente, login/logout, WS fallback, sincronización inicial/reconnect, polling controlado.
- Observabilidad exportada y alertas en Redis PEL, DLQ, fallos ACL y lag.
- Ninguna ruta `develop/master/main` editada por esta tarea; no PR por fase, no deploy.

## Rollback F3

Apagar los cuatro flags de release/Gateway; conservar rutas REST antiguas y el Hub Notifications. Websockets activos del futuro release deben desconectarse al retirar su host. El estado Redis y el Inbox PostgreSQL quedan disponibles para auditoría; no destruir tablas automáticas. Para recuperar, volver al último batch aprobado tras verificar invariantes del manifiesto.

## Cierre de pruebas aisladas F3 — sin aprobación de gate

La última rama intermedia del Gateway se compiló y probó con éxito en [GitHub Actions #42446789096](https://github.com/CustomCodeCR/DholeApiGateway/actions/runs/42446789096) al SHA `097890a33ed05f63bf6b3616d7bd7fe17c412b8e`: **99 PASSED / 0 FAILED / 0 SKIPPED**, build sin errores ni advertencias. Artefacto TRX `13603454219`. Incluye WebSockets autenticados en TestServer, dos receptores permitidos/uno denegado, revocación posterior, 30 casos de permiso denegado, tickets un solo uso, `Origin` y rechazo de eventos CRM que intentan suplantar otros dominios.

**No extrapolar** TestServer `ws://` a WSS público por Traefik. Tampoco prueba la revocación real de Auth ni ACL real end-to-end con usuarios comerciales en staging. La migración SQL sigue sin ejecutarse en servidores; los feature flags permanecen OFF. Los gates F0–F3 aún no están aprobados.
