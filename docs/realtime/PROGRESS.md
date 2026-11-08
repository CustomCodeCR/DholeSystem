# Dhole Realtime Universal — Progress

Plan **2.1.0**, release **rt-20261107-01**. No habilitar funcionalidades ni publicar partes del batch.

| Fase | Estado | Gate | Observación |
|---|---|---|---|
| F0 | BLOQUEADA | RECHAZADO | 16 ramas intermedias creadas; endpoints y ambiente no verificados completamente |
| F1 | EN_PROGRESO | NO APROBADO | Contratos preliminares aislados; 42/42 pruebas CI, pero F0 todavía bloqueada y faltan integración/cobertura |
| F2 | PENDIENTE | NO EVALUADO | Contratos y durabilidad |
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
