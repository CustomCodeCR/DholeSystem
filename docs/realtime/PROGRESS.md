# Dhole Realtime Universal — Progress

Plan **2.1.0**, release **rt-20261107-01**. No habilitar funcionalidades ni publicar partes del batch.

| Fase | Estado | Gate | Observación |
|---|---|---|---|
| F0 | INVENTARIO_17_REPOS_Y_SALUD_STAGING_LOCAL | BLOQUEADO | 27+5 contenedores; 100/100 GET health local, p95 2.606 ms; 578 candidatos sin mapping y WSS/ACL pendientes |
| F1 | CRITERIOS_TÉCNICOS_PASS | APROBACIÓN SECUENCIAL BLOQUEADA | 44/44 .NET8, contrato con productor CRM F2, falta aprobación F0 |
| F2 | DURABILIDAD_Y_REST_CRM_TESTSERVER_PASS | BLOQUEADO | 14/14 en CI; Redis real de staging observado con AOF OFF; requiere migración segura y prueba restauración |
| F3 | DOS_INSTANCIAS_CI_PASS | BLOQUEADO | 100/100, reinicio cursor durable; falta WSS TLS por Traefik y Auth/ACL staging |
| F4 | IMPLEMENTACION_AISLADA_COMPLETA | BLOQUEADA POR F0–F3 Y STAGING | 12/12 gestor, 91/91 regresión, Chromium 200 ciclos Vue sin fuga; 2 vistas piloto reconciliadas por REST simulado |
| F5 | PREPARACION_TECNICA_CRM_EN_RAMA | BLOQUEADO | PATCH cuenta→Outbox v1→Redis worker candidato; TestServer Auth/ACL y 20 versiones PASS; falta E2E real de 2 navegadores + gates F0-F4 |
| F6.01–F6.03 | IMPLEMENTACION_CANDIDATA_CI_PASS | GATES NO APROBADOS | CRM 15/15, Pricing 3/3, Notifications 3/3, Gateway 106+ seguridad, Web F4+seguridad; sin cobertura 100% ni deploy |
| F6.04–F6.13 | 10 IMPLEMENTACIONES CANDIDATAS CI PASS | NO APROBADO | 13/13 productores/mecanismos preparados; 19 nuevas audiencias; Gateway 128/128. F0 inventario + AOF staging + REST snapshots/vistas + WSS/ACL reales pendientes |
| F7 | PREPARACION_TECNICA_CANDIDATA | NO APROBADO | 8 escenarios con pruebas simuladas de navegador; 0/14 caos real de staging verificado; F6 formal bloquea su ejecución |
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
- **F0/F1/F2 siguen sin gate aprobado; F3 formal también NO APROBADA** hasta WSS/TLS real con Traefik, dos instancias reales, JWT/Auth y scopes reales, y validación de ambiente. Ningún merge, despliegue, PR por fase ni flags activados. **El gate formal de F4 estaba bloqueado; su implementación candidata está aislada.**

## F4 — Vue singleton y contingencia offline (2026-11-07, Costa Rica)

- `DholeWeb` rama `feature/dhole-realtime-universal-rt-20261107-01`, versión candidata **1.13.0** (baseline 1.12.4) y ecosistema 1.13.0. Changelog, package-lock, package.json y versión global alineados. **No release**.
- Se conserva NotificationsHub actual. Manager universal singleton `/hubs/realtime` con conexión WSS mediante ticket opaco, estados `connecting/connected/reconnecting/degraded/offline/unauthorized`, token JWT en header de POST (nunca en query).
- Reintentos con jitter y control de falla **inicial**; en reconexión vuelve a suscribir y a hacer GET REST autoritativo de recursos activos; polling escalonado mientras WSS no funciona. Tab oculta/offline suspende reconexiones y GET, reanuda al volver.
- 2 vistas piloto conectadas a REST: CRM account y Pricing rate detail. Versionado/duplicados protegidos, conflictos de formulario detectados sin reemplazar edición; revocación 401/403/404 borra información anteriormente mostrada.
- [CI F4 final run 42447931191](https://github.com/CustomCodeCR/DholeWeb/actions/runs/42447931191) sobre SHA exacto `ed6271db6b32fb33accc1dec2c106e66672ef923`: **SUCCESS**, 11/11 tests F4, 91/91 regresiones CRM/Pricing, `pnpm --frozen-lockfile`, `version:check`, type-check y build producción **PASS**. Incluye las correcciones de seguridad de permisos revocados. Artefacto CI `13604711151`, evidencia `test-evidence/F4-vue-offline-ci.md`.
- Ver documentación `docs/realtime/F4-VUE-CLIENT-OFFLINE.md`. Se verificaron ya 200 montajes Vue reales en Chromium con 0 fugas sostenidas de listeners/sockets; siguen pendientes 2 usuarios de staging por WSS, autorización real y cierres F0–F3.
- **No integrar ni desplegar**. Flags `VITE_DHOLE_REALTIME_ENABLED` y `VITE_DHOLE_REALTIME_BATCH_APPROVED` permanecen ausentes/apagados; las rutas originales REST siguen funcionando.
- `develop/master` de Web avanzaron desde crear la rama (última observación: develop/master v1.12.11; ambos SHAs auditados en manifiesto). No reescribir nada: conciliar en F9 desde SHAs nuevos y realizar CI de regresión antes de cualquier PR único.
- **Gate F4 = NO APROBADO**; F5 no iniciado.

### F4 — cierre de implementación aislada (sin aprobación formal de fase)

- **Evidencia final CI:** [DholeWeb #42448772988](https://github.com/CustomCodeCR/DholeWeb/actions/runs/42448772988), SHA probado exacto `0ac843361b51446967b2f8706a62cf137dce3785`. Workflow **SUCCESS**: 12/12 pruebas del gestor, 91/91 regresiones CRM/Pricing, `version:check`, `type-check`, build con flags apagados.
- **Chromium real + Vue:** 200 montajes/desmontajes, 0 observadores sobrantes, 0 aumento listeners window/document, 0 aumento sockets, sin crecimiento sostenido de heap en segundo lote (−755188 bytes). Detalles completos en `test-evidence/F4-vue-offline-ci.md`.
- **Navegador multiusuario simulado:** usuario A en dos pestañas, usuario B en una, usuario C denegado 403; ambas vistas piloto (`crm.account`, `pricing.rate`) reconciliaron los snapshots REST mock por GET sin escribir, y CRM preservó los formularios sucios y detectó conflicto. **Esto no equivale a Auth/CRM/Pricing real en staging**.
- Caso adicional 12: si llega una nueva invalidación durante GET lento, el cliente programa la segunda lectura tras completar la primera. Se evita perder actualizaciones.
- **IMPLEMENTACIÓN F4 FINALIZADA EN RAMA, GATE FORMAL NO APROBADO**: F0–F3 siguen pendientes; WSS por Traefik, control multiusuario con permisos efectivos reales y escenarios de reconexión en staging no se han ejecutado. No F5, no merge, no despliegue ni activación.

## Intento de cierre formal F0–F4 (2026-11-08)

- [Auditoría de fuentes actualizada, run #42485543924](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42485543924): 17/17 ramas inspeccionadas en lectura; 929 candidatos HTTP, 510 candidatos mutables, 68 archivos workers/handlers y 15 archivos frontend API. Generado `F0-unresolved-gate-items.csv` con **578 candidatos pendientes de revisión** de ruta absoluta, dueño, scope, audiencia, evento, vista y prueba. No afirmar cobertura completa hasta confirmar casos no identificados por heurísticas. La auditoría de entorno real sigue faltando.
- [F1 .NET8 #42485214061](https://github.com/CustomCodeCR/CustomCodeFramework/actions/runs/42485214061), SHA `86645d36403869ccd791debb384bc298a6b2328a`: **44/44** tests, build verde, 0 errores, compatible con formato de eventos F2. Muestra advertencias XML preexistentes. Criterios técnicos F1 satisfechos; gate secuencial dependiente de F0.
- [F2 .NET10 #42485087251](https://github.com/CustomCodeCR/DholeCRMService/actions/runs/42485087251), SHA `ec4bf2c01b4d4a84eff4a1358187b6ac37c4ec78`: **11/11** tests, 0 errores/advertencias. Prueba adicional HTTP TestServer con POST 201 + Outbox PostgreSQL + publisher Redis fallido y GET 200 posterior. **No demuestra aún los endpoints REST CRM reales integrados**.
- [F3 .NET10 #42485284958](https://github.com/CustomCodeCR/DholeApiGateway/actions/runs/42485284958), SHA `9ec7c1a60b21450c04aebca181106cf6ea11c4ce`: **100/100** tests, dos hosts Gateway reales de TestServer compartiendo Redis/PostgreSQL en CI, entrega autorizada por instancia y cursor persistente después de reiniciar. **No demuestra WSS TLS real a través de Traefik ni ACL de usuario de staging**.
- [F4 Vue/Chromium #42448772988](https://github.com/CustomCodeCR/DholeWeb/actions/runs/42448772988), SHA `0ac843361b51446967b2f8706a62cf137dce3785`: **12/12** manager, **91/91** regresiones, **200 ciclos Vue** sin crecimiento de listeners/sockets, 2 vistas piloto por REST simulado y build PASS. No equivalente a integración de datos reales Auth/CRM/Pricing en staging.
- [Gate de evidencia #42485710957](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42485710957): **SUCCESS de auditoría**, NO de aprobación funcional. `scripts/realtime/verify-f0-f4-gates.py` bloquea explícitamente los cinco gates mientras falten pruebas. Reporta pendientes `F0=6, F1=1 (depende F0), F2=4, F3=5, F4=3`. `--require-all` debe fallar hasta que existan evidencias y aprobaciones verificadas. Estado fuente `docs/realtime/gate-evidence.f0-f4.yaml`.
- Ejecutable de baseline seguro `scripts/realtime/collect-staging-baseline.py` añadido. **No se ejecutó contra servidor real**: esta conexión sólo dispone de GitHub, no de sesión SSH ni métricas operativas de `dhole-staging`. Su uso exige ambiente explícito `DHOLE_GATE_ENV=staging` y URL HTTPS autorizada.
- **Resultado:** F1/F2/F3/F4 técnicamente más validadas en CI; cinco gates secuenciales **BLOQUEADOS**, F5 prohibido por el plan. Versiones del batch siguen candidatas y flags OFF. No se modificaron `develop`, `master` ni `main` de este release; no merge ni deploy.

## Trabajo adicional F0 y preparación técnica F5 — 2026-11-08

- [F0 staging read-only #42489552444](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42489552444): workflow **SUCCESS** en runner existente `[self-hosted,linux,x64,dhole]`, sin desplegar, reiniciar contenedores ni escribir datos. La topología consultada mediante etiquetas Docker registró **27 servicios** en el proyecto `dhole-staging` y **5** en `dhole-staging-infra`. Tras probar inequívocamente que el puerto `127.0.0.1:18080` pertenecía al `api-gateway` de staging, se midieron **100/100 GET /health HTTP 200**, p95 **2.606 ms**, p99 **3.397 ms**. Estas latencias son SOLO del health local, no de un cambio realtime; HTTPS/WSS por Traefik, JWT/ACL y métricas REST comerciales continúan NO VERIFICADOS.
- Un primer intento de sondeo público #42489295739 se detuvo **sin emitir solicitudes** por no poder probar la identidad de un host HTTPS de staging; se corrigió usando exclusivamente el puerto local mapeado por Compose con etiqueta de proyecto. No se consultó producción.
- `DholeCRMService`: adaptador `CrmAccountRealtimeCommit` conectado al **PATCH real** de `/api/crm/accounts/{id}`: EF SaveChanges (incluido historial) y escritura Outbox en una transacción PostgreSQL. Evento `crm.account.updated.v1` con `aggregateVersion` y `audienceRef` mínimo; no se envían datos de cliente. Worker requiere 4 controles incluyendo release ID y BatchApproved, con flags apagados por defecto. El REST original sigue disponible si la release no está activa.
- [CI CRM #42489760621](https://github.com/CustomCodeCR/DholeCRMService/actions/runs/42489760621), SHA `12ea9f72cb7aee930c7a6e5b4b82538eb618a492`: **SUCCESS**, compilación real de `Dhole.Crm.Api` y tests `0 errores/0 advertencias`; **14/14 tests PASS, 0 skipped**, incluyendo 20 actualizaciones reales de cuenta (20 eventos únicos Outbox), HTTP PATCH real autenticado en TestServer, GET de segundo usuario autorizado, 403 de usuario sin acceso, 409 de versión obsoleta y protección contra evento duplicado. PostgreSQL 17 y Redis 7 proporcionados por CI; corrección de versiones de dependencias criptográficas vulnerables en el proyecto de tests, sin desactivar NuGet audit.
- El código piloto CRM es una **preparación técnica**, no aprobación F5 ni integración de las fases: falta verificar publicación Stream→Gateway bridge→Web Vue en el **mismo test end-to-end** con 20/20 actualizaciones visibles en segundo navegador, 5/5 desconexiones, permisos efectivos de staging, latencias y rollback por flags. Tampoco hay autorización para anticipar PRs/merges por fase. 
- Estado formal: **F0–F4 BLOQUEADAS**, F5 **BLOQUEADA por prerequisitos**, F6–F10 sin iniciar. La evidencia F0 de salud local reduce incertidumbre pero NO satisface los gates restantes de proxy, producción nativa, endpoint matrix ni arquitectura de staging. Versiones SemVer `1.13.0` global y CRM `1.4.0` continúan **candidatas**. Ningún deploy, PR hacia develop/master ni activación de flags.

## Hallazgo bloqueante de persistencia F0/F2 — 2026-11-08

- [Auditoría live #42490276695](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42490276695), ejecutada de solo lectura en runner del servidor existente: topología 27+5; GET de health por Gateway staging **100/100 HTTP 200**, p95 **3.021 ms**, p99 **3.802 ms** en esta repetición. NO valida TLS ni realtime.
- Inspección al contenedor **redis** del proyecto exacto `dhole-staging-infra`: `INFO persistence` reportó **aof_enabled=0**. El comando activo del contenedor **no** tiene `--appendonly yes` aunque `deploy/docker-compose.staging-infra.yml` de la rama candidata sí lo configura. Se observó volumen persistente `/data`. Redis en staging **NO CUMPLE** durabilidad AOF de F2; el workflow falló deliberadamente, no debe ocultarse con skipped ni desactivar checks.
- PostgreSQL de staging tiene volumen persistente en `/var/lib/postgresql/data` (NO se efectuó restore). Una política de volumen sin backup probado no cumple recuperación.
- **Corrección pendiente en F9 (batch)**: inventariar stream/keys, respaldar y verificar RDB/PostgreSQL, activar AOF con migración segura del dataset y esperar sincronización de AOF, desplegar configuración de Compose candidata como parte de lote completo, comprobar `aof_enabled=1` y `aof_last_write_status=ok`, reiniciar solo bajo runbook autorizado y verificar replay/outbox y rollback de flags. No hacer `CONFIG SET` ni reiniciar aquí porque F0–F8 no pueden cambiar staging/target fuera de F9.
- Gate F0 RECHAZADO y F2 RECHAZADO mientras siga AOF inactivo y sin evidencia de recuperación. F1–F4 siguen no aprobadas secuencialmente. F5 es únicamente preparación técnica en rama. Ningún merge, PR de batch, despliegue o activación ejecutado.

## F6 — Avance de cobertura candidata en ramas intermedias (2026-11-08)

- **F6.01 CRM:** `DholeCRMService@feature/dhole-realtime-universal-rt-20261107-01` componente **1.3.1 → 1.5.0** (candidato global 1.13.0, no release). Mantiene PATCH real y añade Productor PostgreSQL Outbox transaccional para POST cuenta, actividad, PATCH logo, POST archive y POST assign. `CrmAccountRealtimeCommit` usa allowlist de tipos `crm.account.*.v1`, payload mínimo, cuatro flags apagados y versión de recurso monotónica; historia y evento se escriben con negocio. [CI #42491355430](https://github.com/CustomCodeCR/DholeCRMService/actions/runs/42491355430), SHA probado `b73d6393cae0781869e78379cd682ff673b749e6`: **15/15 PASSED, 0 skipped**, compilación API/Tests sin warnings/errores y versión SemVer PASS. Cobertura limitada a rutas de cuenta enumeradas; otras mutaciones CRM siguen pendientes.
- **F6.02 Pricing:** `DholePricingService@feature/dhole-realtime-universal-rt-20261107-01` componente **1.5.7 → 1.6.0**, global propuesto 1.13.0, releaseId común. Nuevo productor en `ServiceDbContext` detecta cambios de `RateHeader`, añade evento `pricing.rate.created|updated|deleted.v1` al **Outbox comercial existente en la misma operación EF**, sin exponer cliente/costos; trabajador enruta eventos a stream `dhole.pricing.realtime.v1` separado de eventos/cachés comerciales. Los cuatro flags se mantienen OFF. [CI #42492328018](https://github.com/CustomCodeCR/DholePricingService/actions/runs/42492328018), SHA `99a855fb588e0169604d43512dd239a4b5546434`: **3/3 contract tests PASSED**, build Persistence con warnings-as-errors (0 warnings), API/test graph y worker compilados (se conservan warnings de analizadores MSTest preexistentes en test graph). No se ha probado un E2E Pricing a múltiples sesiones ni todos los endpoints mutables.
- **Gateway:** Bridge universal ahora consume un stream CRM y otro Pricing, independientes y con grupos durables; Pricing require `Realtime:PricingBridgeEnabled` default false. El parser solo permite `pricing.rate` en su stream y `crm.account` en el suyo; cada destino se revalida por GET REST antes de entregar. [CI Gateway #42492026596](https://github.com/CustomCodeCR/DholeApiGateway/actions/runs/42492026596), SHA `95d9c32576862949d812e58d9b8785c5cfc6ad90`: **106/106 PASS** sin warnings. Se está incorporando mensaje de control `resourceRevoked` para limpiar inmediatamente información visible revocada sin difundir datos de negocio; la evidencia final de esta última modificación debe vincularse a su propio SHA probado.
- **Vue:** Vista detalle de tarifa invalida y recarga GET REST incluso cuando la revisión comercial no cambia (la revisión de Pricing no es un contador universal de mutaciones). [CI Web #42492212712](https://github.com/CustomCodeCR/DholeWeb/actions/runs/42492212712) con F4 manager, regresiones CRM/Pricing y Chromium PASS. Se añadió control de purga `resourceRevoked` sujeto a ejecución CI final.
- **Infraestructura candidata:** `DholeSystem/deploy/docker-compose.services.yml` incluye cuatro flags separados OFF por defecto para CRM, Pricing y Gateway. No habilita realtime ni modifica staging/producción.
- **Gates:** F0–F5 mantienen evidencia que impide aprobación (entre otros AOF apagado en Redis staging). F6.01/F6.02 están implementaciones candidatas limitadas, NO aprobación de servicio al 100%, F6.03–F6.13 por trabajar. No hubo push/merge a `develop`, `master`, `main`, ni PRs finales ni deploy.

### F6.03 Notifications (reuse, 2026-11-08)

- `DholeNotificationsService` usa **el NotificationsHub existente** (`/api/notifications/hub`), sin crear otra conexión para el mismo usuario ni duplicar las notificaciones en el Hub universal. La nueva `NotificationAudiencePolicy` solo permite grupos `user:{Guid}` validados a partir de un JWT autenticado y destinatario explícito; elimina incorporación desde cadenas arbitrarias. `NotificationRealtimeRelayService` procesa ahora la señal Redis mediante cola acotada de un lector, evita tareas fire-and-forget y conserva el buzón persistente como fuente de sincronización ante pérdida de Pub/Sub.
- [GitHub Actions Notifications #42493452879](https://github.com/CustomCodeCR/DholeNotificationsService/actions/runs/42493452879), SHA exacto `687c292d55b904db584935d2f68333413431a6d6`: **SUCCESS**, API y pruebas compilan con cero errores, **3/3 pruebas del nuevo aislamiento** PASS sin skipped y `version:check` PASS. El grafo de tests conserva 30 warnings previos que no representan validación libre de advertencias; no desactivar reglas de seguridad para ocultarlos. Versión componente **1.2.1 → 1.3.0**, global candidata **1.13.0**, flags y targets sin cambios.
- La protección nueva `resourceRevoked` del Gateway envía únicamente el tipo de recurso y su GUID al cliente anteriormente suscrito cuando propietario REST deniega la lectura. Vue elimina inmediatamente datos previamente mostrados, incluso con WebSocket conectado; no es un evento de negocio ni difunde datos comerciales. Referencias CI: [Gateway #42492902414](https://github.com/CustomCodeCR/DholeApiGateway/actions/runs/42492902414) y [Vue #42492867135](https://github.com/CustomCodeCR/DholeWeb/actions/runs/42492867135). Son implementaciones candidatas en rama, pendientes de cobertura de staging/Auth real.
- F6.01–F6.03 no equivalen a F6 integral. Los servicios F6.04–F6.13 se mantienen en intermedias sin cambios funcionales de este batch; gates F0–F5 y F6 siguen fail-closed. Sin deploy, merge ni PR hacia develop/master/main.

## F6.04–F6.13 — Evidencia de cobertura candidata, no aprobación formal (2026-11-08)

- Las 13 subfases tienen productores/eventos o mecanismos de notificación candidatos
  y los checks unitarios/compilación por repo pasan en su rama intermedia
  `feature/dhole-realtime-universal-rt-20261107-01`.
- Reutiliza Outbox para Auth, Config/SRM, Storage, DataExtraction, AI, Agent y Content;
  agrega Outbox aditivo con migración PostgreSQL para AuditLogs y Reports, y SQL 019
  checksummed para la cola nativa de Dynamics. No altera contratos REST públicos existentes.
- El Gateway permite **19** clases nuevas de recursos en 10 streams segregados,
  pero solo tras `Realtime:UniversalServicesBridgeEnabled` y aprobación estricta
  del batch. Cada evento se reautoriza mediante GET del propietario y no contiene
  credenciales, contactos, documentos, precios, prompts ni datos de Dataverse.
- SRM se separa de Config: evento `srm.supplier.changed.v1` y
  `srm.supplier.read` sin privilegios genéricos `config.catalog-items.view`.
  [Config CI #42501309773](https://github.com/CustomCodeCR/DholeConfigService/actions/runs/42501309773)
  **4/4**, sin errores.
- [Gateway CI #42501265245](https://github.com/CustomCodeCR/DholeApiGateway/actions/runs/42501265245)
  **128/128** pruebas, cero omitidas; prueba adicional real Redis+TestServer:
  usuarios A/B reciben la invalidación Config y C denegado no se suscribe,
  con revocación en caliente de B. No es WSS HTTPS real por Traefik.
- Manifiesto central `docs/realtime/release-manifest.yaml`, registro de 13 servicios,
  19 relaciones de cobertura y el guard `verify-f6-candidate.py` alineados
  con SemVer individual. Todos los flags OFF y targets intactos.
- **Gate de F6 NO APROBADO**: 578 candidatos F0 sin auditoría completa,
  `aof_enabled=0` en Redis staging, falta cobertura de otras mutaciones,
  snapshots REST por GUID para varias vistas, pruebas de ACL/tokens reales
  y de resiliencia multiinstancia sobre WSS/TLS de staging. Revisión detallada
  en `F6-CANDIDATE-COVERAGE-20261108.md`.
- **F7 NO INICIADA**, sin merges a develop/master/main, sin producción,
  sin ejecutar migraciones en servidores ni reactivar batch.

## F6 cierre de brechas acotadas y F7 pruebas candidatas — 2026-11-08

**Release:** `rt-20261107-01` — todas las modificaciones en ramas intermedias, flags OFF.
**Estado real:** F6 NO COMPLETADA ni formalmente aprobada; F7 empieza solo como preparación técnica y suite aislada, no como gate de caos validado.

- **F6.08 DataExtraction:** se añadieron respuestas REST mínimas para /execution/{id}, /emailjob/{id} y /airequest/{id}, con scope preexistente, 404 cuando no existe, sin mostrar correos, prompts, payloads ni documentos. [CI #42505716880](https://github.com/CustomCodeCR/DholeDataExtractionService/actions/runs/42505716880) **SUCCESS**, SHA `f11affc3a7ca25604266fcda669fea6a885e9f67`, versión candidata 1.4.0.
- **F6.11 AI:** el endpoint /api/ai/realtime-access/emailjob/{id} ahora entrega estado, versión, intentos y fechas, sin contenido/resultado del modelo; conserva scope de lectura. [CI #42505712586](https://github.com/CustomCodeCR/DholeAIService/actions/runs/42505712586) **SUCCESS**, SHA `a06987eb9a8084ccee97a0a88cce5df56b76e2d0`, versión candidata 1.4.0.
- **F6 Web transversal:** `RealtimeManager` soporta los **21 tipos** aceptados por el Gateway (CRM/Pricing + 19 restantes). Los eventos se clasifican por combinación de dominio y agregado, y los `eventId` duplicados no disparan doble fetch. Eventos nuevos con `aggregateVersion` local/antigua sí invalidan y consultan GET autoritativo, sin reescribir formularios sucios. Logout y expiración purgan snapshots observados.
- **F7 navegador simulado:** pruebas automatizadas candidatas C01/C02/C03/C06/C07/C09/C10/C12 con 22 pruebas totales del gestor, **22/22 PASS**; suite CRM/Pricing, type-check, build de producción con flags OFF y Chromium Vue PASS en [Web CI #42505547084](https://github.com/CustomCodeCR/DholeWeb/actions/runs/42505547084), SHA probado `0582ef29cc8c542e26569a811a39c7dd0c1c61e9`. Versión Web candidata 1.13.0. Estas pruebas usan socket/REST simulado y **no** demuestran TLS/WSS, redis real, permisos Auth efectivos ni durabilidad real en staging.
- **F7 evidencia formal:** `gate-evidence.f7.yaml`, `verify-f7-chaos-gate.py` y workflow `realtime-f7-candidate.yml` exigen 14/14 pruebas reales y >=10 repeticiones críticas C01-C08, con integridad/seguridad y evidencia. [CI guard #42505851181](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42505851181) **SUCCESS del guard fail-closed**, NO aprobación de F7. **Formal F7 = 0/14**.
- **Pendientes:** 578 candidatos por inventariar de F0, mutaciones restantes de 13 servicios, conectar las 19 nuevas clases a vistas y consultas REST concretas, snapshots Dynamics/Content por GUID, Outbox/Inbox y backup/restore, Redis staging con AOF desactivado, TLS/WSS/ACL multiusuario en staging, E2E 20 operaciones por subfase y controles de 14 escenarios F7 reales. Las SHAs no están congeladas, ninguna fase F0-F6 dispone de aprobación formal de batch. **No merge, no deploy, sin PR a develop/master y sin modificación de main**.
