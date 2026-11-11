## [1.31.1] - 2026-11-11

- PATCH DH-20261111-CRM-QUOTE-SELLER-ACCESS-090: coordina corrección de acceso de vendedores desde Cotizaciones CRM para tarifas creadas por Pricing u otro usuario, sin ampliar acceso al resto de los módulos.
- Pricing 1.11.1, Web 1.31.0 y System/global 1.31.1. La validación server-side de cuenta, contacto, ejecutivo y Outbox sigue activa; realtime releaseId existente se preserva. CI/staging pendientes, producción no autorizada.

## [1.31.0] - 2026-11-11

- MINOR DH-20261111-CRM-QUOTE-DELIVERY-089: coordina el selector de destinatarios de cotizaciones en Cuentas CRM; vendedor solo o contacto del cliente con copia al vendedor asignado, validación backend, PDF adjunto y Outbox realtime.
- Versiones coordinadas DholeWeb 1.31.0, DholePricingService 1.11.0 y DholeSystem 1.31.0, sin alterar versiones de otros servicios. CI/staging pendientes; no despliegue a producción autorizado.

## [1.29.2] - 2026-11-11

- PATCH DH-20261111-CRM-INSTITUTIONAL-SELLER-VISIBILITY-088: corrige visibilidad del vendedor institucional Castro Fallas en los selectores de Cuentas y Prospectos; registra versión global Dhole 1.29.2 con DholeWeb 1.29.2.
- La API de DholeCRMService conserva el indicador institucional y contratos REST/SignalR; en master se sincroniza la versión CRM 1.17.1 ya existente. Conserva versiones de los servicios restantes y exige CI/staging antes de promover el release.

## [1.29.0] - 2026-11-11

- MINOR DH-20261111-CRM-LEAD-INSTITUTIONAL-087: manifiesto global y backport a master para vendedor institucional Castro Fallas en Prospectos, CRM 1.17.0, Web 1.29.0.
- Se preservan demás servicios, versionado SemVer, API REST/SignalR y validaciones obligatorias CI/staging. Producción no autorizada.

## [1.27.1] - 2026-11-11

- PATCH DH-20261111-CRM-AGREEMENT-LIST-085: coordina DholeWeb 1.27.1 y DholeSystem 1.27.1 para quitar/restaurar compromisos programables sin alterar «Acuerdos alcanzados».
- Conserva 14 servicios sin modificaciones; REST, SignalR y esquema sin cambios. Staging Web aprobado en develop; promoción de master autorizada para este parche.

## [1.27.0] - 2026-11-11

- MINOR DH-20261111-CRM-PROCEDURE-ATTACHMENTS-085: coordina DholeSystem 1.27.0, DholeCRMService 1.15.0 y DholeWeb 1.27.0 para documentos adjuntos a procedimientos específicos de cuentas.
- Backport aislado hacia master desde release 085 validado en develop/staging. Se mantienen flags realtime deshabilitadas; no es autorización global para activar realtime ni modificar otros 13 componentes.

## [1.25.3] - 2026-11-11

- PATCH DH-20261111-CRM-WORKSPACE-TABS-084: sincroniza el manifiesto global con la corrección de pestañas de Prospectos, Actividades y Seguimientos ya integrada en DholeWeb master 1.25.1 (commit 7396cb4e). Respeta las publicaciones anteriores y mantiene versiones independientes de los 16 componentes.
- Infraestructura realtime y contratos REST sin cambios. La integración master de Web está autorizada; pruebas de staging del flujo completo por verificar.

## [1.25.2] - 2026-11-11

- PATCH DH-20261111-PRICING-OPENING-ATTACHMENTS-084: candidato aislado de master para Pricing 1.10.1 y Notifications 1.3.1, registrando versión global System 1.25.2 en manifiesto de los 16 componentes.
- Conserva los cambios anteriores de master; soportes de solicitudes y archivos de QUO en correos de apertura. CI/staging pendientes, producción no autorizada.

## [1.25.0] - 2026-11-10

- MINOR DH-20261110-CRM-LEAD-DUPLICATE-083: actualiza manifiesto global de los 16 componentes y versiones individuales de CRM 1.13.0, Web 1.25.0, Notifications 1.3.0 y System 1.25.0, preservando los demás servicios.
- Protección de duplicados al crear prospectos, aviso inmediato con vendedor asignado y notificación de sistema. CI y staging requeridos antes de promoción a producción.

## [1.24.0] - 2026-11-10

- MINOR DH-20261110-CRM-ACCOUNT-CATEGORY-SCOPE-082: Actualiza versión global y manifiesto de 16 componentes para Auth, CRM y Web; conserva realtime y configuraciones previas.
- Tests CI obligatorios y staging por validar. Merge a master autorizado expresamente.

## [1.23.0] - 2026-11-10

- MINOR DH-20261110-CRM-LEAD-QUO-PARITY-082: coordina DholeWeb 1.23.0 y DholePricingService 1.10.0 para usar QUO reales de Prospectos, indicadores y asignación histórica segura, manteniendo Cuentas, Auth/CRM y el release 1.22.0 sin cambios incompatibles.
- CI aprobado y staging del batch completo verificado antes de promover a master. Autorización explícita del usuario para master.

## [1.22.0] - 2026-11-10

- MINOR DH-20261110-CRM-ACCOUNT-PROCEDURES-080: release de procedimientos específicos por cuenta; backend CRM 1.11.0, Web 1.22.0 y DholeSystem 1.22.0.
- Promoción master aislada de un release verificado en staging, conservando el estado de producción y los componentes no involucrados; registro explícito de diferencia realtime entre master/develop.
- Versión universal y gates de CI; producción autorizada para este release por solicitud expresa.

## [1.21.0] - 2026-11-10

- MINOR DH-20261110-CRM-CONTACTS-ROLE-MULTISELECT-079: Release global coordinado de CRM para multiselección de contactos y restricción de roles de responsables.
- Se mantienen API REST y realtime existentes. Validación por CI y staging antes de confirmar despliegue.

## [1.20.1] - 2026-11-10

- PATCH DH-20261110-CRM-SELLERS-COMMITMENTS-078: coordina DholeAuthService (filtro de vendedores activos), DholeCRMService (asignación y cierre seguro de compromisos) y DholeWeb (selector y checkboxes).
- Registra versiones de cada componente y mantiene infraestructura realtime REST/SignalR, sin modificar los contratos existentes. CI, staging y producción pendientes.

## [1.20.0] - 2026-11-10

- MINOR DH-20261110-CRM-AGENDA-UNIFIED-077: manifiesto coordinado del CRM con Nueva actividad, participantes/contactos, minuta, agendas globales y compromisos marcables. Integra DholeWeb 1.20.0 y DholeCRMService 1.5.0, reutilizando DholeAuthService 1.2.5.
- Validación CI/staging y promoción del mismo release, preservando las políticas de SignalR.

## [1.19.5] - 2026-11-10

- PATCH DH-20261110-CRM-GLOBAL-AGENDAS-076: coordina DholeAuthService, DholeCRMService y DholeWeb para consultar agendas de otros vendedores y crear actividades con crm.activity.read-all o ambos permisos crm.account.read-all y crm.lead.read-all.
- Registra las versiones independientes y commits candidatos; no modifica los contratos REST ni la infraestructura realtime existente. CI/staging pendientes y producción no autorizada.

# Changelog

## [1.17.20] - 2026-11-10

- PATCH DH-20261110-CRM-HISTORICAL-ACTIVITIES-075: coordina DholeWeb 1.17.20 y DholeCRMService 1.4.6 para crear actividades comerciales históricas sin reprogramarlas ni enviar recordatorios retroactivos. Las actividades ya terminadas se guardan completadas.
- Mantiene los releases de master hasta 1.17.19 y no modifica framework, Auth, SignalR ni esquemas.

## [1.17.19] - 2026-11-10

- PATCH DH-20261110-PRICING-CRM-PROSPECT-REQUESTS-MASTER-076: backport coordinado del hotfix para recuperar en CRM el ejecutivo de cuentas y prospectos al enviar solicitudes normales, editar solicitudes de Ventas, solicitar modificaciones y guardar modificaciones LCL en Pricing. DholeWeb y DholeSystem 1.17.19; resto de servicios conservan sus versiones.
- Aislado del resto de develop 1.19.x; sin cambios REST, SignalR o migraciones. CI y staging antes de la integración en master; autorización del usuario para promocionar a master.

## [1.17.14] - 2026-11-10

- PATCH DH-20261110-CRM-ACTIVITY-FULL-DETAIL-068: integra a master la vista completa de actividades CRM, minutas y compromisos con enlace a actividad principal. Web 1.17.14, CRM 1.4.3 y DholeSystem 1.17.14. Preserva el release Pricing 1.9.11 / TARIFARIO de DholeSystem 1.17.13.
- Sin migraciones de datos, framework ni infraestructura SignalR; versión desarrollada y verificada en staging sobre develop.

## [1.17.13] - 2026-11-10

- PATCH DH-20261110-CRM-HIDE-TARIFARIO-067: DholeSystem 1.17.13 y Pricing 1.9.11 excluyen nombres de cliente histórico que contienen «TARIFARIO» de las QUO pendientes de vinculación del CRM, antes del conteo y la paginación; conservan datos e historial ya vinculado.
- Sin cambios de Framework ni de infraestructura realtime; manifestación del release coordinado con Pricing, autorizado para promoción a master tras staging.

## [1.17.12] - 2026-11-10

- PATCH DH-20261110-PRICING-CRM-REQUEST-IDENTITY-067: versión de ecosistema 1.17.12. Las solicitudes normales y de modificación recuperan identidad comercial CRM desde sus cuentas, mantienen vendedor y compatibilidad histórica. Componentes Web 1.17.12, Pricing 1.9.10, CRM 1.4.2.
- Coordinación de ramas intermedias; CI y staging pendientes. Sin despliegue autorizado a producción ni cambios en CustomCodeFramework.

## [1.17.10] - 2026-11-10

- PATCH DH-20261110-CRM-AGENDA-CLIENT-EXECUTIVE-065: manifiesto central y versiones DholeWeb/DholeSystem a 1.17.10 para Cliente y Ejecutivo comercial en Agenda y seguimientos.
- Se preserva el release previo CRM de búsqueda por cédula 1.17.9, así como las versiones de los otros 14 componentes. Ningún cambio en los servicios API, Hub SignalR o framework.

## [1.17.9] - 2026-11-10

- PATCH DH-20261110-CRM-ACCOUNT-SEARCH-064: incorpora búsqueda por cédula en el listado de cuentas CRM, conservando alcance por usuario, filtros y paginación. Identificación normalizada o histórica, con o sin formato.
- Versión global DholeSystem 1.17.9; DholeWeb 1.17.9; DholeCRMService 1.4.1. Release en ramas intermedias con CI y staging pendientes; no autoriza producción.


## [1.17.5] - 2026-11-10

- PATCH DH-20261110-CRM-QUO-STATUS-061: traducción de estados comerciales de las QUO vinculadas en las vistas CRM, reutilizando la presentación estándar de Pricing sin cambiar enum, datos históricos ni cálculos.
- Versión del ecosistema 1.17.5: DholeWeb 1.17.5, DholeSystem 1.17.5; restantes 14 componentes sin cambios. Regresión de traducciones y preservación de estados.

## [1.17.3] - 2026-11-10

- PATCH DH-20261110-PRICING-CRM-EXECUTIVE-059: release global sincronizado para corregir el guardado de cotizaciones SPOT/tarifarios cuando la cuenta CRM ya tiene ejecutivo comercial asignado. DholeWeb 1.17.3 envía el Auth userId que DholePricingService 1.9.5 exige junto al nombre.
- Registro coordinado de versiones, pruebas y revisión en staging; no se modifica framework, infraestructura realtime ni esquema. La promoción a master ejecutaría despliegue a producción y requiere autorización separada.

## [1.17.2] - 2026-11-10

- PATCH DH-20261110-CRM-QUO-SUPERADMIN-058: interfaz de vinculación QUO histórica colapsable y visible solo a superadministración; Pricing protege las acciones de migración a nivel servidor.
- Release coordinado DholeWeb 1.17.2, DholePricingService 1.9.4 y DholeSystem 1.17.2. Ningún cambio en framework, migraciones o servicios ajenos.

## [1.17.1] - 2026-11-10

- PATCH DH-20261110-CRM-QUO-LIVE-057: indicadores y rutas del CRM toman las QUO asociadas por ID a Pricing, la lista muestra pendientes reales y permite selección múltiple en filtros paginados.
- Release coordinado DholeWeb 1.17.1, DholePricingService 1.9.3, DholeSystem 1.17.1; preserva infraestructura realtime y no modifica CustomCodeFramework.

## [1.16.2] - 2026-11-09

- PATCH DH-20261109-CRM-QUO-LINK-SYNC-056: sincronización de QUO históricas con identidad CRM y exclusión de las ya vinculadas del listado de pendientes.
- Versionamiento coordinado DholeWeb 1.16.1, DholePricingService 1.9.2, DholeSystem 1.16.2. Sin cambios de esquema ni framework.

## [1.16.0] - 2026-11-09

- MINOR: manifest global para el catálogo de QUO históricas en CRM y su vinculación humana confirmada a cuentas. No se modifican otros componentes.
- Release DH-20261109-CRM-LEGACY-QUO-CATALOG-055: DholeWeb 1.16.0, DholePricingService 1.9.0, DholeSystem 1.16.0. No desplegar en producción hasta validar staging.

## [1.15.0] - 2026-11-09

- CRM/Pricing: identidad de cuentas/prospectos y conciliación confirmada del historial de cotizaciones.

## [1.12.22] - 2026-11-09 (QUO-269 seller workflow status)

- Coordinated PATCH DH-20261109-QUO269-SELLER-STATUS-053 (master): PricingService 1.5.22 and Web 1.12.22 display the current Open workflow state in Sales for already-completed QUO-269 without exposing unpublished quote data. The last published commercial snapshot remains unchanged.
- Manifest and global ecosystem version 1.12.22; existing NotificationsHub, F6-F9, ACL and production safety boundaries are preserved.

## [1.12.21] - 2026-11-09 (Seller Pricing status master candidate)

- PATCH coordinado: DholeWeb 1.12.21 y DholePricingService 1.5.21 distinguen solicitudes abiertas en Pricing de revisiones comerciales sin publicar; sincronización periódica del panel vendedor.
- Backport aislado del release DH-20261109-SELLER-PRICING-STATUS-052 desde develop, sin fusionar los cambios del piloto realtime.
- Staging y controles de producción requeridos antes de promocionar; `master` y la producción no se despliegan desde esta rama de trabajo.

## [1.12.6] - 2026-11-08

- Release `DH-20261108-PRICING-COMMERCIAL-TERMS-037` coordina DholeWeb 1.12.6 para mostrar los términos comerciales guardados como ítems independientes, incluyendo saltos de línea literales de cotizaciones antiguas.
- Actualiza el manifiesto global a 1.12.6 sin modificar las versiones históricas de los otros componentes del manifiesto ni sus contratos.
- Las pruebas de regresión verifican que editar/guardar conserva las categorías de condiciones, que cada ítem puede arrastrarse individualmente y que no se borran datos persistidos.
- Integración en ramas intermedias, primero develop; CI y staging obligatorios antes de master.

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
