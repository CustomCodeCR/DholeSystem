# Dhole Realtime Universal — Progress

Plan **2.1.0**, release **rt-20261107-01**. No habilitar funcionalidades ni publicar partes del batch.

| Fase | Estado | Gate | Observación |
|---|---|---|---|
| F0 | BLOQUEADA | RECHAZADO | 16 ramas intermedias creadas; endpoints y ambiente no verificados completamente |
| F1 | EN_PROGRESO | NO APROBADO | Contratos preliminares aislados; 42/42 pruebas CI, pero F0 todavía bloqueada y faltan integración/cobertura |
| F2 | PRELIMINAR | NO APROBADO | Piloto PostgreSQL/Redis en rama CRM, suite de integración en CI; F0/F1 siguen bloqueando el gate |
| F3 | PENDIENTE | NO EVALUADO | Gateway/Hub y grupos |
| F4 | PENDIENTE | NO EVALUADO | Frontend + fallback |
| F5 | PENDIENTE | NO EVALUADO | Piloto vertical |
| F6.01–F6.13 | PENDIENTE | NO EVALUADO | 0/13 servicios aprobados |
| F7 | PENDIENTE | NO EVALUADO | 0/14 casos ejecutados |
| F8 | PENDIENTE | NO EVALUADO | Enforcement servicios futuros |
| F9 | PENDIENTE | NO EVALUADO | Prohibido merge a develop |
| F10 | PENDIENTE | NO EVALUADO | Requiere autorización expresa master/producción |

## Evidencia F0 (2026-11-07)

- 16/16 repositorios accesibles con permiso push; 16 ramas intermedias nuevas desde el SHA exacto de develop.
- 16/16 comparaciones develop...master diverged; véase release-manifest.yaml para SHA y conteos.
- Ningún push, merge o PR hacia develop/master/main. Ningún despliegue.
- VERSIONADO: baselines inspeccionados en 16 version.json; DholeSystem sube 1.12.3 -> 1.12.4 solo en su intermedia por cambios documentales, con CHANGELOG; la versión global del batch 1.13.0 está PROPUESTA y no aplicada a servicios.
- Código inspeccionado parcialmente; CRM README está desactualizado frente a código de endpoints.
- tests de compilación, integración, staging, infraestructura y métricas: NO EJECUTADOS.
- Inventario 100% endpoints/jobs, ownership SRM/System, configuración viva de Redis/Traefik, instancias y permisos de recursos: BLOQUEADOS por falta de inspección/verificación completa.

## Gate F0

**RECHAZADO** hasta completar infraestructura, endpoints/jobs, matriz de permisos y baseline de carga medido. No iniciar F1. Próxima acción permitida: completar F0 en estas mismas ramas intermedias.

## Revalidación solicitada antes de F1 (2026-11-07)

- Se consultaron remotamente las referencias **develop/master/intermedia en los 16 repos**; 16/16 ramas intermedias existen, sin recrear ni mover ninguna. Evidencia exacta: `test-evidence/F0-branch-revalidation-20261107.md`.
- Drift ajeno al batch: Pricing `develop` +2 commits; Web `develop` +3, `master` +2. Cambios fast-forward, no incorporados ni sobrescritos.
- `DholeWeb/src/modules/srm/services/srmApi.ts` documenta rutas SRM `/api/config/srm` y comenta que son responsabilidad de Config. **Candidato de propietario DholeConfigService**; falta corroborar endpoints e implementación backend.
- F0 sigue **BLOQUEADA / RECHAZADO**. F1 sigue **PENDIENTE / NO INICIADA** por gate obligatorio (inventario 100%, infra real y baseline de carga no demostrados). No se han creado contratos ni ejecutado sus >=20 pruebas.
- Sin cambios funcionales, flags activos, merges, PRs a targets ni despliegues. Los cambios de este chequeo son exclusivamente documentos en intermedia DholeSystem.

- Addendum posterior: `DholeSystem/develop` también avanzó **+6 commits** hasta `ebbbaa031f37f10611433b77403da5820ae03345`, versión `1.12.6` (CHANGELOG, `release-manifest.json`, `version.json`). Su rama intermedia no fue movida, y su versión documental 1.12.4 debe reconciliarse con cambios ajenos antes de cualquier release.

## Trabajo nuevo F0 + F1 — 2026-11-07

- F0: inspección de árboles `git/trees/develop?recursive=1` en 16 repos y `CustomCodeFramework/master`; evidencias `test-evidence/F0-source-inventory-services-01-08.csv` y `F0-source-inventory-components-09-17.csv`. **646 archivos candidatos** a examinar (endpoints, jobs, pipelines, infraestructura y clientes), sin afirmar aún rutas/jobs al 100%. SRM confirmado en `DholeConfigService/src/Dhole.Config.Api/Endpoints/SrmCatalogEndpoints.cs`.
- F0: Notifications ya implementa `NotificationsHub`; DholeWeb cliente específico `notificationRealtime.ts`; Gateway tiene `UseWebSockets` y middleware de proxy. La solución universal debe reutilizar y no duplicar estas funciones.
- Nueva dependencia F1: `CustomCodeCR/CustomCodeFramework` fue auditado; faltaba `develop`, creada sin borrar master desde `18e98bcc1913a7aadfea2b1d3cd8b3cf179bfa97`. Intermedia con releaseId único creada desde el mismo SHA. Total: **17 repos dentro del manifiesto**, de los cuales **13 son servicios**.
- F1: código de contratos preliminares en `CustomCodeFramework.Messaging.Realtime`, no se han modificado firmas previas. Versión candidata `0.3.0` (antes `0.2.0`).
- F1: [Actions run 42443081145](https://github.com/CustomCodeCR/CustomCodeFramework/actions/runs/42443081145), commit `a81447dd00d004d6a32eb28001a379ee89ddb552`: **build OK; 42 tests passed, 0 failed, 0 skipped**, archivo TRX subido. Hay avisos CS1591 sobre comentarios XML y advertencias del runner Node, pero cero errores de compilación.
- F1: catálogo semilla `docs/realtime/event-catalog.draft.yaml`, 13 eventos propuestos, aún no cotejados con permisos/contratos reales.
- Gate formal F0: **BLOQUEADO** por endpoints/jobs todavía pendientes de completar, infra viva y cargas no medidas. Gate formal F1: **NO APROBADO** porque falta cerrar F0 y probar integración multi-servicio. No ejecutar F2, PRs finales ni despliegues.

## F0 — escaneo automatizado completado, gate NO APROBADO

- [CI F0 run 42443461440](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42443461440) **PASSED**, clonación de solo lectura 17/17 intermedias; manifiesto validado. **928** rutas fuente candidatas, **67** workers/handlers candidatos, **13** frontend REST clientes candidatos. Dos artefactos subidos; detalles en `test-evidence/F0-actions-audit-42443461440.md`.
- [CI F1 run 42443081145](https://github.com/CustomCodeCR/CustomCodeFramework/actions/runs/42443081145) **PASSED** en framework, compilación sin errores y **42/42** pruebas unitarias. Detalles en `test-evidence/F1-contract-tests-42443081145.md`.
- F0 permanece `BLOQUEADA` porque el escáner no demuestra rutas/jobs 100% trazados, permisos, dueños System completos, proxy/realtime efectivo ni baseline de carga en servidores. F1 `EN_PROGRESO` de forma preliminar, sin gate F1 formal aprobado; F2 prohibida.
- Control de versión: DholeSystem `1.13.0` candidato y framework `0.3.0` candidato. Release global **NO PUBLICADO**. No PRs a develop/master, no merges, no staging/prod, flags OFF.

## Última comprobación F0 de guard CI (2026-11-07 local)

- `scripts/realtime/verify-branch-policy.py` agregado y ejecutado: **BRANCH_POLICY_OK** sobre manifiesto de 17 repos, flags OFF y sin PRs prematuros.
- [CI F0 con guard explícito, run 42443654263](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42443654263): **success**, 17/17 intermedias, inventario 928 rutas / 67 handlers / 13 clientes REST candidatos. SHA probado del workflow `9100480d703b1d6a534c7130314fd1b626858a7b`.
- Auditoría de branch protections nativas: `GET /branches/develop/protection` de DholeSystem y `GET /branches/master/protection` de framework dieron **403** al conector. Evidencia en `test-evidence/F0-branch-protections-access.md`; enforcement nativo NO VERIFICADO. El guard del pipeline **no sustituye reglas de protección reales**.
- **F0 BLOQUEADA; F1 EN_PROGRESO preliminar con 42 pruebas aprobadas.** No continuar a F2, no merges, no despliegues.

## F2 — implementación candidata aislada (2026-11-07 Costa Rica)

- Reutiliza rama intermedia existente de `DholeCRMService` (`rt-20261107-01`), sin escribir en targets.
- Añade migración `20261108130000_AddRealtimeDurabilityPilot` y tablas `crm_realtime_outbox/inbox`, separadas de recordatorios existentes.
- Añade `CrmRealtimeOutboxWriter` con transacción de negocio obligatoria, `CrmRealtimeOutboxProcessor` con `SKIP LOCKED`, lease/retry exponencial con jitter y DLQ, `CrmRealtimeInboxStore` que hace efecto + insert en misma transacción, ACK posterior al commit.
- Worker `CrmRealtimeOutboxWorker` registrado y desactivado: requiere simultáneamente `Features:UniversalRealtimeEnabled` y `Realtime:Outbox:Enabled`. No se han activado flags.
- CRM versión candidata `1.4.0` (baseline `1.3.1`) y ecosistema candidato `1.13.0`, CHANGELOG y metadatos de assembly actualizados; sin release ni publicación.
- CI candidato `.github/workflows/realtime-f2-durability.yml`, PostgreSQL 17 + Redis 7, prueba 1.000 commits/1.000 eventos/Inbox idempotente, rollback, reintentos, DLQ y replay pre-ACK. **No declarar tests verdes hasta verificar ejecución exacta y SHA.**
- Runbook: `F2-OUTBOX-INBOX-RUNBOOK.md`. Pendiente probar pérdida/restauración real de Redis con AOF, seguridad, retención, backlog, 100% mutaciones y performance. F2 formal **NO APROBADA** por gates F0/F1.

### F2 — evidencia final de implementación candidata (2026-11-07 local)

- `DholeCRMService` SHA **b28ae8278ea28b05624ec30021ada38ad3d8ca21**, versión candidata **1.4.0** (anterior 1.3.1), sin merge. 
- [CI F2 run 42444994037](https://github.com/CustomCodeCR/DholeCRMService/actions/runs/42444994037): **build 0 errores/0 advertencias; 10/10 pruebas aprobadas, 0 omitidas**, incluido lote de 1.000 commits; DLQ, idempotencia, XAUTOCLAIM, recuperación PostgreSQL→Redis tras pérdida del stream, rechazo PII.
- [CI AOF run 42444816160](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42444816160): configuración staging en rama intermedia y volumen efímero verificados, sobrevive eliminación/recreación de contenedor. **No** equivale a prueba de infraestructura staging/producción real.
- Gate F2 **NO APROBADO** hasta F0/F1 aprobadas, retención/alertas reales, backups, auditoría de permisos y prueba del conjunto REST/Hub real. No F3, no PR, no merge, no deployment, flags OFF.
- Evidencia detallada: `test-evidence/F2-CRM-DURABILITY-CI.md`; runbook `F2-OUTBOX-INBOX-RUNBOOK.md`; `stream-registry.f2.yaml`.

## F3 — implementación candidata del Hub universal (2026-11-07 Costa Rica)

- `DholeApiGateway` rama `feature/dhole-realtime-universal-rt-20261107-01`, versión componente **1.4.0** (anterior 1.3.1), ecosistema candidato **1.13.0**. No `develop/master/main` editados.
- Host `/hubs/realtime`, tickets de conexión Redis GETDEL un uso (60s), JWT solo header/ticket, ACL delegada a CRM/Pricing por GET y revalidación de permisos **antes de cada envío**; clientes no escogen grupos arbitrarios. Hub de Notifications preservado.
- Bridge `dhole.crm.realtime.v1` con grupo Redis durable por InstanceId, `XAUTOCLAIM`, Inbox PostgreSQL `realtime.gateway_inbox`, cuarentena `gateway_deadletter`, ACK después de persistencia, notificaciones mínimas sin PII.
- Activación requiere simultáneamente `Features:UniversalRealtimeEnabled`, `Realtime:Enabled`, `Realtime:BatchApproved` y release ID exacto. Además `Realtime:BridgeEnabled` para consumir Redis. **Todos apagados** por defecto, incluido Compose candidato intermedio.
- Seguridad: Origin WS validado server-side, protección contra expiración JWT, límite de suscripciones y tokens efímeros. `NuGet` detectó dependencias crypto transitivas vulnerables durante CI; se subió a paquetes corregidos sin desactivar alertas de seguridad.
- [CI F3 seguridad base 42446139059](https://github.com/CustomCodeCR/DholeApiGateway/actions/runs/42446139059) compiló y aprobó **80/80** pruebas, con 30 casos de lectores denegados; repositorio versionado únicamente en rama intermedia. 
- CI extendida de WebSocket TestServer, dos usuarios autorizados/uno denegado y revocación de permisos **validada**: [run 42446789096](https://github.com/CustomCodeCR/DholeApiGateway/actions/runs/42446789096), SHA exacto `097890a33ed05f63bf6b3616d7bd7fe17c412b8e`, **99/99 pruebas PASS**, 0 omitidas, 0 errores/advertencias de compilación. Incluye tres casos nuevos de aislamiento de dominio/eventos y metadata.
- ADR `ADRs/0002-gateway-hub-authorization.md`, runbook `F3-HUB-GATEWAY-RUNBOOK.md`, migración SQL de Gateway solo como candidata.
- **F0/F1/F2 siguen sin gate aprobado; F3 formal también NO APROBADA** hasta WSS/TLS real con Traefik, dos instancias reales, JWT/Auth y scopes reales, y validación de ambiente. Ningún merge, despliegue, PR por fase ni flags activados. **F4 bloqueada.**
