## [1.52.1] - 2026-11-13

- PATCH DH-20261113-PRICING-OWN-LCL-141: release coordinado Pricing 1.18.2 y Web/System 1.52.1. Corrección CFS LCL propio por CBM cobrable (mínimo 1) en guardado, lectura histórica, API, PDF y totales; sin cambiar coloader/Miami ni revisiones publicadas.
- Compatible con develop 1.52.0; integrar master mediante lote coordinado tras CI/staging.

## [1.52.0] - 2026-11-13

- MINOR DH-20261113-CRM-BITACORA-DIRECT-TASKS-PARENT-141: bitácoras comerciales crean recordatorios directos de acuerdos con fecha futura, sin botones intermedios. El CRM preserva la relación padre-hija mediante FK `origin_activity_id`, recupera recordatorios heredados y presenta acceso a la bitácora padre en el detalle.
- Versiones coordinadas: DholeWeb 1.52.0, DholeCRMService 1.31.0, DholeSystem/ecosistema 1.52.0; otros componentes sin incremento. CI, versión y staging obligatorios antes de integrar master y publicar producción.

## [1.51.2] - 2026-11-13

- PATCH DH-20261113-PRICING-OWN-LCL-140: Web 1.51.2 y sistema/ecosistema 1.51.2. Corrige cotizaciones LCL propias históricas: CFS por CBM cobrable, recuperación segura del POL comercial chino y recálculo de la recolecta sin pérdida de importes; elimina detalles genéricos ajenos a la matriz al guardar.
- PricingService conserva 1.18.1. Manifiesto y CHANGELOG coordinados, no se alteran otros servicios. Validar CI + staging antes de promover de develop a master; no se modificará main.

## [1.51.1] - 2026-11-13

- PATCH DH-20261113-PRICING-OWN-LCL-139: release coordinado Pricing/Web para CFS de LCL propio por CBM cobrable, persistencia de Manejos y costos editados, y cotización sin cargos automáticos ajenos al consolidado. Pricing 1.18.1, Web 1.51.1, DholeSystem/ecosistema 1.51.1; resto de servicios sin cambios.
- Ramas intermedias por repositorio. Integrar develop y comprobar CI/staging antes de master. Sin autorización de producción; main intacta. REST, SignalR y Outbox existentes compatibles.

## [1.51.0] - 2026-11-13

- MINOR DH-20261113-CRM-BITACORA-AGREEMENT-TASKS-138: release coordinado de bitácoras editables con tareas opcionales desde acuerdos, recordatorios de seguimientos vinculados, historial de origen y regresión específica en Web y CRM. Web 1.51.0, CRM 1.30.0, sistema/ecosistema 1.51.0; demás componentes conservan versiones vigentes.
- Ramas intermedias por repositorio, CI y validación staging obligatorios antes de promover a master. Producción no autorizada.

## [1.50.0] - 2026-11-13

- MINOR DH-20261113-CRM-SELLER-ACTIVITY-REPORTS-137: manifiesto coordinado de reportes de actividades comerciales CRM (general y por vendedor), indicadores, desglose por tipo, filtros, Excel y PDF. Web 1.50.0, CRM 1.29.0, Sistema/ecosistema 1.50.0; resto de componentes conserva su versión previa por rama.
- CI y staging pendientes; sin autorización para despliegue productivo.

## [1.49.0] - 2026-11-13

- MINOR DH-20261113-CRM-AGENDA-NOTES-FILTERS-136: manifiesto coordinado de navegación CRM Agenda/Calendario/Bitácora · Notas, filtros de cliente y vendedor, tarjetas con notas y documentos. DholeWeb 1.48.4 → 1.49.0; DholeCRMService 1.28.3 → 1.28.4; ecosistema 1.48.4 → 1.49.0.
- Se preservan autorizaciones CRM, API REST, SignalR, sincronización idempotente y despliegue de staging primero. Producción no autorizada.

## [1.48.4] - 2026-11-13

- PATCH DH-20261113-PRODUCTION-DEPLOY-SKIP-135: registra la corrección coordinada de la condición if en los jobs de producción Auth/CRM/Web; se eliminan los bloqueos por mensaje de commit que marcaban deploy Skipped, sin flags.
- Versiones Auth 1.9.2 → 1.9.3; CRM 1.28.2 → 1.28.3; Web 1.48.3 → 1.48.4; DholeSystem 1.48.1 → 1.48.4; ecosistema → 1.48.4. CI y staging requeridos antes de master. Publicación solicitada por usuario 2026-11-13.

## [1.48.1] - 2026-11-13

- PATCH DH-20261113-CRM-AGENDA-RETURN-132: manifiesto global del retorno desde detalle de actividades a Agenda y seguimientos (`/crm/followups`) en DholeWeb.
- Ecosistema y DholeSystem 1.47.4 → 1.48.1, alineados con DholeWeb 1.48.0 → 1.48.1 y la nueva Bitácora comercial. Otros microservicios sin cambios; REST/SignalR intactos.
- CI y staging pendientes; master auto-despliega y requiere autorización expresa antes de fusionar.

## [1.47.4] - 2026-11-13

- PATCH DH-20261113-CRM-DRAFT-RECOVERY-130: manifiesto del release coordinado de recuperación de borradores CRM; mantiene compatibilidad REST, SignalR, Outbox y servicios sin cambios.
- DholeSystem 1.46.3 → 1.47.4, DholeWeb 1.47.3 → 1.47.4, DholeCRMService 1.27.3 → 1.27.4, ecosistema 1.47.3 → 1.47.4. Compilaciones, gates CI y staging pendientes; producción no autorizada.

## [1.46.3] - 2026-11-13

- PATCH DH-20261113-OPERATIONS-NO-FLAGS-128: elimina el bloqueo de despliegue de DholeOperationsService en master que dependía de una variable manual.
- DholeOperationsService 0.1.1 → 0.1.2; DholeSystem y ecosistema 1.46.2 → 1.46.3. Se conservan las versiones de los demás servicios.
- Deploy por push automático en develop/staging y master/producción, sin flags de habilitación. Mantiene reglas de ramas intermedias, pruebas CI, readiness y autorización de release previa al merge master.

## [1.46.2] - 2026-11-12

- PATCH DH-20261112-OPERATIONS-STAGING-127: OperationsService 0.1.0 → 0.1.1 habilita deploy automático en staging al integrar `develop`, igual que ConfigService.
- DholeSystem y ecosistema 1.46.1 → 1.46.2; manifiesto registra 17 repositorios y conserva las versiones de los demás servicios.
- CI y staging pendientes; promoción a master condicionada a validación. Producción permanece protegida.

## [1.46.1] - 2026-11-12

- MINOR DH-20261112-OPERATIONS-BOOTSTRAP-126: registra DholeOperationsService v0.1.0 en el manifiesto global del ecosistema Dhole.
- Copia estructura y deploys de DholeConfigService adaptados a Operations, respetando branches develop y master, nunca main.
- DholeSystem y ecosistema 1.44.3 → 1.46.1. La versión de Operations nace en 0.1.0; los demás componentes mantienen su versión.
- CI y staging deben validarse y las variables de habilitación deben configurarse antes de despliegues. Producción no autorizada.

## [1.44.3] - 2026-11-12

- PATCH DH-20261112-CRM-REMINDER-CONTEXT-124: los recordatorios comerciales de CRM identifican cliente o prospecto y enlazan al detalle del compromiso, ya sea actividad o seguimiento; también en escalaciones a supervisión.
- `crm-workers` obtiene `Crm:PublicWebBaseUrl` desde el origen Web permitido `CORS_WEB_ORIGIN`, conservando el dominio propio de staging/producción sin fijar enlaces en código ni exponer credenciales.
- Versiones: DholeCRMService 1.25.2 → 1.25.3; DholeSystem y ecosistema 1.44.2 → 1.44.3. Resto de servicios sin cambios. Compatibilidad REST/SignalR/Outbox; sin migraciones.
- CI, pruebas de regresión y validación de staging pendientes. Master auto-despliega producción y requiere autorización expresa antes de fusionar.

## [1.44.2] - 2026-11-12

- PATCH DH-20261112-PRICING-TARIFF-MODAL-123: DholeWeb rediseña el modal «Aplicar tarifario a cliente», con superficie opaca, mayor tamaño y selector CRM sin recortes. Misma lógica de cuentas, prospectos, ejecutivo y QUO derivadas.
- Versiones DholeWeb 1.44.1 → 1.44.2, DholeSystem/ecosistema 1.44.1 → 1.44.2; PricingService 1.17.0 y CRMService 1.25.2 sin modificaciones. Compatibles REST, realtime/SignalR y Outbox.
- Pruebas y staging pendientes; manifiesto actualizado. No habilitar producción antes de autorización.

## [1.44.1] - 2026-11-12

- PATCH DH-20261112-PRICING-TRANSIT-LABEL-122: en la pantalla 6 de terrestre, aéreo y marítimo el campo de días se muestra como «Días de tránsito» en todas las modalidades; mantiene intactos datos y contratos.
- DholeWeb 1.44.0 → 1.44.1, DholeSystem/ecosistema 1.44.0 → 1.44.1; se actualiza el manifiesto centralizado. CI, compilación y staging requeridos antes de promover a master.

## [1.44.0] - 2026-11-12

- MINOR DH-20261112-PRICING-TARIFF-CRM-121: release coordinado de «Aplicar tarifario a cliente» con selector CRM y vinculación de cuentas/prospectos al duplicar tarifarios maestros. El ejecutivo se obtiene de CRM y el servicio Pricing valida ID, permisos y nombre canónico.
- DholeWeb 1.43.6 → 1.44.0; DholePricingService 1.16.3 → 1.17.0; DholeSystem/global 1.43.8 → 1.44.0. CRM 1.25.2 sin cambios; manifiesto actualizado. REST legado, SignalR, Redis Streams y Outbox compatibles.
- CI y pruebas staging pendientes; no desplegar en producción sin validar y autorizar. No hay migraciones de datos.

## [1.43.8] - 2026-11-12

- PATCH DH-20261112-PRICING-CRM-LEAD-OWNER-120: DholeCRMService 1.25.1 → 1.25.2 corrige GET /pricing-client-options para proyectar IsCastroFallasExecutive real en prospectos y evitar presentar Maurice Lang cuando el CRM indica Castro Fallas.
- DholeSystem/ecosistema 1.43.7 → 1.43.8, manifiesto central reconciliado con la versión real CRM; DholeWeb 1.43.6 y PricingService 1.16.3 sin cambios. Contratos REST, ACL, SignalR y Outbox conservados.
- CI y staging con TARIFARIO aún pendientes. No hay modificación de datos ni migración de base de datos.

## [1.43.7] - 2026-11-12

- PATCH DH-20261112-PRICING-CRM-TARIFF-119: release coordinado de DholeWeb 1.43.5 → 1.43.6 para respetar el ejecutivo institucional Castro Fallas en Pricing y crear tarifarios maestros al seleccionar el registro TARIFARIO del CRM.
- DholeSystem y versión global 1.43.6 → 1.43.7. DholeCRMService y DholePricingService conservan sus versiones actuales, sin migraciones ni cambios REST/SignalR.
- Manifiesto actualizado; pendientes CI, comprobación de endpoints CRM y prueba de recuperación de borradores y clasificación de maestros en staging. Producción no autorizada.

## [1.43.6] - 2026-11-12

- PATCH DH-20261112-DYNAMICS-QUO-613-619-118: conciliación segura de QUO-613 con la única línea real Dhole por USD 10 395, sin duplicar, y recuperación de QUO-619 solo tras confirmación administrativa de no aplicación de cabecera previamente reservada.
- Versiones: Connector 1.4.0 → 1.4.1; Pricing 1.16.2 → 1.16.3; Web 1.43.4 → 1.43.5; DholeSystem/global 1.43.5 → 1.43.6. SemVer, manifiesto, Outbox, SignalR y REST compatibles. CI/staging pendientes; sin producción.

## [1.43.5] - 2026-11-12

- PATCH DH-20261112-PRICING-LTL-CURRENCY-VALUE-118: versión global del ajuste de moneda en Pantalla 5 LTL de DholeWeb, donde venta, costo y mínimo usan Config.currencies.Value en lugar de códigos CUR-*.
- DholeSystem/ecosistema 1.43.4 → 1.43.5; DholeWeb 1.43.3 → 1.43.4; PricingService 1.16.2 sin cambios. Se preserva la corrección de Outbox y el historial; REST/SignalR intactos. CI/staging pendientes, producción no autorizada.

## [1.43.4] - 2026-11-12

- PATCH DH-20261112-PRICING-OUTBOX-CORRELATION-115: corrige el error de persistencia Outbox por correlation_id mayor de varchar(100) al reenviar aceptación de QUO-00000-000609.
- DholePricingService 1.16.1 → 1.16.2 y DholeWeb 1.43.2 → 1.43.3. DholeSystem/ecosistema 1.43.3 → 1.43.4. No se modifican el framework ni el esquema de PostgreSQL.
- Identificadores compactos deterministas más SHA-256 de respaldo garantizan la idempotencia por operación. DhModal presenta la razón real de fallos sin inventar relación con Reports.
- Mantiene REST, Redis Streams, SignalR y Outbox existentes. CI/staging/SMTP pendientes antes de confirmar entrega de QUO-609.

## [1.43.3] - 2026-11-12

- PATCH DH-20261112-DYNAMICS-IDTRA-FIRST10-117: versionado coordinado con DholePricingService 1.16.1 para admitir más de diez IDTRA en una QUO y mapear los primeros diez distintos y ordenados a Dynamics sin alterar la lista completa en Pricing.
- DholeSystem/ecosistema 1.43.2 → 1.43.3; el resto de componentes mantiene su versión; conector Dynamics, RateId, importes, revisiones, idempotencia, REST y SignalR no cambian.
- Release candidato en ramas intermedias; pendiente CI, staging, comprobación de cabecera/línea y autorización de producción.

## [1.43.2] - 2026-11-12

- PATCH DH-20261112-LTL-CFZ-ROUTE-116: LTL propio CFZ Panamá → San José Costa Rica vuelve a ser seleccionable sin requerir una fila maestra previamente creada; genera la ruta dinámicamente con los cuatro cargos activos de Costos y recargos, por peso y tramo configurado.
- DholeSystem/ecosistema 1.43.1 → 1.43.2, DholeWeb 1.43.1 → 1.43.2. PricingService 1.16.0 conserva su versión y contratos actuales. No altera SignalR, Outbox ni otros servicios.
- Verificación de CI, staging y aceptación del flujo real requeridas antes de promoción a producción.

## [1.43.1] - 2026-11-12

- PATCH DH-20261112-LTL-PANAMA-COSTS-115: release global coordinado de LTL propio CFZ Panamá → San José Costa Rica: los cargos de Bunker, Gastos Panamá a Costa Rica, Flete Terrestre Internacional y Custodia + Marchamo provienen del catálogo de Costos y recargos de Pricing, con cálculos por peso y sin doble flete.
- DholeWeb 1.43.0 → 1.43.1 y DholeSystem/ecosistema 1.43.0 → 1.43.1. DholePricingService permanece 1.16.0 por reutilizar los endpoints existentes. Realtime, REST y otros servicios sin alteraciones.
- CI y staging pendientes de confirmación; producción no autorizada.

## [1.43.0] - 2026-11-12

- MINOR DH-20261112-PRICING-RESEND-CHOICE-114: selección de notificación para reenvíos en QUO aceptadas, desde DhModal. Opciones: apertura con PDF y respaldos, cotización enviada según CRM y aviso preliminar SIN PDF.
- Pricing distingue errores de generación de PDF, descarga de adjuntos y persistencia Outbox. En caso de fallos de Reports, se permite aviso SIN PDF claramente identificado como incompleto, sin cambiar aceptación ni IDTRA.
- Componentes: DholePricingService 1.15.0 → 1.16.0, DholeWeb 1.42.0 → 1.43.0, DholeSystem/global 1.42.0 → 1.43.0. Otros servicios conservan su versión; REST/SignalR/Outbox existentes.
- CI, staging y confirmación SMTP pendientes.

## [1.42.0] - 2026-11-12

- MINOR DH-20261112-PRICING-ACCEPTANCE-MAIL-113: notificación de aceptación de QUO con copia a Pricing y vendedor, aviso de fallos en Outbox y reenvío manual desde DhModal para cotizaciones aceptadas.
- Pricing 1.14.0 → 1.15.0, Web 1.41.2 → 1.42.0, System/global 1.41.2 → 1.42.0. No altera estado comercial, IDTRA ni esquemas; compatibilidad REST/SignalR/Outbox conservada.
- CI y staging antes de producción. QUO-00000-000609 pendiente de verificación SMTP y reenvío real.

## [1.41.2] - 2026-11-12

- PATCH DH-20261112-PRICING-LINKED-QUO-NUMBER-113: Pricing Crystal y wizard legado muestran el QUO Number de la cotización aceptada vinculada en vez del UUID interno. El ID persiste exclusivamente para navegación y enlace comercial.
- DholeSystem 1.41.1 → 1.41.2, DholeWeb 1.41.1 → 1.41.2, PricingService 1.14.0 sin cambios. Compatible con REST, SignalR, Outbox e infraestructura existente. CI/staging pendientes.

## [1.41.1] - 2026-11-12

- PATCH DH-20261112-PRICING-CLIENT-QUO-PICKER-112: release coordinado de DholeWeb para listar de forma automática todas las QUO enviadas y aceptadas del cliente en «Cliente aceptó otra QUO», con paginación, búsqueda local y ruta/estado visibles.
- El vínculo requiere que la QUO ganadora esté aceptada y pertenezca al mismo cliente. Reutiliza endpoints existentes de DholePricingService 1.14.0, sin alterar REST, SignalR ni datos.
- DholeSystem 1.40.1 → 1.41.1; DholeWeb 1.41.0 → 1.41.1. CI/staging pendientes; sin autorización para producción.

## [1.40.1] - 2026-11-12

- PATCH DH-20261112-CRM-DRAFT-DHMODAL-111: release global coordinado de DhModal para recuperación de borradores de CRM; confirma recuperar, descartar o posponer desde componentes internos Dhole. Evita diálogos nativos y elimina prompts de formularios cerrados.
- DholeWeb 1.40.0 → 1.40.1; CRMService 1.24.0 → 1.24.1; DholeSystem 1.40.0 → 1.40.1; mantiene intacta la infraestructura realtime y API Manager previos.
- CI y staging pendientes, sin despliegue manual autorizado.

## [1.40.0] - 2026-11-11 (Dhole API Manager)

- MINOR: Aprovisionamiento por entorno de identidad técnica única de lectura para los ocho catálogos de Config.
- Sin credenciales comprometidas; se conserva ThirdParty deshabilitado hasta la configuración segura del entorno.
- Release coordinado Gateway 1.6.0 / Web 1.40.0, pendiente de staging.

## [1.39.0] - 2026-11-11

- MINOR DH-20261111-CRM-DRAFT-RECOVERY-109: registra release coordinado de autoguardado CRM Web 1.39.0 y CRMService 1.24.0, con recuperación local por formulario/usuario/registro sin mutar registros de CRM hasta confirmar guardar.
- Actualiza el manifiesto central conservando las versiones existentes de los otros servicios; no cambia la infraestructura realtime, SignalR ni los contratos REST.
- DholeSystem 1.38.1 → 1.39.0; versión global 1.39.0. CI y staging pendientes. Producción no autorizada.

## [1.38.1] - 2026-11-11

- PATCH DH-20261111-CRM-GEOAPIFY-CSP-108: registra el hotfix CSP para búsqueda Geoapify en visitas CRM. DholeWeb 1.38.0 → 1.38.1 y DholeSystem 1.37.2 → 1.38.1; versión global 1.38.1.
- El servidor Nginx de DholeWeb agrega exclusivamente https://api.geoapify.com a connect-src, mantiene restricciones CSP y agrega prueba de regresión. No cambia contratos REST, microservicios, SignalR ni datos.
- Release candidato: verificar tests, compilación, nginx -t y búsqueda de direcciones en staging antes de desplegar en producción.

## [1.37.2] - 2026-11-11

- PATCH DH-20261111-PRICING-QUO-LINK-ACTION-106: versiona la corrección de Web para mostrar el botón «Cliente aceptó otra QUO» en el asistente Crystal de Pricing y en duplicación FCL, vinculando únicamente QUO originales ya existentes.
- Componentes: DholeWeb 1.37.1 → 1.37.2 y DholeSystem 1.37.0 → 1.37.2; versión global 1.37.2. Pricing 1.14.0 sin cambios. Sin modificación de endpoints REST, SignalR, Outbox, base de datos o infraestructura realtime.
- Validar CI y staging antes de promocionar a master; producción sólo mediante merge autorizado.

## [1.37.0] - 2026-11-11

- MINOR DH-20261111-PRICING-QUO-LINKED-104: nuevo estado comercial QUOVinculada para cotizaciones cuya operación fue aceptada bajo otra QUO del mismo cliente. El vínculo a la QUO aceptada es obligatorio, persistente y validado en Pricing.
- El módulo Web muestra «Cliente aceptó otra QUO» con búsqueda, selección y navegación al documento aceptado; las tarifas vinculadas se muestran por separado y no computan como vencidas o no aceptadas.
- Componente DholeSystem 1.35.0 → 1.37.0, ecosistema Dhole 1.37.0. Contratos REST, SignalR e infraestructura Outbox preservados. CI/staging pendientes; sin autorización de producción.

## [1.35.0] - 2026-11-11

- MINOR DH-20261111-CRM-QUOTE-MULTI-CONTACTS-102: múltiples destinatarios para todas las futuras cotizaciones por cuenta CRM. Web utiliza DhMultiSelect y elimina el selector de cotización individual; CRM guarda la lista de contactos con migración compatible; Pricing valida y envía el PDF a cada contacto con copia al vendedor.
- Componentes del release: CRM 1.22.0, Pricing 1.13.0, Web 1.35.0 y System/global 1.35.0. Compatibilidad REST, SignalR y Outbox mantenida. CI/staging pendientes y producción sin autorización.

## [1.33.1] - 2026-11-11

- PATCH DH-20261111-CRM-QUOTE-PREFERENCE-REALTIME-094: actualiza el release global y CRM 1.20.1 para el evento Outbox al cambiar las preferencias de destinatario de cotizaciones, reutilizando la infraestructura realtime existente.
- Complementa 093: Pricing 1.12.0, Web 1.33.0; CI y staging pendientes, sin despliegue a producción autorizado.

## [1.33.0] - 2026-11-11

- MINOR DH-20261111-CRM-ACCOUNT-QUOTE-DELIVERY-093: preferencias de destinatario permanentes por cuenta CRM para todas las cotizaciones futuras. CRM 1.20.0, Pricing 1.12.0, Web 1.33.0, System/global 1.33.0.
- Aplicación en cada transición Sent, copia al vendedor asignado, validación de contacto, Outbox/realtime existentes y compatibilidad REST.
- CI y staging pendientes, producción no autorizada hasta aprobación expresa.

## [1.32.1] - 2026-11-11

- MINOR DH-20261111-CRM-QUOTE-SEND-VISIBLE-092: sincroniza la versión global con el frontend que muestra el botón «Enviar cotización» en la cabecera de todas las cuentas, incluso sin tarifas vinculadas; mantiene los controles de destinatario, contacto y copia al vendedor.
- DholeWeb 1.32.1, DholeSystem/global 1.32.1, Pricing 1.11.1 sin cambios en backend, API REST ni eventos realtime. La línea develop mantiene las funciones Geoapify propias de Web 1.32.0; no se introducen esas funcionalidades en master con este backport.
- CI/staging pendientes; producción no autorizada en el manifiesto de candidato.

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

- MINOR DH-20261111-CRM-LEAD-INSTITUTIONAL-087: sincroniza versión global del ecosistema para habilitar Castro Fallas como vendedor institucional de prospectos con CRM 1.17.0 y Web 1.29.0.
- Manifiesto conserva las versiones de los demás microservicios, las políticas de permisos, contratos REST/SignalR y gates de CI/staging. Producción no autorizada.

## [1.27.1] - 2026-11-11

- PATCH DH-20261111-CRM-AGREEMENT-LIST-085: registra la exclusión y restauración de compromisos derivados de acuerdos en DholeWeb 1.27.1 con versión global DholeSystem 1.27.1.
- Conserva texto histórico, APIs REST, infraestructura realtime y versiones de otros 14 servicios. CI y staging pendientes; producción no autorizada.

## [1.27.0] - 2026-11-11

- MINOR DH-20261111-CRM-PROCEDURE-ATTACHMENTS-085: manifiesto global de adjuntos para procedimientos específicos de clientes; actualiza DholeCRMService 1.15.0 y DholeWeb 1.27.0, preservando las otras 13 versiones de servicios y Gateway.
- Permisos de cuenta aplicados a adjuntos, carga múltiple, vista previa y reintento. Interfaces REST/SignalR compatibles y Dhole Storage reutilizado. CI/staging pendientes y producción no autorizada.

## [1.25.3] - 2026-11-11

- PATCH DH-20261111-CRM-WORKSPACE-TABS-084: sincroniza el manifiesto global con la corrección de pestañas de Prospectos, Actividades y Seguimientos ya integrada en DholeWeb master 1.25.1 (commit 7396cb4e). Respeta las publicaciones anteriores y mantiene versiones independientes de los 16 componentes.
- Infraestructura realtime y contratos REST sin cambios. La integración master de Web está autorizada; pruebas de staging del flujo completo por verificar.

## [1.25.2] - 2026-11-11

- PATCH DH-20261111-PRICING-OPENING-ATTACHMENTS-084: agrega al manifiesto global Pricing 1.10.1, Notifications 1.6.1 y System 1.25.2, conservando el release paralelo CRM Workspace 1.25.1 y demás componentes.
- La apertura adjunta PDF comercial, soportes de todas las solicitudes vinculadas y documentos finales de la QUO, sin duplicados; CI de Pricing/Notifications y gates de versión aprobados. Validación de correo real en staging pendiente; producción no autorizada.

## [1.25.1] - 2026-11-11

- PATCH DH-20261111-CRM-WORKSPACE-TABS-084: registra DholeWeb 1.25.1 (pestañas unificadas de Prospectos, Actividades y Seguimientos) y DholeSystem 1.25.1 en el manifiesto del ecosistema; mantiene sin incrementos los otros 14 componentes.
- Corrección exclusivamente frontend, sin cambios en contratos REST/SignalR. Compilación, CI y staging pendientes; producción no autorizada.

## [1.25.0] - 2026-11-10

- MINOR DH-20261110-CRM-LEAD-DUPLICATE-083: actualiza manifiesto global de los 16 componentes y versiones individuales de CRM 1.13.0, Web 1.25.0, Notifications 1.6.0 y System 1.25.0, preservando los demás servicios.
- Protección de duplicados al crear prospectos, aviso inmediato con vendedor asignado y notificación de sistema. CI y staging requeridos antes de promoción a producción.

## [1.24.0] - 2026-11-10

- MINOR DH-20261110-CRM-ACCOUNT-CATEGORY-SCOPE-082: Release global coordinado de Auth 1.8.0, CRM 1.12.0, Web 1.24.0 y System 1.24.0, preservando todos los demás servicios.
- CI y staging pendientes; no se autorizó despliegue a producción.

## [1.23.0] - 2026-11-10

- MINOR DH-20261110-CRM-LEAD-QUO-PARITY-082: coordina Web 1.23.0 / Pricing 1.10.0 / System 1.23.0 para QUO reales de prospectos, indicadores y reconciliación administrativa de QUO históricas.
- Preserva el release de procedimientos de cuentas 1.22.0, sin cambios de esquema, Framework, API Gateway ni SignalR.

## [1.22.0] - 2026-11-10

- MINOR DH-20261110-CRM-ACCOUNT-PROCEDURES-080: manifiesto coordinado de CRM 1.11.0 y Web 1.22.0 para múltiples procedimientos específicos en cuentas.
- Incluye esquema aditivo, CRUD autorizado, interfaz expandible y reutilización de realtime CRM. CI y staging pendientes; producción no autorizada.

## [1.21.0] - 2026-11-10

- MINOR DH-20261110-CRM-CONTACTS-SELLERS-078: coordina Web 1.21.0, Auth 1.7.0, CRM 1.10.0 con multiselección de contactos y roles comerciales.
- Preserva el release de prospectos 079 y funcionalidades anteriores. Sin cambios de esquema.

## [1.20.2] - 2026-11-10

- PATCH DH-20261110-CRM-LEAD-PARITY-079: versiona el manifiesto DholeWeb y DholeSystem 1.20.2 para la vista de Prospectos (Ficha, Historial de rutas, KPI cotizaciones vinculadas), preservando el release 078 de CRM.
- Contratos REST y SignalR intactos; pruebas CI y staging obligatorias antes de master. Sin despliegue autorizado.

## [1.20.1] - 2026-11-10

- PATCH DH-20261110-CRM-SELLERS-COMMITMENTS-078: coordina DholeAuthService (filtro de vendedores activos), DholeCRMService (asignación y cierre seguro de compromisos) y DholeWeb (selector y checkboxes).
- Registra versiones de cada componente y mantiene infraestructura realtime REST/SignalR, sin modificar los contratos existentes. CI, staging y producción pendientes.

## [1.20.0] - 2026-11-10

- MINOR DH-20261110-CRM-AGENDA-UNIFIED-077: la actividad principal permite completar los compromisos vinculados desde el calendario. Mantiene la implementación consolidada 076 de agendas globales CRM, participantes, minutas, permisos y sincronización.
- Coordinado con DholeWeb 1.20.0; DholeCRMService 1.9.2 y DholeAuthService 1.6.3 sin cambios adicionales. Compilación y staging pendientes.

## [1.19.5] - 2026-11-10

- PATCH DH-20261110-CRM-GLOBAL-AGENDAS-076: coordina DholeAuthService, DholeCRMService y DholeWeb para consultar agendas de otros vendedores y crear actividades con crm.activity.read-all o ambos permisos crm.account.read-all y crm.lead.read-all.
- Registra las versiones independientes y commits candidatos; no modifica los contratos REST ni la infraestructura realtime existente. CI/staging pendientes y producción no autorizada.

# Changelog

## [1.19.4] - 2026-11-10

- PATCH DH-20261110-CRM-HISTORICAL-ACTIVITIES-075: incorpora DholeWeb 1.19.4 y DholeCRMService 1.9.1 para guardar actividades CRM en fechas pasadas como completadas, sin alterar recordatorios futuros ni enviar avisos retroactivos.
- Conserva releases previos, especialmente DholeWeb 1.19.3 y DholeSystem 1.19.2; sin migración ni cambio al framework o SignalR.

## [1.19.2] - 2026-11-10

- PATCH DH-20261110-PRICING-CRM-SELLER-MODIFICATION-075: manifiesto coordinado DholeWeb/DholeSystem 1.19.2 para cubrir prospectos CRM en solicitudes de modificación de vendedores. Los otros servicios retienen versiones; sin cambios de contratos, SignalR ni migraciones.
- Se requiere validación CI y staging antes de promover el mismo hotfix a master.

## [1.19.1] - 2026-11-10

- PATCH DH-20261110-PRICING-CRM-LEAD-REQUESTS-074: corrección coordinada del ejecutivo comercial CRM para solicitudes normales/editadas y modificaciones de QUO con cuentas y prospectos. Versiona DholeWeb y DholeSystem 1.19.1; mantiene los demás servicios. Incluye validación por ID de CRM antes del envío para registros de prospectos históricos.
- Ramas intermedias y CI/staging pendientes, sin cambio de contratos REST, infraestructura SignalR ni migraciones; no desplegar producción sin autorización.

## [1.19.0] - 2026-11-10

- MINOR DH-20261110-CRM-AGENDA-RECONCILED-070: manifiesto centralizado de agenda comercial y compromisos vinculados. Versiones coordinadas DholeWeb 1.19.0, DholeCRMService 1.9.0 y DholeSystem 1.19.0.
- Conserva todos los cambios de Pricing y CRM de 1.18.2 y la infraestructura de realtime sin activar producción. CI/staging pendientes.

## [1.18.2] - 2026-11-10

- PATCH DH-20261110-PRICING-MODIFICATION-CRM-OWNER-072: manifiesto del ecosistema Dhole y DholeSystem 1.18.2 para la corrección del ejecutivo comercial CRM en modificaciones de Pricing. DholeWeb 1.18.2; los otros 14 componentes no modificados conservan su versión.
- Candidato intermedio para develop, validación CI/staging pendiente y posterior promoción coordinada. Sin modificaciones de datos, contratos REST o SignalR, y sin desplegar producción.

## [1.18.1] - 2026-11-10

- PATCH DH-20261110-CRM-ADMIN-CALENDAR-NAV-071: actualiza navegación de DholeWeb a 1.18.1 para mostrar Actividades y Seguimientos a todos los administradores de Auth. Respeta la autorización servidor de agenda completa del release 1.18.0, los permisos de lectura/escritura, Auth y CRM existentes.
- DholeSystem 1.18.1, resto de servicios sin cambio de versión; CI y staging pendientes.

## [1.18.0] - 2026-11-10

- MINOR DH-20261110-CRM-ADMIN-CALENDAR-069: administradores autorizados por Auth acceden a agendas de todos los vendedores y ven los seguimientos creados por políticas, con asunto, fechas, política e historial. Versiones Auth 1.6.0, CRM 1.8.0 y Web/System 1.18.0.
- Sin migraciones ni cambios de infraestructura SignalR; CI y staging pendientes; no hay despliegue a producción.

## [1.17.13] - 2026-11-10

- PATCH DH-20261110-CRM-HIDE-TARIFARIO-067: manifiesto global preparado para DholePricingService 1.9.11 y DholeSystem 1.17.13. Las cotizaciones pendientes en CRM no muestran nombres históricos con «TARIFARIO»; conteo, paginación y selección masiva se filtran desde Pricing antes de paginar.
- Sin cambio en datos persistidos, cotizaciones ya vinculadas, DholeWeb ni CustomCodeFramework; integración y staging pendientes antes de producción.

## [1.17.12] - 2026-11-10

- PATCH DH-20261110-PRICING-CRM-REQUEST-IDENTITY-067: versión de ecosistema 1.17.12. Las solicitudes normales y de modificación recuperan identidad comercial CRM desde sus cuentas, mantienen vendedor y compatibilidad histórica. Componentes Web 1.17.12, Pricing 1.9.10, CRM 1.7.5.
- Coordinación de ramas intermedias; CI y staging pendientes. Sin despliegue autorizado a producción ni cambios en CustomCodeFramework.

## [1.17.11] - 2026-11-10

- PATCH DH-20261110-CRM-ACTIVITY-FULL-DETAIL-066: DholeWeb 1.17.11, DholeCRMService 1.7.4 y DholeSystem 1.17.11 muestran el detalle completo de actividades, sus notas, compromisos y actividad principal vinculada. API únicamente de lectura, sin migración y con controles de acceso existentes.
- Mantiene el manifiesto de los demás servicios sin cambios; CI y staging pendientes, sin despliegue a producción.

## [1.17.10] - 2026-11-10

- PATCH DH-20261110-CRM-AGENDA-CLIENT-EXECUTIVE-065: manifiesto global sincronizado con DholeWeb 1.17.10 para las columnas Cliente y Ejecutivo comercial en Agenda y seguimientos.
- Se preserva el release CRM de búsqueda por cédula 1.17.9, las versiones de los 14 servicios restantes y la identidad `rt-20261107-01` usada por el control realtime de staging. Sin cambios de infraestructura ni código de negocio.

## [1.17.9] - 2026-11-10

- PATCH DH-20261110-CRM-ACCOUNT-SEARCH-064: incorpora búsqueda por cédula en el listado de cuentas CRM, conservando alcance por usuario, filtros y paginación. Identificación normalizada o histórica, con o sin formato.
- Versión global DholeSystem 1.17.9; DholeWeb 1.17.9; DholeCRMService 1.7.3. Release en ramas intermedias con CI y staging pendientes; no autoriza producción.


## [1.17.8] - 2026-11-10

- PATCH DH-20261110-CRM-QUO-STATUS-061: actualización coordinada del manifiesto global a 1.17.8 tras integrar los releases 1.17.6 y 1.17.7 del frontend. Se conserva su funcionalidad de solicitudes FCL con múltiples POE y se incorporan las etiquetas de estado de QUO en CRM.
- DholeWeb 1.17.8 y DholeSystem 1.17.8; los demás componentes mantienen sus versiones actuales, sin cambios de datos, APIs o framework.

## [1.17.5] - 2026-11-10

- PATCH DH-20261110-CRM-QUO-STATUS-061: traducción de estados comerciales de las QUO vinculadas en las vistas CRM, reutilizando la presentación estándar de Pricing sin cambiar enum, datos históricos ni cálculos.
- Versión del ecosistema 1.17.5: DholeWeb 1.17.5, DholeSystem 1.17.5; restantes 14 componentes sin cambios. Regresión de traducciones y preservación de estados.

## [1.17.3] - 2026-11-10

- PATCH DH-20261110-PRICING-CRM-EXECUTIVE-059: release global sincronizado para corregir el guardado de cotizaciones SPOT/tarifarios cuando la cuenta CRM ya tiene ejecutivo comercial asignado. DholeWeb 1.17.3 envía el Auth userId que DholePricingService 1.9.5 exige junto al nombre.
- Registro coordinado de versiones, pruebas y revisión en staging; no se modifica framework, infraestructura realtime ni esquema. La promoción a master ejecutaría despliegue a producción y requiere autorización separada.

## [1.17.2] - 2026-11-10

- PATCH DH-20261110-CRM-QUO-SUPERADMIN-058: formulario de vinculación de QUO históricas colapsable, oculto a perfiles ordinarios y protegido por autorización de superadministración en Pricing.
- Release coordinado DholeWeb 1.17.2, DholePricingService 1.9.4 y DholeSystem 1.17.2. No se cambia el framework ni se introducen migraciones de datos.

## [1.17.1] - 2026-11-10

- PATCH DH-20261110-CRM-QUO-LIVE-057: indicadores y rutas del CRM toman las QUO asociadas por ID a Pricing, la lista muestra pendientes reales y permite selección múltiple en filtros paginados.
- Release coordinado DholeWeb 1.17.1, DholePricingService 1.9.3, DholeSystem 1.17.1; preserva infraestructura realtime y no modifica CustomCodeFramework.

## [1.17.0] - 2026-11-09 (candidate, RT crítico Auth/Notifications)

- MINOR: release candidato DH-20261109-RT-CRITICAL-056. El NotificationsHub existente recibe eventos de seguridad del Auth Outbox para expulsión de sesión individual o usuario bloqueado y refresco de permisos en el navegador; sin nuevo hub ni cambio de framework.
- Manifest y componentes: DholeSystem 1.17.0, DholeAuthService 1.5.0, DholeNotificationsService 1.5.0, DholeWeb 1.17.0. CRM, Pricing, Config y Gateway siguen sin cambio de código; su realtime existente debe verificarse funcionalmente por pantalla.
- Pendiente CI, pruebas WSS autenticado con dos sesiones, cobertura funcional de CRM/Pricing/Config, reconciliación y auditoría staging. develop/master y producción no integrados por este candidato.


## [1.16.2] - 2026-11-09

- PATCH DH-20261109-CRM-QUO-LINK-SYNC-056: sincronización de identidad de cuentas y ejecutivos CRM en las tarifas QUO y exclusión de cotizaciones ya vinculadas del listado de migración.
- Coordinación DholeWeb 1.16.1 / DholePricingService 1.9.2 / DholeSystem 1.16.2; sin cambios de esquema o framework. CI y staging obligatorios antes de master.

## [1.16.1] - 2026-11-09

- PATCH: coordinated CRM 1.7.2 and Pricing 1.9.1 owner ACL endpoints for collection-level realtime subscriptions to accounts, leads, rates and costs through existing NotificationsHub.
- Publish sanitized list invalidations in transactional Outbox on CRM account/lead and Pricing rate/cost writes. Staging deploy workflows now load the current DholeSystem/develop Compose to avoid stale or production flags; no changes to CustomCodeFramework.
- Preserves concurrent release 1.16.0. Version manifest covers all 16 components; client cross-user acceptance and module-wide coverage remain pending. Master/production untouched.


## [1.16.0] - 2026-11-09

- MINOR: catálogo completo de QUO históricas consultable desde el CRM, con vinculación verificada a cuentas existentes y separación estricta de clientes ya asociados.
- Release coordinado DH-20261109-CRM-LEGACY-QUO-CATALOG-055: DholeWeb 1.16.0, DholePricingService 1.9.0; demás componentes sin cambios. Staging y pruebas obligatorios antes de promoción a master.

## [1.15.4] - 2026-11-09

- PATCH: paired with DholeWeb 1.15.3 to restore bounded owner REST reconciliation while the NotificationsHub WebSocket is connected, covering missed/reordered catalog, costs, rate and CRM invalidations without overwriting dirty forms.
- The read-only staging runtime audit now records sanitized Redis Config consumer-group pending/lag counters. The previous audit confirmed the public JS bundle and staging bundle match, both anonymous negotiate paths return 401, all required Config/Notifications feature flags are active, and the Notifications consumer group exists.
- Production/master unchanged. Connected cross-user realtime delivery requires authenticated browser acceptance, not inferred from infrastructure checks.


## [1.15.3] - 2026-11-09

- PATCH: read-only staging audit checks public Dhole domain against actual staging frontend bundle, both HTTP SignalR negotiate routes, container realtime flags and Notifications consumer group in the staging Redis stream. Exposes configuration and route mismatches without printing credentials, tokens, payloads or database rows.
- No framework, production/master, live data or feature-flag changes. Full two-user functional realtime acceptance still required.


## [1.15.2] - 2026-11-09

- PATCH: staging-only NotificationsHub catalog-list realtime pilot. Enable Config transactional outbox, Notifications resource host and browser catalog refresh in staging Compose; preserve production fail-closed feature flags.
- Coordinated DholeConfigService 1.4.1, DholeNotificationsService 1.4.1, DholeWeb 1.15.2, DholeSystem 1.15.2; no framework changes. Two-user WSS functional validation remains pending.


## [1.15.1] - 2026-11-09 (Seller Open decision)

- PATCH DH-20261109-SELLER-OPEN-DECISION-054: Web 1.15.1 y PricingService 1.8.1 habilitan Aceptar/Rechazar sobre cotizaciones Abiertas con revisión publicada, validando permisos, aprobación y ausencia de trabajo activo en Pricing.
- No se publican borradores ni PDFs no enviados. Realtime y sus gates permanecen sin cambios.

## [1.15.0] - 2026-11-09

- Release coordinado de selección CRM y conciliación manual de QUO anteriores.

## [1.14.4] - 2026-11-09 (QUO-269 seller workflow status)

- Coordinated PATCH DH-20261109-QUO269-SELLER-STATUS-053 (develop): PricingService 1.7.2 and Web 1.14.4 display the current Open workflow state in Sales for already-completed QUO-269 without exposing unpublished quote data. The last published commercial snapshot remains unchanged.
- Manifest and global ecosystem version 1.14.4; existing NotificationsHub, F6-F9, ACL and production safety boundaries are preserved.

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
