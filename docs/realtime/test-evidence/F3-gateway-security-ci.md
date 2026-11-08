# F3 — Evidencia comprobable de Gateway, SignalR, Redis y PostgreSQL

**Plan:** v2.1.0 · **Release:** `rt-20261107-01` · **Condición:** candidato de rama intermedia, sin F3 formal aprobado.

## Suite F3 funcional, HTTP + WebSocket + JWT

- Repo: `CustomCodeCR/DholeApiGateway`.
- [GitHub Actions 42446649159](https://github.com/CustomCodeCR/DholeApiGateway/actions/runs/42446649159) — **SUCCESS**, SHA `2ced27b22809b76e80c9b3d651bb09aa041ac118`.
- Build .NET 10: **0 warnings, 0 errors**.
- **96 PASS, 0 FAIL, 0 SKIPPED**. xUnit sobre Gateway y paquetes asociados con Redis 7 y PostgreSQL 17 efímeros.
- Trazas y TRX: `rt-20261107-01-f3-gateway-security`, artifact ID `13603733287`.
- Casos incluidos: 30 sujetos sin acceso reciben 403, whitelist de recursos y grupos, falsificación de audiencia, dos identidades válidas, tickets WSS opacos de un solo uso con Redis `GETDEL`, control de Origin y servidor `TestServer` con conexiones WebSocket y JWT válidos, 2 suscriptores autorizados/1 rechazado, XADD→bridge→SignalR, revocación de permisos antes del siguiente evento; esquema SQL Gateway aplicado en PostgreSQL temporal.
- **Nota:** TestServer utiliza `ws://` local, no WSS con Traefik; ACL de servicio propietario en integración fue simulado por un `IRealtimeResourceAuthorizer` de pruebas (aunque la implementación REST concreta tiene pruebas unitarias de fallos/403). NO es evidencia de Auth/CRM/Pricing integrado en staging.

## Endurecimiento adicional pendiente de evidencia exacta de SHA

- La rama intermedia añadió una comprobación estricta de `aggregateType` y dominio de productor CRM al bridge, admite upstream HTTPS de origen confiable y agrega tres tests de inyección cross-service/PII.
- [Run F3 posterior 42446789096](https://github.com/CustomCodeCR/DholeApiGateway/actions/runs/42446789096), SHA `097890a33ed05f63bf6b3616d7bd7fe17c412b8e`: **se debe consultar su estado/conclusión antes de declarar verde el SHA posterior**.

## Bloqueos explícitos

- F0 F1 F2: gates sin aprobación formal.
- WSS externo `/hubs/realtime` detrás de Traefik en `dhole-staging`: NO EJECUTADO.
- 2 instancias reales / fallos de host / respaldo Redis en staging: NO EJECUTADO.
- ACL de usuarios CRM/Pricing/Auth reales y 30 pruebas negativas reales: NO EJECUTADO.
- Revocación de sesión Auth real, grupos en desconexión y permisos cambiantes: prueba aislada no reemplaza validación de entorno.
- Rotar y externalizar claves JWT si se confirma una clave estática versionada realmente usada; no desplegar config insegura.
- No se aplicó migración SQL en servidores; no hubo merges, PRs a targets ni despliegues.

**Gate:** F3 `NO_APROBADO`; F4 no iniciada.
