# Changelog

## [1.15.0] - 2026-11-09

- Release CRM/Pricing: búsqueda unificada de cuentas y prospectos, asignación automática del vendedor y conciliación explícita de cotizaciones antiguas.
- Se conservan montos, revisiones y estados; asociación por UUID y validación manual del histórico.

## [1.14.3] - 2026-11-09 (Seller Pricing status reconciliation)

- PATCH coordinado: DholePricingService 1.7.1 y DholeWeb 1.14.3 separan modificaciones abiertas de revisiones todavía sin publicar, y reconcilian el panel comercial con el estado de la API.
- Manifest 1.14.3 / release DH-20261109-SELLER-PRICING-STATUS-052. Se conservan las restricciones de exposición comercial y los gates realtime pendientes F6–F9.
- Staging y compilación pendientes de CI; ninguna autorización adicional de producción implícita.

## [1.14.2] - 2026-11-09 (F9 Gateway WebSocket auth status recovery)

- PATCH: coordinated Gateway 1.5.2 / global 1.14.2 for F9 staging; ClientWebSocket upstream handshake 401/403 now propagated rather than incorrectly converted to 502. Genuine destination failures remain 502.
- Gateway 1.5.1 staging smoke confirmed public HTTPS health but failed on unauthenticated WebSocket 502; 1.5.2 must be proven by the same live negative test. Formal authenticated WSS/ACL and F6–F8 remain pending.
- Scope Gateway and System only, no production/master changes or feature-flag approvals.


## [1.14.1] - 2026-11-09 (F9 Gateway postdeploy smoke recovery)

- PATCH: coordinated Gateway 1.5.1 / System 1.14.1 version registry for staging-only F9 health 403 recovery; existing notifications Hub route preserved.
- Confirmed DholeSystem staging infrastructure curl HTTPS /health returned HTTP 200 on 2026-11-09 while Gateway Python urllib F9 received HTTP 403. Gateway candidate switches smoke transport to curl, keeps TLS and deny checks; runtime re-validation required.
- Formal F6 promotion remains enforced for master and manual audit; for develop/staging it is deferred until postdeploy evidence as explicitly authorized. SemVer and manifest checks remain mandatory.
- Scope limited to DholeApiGateway and DholeSystem; other component versions unchanged. F6/F7/F8 and authenticated WSS/ACL evidence remain pending. No master/production authorization.


## [1.14.0] - 2026-11-09 (NotificationsHub universal realtime pilot; candidate)

- Integración a `develop` aprobada expresamente el 2026-11-09 sin exigir F6–F8 antes de staging; los 16 PR del release se fusionaron a `develop`, incluido DholeSystem #161 (8b0b3dc5). F6–F8 **no están aprobados**: registrar evidencias reales de WSS/ACL, 14 pruebas de resiliencia y servicios futuros tras desplegar staging. `master`/producción permanecen fuera de alcance.

- MINOR: Stage-first NotificationsHub pilot deployment plan and 16-repository release scope; removed Gateway realtime-host override. No deployment, staging audit or production activation yet.
- Ecosystem candidate 1.14.0 / 16 Dhole repositories; CustomCodeFramework excluded. Release `rt-20261107-01`, isolated branch `feature/rt-notificationshub-20261109-01`.
- Staging compile, deployment and post-deploy security audit pending; `develop`, `master` and production not changed by this candidate.


## [1.13.15] - 2026-11-08 (F2/F6/F10 safety hardening, isolated)

- F10: removed destructive production deploy step that deleted all non-target remote branches; deployed workflows now preserve release branches and use read-only GitHub contents permission.
- F2/F6: added independent read-only production Redis AOF inspection and synthetic tests alongside the existing staging preflight. Artifacts report runtime AOF separately from unverified startup persistence and backup restoration; no restart or mutation.
- Recorded the user's Redis AOF runtime observations for both containers as operator-supplied evidence, not a CI attestation. Formal F6/F7/F8 gates and feature flags remain blocked/off; no merge or deployment is authorized by this change.
- Coordinated PATCH SemVer bump for the 17-repository candidate release to ecosystem 1.13.15.



## [1.13.14] - 2026-11-08 (F9 staging-first review sequence)

- Tras auditar el orden de despliegues, el smoke se ubica al final de `DholeApiGateway/.github/workflows/deploy-staging.yml` y se empaqueta en el repo de Gateway; el workflow de infraestructura no lo ejecuta antes de que el Gateway termine de desplegar.

- F9: se documenta la comprobación funcional de SignalR en staging **posterior** al despliegue de develop, no como prerrequisito de la revisión de F3. Se mantiene el guard pre-deploy de persistencia de Redis y PostgreSQL; prueba HTTPS/Hub anónima automatizada luego del deploy, sin JWT QA. El rechazo 404 se registra como pendiente, nunca como éxito.
- Excepción F3 de revisión permanece acotada a análisis de código y no autoriza merge/deploy por sí misma. F7/F8 y F10 mantienen validaciones independientes. Versión global 1.13.14 alineada en 17 componentes, sin activar realtime en servidores.



## [1.13.13] - 2026-11-08 (F3 CI TLS/WSS, candidato aislado)

- Se retiraron todas las referencias a secretos/variables QA del workflow principal F3 de DholeSystem; el ensayo live WSS se ejecuta automáticamente en DholeApiGateway sobre infraestructura efímera y se preserva su gate de seguridad.

- F3: Gateway real y Traefik TLS/WSS en GitHub Actions sin JWT QA, variables manuales, SSH ni dependencias del servidor. Dos identidades sintéticas autorizadas y una denegada superaron autorización owner-REST. CI Gateway #42538238853 PASS (suite previa + WSS real); no valida el WSS efectivo de staging.
- Registrados archivos de test F3, evidencia, release-manifest y registro de 17 versiones PATCH; flags de producción siguen apagados, sin merge a develop/master.
- El gate F3 formal sigue NO APROBADO porque el montaje es efímero GitHub-hosted y no equivale a validación de staging ni pruebas de revocación con identidades reales.



## [1.13.12] - 2026-11-08 (candidato F6/F9, no fusionado)

- Añadido auditor de solo lectura para Redis/PostgreSQL reales de staging: valida proyecto y volúmenes Docker exactos, INFO persistence, AOF sano y estado de rewrite antes de cualquier intervención o nuevo deploy; no realiza CONFIG SET, SAVE, BGSAVE ni cambios de infraestructura.
- Workflow self-hosted automático exclusivamente en rama candidata; sube evidencia saneada (solo booleanos) y falla con AOF OFF sin tocar producción. Siete tests negativos/positivos verifican detección de estados inseguros.
- F9 y F10 siguen BLOQUEADOS hasta pruebas formales F0–F8; global 1.13.12 candidato pendiente de sincronización de todos los componentes.



## [1.13.11] - 2026-11-08 (candidato F9/F10, sin integración)

- Corrige tres fallos de CI reales: Config MSTest analyzer (1.3.2), Reports PostgreSQL 17 en workflow principal (1.5.2), Gateway catálogo service-versions y versiones reales de 13 microservicios (1.4.3). Reejecutadas las pruebas principales de esos componentes.
- Reconciliación universal de versionado del batch `rt-20261107-01` a `ecosystemVersion=1.13.11` en las 17 ramas, con bump PATCH por servicio, DLL/NuGet/Web lockfile y CHANGELOG respectivos. `release-manifest.json`, manifiesto de fases, registro F6 y guard F9 actualizados.
- Los 17 pull requests a develop siguen como DRAFT, los flags realtime apagados, sin despliegue a staging/producción. Sigue pendiente F0 inventario 639 firmas, Redis staging con AOF OFF y restauración, F7 14 escenarios de staging y F8 formal.



## [1.13.10] - 2026-11-08 (candidato F9, sin fusiones)

- Coordinación SemVer universal del release `rt-20261107-01` en las 17 ramas intermedias: versión global `1.13.10` en todos los `version.json`, con PATCH independiente por componente, metadatos AssemblyVersion/PackageVersion y CHANGELOG respectivos; no se han publicado ni fusionado.
- Actualiza el manifiesto de 17 componentes, el registro de los 13 productores realtime y el guard F6 para las versiones candidatas finales; la auditoría F0 deberá confirmar los 17 SHA y versión global uniforme.
- Preparación F9 y guard F10 conservan estado DRAFT/BLOQUEADO mientras falten fuente validada, AOF y restauración real de staging, los 14 escenarios F7, la protección de ramas y el batch CI. Ningún cambio en develop/master.



## [1.13.9] - 2026-11-08 (F9 candidato, solo rama intermedia)

- Merge real de los 6 commits existentes de `develop` (padre ebbbaa031f37) dentro de la rama realtime, preservando el release histórico `DH-20261108-PRICING-COMMERCIAL-TERMS-037`, sus notas 1.12.6 y copia intacta de su manifiesto.
- Reconciliación coordinada con Pricing 1.6.1, que integró los 21 commits de develop incluyendo hotfixes de tarifas FCL 1.5.8–1.5.18; nuevos metadatos globales de batch 1.13.9, sin versionar manualmente develop/master.
- Corrige `release-manifest.json` legado, que conservaba global 1.13.1: ahora versión 1.13.9 y el listado real de 17 componentes a liberar, cada uno con su versión independiente; no supone que todos tienen la misma versión.
- Ningún gate F0–F10 declarado aprobado ni flags habilitados. F9 PR continúa DRAFT.



## [1.13.8] - 2026-11-08 (candidato F9/F10, sin fusiones)

- F9: creadas 17 PR a `develop` en borrador, una por repositorio; inventario de números y URLs e inspección de política con pruebas negativas. Pricing y System requieren reconciliar commits de develop.
- F10: guard de producción fail-closed ejecutado antes de cualquier mutación en el workflow `deploy-production.yml`; bloquea si cualquiera de los gates F0–F9, la coherencia de versión global, los SHA finales, la prueba de restauración o la verificación de idéntico release de 17 repos no están aprobados. Autorización del usuario registrada, sin despliegue ni cambios a master.
- Se añaden tests positivos/negativos de preparación F9 y gate F10. Las 17 PR siguen draft, jamás auto-merge.



## [1.13.7] - 2026-11-08 (candidato F9, NO fusionado)

- F9 staging safety: despliegue deja de forzar `docker compose --force-recreate postgres redis`; guard previo fail-closed verifica identidad exacta de Redis staging, montaje persistente y AOF activo y estable ANTES de ejecutar `compose pull/up`. El estado observado AOF OFF bloquea el redeploy hasta realizar migración segura y restore.
- Se añaden siete pruebas de regresión de fallo seguro y un control CI del orden guard->pull->up; sin secretos, cambios en producción ni fusiones.



## [1.13.6] - 2026-11-08 (candidato aislado)

- F0/F3: guard CI sobre los 17 repos existentes verifica Hub SignalR Notifications, cliente WSS con ticket, proxy WebSocket del Gateway, nuevo Hub universal detrás de flags, Redis AOF y volúmenes persistentes declarados en Docker Compose.
- No se requieren usuarios QA nuevos ni secretos para validar código/Compose; continúa pendiente demostrar runtime AOF y WSS del Hub universal sin confundirlo con Notifications.



## [1.13.5] - 2026-11-08 (candidato aislado)

- F3: test de staging con dos JWT de usuarios QA, GET propietario y suscripción SignalR por WSS/TLS con ticket; ruta HTTPS únicamente staging, sin escrituras de negocio ni secretos en evidencia; ejecución real bajo opt-in de GitHub Actions, tests de seguridad offline.



## [1.13.4] - 2026-11-08 (candidato aislado)

- F0/F9: verificador transversal de versiones exactas para 17 repositorios, incluidas coherencia SemVer, CHANGELOG, manifiesto y SHAs congelados. Modo candidato documenta discrepancias sin autorizar promoción; modo formal rechaza cualquier drift o falta de gate. Pruebas positivas y negativas en CI aislado.



## [1.13.3] - 2026-11-08 (candidato aislado, sin publicación)

- F6: reparado CI de revisión del release que rechazaba incrementos legítimos al exigir la versión estática 1.13.1. Ahora valida Semantic Versioning creciente, versión de DholeSystem, candidata global, manifiesto y CHANGELOG de forma coherente, manteniendo flags OFF y gate bloqueado.



## [1.13.2] - 2026-11-08 (candidato aislado, sin publicación)

- F0/F6: conciliación automatizada de firmas HTTP, workers y protocolos adicionales de 17 repos con decisiones revisadas ancladas al SHA inspeccionado. Evita aceptación de evidencias obsoletas, rutas sin ACL/GET/consumidor y excepciones sin aprobación; casos positivos/negativos de CI.
- El inventario continúa sin aprobar: una firma fuente no equivale necesariamente a una operación de negocio distinta. Ningún gate F0–F10, despliegue o merge se declara completado por esta herramienta.



## [1.13.1] - 2026-11-08

- Reconcile the current realtime candidate manifest and record Vue revocation/lifecycle regression evidence; retain all formal release gates as incomplete.

- F7 (candidato aislado): CRM C08 prueba 10 carreras reales contra Postgres con 2 clientes del mismo actor, 409 y Outbox sin doble publicación, CI #42511869179 PASS; Gateway C13 se sustenta en CI #42501705251 de dos hosts TestServer con cursor durable. Los 14 escenarios tienen ahora evidencia candidata parcial, pero 0/14 validados formalmente staging; F8/F9 bloqueadas.

- F0/F6 (candidato sin aprobar): CI de inventario ampliado #42511529610 inspecciona 17 ramas intermedias; 512 rutas mutables y 70 worker files=582 sin revisión formal, más 57 firmas adicionales (6 dinámicas, 9 GraphQL/gRPC, 42 hosted-worker) con posibles solapamientos, todas NO_VERIFICADAS. No equivale a cobertura real del 100%.

- F8 (candidato aislado SIN PUBLICAR): scaffold generador de nuevo servicio Dhole, manifiesto versionado, puerta de CI contra endpoints/workers sin Outbox/evento/ACL/REST/tests y plantilla PR; 20/20 casos positivos/negativos CI #42511408397 PASS, muestra .NET8/PostgreSQL/Redis con caída/replay idempotente PASS. Gate formal F8/F9 NO APROBADO por F0–F7, Hub/ACL reales y branch protection 403, sin merge/despliegue.

- F6/F7 (sin publicación): reauditoría de staging #42508243878 demuestra Gateway health 100/100 pero negociación realtime HTTP 404, flags OFF y Redis `aof_enabled=0`; los gates permanecen bloqueados y F8 no autorizada. Ningún deploy ni merge del batch.

- F6/F7 (candidatos): inventario por archivo/línea de 510 rutas mutables y 70 candidatos de workers (580 sin aprobar) en CI F0 #42507019304; ensayo Redis RDB→AOF seguro #42507199248 tras detectar pérdida en #42507114616; caos Redis C04/C05/C11 aislado #42506868019; control F7 12 pruebas candidatas parciales, 0/14 staging.

- F6.10/F6.13 (candidatos): snapshots REST de estado mínimos en Dynamics y Content, sin datos sensibles, CI #42506195403 y #42506192534 verdes; F7 añade runbook reproducible C01–C14, sin inyectar fallos en staging ni aprobar F6/F7.

- F6/F7 (candidato no publicado): se corrigió recuperación REST mínima en AI/DataExtraction (CI #42505712586 y #42505716880), cliente Web para 21 recursos y ocho simulaciones F7 (Web CI #42505547084). Se creó guard F7 #42505851181 que falla ante aprobación sin 14/14 evidencias reales; los gates formales, Redis AOF y WSS staging permanecen bloqueados.


## [1.13.0] — 2026-11-07 (candidato de batch, SIN PUBLICAR)

- F6.04–F6.13: productores/mecanismos realtime candidatos para los 13 servicios, 10 streams segregados y 19 nuevos recursos con autorización por propietario. Config/SRM separa audiencia de proveedores. Gateway 128/128 en #42501265245, Config 4/4 en #42501309773, guard central de 17 repos en #42500725384. **Gates formales BLOQUEADOS** por inventario, AOF staging, WSS/ACL y vistas REST pendientes. F7 no iniciada; sin merges ni despliegues.


- F6.01 CRM componente candidato 1.5.0: invalidaciones Outbox por ciclo de vida de cuentas, 15/15 tests en #42491355430; no se aprueba cobertura global.
- F6.02 Pricing componente candidato 1.6.0: eventos PII-free en Outbox de `RateHeader` y stream aislado, 3/3 tests #42492328018; Gateway consume ambos streams separados, 106/106 tests #42492026596; Vue reconciliación REST aprobada #42492212712.
- F6.03 Notifications componente candidato 1.3.0: preserva Hub de usuario e inbox REST, endurece audiencia por GUID JWT autenticado y cola acotada del relay, 3/3 tests #42493452879.
- Seguridad F6: `resourceRevoked` elimina inmediatamente snapshots en Vue cuando el Gateway retira permiso de lectura, sin revelar negocio; CI Gateway #42492902414 y Web #42492867135 PASSED.
- Manifiesto central y registro de servicios actualizados; guard F6 en rama intermedia verifica SemVer de 3 servicios, 17 repositorios, flags OFF y gates cerrados, CI #42493866847 PASS. Versiones todavía candidatas; sin deploy ni merges a develop/master.
- Auditoría F0 de persistencia del staging real encontró Redis AOF desactivado pese a volumen persistente; se conserva gate F0/F2 bloqueado y se documenta la migración segura de AOF para la fase F9. No se modificó el runtime.
- Auditoría F0 sobre runner real de staging, de solo lectura: 27 contenedores de servicios + 5 de infraestructura y 100/100 GET /health HTTP local, p95 2.606 ms, p99 3.397 ms; TLS/WSS, Auth y backup restaurado siguen pendientes.
- Preparación técnica F5 CRM: el PATCH real de cuenta ahora genera Outbox en la misma transacción que cambios e historial, bajo flags OFF por defecto. CI de API/TestServer/PostgreSQL/Redis 14/14 PASS en SHA 12ea9f72cb7aee930c7a6e5b4b82538eb618a492; no equivale a prueba completa multiusuario SignalR/Vue.
- Se corrigieron dependencias criptográficas vulnerables del proyecto de pruebas, manteniendo auditoría NuGet y compilación con warnings-as-errors. Los gates formales F0–F5 siguen BLOQUEADOS; documentación y manifiesto registran SHAs sin congelar release ni promoverla.
- Release coordinado `rt-20261107-01`: F0 investigación de árboles de fuente y manifiesto extendido con `CustomCodeFramework` como dependencia adicional.
- F1 contratos compartidos .NET8: 44/44 pruebas PASS en Actions run 42485214061 (en rama intermedia); compatible con productor CRM F2 y rechazo de PII anidada. F2 CRM 11/11 y F3 Gateway 100/100 en CI aislada, F4 Vue/Chromium completada en CI.
- Auditoría F0 ahora registra 17 repos, 929 rutas candidatas, 510 mutables, 68 handlers/jobs y 578 candidatos por revisar. Manifiesto de gates, script bloqueante, runbook de staging y reporte de incumplimientos agregados; no se aprueban gates sin infraestructura real.
- Documentación de fuentes candidatas, SRM/Config confirmado, catálogo semilla de eventos y riesgo de divergencias entre ramas.
- **No se integró a develop/master ni se desplegó:** F0 y F1 todavía no cuentan con gate formal aprobado; el resto de servicios mantiene sus versiones actuales hasta release completo.



## [1.12.6] - 2026-11-08

- Release `DH-20261108-PRICING-COMMERCIAL-TERMS-037` coordina DholeWeb 1.12.6 para mostrar los términos comerciales guardados como ítems independientes, incluyendo saltos de línea literales de cotizaciones antiguas.
- Actualiza el manifiesto global a 1.12.6 sin modificar las versiones históricas de los otros componentes del manifiesto ni sus contratos.
- Las pruebas de regresión verifican que editar/guardar conserva las categorías de condiciones, que cada ítem puede arrastrarse individualmente y que no se borran datos persistidos.
- Integración en ramas intermedias, primero develop; CI y staging obligatorios antes de master.


## [1.12.4] - 2026-11-07 (solo rama intermedia; no publicado)

- F0 del batch `rt-20261107-01`: auditoría remota de ramas y versiones en 16 repositorios, registro de baselines, divergencias y 16 ramas intermedias desde develop.
- Agrega documentación versionada `docs/realtime/` con manifiesto de batch, inventario inicial, matriz de cobertura bloqueada, ADR, rollback y evidencia. Sin cambios funcionales ni activación realtime.
- F0 **BLOQUEADA** hasta completar inventario de endpoints/jobs, infraestructura y mediciones; F1, merges y despliegues prohibidos.
- Este incremento PATCH corresponde exclusivamente a DholeSystem en la rama intermedia; el incremento MINOR del batch y sincronización de ecosistema están pendientes y no son release aprobado.



## [1.12.3] - 2026-11-08

- Release DH-20261108-CRM-REDIS-OUTBOX-034: corrige la causa en producción de avisos CRM sin entrega: falta de registro del publicador Redis en DholeCRMService 1.3.0.
- Incrementa CRM a 1.3.1 e integra prueba de publicación real en Redis, recuperando el outbox persistente.
- DholeWeb 1.12.3 hace visible siempre el botón Guardar actividad y muestra el estado de programación de los avisos, evitando formularios sin guardar.
- Mantiene CI, staging y validación de entrega como condiciones obligatorias previas a producción.


## [1.12.0] - 2026-11-07

- Release DH-20261107-CRM-NOTIFICATIONS-031: coordina DholeCRMService 1.3.0 y DholeWeb 1.12.0 para recurrencia de actividades y recordatorios.
- Manifiesto 1.12.0: notificación en el inicio, recordatorios periódicos idempotentes y migración de actividades recurrentes.
- Promoción a develop, pruebas de staging y autorización de producción permanecen pendientes.


## [1.11.4] - 2026-11-07

- Actualiza el manifiesto global 1.11.4 para la visualización persistida de subQUO en Pantalla 8; DholePricingService conserva su versión y contrato existentes.
- Release `DH-20261107-MULTIQUO-SAVED-ACCORDIONS-029`. Pruebas de compilación/CI y staging previas a la promoción coordinada.


## [1.11.3] - 2026-11-07

- Registra el release de traspaso automático de Inland FCL entre Proveedor y Líneas y los componentes participantes.
- Release `DH-20261107-FCL-HAULAGE-HANDOFF-028`. Integración primero en `develop`, validación staging y promoción del mismo lote a `master`.


## [1.11.2] - 2026-11-07

- Manifiesto global del release coordinado: Inland automático, Value de moneda, PDF e interfaz de resumen.
- Release DH-20261107-MULTIQUO-VALUE-INDEX-027. Merge coordinado a develop y master sujeto a CI y staging.


## [1.11.1] - 2026-11-07 (pendiente de CI/staging)

- Actualiza el manifiesto global del lote MultiQUO con versiones de Web, Pricing y Reports, sin autorización de producción.
- Release DH-20261107-MULTIQUO-PERSISTED-PDF-026; sin autorización de despliegue a producción.


## [1.10.1] - 2026-11-07

- Coordina el parche de DholeWeb con navegación sticky, acordeones de subtarifas y cargos Merchant/Carrier.
- Mantiene el guardado agrupado pendiente y exige validación staging antes de master y autorización expresa para despliegue de producción.

## [1.10.0] - 2026-11-07

- Coordina el release de interfaz DholeWeb 1.10.0: persistencia visible de POE y POD, navegación anterior/siguiente por ruta, recarga segura de costos y vista detallada de cada subtarifa.
- Actualiza versión global y de DholeSystem a 1.10.0; registra los cambios de DholeWeb en el manifiesto centralizado.
- Conserva pendiente la API transaccional para guardar la tarifa principal y sub-QUO. Mantiene el despliegue a producción sin autorización hasta validaciones finales.


## [1.9.0] - 2026-11-07

- Coordina el release DH-20261107-SEQUENTIAL-POE-WIZARD-022 del asistente de cotizaciones marítimas por POE y naviera.
- Reordena la pantalla 5 para seleccionar tarifas disponibles y opciones manuales sin diálogos intermedios; pantallas 6 y 7 recorren cada opción preservando su estado.
- Actualiza DholeWeb y DholeSystem a 1.9.0; el backend de guardado agrupado de sub-QUO continúa pendiente de implementación y validación de staging.
- Mantiene el release sin autorización de producción.


## [1.8.0] - 2026-11-07

- Coordina DH-20261107-MANUAL-CARRIER-WIZARD-021: selección mixta de tarifas preaprobadas, preautorizadas y navieras manuales por POE, con pregunta para agregar otra naviera o continuar.
- Mejora el asistente de pantallas 6 y 7 con navegación por alternativa y preservación de datos de costos, flete y agente por POE–naviera.
- Incrementa DholeWeb y DholeSystem de 1.7.0 a 1.8.0, con registro centralizado y pruebas.
- Mantiene bloqueado el guardado parcial hasta implementar API transaccional de grupos de sub-QUO en Pricing.



## [1.7.0] - 2026-11-07

- Preparación coordinada DH-20261107-MULTI-POE-CARRIERS-020 (DholeWeb + DholeSystem).
- Pantalla 3: destinos POE en tarjetas numeradas; pantalla 5: selección múltiple de navieras por cada POE; pantallas 6–8: alternativas independientes POE–naviera.
- Versiones de DholeWeb y DholeSystem 1.6.0 → 1.7.0 (MINOR), con manifiesto y controles de CI.
- La creación comercial de grupos de sub-QUO aún requiere integración transaccional de Pricing API; bloquear guardados parciales.
- La promoción a producción queda supeditada a verificaciones y autorización expresa.



## [1.6.0] - 2026-11-07

- Coordina el release DH-20261107-MULTI-POE-SELECTOR-019 para seleccionar varios POE y alternar pestañas individuales de tarifa.
- Incrementa DholeWeb 1.5.0 → 1.6.0 y DholeSystem 1.5.0 → 1.6.0; PricingService/ReportsService mantienen sus versiones previas.
- Registra explícitamente la limitación del backend: no se pueden guardar varias sub-QUO en una transacción, por lo que el frontend impide guardados parciales.
- Mantiene dependencias del release multi-QUO pendientes y requiere validaciones de staging antes de master.



## [1.5.0] - 2026-11-06 (en desarrollo, sin publicar)

- Prepara el release global DH-20261106-MULTI-QUO-018 para cotizaciones agrupadas con alternativas por POE, ruta, naviera y Merchant/Carrier.
- Registra DholeWeb 1.5.0, DholePricingService 1.4.0 y DholeReportsService 1.4.0 en ramas de implementación, sin integrar a staging o producción.
- Bloquea formalmente la promoción mientras no exista API transaccional, wizard completo, PDF integrado y pruebas de CI/staging.



## [1.3.14] - 2026-11-06

- Registra el release coordinado DH-20261106-PRICING-INLAND-LCL-016 con DholeWeb 1.3.7 y DholePricingService 1.2.8.
- Corrige la dirección de entrega y elimina la validación LCL de naviera oculta.
- Añade persistencia de ubicaciones, migración y verificación de versión; promoción a producción pendiente de staging y autorización.
- Sin cambios al contrato SignalR ni a los servicios no involucrados.


## [1.3.9] - 2026-11-06

- Cierra extracciones de octubre y meses anteriores según la fecha de recepción y calendario de Costa Rica; solo noviembre queda activo.
- Conserva correo y adjuntos históricos, solicitudes Pricing ya enviadas y filas importadas.
- DataExtraction 1.3.2 a 1.3.3: archivado gradual, prevención de reencolado, API HTTP 410 para solicitudes obsoletas.
- AIService 1.3.5 a 1.3.6: cancela tareas antiguas pendientes y trata HTTP 410 como cierre esperado.
- DholeSystem 1.3.8 a 1.3.9. Release DH-20261106-HISTORICAL-CLOSE-011.



## [1.3.8] - 2026-11-06

- Release de optimización de extracción de correos: Qwen genera filas JSON compactas y evita 22 valores null por tarifa.
- DholeAIService 1.3.4 a 1.3.5; DholeSystem 1.3.7 a 1.3.8.
- Sin borrado de colas, sin incremento de paralelismo y sin interrupción de servicios persistentes.
- Se requiere staging previo a producción. DH-20261106-AI-THROUGHPUT-010.



## [1.3.7] - 2026-11-06

- Valida servicios de infraestructura sin reiniciarlos ni borrar sus volúmenes persistentes en producción.
- Registra fallos de salud con el nombre del servicio y diagnóstico, eliminando reinicios innecesarios de Ollama.
- Coordina el cambio de AIService 1.3.4 para agilizar Qwen y mejorar salida JSON.
- Release DH-20261106-AI-RELIABILITY-009.



## [1.3.6] - 2026-11-06

- Registra el release coordinado DH-20261106-MODIFICATION-CLOSURE-008 para evitar cierre automático de modificaciones.
- DholePricingService 1.2.5 → 1.2.6 y DholeWeb 1.3.2 → 1.3.3; incrementa DholeSystem a 1.3.6.
- Separa guardar de enviar al vendedor, bloquea cierre por SLA y revisión, y protege cancelaciones auditadas.
- Requiere validación en staging antes de master y no autoriza despliegue en producción.



## [1.3.4] - 2026-11-06

- Coordina control de saturación AI y extracción de tarifas desde correos sin pérdida de fuentes.
- DholeAIService 1.3.2 → 1.3.3: recuperación de duplicados de AI y menor concurrencia.
- DholeDataExtractionService 1.3.1 → 1.3.2: MarkItDown prioritario en documentos Office, backpressure y límite de reintentos.
- Requiere pruebas de staging antes de permitir integración a master y autorización explícita antes del despliegue de producción.



## [1.3.3] - 2026-11-05

- Release coordinado para corregir Otras pestañas y mostrar versiones SemVer de servicios en monitoreo.
- Registra DholeWeb 1.3.0 y DholeApiGateway 1.3.0; conserva las versiones de los otros 13 componentes.
- Diferencia versiones del proceso en ejecución de versiones declaradas en el manifiesto.


## [1.3.2] - 2026-11-05

- Release coordinado de recuperación de GitHub Actions para AI, Storage y Agent.
- Registra la versión global y el estado de las cuatro modificaciones del lote.


## [1.3.1] - 2026-11-05

- Define release global 1.3.1 y registra versiones SemVer independientes de 16 componentes.
- Activa el deploy de infraestructura de producción por push a master sin confirmación manual; staging continúa por develop.
- Conserva validaciones de volúmenes persistentes, host, red y servicios existentes.


## [1.3.0] - 2026-11-05

- Release coordinado de DholeAIService y DholeDataExtractionService para procesar correos tarifarios por lotes.
- Bumps individuales de 1.2.0 a 1.3.0 y manifiesto global 1.3.0; componentes no modificados conservan 1.2.0.
- Verificación obligatoria de Semantic Versioning por componente en el release.
- No se autoriza producción sin pruebas de staging.


## [1.2.0] - 2026-11-05

- Incorporates universal Dhole SemVer policy with GitHub Actions checks.
- Synchronizes service assembly metadata with the ecosystem version.
- Adds permanent Codex instructions and coordinated release requirements.
