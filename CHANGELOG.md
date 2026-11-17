## [1.69.2] - 2026-11-17 (DH-187 · Operations esquema propio y mensajería framework)

- PATCH coordinado sobre DH-186 SRM (1.69.1): registra Operations 0.4.1 y respeta todas las versiones y configuraciones del release SRM simultáneo.
- DholeOperationsService migra sus 18 tablas de public al esquema operations sin pérdida de información y aplica las entidades y mapeos Inbox/Outbox del mismo CustomCodeFramework que usa DholeConfigService.
- PostgreSQL conserva los eventos, índices y claves foráneas; las pruebas de migración de datos heredados aprobaron 4 tests unitarios y 6 integraciones. No se autoriza producción sin validar staging.

## [1.69.1] - 2026-11-17 (DH-186 · SRM: selects de crédito e IBAN)

- PATCH coordinado: DholeWeb 1.66.0 → 1.66.1; DholeSystem/ecosistema 1.69.0 → 1.69.1. Los otros componentes conservan su versión registrada.
- Los selects de cobertura de crédito no se superponen con campos posteriores. Las cuentas bancarias explican la causa de un IBAN inválido sin omitir checksum MOD-97, cambiar contratos REST/realtime o permisos.
- Candidato de release desde ramas intermedias; CI, pruebas en staging y autorización explícita antes de producción.

## [1.69.0] - 2026-11-17 (DH-185 · Primeras tablas de Operations)

- MINOR: seis nuevas tablas de Operations para cotizaciones, costos y proveedores vinculados, hitos, tareas, notas y auditoría. PostgreSQL migra de forma aditiva y transaccional.
- Se conservan 12 tablas existentes con sus registros; tests de PostgreSQL e inspección SQL en cada despliegue exigen 18 tablas y la migración DH-185 aplicada.
- DholeOperationsService 0.3.1 → 0.4.0; DholeSystem/ecosistema 1.68.0 → 1.69.0; sin modificar otras versiones.
- No se afirma sincronización de costos con Pricing hasta integrar el procesamiento de eventos y validaciones.

## [1.68.0] - 2026-11-17 (DH-184 · Gateway Operations, estados y base de datos)

- MINOR: integración de DholeOperationsService con API Gateway `/api/operations` y Hub SignalR `/hubs/operations`; health `/api/health/operations` comprueba PostgreSQL/Redis por `/ready`.
- Estado técnico Operations visible en DholeWeb con versión real, registro, HTTP, latencia y actualización manual.
- Variables OPERATIONS_DB/HTTP/GRPC en las copias de runtime staging/producción; los workflows de Operations aseguran `dhole_operations` idempotentemente en su PostgreSQL correspondiente.
- Release coordinado: DholeApiGateway 1.11.0, DholeWeb 1.66.0, DholeOperationsService 0.3.1, DholeSystem/ecosistema 1.68.0.

## [1.67.0] - 2026-11-16 (Operations backend · núcleo de expedientes, pool, SignalR y documentos · DH-183)

- MINOR: DholeOperationsService 0.2.0 → 0.3.0, DholeSystem/ecosistema 1.66.3 → 1.67.0; otros componentes conservan sus versiones.
- Creación manual de expediente y consecutivo IDTRA con PostgreSQL transaccional; pool multiempresa con asignación ponderada, reglas de modalidad/ruta, concurrencia y primer estado Aperturas.
- Metadatos de documentos y trabajos de extracción enlazados a Storage; DataExtraction/AI asíncrono sin completar hasta definir contrato interno autenticado.
- SignalR restringido a grupos por expediente autorizado, replay REST saneado y migración compatible Outbox/Inbox; no publicación de datos comerciales.
- Rama intermedia y PR a develop; CI, pruebas de regresión, migración y validación de staging pendientes. Sin autorización de despliegue a producción.
## [1.66.3] - 2026-11-16 (SRM: resiliencia de Hacienda y footer sin superposición · DH-182)

- PATCH coordinado DH-20261116-SRM-HACIENDA-182: DholeWeb 1.65.2 → 1.65.3; DholeSystem/ecosistema 1.66.2 → 1.66.3. Versiones de Config y demás servicios se conservan.
- SRM soporta un reintento único de errores de transporte, mensajes sin rutas ni identificaciones, no reintenta errores de autorización o límites; formulario de proveedores mantiene sus campos visibles con acciones fuera del scroll del drawer.
- Sin cambios en API, scopes, credenciales bancarias, realtime o contratos REST. CI, pruebas en staging y autorización expresa de producción requeridas.

## [1.66.2] - 2026-11-16 (SRM: validación IBAN por país · DH-181)

- PATCH coordinado DH-20261116-SRM-IBAN-181: DholeWeb 1.65.1 → 1.65.2, DholeConfigService 1.8.0 → 1.8.1 y DholeSystem/ecosistema 1.66.1 → 1.66.2; los demás microservicios mantienen sus versiones.
- SRM: prefijo del país del banco, límite ISO 13616, contador y checksum MOD-97; cuentas nacionales de países no adheridos sin prefijos ficticios. Pruebas unitarias y formularios de alta/edición.
- Candidatos intermedios para develop/master; CI, build y staging pendientes antes de integración master o despliegue a producción.

## [1.66.1] - 2026-11-16 (Multimodal Panamá: sobrepeso calculado por excedente · DH-180)

- PATCH coordinado DH-20261116-PRICING-PANAMA-OVERWEIGHT-180: DholeWeb 1.65.0 → 1.65.1; DholeSystem y ecosistema 1.66.0 → 1.66.1; sin cambios de contrato en Pricing/REST/SignalR.
- El umbral FCL Panamá → Costa Rica es 19.000 kg por contenedor y solo el exceso se valora mediante los cuatro costos maestros de LTL Panamá → Costa Rica: Flete Terrestre, Bunker, Gastos y Custodia + Marchamo.
- Validación de pesos y cargos, eliminación de duplicados, fail-closed con catálogos incompletos. Candidatos intermedios para develop/master; CI y staging pendientes; no desplegar a producción sin autorización.

## [1.66.0] - 2026-11-16 · CRM/SRM y Hacienda unificados (DH-179 master candidate)

- MINOR coordinado: Web 1.65.0, DholeSystem 1.66.0. Pestañas horizontales funcionales SRM para alta y edición de CRM, manteniendo contactos, direcciones, perfil comercial y permisos de crédito.
- Hacienda automática en CRM: cédula CR válida consulta/actualiza nombre y tipo, permite reconsulta, evita respuesta antigua y se sincroniza antes del guardado.
- Backport selectivo preservando cambios preexistentes de producción. Integración master y despliegue a producción pendientes de autorización expresa.

## [1.65.0] - 2026-11-16 · SRM/Hacienda como CRM (DH-178 master candidate)

- MINOR: Backport Web 1.64.0 y System 1.65.0; formulario por pestañas y actualización automática de razón social/actividad al consultar Hacienda de Costa Rica.
- Manejo de respuestas obsoletas, guardado sin perder verificación y continuidad de scopes de cuentas bancarias. No hay cambios en Config/Auth.
- Staging, CI sobre master y autorización expresa de despliegue necesarios; sin promoción automática desde esta rama.

## [1.64.1] - 2026-11-16 (CRM: estado de actividad sincronizado tras finalizar)

- PATCH DH-20261116-CRM-COMPLETION-STATE-SYNC-177: DholeWeb 1.63.1 verifica en CRM el estado real de la actividad después de un error en POST y al recuperar foco de la pestaña; limpia alertas obsoletas únicamente cuando el GET confirma finalización, y muestra fecha real, tipo de gestión legible y verificación manual.
- Se preservan condiciones y validaciones de DholeCRMService, permisos, historial, recordatorios y realtime. Ecosistema Dhole 1.64.0 → 1.64.1; CI y validación multiusuario en staging antes de promover master.


## [1.64.0] - 2026-11-16 · SRM proveedores / Hacienda / cuentas bancarias seguras (DH-176 master)

- MINOR: Auth 1.13.0, Config 1.8.0, Web 1.63.0 y DholeSystem 1.64.0 por backport selectivo del release de proveedores a master.
- Perfiles UPPER CASE, teléfono, RUC/NIT, dirección, actividad económica, contacto Finanzas, observaciones y Hacienda Costa Rica.
- Cuentas bancarias separadas, cifradas AES-256-GCM y autorizadas por nuevos scopes. Requiere variable de cifrado persistente `DHOLE_SRM_BANK_KEY_BASE64` antes de operar cuentas.
- Autorización expresa del usuario para producción recibida el 16 de noviembre de 2026; validación de lectura/escritura bancaria y smoke de Hacienda pendientes.

## [1.63.10] - 2026-11-16 (Completar actividad comercial desde seguimiento y visita)

- PATCH DH-20261116-CRM-ACTIVITY-COMPLETE-175: Web 1.62.8 muestra códigos activos del catálogo Config para el resultado de completar y delega al backend CRM el timestamp de ocurrencia; CRM acepta la fecha real opcional y normaliza Completed a COMPLETED si ese resultado está activo.
- Actualización de CRM master a 1.33.1 (manifiesto anterior referenciaba 1.33.0 aunque master compilaba 1.32.0) y develop a 1.34.1. DholeSystem/ecosistema 1.63.9 → 1.63.10. Pruebas de regresión y compatibilidad REST/SignalR, validar staging antes de promover a producción.

## [1.63.9] - 2026-11-16 (Bitácoras CRM: hora real UTC del servidor)

- PATCH DH-20261116-CRM-BITACORA-SERVER-CLOCK-174: Web 1.62.6 → 1.62.7 deja el timestamp de realización al servidor CRM al guardar bitácoras y actividades históricas para evitar fallos por relojes de usuarios adelantados.
- Preserva acuerdos futuros, notificaciones, perfiles de vendedor y realtime sin cambios de contratos. DholeSystem/ecosistema 1.63.8 → 1.63.9. Validar CI, staging y autorización para producción.

## [1.63.8] - 2026-11-16 (Cliente/prospecto visible al editar o recargar QUO)

- PATCH DH-20261116-PRICING-CRM-EDIT-HYDRATION-173: DholeWeb 1.62.5 → 1.62.6 preserva en el selector comercial el nombre histórico de una QUO sin vínculo CRM e indica que debe seleccionarse explícitamente la cuenta o prospecto, sin asignar identidades por similitud.
- Las QUO vinculadas siguen resolviendo su cliente y ejecutivo en CRM mediante ClientAccountId/ClientLeadId y permisos existentes. No se modifican los contratos REST, bases de datos, scopes, costos ni eventos SignalR.
- DholeSystem/ecosistema 1.63.7 → 1.63.8. Prueba de regresión, compilación, CI, staging y aprobación de producción requeridos antes de master.

## [1.63.7] - 2026-11-16 (CBM por cotización vinculada a consolidado LCL propio)

- PATCH DH-20261116-OWN-LCL-QUO-CBM-172: Pricing 1.22.1 → 1.22.2 amplía el contrato de QUOs vinculadas con CBM físicos y cobrables; Web 1.62.4 → 1.62.5 los presenta por QUO en el consolidado sin modificar costos, estados ni permisos.
- DholeSystem/ecosistema 1.63.6 → 1.63.7; cambios solo de lectura, sin migración ni cambios realtime. Requiere pruebas, CI, compilación, staging y autorización expresa antes de promoción a master.

## [1.63.6] - 2026-11-16 (Creación de seguimientos desde clientes y prospectos)

- PATCH DH-20261116-CRM-FOLLOWUPS-CREATE-171: DholeWeb 1.62.3 → 1.62.4 y DholeSystem/ecosistema 1.63.5 → 1.63.6. Historial CRM permite crear un seguimiento comercial desde la cuenta o el prospecto, reutilizando el formulario existente con vínculo y responsable precargados.
- Sin cambios en backend, endpoints REST, SignalR, estructura de datos ni scopes. Pruebas de regresión, compilación, CI y validación de staging obligatorias antes de promocionar el mismo release a master; desplegar producción no está autorizado.

## [1.63.5] - 2026-11-16 (Modales CRM responsivos y recuperación de borrador)

- PATCH DH-20261116-CRM-MOBILE-MODALS-170: DholeWeb 1.62.3 y DholeSystem/global 1.63.5. Modal de actividad y recuperación de borrador con superficies opacas, fondo prioritario más oscuro y acciones responsivas para móviles. Preserva mejoras de pantallas CRM/Configuración de 1.63.4.
- No se modifica API REST, SignalR, permisos ni servicios backend. El release requiere CI, compilación, validación de staging y promoción de la misma corrección a master. El usuario autorizó explícitamente producción el 2026-11-16, condicionado a las validaciones obligatorias.

## [1.63.4] - 2026-11-16 (Responsive móvil: Configuración y CRM)

- PATCH DH-20261116-MOBILE-CRM-SETTINGS-169: DholeWeb 1.62.2 adapta las tarjetas de Configuración, las pestañas de Clientes/Prospectos y las vistas de Agenda a móviles sin romper el diseño de escritorio.
- El calendario comercial inicia en modo lista en teléfonos; el modo mensual de siete columnas conserva la visualización de rangos y permite desplazamiento horizontal. Encabezados y acciones ya no ocupan espacios superpuestos en pantallas pequeñas.
- DholeSystem/global 1.63.4; release coordinado exclusivamente entre Web y System. Sin cambios en contratos REST, SignalR, servicios backend ni permisos. Pruebas, compilación, inspección visual en móvil y staging pendientes. Master y producción sin autorización de despliegue.

## [1.63.3] - 2026-11-16 (Gateway DNS checkout deployment hardening)

- PATCH DH-20261116-GATEWAY-DEPLOY-DNS-168: Gateway 1.10.3 incorpora reintentos limitados para obtener DholeSystem desde los workflows develop y master, manteniendo ramas y definiciones de despliegue correctas.
- Requiere clones completos y validados; nunca utiliza infraestructura obsoleta para continuar y emite diagnóstico de DNS persistente. DholeSystem/global 1.63.3, manifiesto coordinado sin nuevas capacidades ni migraciones.
- Verificación CI y staging del release antes de producción.

## [1.63.2] - 2026-11-16 (Publicación segura de solicitudes externas)

- PATCH DH-20261116-API-PRICING-IDENTITY-167: DholeApiGateway 1.10.2 emite JWT de propósito limitado para POST Solicitar tarifa y DholePricingService 1.22.1 valida el vendedor fijo de contrato o el ejecutivo institucional Castro Fallas.
- Se mantienen Auth, API Keys, scopes, idempotencia, outbox y auditoría sin flags ni credenciales en Git.
- DholeSystem y ecosistema 1.63.2; release coordinado con CI y verificación de staging antes de promoción a producción.

## [1.63.1] - 2026-11-16 (API Manager: clientes, prospectos y vendedor Castro Fallas)

- PATCH DH-20261116-API-CRM-166: Web 1.62.1 selecciona cuentas o prospectos del directorio comercial unificado de CRM y conserva la distinción institucional.
- Gateway 1.10.1 permite omitir sellerUserId: Pricing utiliza la identidad técnica autenticada como actor operativo; el ejecutivo comercial se mantiene como Castro Fallas. No se utilizan GUID ficticios.
- DholeSystem/global 1.63.1, manifiesto coordinado y CI/staging obligatorios antes de producción.

## [1.63.0] - 2026-11-16 (API Manager: descubrimiento y valores predeterminados)

- MINOR DH-20261116-API-MANAGER-165: Dhole global 1.63.0; Gateway 1.10.0, Web 1.62.0 y System 1.63.0.
- Permite almacenar campos fijos en APIs POST/PUT/PATCH y seleccionar una cuenta real de CRM con su ejecutivo para solicitud de tarifas. El consumidor no puede reemplazar los valores bloqueados.
- Agrega fallback de rutas aprobadas cuando el inventario remoto no responde; conserva controles de credenciales y API Keys. CI, pruebas y staging previos a producción.

## [1.62.1] - 2026-11-16 (API Manager: edición y publicación segura)

- PATCH DH-20261116-API-MANAGER-164: global 1.62.1, Gateway 1.9.1, Web 1.61.1 y System 1.62.1. Otros componentes conservan sus versiones previas.
- Soluciona la edición de APIs guardadas y habilita identidad técnica de lectura exclusiva para catálogos Config, sin superadmin ni publicación automática.
- Release coordinado mediante CI y staging antes de integración a producción.

## [1.62.0] - 2026-11-16 (Scopes propios LCL Create/Update/View)

- MINOR DH-20261116-OWN-LCL-SCOPES-163: global 1.62.0, Auth 1.11.0, Pricing 1.21.0, Web 1.61.0. Registro idempotente de permisos y validación por operación, sin flags.
- Consolidados LCL propios permiten visualizar, crear o editar según scopes explícitos. Se mantiene lectura desde el wizard mediante pricing.rate.view y consulta de QUOs vinculadas.
- CI y staging obligatorios; manifiesto centralizado actualizado.

## [1.61.0] - 2026-11-16 (QUOs por consolidado LCL propio)

- MINOR DH-20261116-OWN-LCL-QUOS-162: versión global de Pricing 1.20.0, Web 1.60.0 y System 1.61.0.
- Consolidados LCL propios muestran cotizaciones vinculadas con la referencia guardada, fechas, clientes y estados, y acceso de solo lectura a cada QUO.
- API REST compatible, sin cambiar consumos CBM, eventos existentes ni cotizaciones. CI y staging obligatorios antes de master/producción.

## [1.60.1] - 2026-11-15 (Patch CI/CD rápido y seguro)

- PATCH DH-20261115-DEPLOY-FASTPATH-146: AI y DataExtraction eliminan restauraciones .NET y regresiones repetidas durante producción; PR ejecuta compilación, tests y versionamiento.
- Deploy master comprueba revisión actual y evita ejecutar revisiones obsoletas; se elimina la eliminación automática de ramas en DataExtraction.
- Infraestructura de staging y producción sólo se redespliega automáticamente si cambia deploy/**; release-manifest/version.json/CHANGELOG no reinician servicios existentes.
- Versions AI 1.8.1, DataExtraction 1.8.1, DholeSystem/global 1.60.1; staging y CI antes de master.

## [1.60.0] - 2026-11-15 (Centro de colas de extracción e IA)

- MINOR: release global DH-20261115-QUEUE-CONTROL-145 de AI 1.8.0, DataExtraction 1.8.0, Web 1.59.0 y System 1.60.0.
- Cola operativa desde Web: diagnóstico por correo/IA, búsqueda, paginación, leases, tiempos, errores, estado de infraestructura y reintentos seguros.
- Sin modificación de modelo Ollama ni eliminación manual de Redis. CI, staging y validación de permisos pendientes; master/producción no autorizados.

## [1.59.0] - 2026-11-15 (CPU document evidence release candidate)

- MINOR global: coordinación AI 1.7.0 + DataExtraction 1.7.0. Integración de MarkItDown, Tesseract (CPU selectivo) y clasificación documental con evidencia por campo.
- No cambia el modelo actual de Ollama. Añade clasificación conservadora de documentación no tarifaria antes de procesos costosos de AI.
- Manifiesto central 17 repositorios actualizado manteniendo intactas versiones de servicios no modificados.
- CI, staging y benchmark con corpus etiquetado pendientes; el objetivo 99,9% NO está validado. Producción no autorizada.
- Release DH-20261115-CPU-DOC-EVIDENCE-144.

## [1.58.0] - 2026-11-15 (API Manager: metadatos completos y filtros de terminal)

- MINOR DH-20261115-API-METADATA-161: coordina Gateway 1.9.0 y Web/System 1.58.0 para exponer JSON real de Config y filtrar CY, SD y APT por registro.
- Sin migraciones ni flags de Config; conserva APIs existentes, API Keys y autenticación por ruta. CI y staging obligatorios antes de promover producción.

## [1.57.1] - 2026-11-15 (API Manager: eliminar bandera de habilitación)

- PATCH DH-20261115-THIRD-PARTY-404-155: elimina ThirdParty__Enabled=false de la configuración Compose de Gateway para master y develop.
- Mantiene la conexión a dhole_integrations desde variables existentes y los tokens técnicos limitados por ruta; no agrega secretos ni permisos.
- Coordina DholeApiGateway 1.8.1 y DholeWeb 1.57.1 para que el error del API Manager informe almacenamiento no disponible en lugar de HTTP 404.

## [1.56.0] - 2026-11-14 (API Manager universal route discovery)

- MINOR: coordina versiones de los 17 componentes y agrega registro de Operations a Gateway para su inventario REST.
- Mantiene las rutas, Compose y servicios existentes; la exposición a terceros requiere aprobación y token técnico por ruta.

## [1.55.0] - 2026-11-14 (Dhole API Manager coordinated release)

- MINOR: añade la configuración de ocho identidades técnicas de catálogos Config desde develop, sin alterar los demás servicios de producción.
- Integra Gateway 1.6.2 / Web y System 1.55.0, conservando las mejoras CRM/Pricing de 1.54.0 y sus datos.
- La publicación requiere que ThirdParty esté habilitado con token de solo lectura y comprobaciones posteriores al despliegue.

## [1.54.0] - 2026-11-14

- MINOR DH-20261114-CRM-CALENDAR-SPANS-142: calendario de varios días y horas y recordatorios con fecha final (Web 1.53.0 → 1.54.0; CRM 1.31.0 → 1.32.0; DholeSystem/ecosistema 1.53.0 → 1.54.0).
- Manifiesto central actualiza el release coordinado; los demás servicios conservan sus versiones. Migración PostgreSQL aditiva y contratos REST/realtime compatibles. Master bloqueado hasta validar staging y autorización para producción.

## [1.53.0] - 2026-11-14

- MINOR DH-20261114-CRM-RECORD-FOLLOWUPS-142: release coordinado de «Seguimientos» CRM en Prospectos y Clientes, historial consolidado con filtros y enlaces de detalle, cuentas agrupadas y REST/SignalR existentes.
- DholeWeb y DholeSystem 1.52.1 → 1.53.0; CRM 1.31.0 sin cambios. Promoción controlada desde develop con CI, staging y aprobación para producción.

## [1.52.1] - 2026-11-13

- PATCH DH-20261113-PRICING-OWN-LCL-141: master 1.52.0 → 1.52.1, Pricing 1.18.2 y Web 1.52.1. CFS propio LCL usa CBM cobrable (1 CBM mínimo) al guardar y consultar cotizaciones anteriores. Sin afectar coloader, Miami, REST ni realtime.
- Lote coordinado tras CI/staging con ramas intermedias. Historial de revisiones intacto.

## [1.52.0] - 2026-11-13

- MINOR DH-20261113-CRM-BITACORA-DIRECT-TASKS-PARENT-141: bitácoras comerciales crean recordatorios directos de acuerdos con fecha futura, sin botones intermedios. El CRM preserva la relación padre-hija mediante FK `origin_activity_id`, recupera recordatorios heredados y presenta acceso a la bitácora padre en el detalle.
- Versiones coordinadas: DholeWeb 1.52.0, DholeCRMService 1.31.0, DholeSystem/ecosistema 1.52.0; otros componentes sin incremento. CI, versión y staging obligatorios antes de integrar master y publicar producción.

## [1.51.2] - 2026-11-13

- PATCH DH-20261113-PRICING-OWN-LCL-140: Web 1.51.2 y sistema/ecosistema 1.51.2. Corrige cotizaciones LCL propias históricas: CFS por CBM cobrable, recuperación segura del POL comercial chino y recálculo de la recolecta sin pérdida de importes; elimina detalles genéricos ajenos a la matriz al guardar.
- PricingService conserva 1.18.1. Manifiesto y CHANGELOG coordinados, no se alteran otros servicios. Validar CI + staging antes de promover de develop a master; no se modificará main.

## [1.51.1] - 2026-11-13

- PATCH DH-20261113-PRICING-OWN-LCL-139: backport coordinado en master del fix LCL propio, con CFS por CBM cobrable y Manejos persistidos; se evita introducir cargos automáticos fuera del consolidado. Pricing 1.18.1, Web 1.51.1, DholeSystem/ecosistema 1.51.1.
- Sin cambios en main ni degradación de versiones; CI, manifiesto y validación staging obligatorios.

## [1.51.0] - 2026-11-13

- MINOR DH-20261113-CRM-BITACORA-AGREEMENT-TASKS-138: release coordinado de bitácoras editables con tareas opcionales desde acuerdos, recordatorios de seguimientos vinculados, historial de origen y regresión específica en Web y CRM. Web 1.51.0, CRM 1.30.0, sistema/ecosistema 1.51.0; demás componentes conservan versiones vigentes.
- Ramas intermedias por repositorio, CI y validación staging obligatorios antes de promover a master. Producción no autorizada.

## [1.50.0] - 2026-11-13

- MINOR DH-20261113-CRM-SELLER-ACTIVITY-REPORTS-137: manifiesto coordinado de reportes de actividades comerciales CRM (general y por vendedor), indicadores, desglose por tipo, filtros, Excel y PDF. Web 1.50.0, CRM 1.29.0, Sistema/ecosistema 1.50.0; resto de componentes conserva su versión previa por rama.
- CI y staging pendientes; sin autorización para despliegue productivo.

## [1.49.0] - 2026-11-13

- MINOR DH-20261113-CRM-AGENDA-NOTES-FILTERS-136: manifiesto de release coordinado para filtros cliente/vendedor y bitácora de notas independiente en CRM. Versiones: Web 1.49.0, CRM 1.28.4, Sistema/ecosistema 1.49.0; componentes restantes conservan sus versiones previas.
- API REST, SignalR, permisos y operaciones existentes mantienen compatibilidad. CI/staging pendientes; master y producción no autorizados.

## [1.48.4] - 2026-11-13

- PATCH DH-20261113-PRODUCTION-DEPLOY-SKIP-135: registra la corrección coordinada de la condición if en los jobs de producción Auth/CRM/Web; se eliminan los bloqueos por mensaje de commit que marcaban deploy Skipped, sin flags.
- Versiones Auth 1.9.2 → 1.9.3; CRM 1.28.2 → 1.28.3; Web 1.48.3 → 1.48.4; DholeSystem 1.47.5 → 1.48.4; ecosistema → 1.48.4. CI y staging requeridos antes de master. Publicación solicitada por usuario 2026-11-13.

## [1.47.5] - 2026-11-13

- PATCH DH-20261113-CRM-AGENDA-RETURN-132 (backport master): registro global de la corrección «Volver al listado» desde actividades CRM hacia `/crm/followups`, validada previamente en develop Web 1.48.1.
- DholeSystem/ecosistema 1.47.4 → 1.47.5; DholeWeb 1.47.4 → 1.47.5; demás componentes conservan sus versiones. Manifiesto actualizado; sin cambios backend, REST ni SignalR.
- Pruebas de regresión, TypeScript y build Web superaron CI; despliegues de Web e infraestructura en staging exitosos. Promoción a master autorizada expresamente por usuario el 2026-11-13; master aplica este backport aislado sin Bitácora comercial 1.48.0.

## [1.47.4] - 2026-11-13

- PATCH DH-20261113-CRM-DRAFT-RECOVERY-130: manifiesto del release coordinado de recuperación de borradores CRM; mantiene compatibilidad REST, SignalR, Outbox y servicios sin cambios.
- DholeSystem 1.46.3 → 1.47.4, DholeWeb 1.47.3 → 1.47.4, DholeCRMService 1.27.3 → 1.27.4, ecosistema 1.47.3 → 1.47.4. Compilaciones, gates CI y staging pendientes; producción no autorizada.

## [1.46.3] - 2026-11-13

- PATCH DH-20261113-OPERATIONS-NO-FLAGS-128: DholeOperationsService 0.1.1 → 0.1.2 elimina el flag que saltaba deploy de producción.
- DholeSystem/ecosistema 1.46.2 → 1.46.3; manifiesto actualizado sin modificar las versiones de los otros servicios.
- Los pushes a develop/master disparan despliegues automáticamente, sin flags. Validación de CI y staging antes de promover a producción.

## [1.46.2] - 2026-11-12

- PATCH DH-20261112-OPERATIONS-STAGING-127: habilita staging automático de DholeOperationsService en `develop`; Operations 0.1.0 → 0.1.1.
- DholeSystem/ecosistema 1.46.1 → 1.46.2, sin cambiar otros componentes. La producción sigue sujeta a autorización.
- CI validado; readiness del servicio en staging pendiente.

## [1.46.1] - 2026-11-12

- MINOR DH-20261112-OPERATIONS-BOOTSTRAP-126: registra DholeOperationsService v0.1.0 en el manifiesto del ecosistema.
- El servicio sigue la arquitectura y despliegues de DholeConfigService, usando exclusivamente `develop`, `master` y ramas intermedias; no se utiliza `main`.
- DholeSystem/ecosistema 1.44.3 → 1.46.1. Se conservan las versiones de los 16 componentes existentes.
- Compilación y pruebas de Operations CI satisfactorias; provisioning y smoke de staging pendientes. Producción no autorizada.

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

- PATCH DH-20261112-PRICING-TRANSIT-LABEL-122: DholeWeb 1.44.0 → 1.44.1 y DholeSystem/ecosistema 1.44.0 → 1.44.1. Etiqueta unificada «Días de tránsito» en pantalla 6 terrestre, aérea y marítima, sin cambios de contrato, reglas ni datos.
- Manifiesto central sincronizado con la rama master actual. Validaciones CI y staging requeridas.

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

- PATCH DH-20261112-PRICING-LTL-CURRENCY-VALUE-118: release global coordinado con DholeWeb para mostrar Config.currencies.Value en precio, costo y mínimo de las tarifas LTL propias y coloaders, evitando CUR-*.
- DholeSystem/global 1.43.4 → 1.43.5, Web 1.43.3 → 1.43.4, PricingService 1.16.2 sin cambio. CI/staging exitosos y master expresamente autorizado; REST/SignalR compatibles.

## [1.43.4] - 2026-11-12

- PATCH DH-20261112-PRICING-OUTBOX-CORRELATION-115: corrige el error de persistencia Outbox por correlation_id mayor de varchar(100) al reenviar aceptación de QUO-00000-000609.
- DholePricingService 1.16.1 → 1.16.2 y DholeWeb 1.43.2 → 1.43.3. DholeSystem/ecosistema 1.43.3 → 1.43.4. No se modifican el framework ni el esquema de PostgreSQL.
- Identificadores compactos deterministas más SHA-256 de respaldo garantizan la idempotencia por operación. DhModal presenta la razón real de fallos sin inventar relación con Reports.
- Mantiene REST, Redis Streams, SignalR y Outbox existentes. CI/staging/SMTP pendientes antes de confirmar entrega de QUO-609.

## [1.43.3] - 2026-11-12

- PATCH DH-20261112-DYNAMICS-IDTRA-FIRST10-117: coordinado con DholePricingService 1.16.1, Dynamics mapea los primeros diez IDTRA normalizados y distintos de cada QUO aunque Pricing conserve más referencias.
- DholeSystem/ecosistema 1.43.2 → 1.43.3; preserva versiones de demás componentes, RateId, importes, revisión, idempotencia, REST, Outbox y SignalR.
- Pricing CI .NET y tests de regresión aprobados; falta staging, confirmación de existencia en Dynamics y autorización de producción.

## [1.43.2] - 2026-11-12

- PATCH DH-20261112-LTL-CFZ-ROUTE-116: LTL propio CFZ Panamá → San José Costa Rica vuelve a ser seleccionable sin requerir una fila maestra previamente creada; genera la ruta dinámicamente con los cuatro cargos activos de Costos y recargos, por peso y tramo configurado.
- DholeSystem/ecosistema 1.43.1 → 1.43.2, DholeWeb 1.43.1 → 1.43.2. PricingService 1.16.0 conserva su versión y contratos actuales. No altera SignalR, Outbox ni otros servicios.
- Verificación de CI, staging y aceptación del flujo real requeridas antes de promoción a producción.

## [1.43.1] - 2026-11-12

- PATCH DH-20261112-LTL-PANAMA-COSTS-115: registra el release coordinado para LTL propio CFZ Panamá → San José Costa Rica con Bunker, Flete Terrestre Internacional, Gastos Panamá a Costa Rica y Custodia + Marchamo calculados desde Costos y recargos según peso.
- DholeWeb 1.43.0 → 1.43.1; DholeSystem/ecosistema 1.43.0 → 1.43.1; PricingService 1.16.0 sin cambios. Mantiene REST, SignalR y versionamiento de los demás componentes.
- Candidato master bloqueado hasta la aceptación de staging y autorización explícita de producción.

## [1.43.0] - 2026-11-12

- MINOR DH-20261112-PRICING-RESEND-CHOICE-114: selección de notificación para reenvíos en QUO aceptadas, desde DhModal. Opciones: apertura con PDF y respaldos, cotización enviada según CRM y aviso preliminar SIN PDF.
- Pricing distingue errores de generación de PDF, descarga de adjuntos y persistencia Outbox. En caso de fallos de Reports, se permite aviso SIN PDF claramente identificado como incompleto, sin cambiar aceptación ni IDTRA.
- Componentes: DholePricingService 1.15.0 → 1.16.0, DholeWeb 1.42.0 → 1.43.0, DholeSystem/global 1.42.0 → 1.43.0. Otros servicios conservan su versión; REST/SignalR/Outbox existentes.
- CI, staging y confirmación SMTP pendientes.

## [1.42.0] - 2026-11-12

- MINOR DH-20261112-PRICING-ACCEPTANCE-MAIL-113: notificaciones de aceptación de QUO con copias a Pricing y vendedor, reenvío manual desde DhModal y errores explícitos de Outbox; incidente QUO-00000-000609.
- Release coordinado: DholePricingService 1.14.0 → 1.15.0, DholeWeb 1.41.2 → 1.42.0 y DholeSystem 1.41.2 → 1.42.0; versión global 1.42.0. Sin cambios en esquema, REST o SignalR.
- CI y staging antes del despliegue de producción; verificar la cola de Notifications y la entrega SMTP, no marcar el mensaje como entregado antes de confirmación.

## [1.41.2] - 2026-11-12

- PATCH DH-20261112-PRICING-LINKED-QUO-NUMBER-113: Pricing Crystal y wizard legado muestran el QUO Number de la cotización aceptada vinculada en vez del UUID interno. El ID persiste exclusivamente para navegación y enlace comercial.
- DholeSystem 1.41.1 → 1.41.2, DholeWeb 1.41.1 → 1.41.2, PricingService 1.14.0 sin cambios. Compatible con REST, SignalR, Outbox e infraestructura existente. CI/staging pendientes.

## [1.41.1] - 2026-11-12

- PATCH DH-20261112-PRICING-CLIENT-QUO-PICKER-112: release coordinado de DholeWeb para listar de forma automática todas las QUO enviadas y aceptadas del cliente en «Cliente aceptó otra QUO», con paginación, búsqueda local y ruta/estado visibles.
- El vínculo requiere que la QUO ganadora esté aceptada y pertenezca al mismo cliente. Reutiliza endpoints existentes de DholePricingService 1.14.0, sin alterar REST, SignalR ni datos.
- DholeSystem 1.39.1 → 1.41.1; DholeWeb 1.41.0 → 1.41.1. CI/staging pendientes; sin autorización para producción.

## [1.39.1] - 2026-11-12

- PATCH DH-20261112-CRM-DRAFT-DHMODAL-111: metadatos del release aislado de master para recuperación de borradores CRM por DhModal, sin confirmaciones nativas.
- DholeWeb 1.39.0 → 1.39.1; DholeCRMService 1.24.0 → 1.24.1; DholeSystem 1.39.0 → 1.39.1. Conserva SignalR/REST y evita fusionar cambios ajenos de develop.
- CI y staging requeridos antes de producción.

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

## [1.36.0] - 2026-11-11

- MINOR DH-20261111-CRM-QUOTE-MULTI-CONTACTS-102: múltiples destinatarios para todas las futuras cotizaciones por cuenta CRM. Web utiliza DhMultiSelect y elimina el selector de cotización individual; CRM guarda la lista de contactos con migración compatible; Pricing valida y envía el PDF a cada contacto con copia al vendedor.
- Componentes del release: CRM 1.22.0, Pricing 1.13.0, Web 1.36.0 y System/global 1.35.0. Compatibilidad REST, SignalR y Outbox mantenida. CI/staging pendientes y producción sin autorización.

## [1.33.1] - 2026-11-11

- PATCH DH-20261111-CRM-QUOTE-PREFERENCE-REALTIME-094: actualiza el release global y CRM 1.20.1 para el evento Outbox al cambiar las preferencias de destinatario de cotizaciones, reutilizando la infraestructura realtime existente.
- Complementa 093: Pricing 1.12.0, Web 1.33.0; CI y staging pendientes, sin despliegue a producción autorizado.

## [1.33.0] - 2026-11-11

- MINOR DH-20261111-CRM-ACCOUNT-QUOTE-DELIVERY-093: preferencias de destinatario permanentes por cuenta CRM para todas las cotizaciones futuras. CRM 1.20.0, Pricing 1.12.0, Web 1.33.0, System/global 1.33.0.
- Aplicación en cada transición Sent, copia al vendedor asignado, validación de contacto, Outbox/realtime existentes y compatibilidad REST.
- CI y staging pendientes, producción no autorizada hasta aprobación expresa.

## [1.32.1] - 2026-11-11

- MINOR DH-20261111-CRM-QUOTE-SEND-VISIBLE-092: sincroniza la versión global con el frontend que muestra el botón «Enviar cotización» en la cabecera de todas las cuentas, incluso sin tarifas vinculadas; mantiene los controles de destinatario, contacto y copia al vendedor.
- DholeWeb 1.31.1, DholeSystem/global 1.32.1, Pricing 1.11.1 sin cambios en backend, API REST ni eventos realtime. La línea develop mantiene las funciones Geoapify propias de Web 1.32.0; no se introducen esas funcionalidades en master con este backport.
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
