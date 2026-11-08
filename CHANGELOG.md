# Changelog

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
