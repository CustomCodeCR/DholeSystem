# F6 — Cobertura candidata de 13 servicios (2026-11-08)

**Release:** `rt-20261107-01` | **Plan:** 2.1.0 | **Versión global propuesta:** 1.13.0.  
**Estado:** IMPLEMENTACIÓN EN RAMAS INTERMEDIAS / GATE FORMAL NO APROBADO. F7 NO INICIADA.

Este documento distingue *productor + esquema + compilación + CI* de la aprobación real del
sistema realtime. No se ha fusionado a `develop`, `master` o `main`, no se ejecutó
despliegue y todos los flags permanecen **OFF**. Un éxito de CI no reemplaza
staging con TLS/WSS, permisos reales ni inventario F0 completo.

| Subfase | Servicio | SemVer candidato | Tipo de cambio | CI comprobado |
|---|---|---|---|---|
| F6.01 | CRM | 1.5.0 | cambios de cuenta y actividad; Outbox PostgreSQL propio | [15 pruebas #42491355430](https://github.com/CustomCodeCR/DholeCRMService/actions/runs/42491355430) |
| F6.02 | Pricing | 1.6.0 | RateHeader; Outbox/worker existente | [3 pruebas #42492328018](https://github.com/CustomCodeCR/DholePricingService/actions/runs/42492328018) |
| F6.03 | Notifications | 1.3.0 | Hub de notificaciones existente y lector acotado | [3 pruebas #42493452879](https://github.com/CustomCodeCR/DholeNotificationsService/actions/runs/42493452879) |
| F6.04 | Auth | 1.3.0 | usuario y cambios UserRole/UserScope | [3 pruebas #42500120665](https://github.com/CustomCodeCR/DholeAuthService/actions/runs/42500120665) |
| F6.05 | Config / SRM | 1.3.0 | grupos e ítems (fachada SRM sobre catálogo) | [3 pruebas #42496953424](https://github.com/CustomCodeCR/DholeConfigService/actions/runs/42496953424) |
| F6.06 | AuditLogs | 1.3.0 | eventos auditados con nuevo Outbox/migración PostgreSQL | [3 pruebas #42497034373](https://github.com/CustomCodeCR/DholeAuditLogsService/actions/runs/42497034373) |
| F6.07 | Storage | 1.3.0 | archivos/versiones/referencias sin contenido | [3 pruebas #42496897714](https://github.com/CustomCodeCR/DholeStorageService/actions/runs/42496897714) |
| F6.08 | DataExtraction | 1.4.0 | ejecuciones y trabajos de correo/IA | [3 pruebas #42499963178](https://github.com/CustomCodeCR/DholeDataExtractionService/actions/runs/42499963178) |
| F6.09 | Reports | 1.5.0 | plantillas con nuevo Outbox/migración PostgreSQL | [3 pruebas #42497281919](https://github.com/CustomCodeCR/DholeReportsService/actions/runs/42497281919) |
| F6.10 | DynamicsConnector | 1.3.0 | alta/replay autorizados de trabajos con migración SQL 019 | [3 pruebas y SQL #42499971169](https://github.com/CustomCodeCR/DholeDynamicsConnectorService/actions/runs/42499971169) |
| F6.11 | AI | 1.4.0 | ejecuciones y trabajos de análisis | [3 pruebas #42499975894](https://github.com/CustomCodeCR/DholeAIService/actions/runs/42499975894) |
| F6.12 | Agent | 1.3.0 | ejecuciones, definiciones y agendas | [3 pruebas #42496919190](https://github.com/CustomCodeCR/DholeAgentService/actions/runs/42496919190) |
| F6.13 | Content | 1.3.0 | contenidos, menús y ajustes (sin datos privados) | [5 pruebas #42499966816](https://github.com/CustomCodeCR/DholeContentService/actions/runs/42499966816) |

**Gateway:** 10 streams adicionales, 18 clases de recurso nuevas y `Realtime:UniversalServicesBridgeEnabled=false`
independiente de CRM/Pricing. Validación de `producer` + `eventType` + `aggregateType` +
`audienceRef` + stream; evento por conexión explícita, con autorización delegada
por GET del servicio propietario **al suscribirse y antes de cada envío**. Eventos
repetidos se desduplican por `EventId` en Inbox PostgreSQL; reconexiones
reconciliarán con REST, nunca aplicarán mutaciones de negocio desde un evento.

- [Gateway 126/126 #42499913276](https://github.com/CustomCodeCR/DholeApiGateway/actions/runs/42499913276), incluye pruebas negativas por los 18 recursos, 10 streams y productores forjados.
- [Guard de 13 candidatos y 17 repos #42500725384](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42500725384) confirma versiones, flags OFF y ausencia de promoción; **no aprueba F6**.
- Nuevos endpoints de autorización de solo lectura: Auth user, DataExtraction execution/emailjob/airequest, AI emailjob, Content menu/setting y Dynamics job. Se prueban las compilaciones y políticas estáticas; JWT de usuario real, ámbitos y revocación deben verificarse en staging.
- El CSV `coverage-matrix.csv` contiene 18 relaciones nuevas productor/audiencia/GET propietario. Las 13 filas `INVENTARIO_PENDIENTE` siguen abiertas: no representan 100% de mutaciones.

## Riesgos y gates pendientes de verificación

1. **F0/F2:** inventario de 578 candidatos HTTP/workers aún sin mapeo completo; Redis `dhole-staging-infra` tiene `aof_enabled=0`, la recuperación AOF y restauración real de PostgreSQL no se han demostrado.
2. **F3/F6:** validar WSS HTTPS/Traefik con **dos instancias reales** de Gateway, autorizaciones DholeAuth y permisos de negocio, dos navegadores simultáneos, denegación 401/403/404, revocación durante sesión, orden/reintentos y reconexiones. El CI actual usa TestServer/Redis/PostgreSQL efímeros, no el entorno final.
3. **Cobertura funcional:** solo se implementaron los productores indicados. No se han auditado TODAS las rutas de mutación de los 13 servicios. Faltan snapshots REST por GUID para DataExtraction execution/airequest, AI emailjob, Content menu/setting y el detalle de job Dynamics que requiere `code`; el endpoint `realtime-access` autoriza pero NO reemplaza la respuesta REST para reconstruir datos. SRM tiene permisos `srm.*` propios y los GET generales de Config exigen `config.*`; su equivalencia debe diseñarse y probarse sin elevar permisos.
4. **Identidad/versiones:** varias invalidaciones usan versión temporal local como pista, NO versión de recurso global entre réplicas. El cliente debe invalidar y consultar el REST propietario siempre. Los esquemas mínimos no contienen tokens, correos, nombres, rutas de archivos, datos Dataverse, PDFs, prompts o resultados IA.
5. **Frontend:** manager Vue universal y dos vistas piloto CRM/Pricing ya tienen pruebas en CI. El acoplamiento de las vistas específicas de los diez propietarios nuevos y pruebas end-to-end de usuario real sigue pendiente.
6. **Batch:** las 17 ramas intermedias deben reconciliarse contra HEAD de `develop` y `master`; ejecutar revisión de conflictos, suite de regresión global y pruebas E2E, actualizar SHAs congelados y aprobar gates secuenciales. Ni F9 ni F10 autorizados; producción no autorizada.

## Regla de continuidad

**F6 no se aprueba únicamente porque existan 13 productores y todos los CI sean verdes.**
`f6FormalApproved=false`; la fase F7 de contingencia permanece **NO INICIADA** hasta
que los controles anteriores tengan evidencia verificable y todos los gates
secuenciales previos resulten aprobados. No desactivar validaciones, inventar
métricas, simular approvals ni cambiar targets para declarar éxito.

La implementación candidata permite trabajar las faltas restantes dentro de
las mismas ramas, sin romper APIs REST existentes ni anticipar despliegues.
