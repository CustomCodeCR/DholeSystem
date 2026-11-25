## [1.124.34] - 2026-11-25

- DH-20261125-OWN-LCL-APPROVED-REFERENCE: coordinate Pricing 1.29.13 and Web 1.124.34; approved Maersk Balboa reference fallback with explicit provenance. CI and staging pending.

## [1.124.33] - 2026-11-25

- DH-20261125-OWN-LCL-MAERSK-BALBOA: isolated master backport of Pricing 1.29.12 and Web 1.124.33; all 17 baseline versions verified. CI and authenticated staging pending; no production integration yet.

## [1.124.32] - 2026-11-24

- DH-20261124-PRICING-AIR-QUANTITY-SAVE: conservar precios unitarios negociados al editar agente válido y peso/bultos/tarimas de cotizaciones aéreas existentes; cantidades recalculadas con el flujo existente y validación de cambios estructurales mantenida. DholeWeb/System 1.124.32; otros servicios sin cambios. CI y staging pendientes.

## [1.124.31] - 2026-11-24

- DH-20261124-PRICING-AIR-AGENT-SAVE: corrección aislada del guardado de cotizaciones aéreas al modificar exclusivamente un agente válido; conservar costos negociados y evitar sustituciones automáticas. DholeWeb/System 1.124.31; otros servicios sin cambios. CI y staging pendientes.

## [1.124.30] - 2026-11-24

- DH-20261124-PRICING-EDIT-CONTEXT-NORMALIZATION: candidato aislado a master de DholeWeb/System 1.124.30; CI de develop aprobado, versiones de los 15 servicios restantes verificadas; staging funcional y CI de master pendientes.

## [1.124.29] - 2026-11-24

- DH-20261124-PRICING-COST-CONTEXT-RELINK: candidato aislado para separar identidad CRM y reconciliación de costos persistidos. DholeWeb/System 1.124.29; Pricing 1.29.11. CI y staging pendientes.

## [1.124.28] - 2026-11-24

- DH-20261124-PRICING-DUPLICATE-RELINK: candidato aislado para recuperación del vínculo CRM de duplicados existentes. DholeWeb/System 1.124.28; Pricing 1.29.11. CI y staging pendientes.

## [1.124.27] - 2026-11-24

- DH-20261124-PRICING-HISTORICAL-EDIT: candidato de promoción aislada del hotfix integrado en develop. Conserva vínculos CRM en duplicación y corrige reconciliación de costos en edición. CI de candidato y validación staging pendientes.

## [1.124.26] - 2026-11-24

- DH-20261124-VERSION-CARD-FIX: corregir tamaño y contenido duplicado del card de versión de Topbar. Web/System 1.124.26; demás componentes sin cambios. CI/staging pendientes.

## [1.124.25] - 2026-11-24

- DH-20261124-TOPBAR-VERSION-CARD: versión dentro de DhCard compacto entre notificaciones y usuario. Web/System 1.124.25; demás componentes sin cambios. Logo del sidebar centrado respecto al card completo. CI/staging pendientes.

## [1.124.24] - 2026-11-24

- DH-20261124-TOPBAR-VERSION: trasladar versión a la barra superior y liberar sidebar. Web/System 1.124.24; demás componentes sin cambios. CI/staging pendientes.

## [1.124.23] - 2026-11-24

- DH-20261124-SIDEBAR-VERSION-FOOTER: mover la versión del sistema al pie fijo del sidebar y mostrarla con tooltip en modo compacto. Web/System 1.124.23; demás componentes sin cambios. CI/staging pendientes.

## [1.124.22] - 2026-11-24

- DH-20261124-SIDEBAR-BRAND-MOTION: transición animada del logo al expandir/colapsar sidebar y reducción de 15%. Web/System 1.124.22; demás componentes sin cambios. CI/staging pendientes.

## [1.124.21] - 2026-11-24

- DH-20261124-EXACT-SVG-LOGO: SVG exacto entregado por el usuario, colores CSS y favicon original #A90E19. Web/System 1.124.21; demás componentes sin cambios. Descripciones de marca solo al pasar el mouse sobre el logo. CI/staging pendientes.

## [1.124.20] - 2026-11-24

- DH-20261124-OFFICIAL-SQUARE-LOGO: logo oficial rectangular, O cuadrada y favicon rojo transparente. Web/System 1.124.20; restantes componentes sin cambios. CI/staging pendientes.

## [1.124.19] - 2026-11-24

- DH-20261124-THEME-LOGO: logotipo SVG transparente vinculado al tema y favicon ICO rojo original. Web/System 1.124.19; restantes 15 versiones comprobadas en master sin cambios. CI y staging pendientes.

## [1.124.17] - 2026-11-24

- DH-20261124-LCL-EDIT-COST: promoción aislada de la corrección LCL de develop. Web/System 1.124.17; las demás 15 versiones se verificaron contra master. CI develop superado; CI master y staging pendientes de validación.

## [1.124.16] - 2026-11-24

- DH-20261124-PERSISTED-DETAIL-IDENTITY: promover corrección general de identificadores de cargos históricos y fletes independientes. Web/System 1.124.16; otros componentes sin cambio; CI/staging pendientes.

## [1.124.15] - 2026-11-24

- DH-20261124-INLAND-PERSISTED-EDIT: promover aisladamente la corrección del Inland persistido integrado en develop. Web/System 1.124.15; demás componentes conservan sus versiones en master. CI de candidato y staging pendientes.

## [1.124.11] - 2026-11-24 · DH-20261124-INLAND-AUTO-SELECTION

## [1.124.14] - 2026-11-24

- DH-20261124-EXPIRED-APPROVAL-TRANSACTION: corregir transacciones EF/Npgsql de solicitudes y decisiones de vencimiento, conservar historial y Outbox atómicos. Pricing 1.29.10, Web/System 1.124.14.


## [1.124.13] - 2026-11-24

- DH-20261124-EXPIRED-APPROVAL-ACCESS: corregir acceso del vendedor a solicitudes de vencimiento; mostrar registro de motivos y decisiones desde historial de cotización. Pricing 1.29.9, Web/System 1.124.13, demás versiones sin cambios.


## [1.124.12] - 2026-11-24

- DH-20261124-EXPIRED-REASON-MODAL: corregir formulario de justificación de vencimiento y manejo de errores; texto genérico de jefatura. Web/System 1.124.12, demás versiones sin cambios.


- PATCH Web/System: restablece selección automática de inland Merchant/Naviera en P6 de cotizaciones editables persistidas sin elección válida. Mantiene elección válida, vista de solo lectura y costos históricos. CI/staging pendientes; REST, SignalR y BD sin cambios.

## [1.124.9] - 2026-11-24 · DH-20261124-GLOBAL-COMMERCIAL-ACTIONS

- PATCH coordinado: Web/System 1.124.9, Pricing 1.29.8. Gestión comercial global sin alterar titularidad. CI/staging antes de master.

## [1.124.8] - 2026-11-24 · DH-20261124-PRICING-PANAMA-PERSISTED-SAVE

- PATCH Web/System: conserva identidad histórica del tramo CFZ–GAM y venta del excedente al guardar, reconcilia antes de serializar y deja Auto Pricing como cálculo explícito para cotizaciones guardadas. CI/staging pendientes; producción no desplegada.

## [1.124.7] - 2026-11-24 · DH-20261124-PRICING-PANAMA-EXCESS-EDIT

- PATCH Web/System: conserva los cargos históricos del excedente FCL Panamá al editar y separa su flete de Merchant/Naviera. Pruebas de regresión añadidas; integración a master condicionada a CI y staging.

## [1.124.6] - 2026-11-24 · DH-20261124-PRICING-LCL-EDIT-NAV

- PATCH: navegación de LCL editable/duplicado P6 → P7 sin naviera; conserva conciliación de costos y validación de guardado. Web/System 1.124.5 → 1.124.6; 15 componentes restantes verificados sin cambios en master. CI/staging pendientes; producción no desplegada.

## [1.124.3] - 2026-11-24 · DH-20261124-PRICING-SENT-CRM-FIX

## [1.124.5] - 2026-11-24

- DH-20261124-SELLER-EXPIRED-RENEWAL: autorización de jefatura aplicada al flujo comercial de actualización de tarifas vencidas, con motivo, historial, Outbox y notificaciones existentes. Pricing 1.29.7, Web 1.124.5, 14 componentes restantes verificados sin cambios. CI/staging pendientes.

- PATCH: Pricing 1.29.5 → 1.29.6; Web/System 1.124.3 → 1.124.4. Omite avisos de Aperturas cuando existe IDTRA actual o histórico, verifica antes de publicar Outbox y comunica omisión en el modal de reenvío. Las notificaciones comerciales se conservan.
- Manifiesto actualizado; demás versiones conservadas de la rama base. CI, staging y verificación final pendientes; producción no desplegada.


- PATCH: Pricing 1.29.4 → 1.29.5; System 1.120.11 → 1.124.3. Se corrige la exigencia indebida de cuenta CRM en la transición Sent autorizada por Pricing, sin relajar permisos de CRM exclusivo ni validación de destinatarios vinculados.
- Web 1.124.2 → 1.124.3 (solo metadatos de versión, requisito CI). Versiones de los otros 14 componentes verificadas en master y conservadas; manifiesto actualizado. CI y staging pendientes; producción no desplegada.

## [1.120.11] - 2026-11-23 · DH-20261123-PRICING-LCL-INCH-PERSISTENCE-432

- PATCH coordinado: DholeWeb evita reinterpretar las medidas LCL/LTL en pulgadas como centímetros al guardar/reabrir y rehidratar datos del POL.
- Regresión con cinco tarimas Miami: volumen físico 68.248 CFT conservado; payload REST sigue normalizado en cm y visualización respeta unidades seleccionadas.
- Versión global DholeSystem/DholeWeb 1.120.10 → 1.120.11. Otros 15 componentes mantienen sus versiones individuales; manifiesto central de 17 repositorios actualizado.
- Promoción selectiva a master expresamente autorizada por el usuario; CI de develop aprobado, CI master y prueba autenticada de staging pendientes. Se conservan las versiones de los otros 15 servicios de producción.

## [1.120.10] - 2026-11-23 · DH-20261123-CRM-LEAD-AUDIT-431

- PATCH coordinado y selectivo: DholeWeb incorpora historial de cambios de Prospectos, separado de historial de rutas, y CRM agrega auditoría persistente PostgreSQL con actor, fecha, campos antes/después, autorización y paginación.
- DholeSystem/DholeWeb 1.120.9 → 1.120.10; DholeCRMService 1.43.0 → 1.43.1; los otros 14 componentes conservan sus versiones master; sin arrastrar las ramas divergentes de develop.
- CI de candidatos master, verificación autenticada en staging y autorización de despliegue de producción pendientes; master despliega Web y CRM automáticamente al integrar.

## [1.120.9] - 2026-11-23 · DH-20261123-PRICING-MODIFICATION-422

- PATCH coordinado: comparación de cambios de modalidad/tipo de embarque y protección de CostId/RateDetailId en edición P7, sin eliminación financiera implícita; conserva el release 1.120.8 de IVA POL/POE.
- Se preservan los otros 15 componentes del ecosistema. Producción autorizada por el solicitante, sujeta a CI completo y validación en staging antes de promoción.

## [1.120.8] - 2026-11-23

- PATCH DH-20261123-PRICING-VAT-RELEASE-430: release coordinado DholeSystem/DholeWeb para corregir el IVA de Pantalla 7 por POL/POE y por sentido importación/exportación, con multi-POE.
- Sin cambio de contrato API y sin nuevos componentes DH; validar staging antes de master.

## [1.120.7] - 2026-11-23 · DH-20261123-PRICING-LTL-EDIT-NAV-422

- PATCH DholeSystem/DholeWeb 1.120.6 → 1.120.7: navegación de edición en cotizaciones LTL existentes permite revisar P7 desde P6 sin validaciones de una tarifa nueva.
- No revaloriza, reemplaza ni borra líneas históricas con una simple navegación; mantiene validación de guardado y los contratos REST, SignalR y Outbox/Inbox vigentes.
- Manifiesto de 17 repositorios actualizado; otros 15 componentes conservan sus versiones individuales. Pendiente CI/staging, no desplegar producción sin autorización expresa.

## [1.120.6] - 2026-11-23 · DH-20261123-PRICING-EDIT-STEP6-421 (candidato master)

- PATCH aislado de la navegación P6→P7 al editar flete terrestre de una cotización guardada. No se alteran cargos históricos ni validación al guardar.
- DholeSystem/DholeWeb pasan de master 1.120.3 al candidato 1.120.6; releases 1.120.4/1.120.5 preservados en develop, sin traer código incompleto a master. Demás 15 componentes sin cambios.
- CI/staging y autorización expresa de producción requeridos antes de integrar master.

## [1.120.3] - 2026-11-23 · DH-20261123-CORS-PREFLIGHT-419

- PATCH coordinado: DholeWeb enruta solicitudes autorizadas de la API bajo el origen propio, comparte caché de catálogos por sesión y mantiene los componentes DH y contratos REST/SignalR intactos.
- DholeApiGateway añade duración de una hora a las respuestas preflight CORS compatibles; la allowlist y seguridad JWT no cambian.
- Versiones: DholeSystem/DholeWeb 1.120.2 → 1.120.3; DholeApiGateway 1.11.0 → 1.11.1; 14 servicios restantes sin modificación. Manifiesto central de 17 componentes sincronizado.
- Desarrollo a ramas intermedias y PR develop/staging; master se promueve solo tras validación y aprobación de producción.

## [1.120.2] - 2026-11-23 · DH-20261123-PRICING-LTL-NUMERIC-418

- PATCH master selectivo del consolidado LTL propio: corregir error de .trim() previo a POST con valores numéricos de Vue, mostrar errores específicos y asegurar que «Crear ruta» se pueda enviar.
- Incluye creación de rutas alternativas por ciudad, preservando San Pedro Sula cuando se agrega Tegucigalpa, y pruebas de regresión de ambos escenarios.
- Releases LTL 417+418 exclusivamente, sin integrar funciones incompletas de Operations 416 presentes únicamente en develop.
- Versiones en master: DholeSystem y DholeWeb 1.119.1 → 1.120.2; 15 servicios restantes conservan sus versiones de producción. Manifiesto de 17 componentes actualizado.
- CI, staging, permiso de producción y health checks son obligatorios previo/post merge.

## [1.120.1] - 2026-11-23 · DH-20261123-PRICING-LTL-ROUTES-417

- PATCH: permitir consolidado LTL adicional por destino, independiente de las rutas actuales. Acción de duplicado con importes/cargos y prevención de actualización accidental de ruta original.

## [1.119.1] - 2026-11-23 · DH-20261123-PRICING-RETURN-MODAL-415

- PATCH: promover selectivamente el botón «Ver devolución» y el historial de Pricing dentro de DhModal en Dashboard comercial.
- Release global con DholeWeb/DholeSystem 1.119.0 → 1.119.1, 15 componentes sin cambios; se preservan contratos REST, realtime y los commits existentes de master.
- CI, verificación funcional en staging y controles de despliegue pendientes antes de master.

## [1.119.0] - 2026-11-22 · DH-20261122-OPS-CASE-OVERVIEW-414

- MINOR: release coordinado de visibilidad y resumen del expediente IDTRA: CRM como fuente de identidad de cliente/ejecutivo, Auth para nombres de operativos, estados por departamento y consulta del superusuario.
- Manifiesto universal de 17 componentes: DholeSystem y DholeWeb 1.118.0 → 1.119.0, DholeOperationsService 0.16.0 → 0.17.0 y DholeCRMService 1.42.8 → 1.43.0; otros 13 sin cambios.
- Integración pendiente de CI y staging; master y despliegue de producción no autorizados.


## [1.117.1] - 2026-11-22 · DH-20261122-DHOLE-ERP-411 (master integrated candidate)

- PATCH: DHOLE ERP no tiene pronunciación obligatoria: eliminadas las guías visibles, tooltips y claves de idioma. La sigla corporativa y la marca permanecen.
- Corregido test:branding en Docker sin .env. Coordinación DholeWeb/DholeSystem 1.117.0 → 1.117.1; el resto de componentes conserva versiones. Validaciones staging necesarias antes de master.

## [1.117.0] - 2026-11-22 · DH-20261122-DHOLE-ERP-410 (branding integrated)

- MINOR: identidad corporativa de la plataforma interna DHOLE ERP: nombre visible en acceso, navegación, metadata, logo y mensajes. Digital Hub for Operations, Logistics & Ecosystem.
- DholeWeb y DholeSystem 1.116.1 → 1.117.0. Reservados DHOLE CLOUD, DHOLE X4 y GIO. Contratos REST/SignalR, outbox/inbox y rutas sin cambios.

## [1.116.1] - 2026-11-22 · DH-20261122-PRICING-RETURN-EMAIL-409 (master selective candidate)

- PATCH: plantilla HTML de devolución compatible con Outlook, asunto sin UUID, cliente/ruta/modalidad y motivo claros, botón «Corregir y reenviar solicitud». UUID solo en URL técnica y correlación interna.
- Eliminar UUID del modal Pricing en DholeWeb. Pricing 1.26.25 → 1.26.26; Web/System 1.116.0 → 1.116.1; otros 14 componentes conservan versiones.
- Solo ajustes necesarios de Pricing/Web/System, sin combinar modificaciones de otras ramas. Mantiene REST, SignalR, Redis Outbox/Inbox y trazabilidad. Requiere staging y autorización de producción antes del merge master.

## [1.116.0] - 2026-11-22 · DH-20261122-OPERATIONS-ASSIGNMENT-SUMMARY-408

- MINOR: nueva selección de equipo de Aperturas antes de crear IDTRA, con control del pool de dos validadores y reintentos de asignación.
- Estibable únicamente para LCL/LTL y peso diferido a Coordinación Origen; vista de resumen y drawer reorganizadas por secciones del expediente.
- Versionamiento global de DholeWeb y DholeSystem 1.115.1 → 1.116.0 y DholeOperationsService 0.15.1 → 0.16.0, otros 14 componentes sin cambios.
- PR master pendiente de autorización; no se ejecuta despliegue de producción de Web ni Operations hasta recibirla.

## [1.115.1] - 2026-11-22 · DH-20261122-PRICING-RETURN-407

- PATCH coordinado de devoluciones de solicitudes comerciales en Pricing: UX «Devolver tarifa» / «Devuelta por Pricing», motivo obligatorio y revisión del historial íntegro desde Ventas.
- DholePricingService 1.26.24 → 1.26.25 identifica la solicitud original en notificaciones Email/System y verifica conservación del ID e historial en correcciones y reenvíos; DholeWeb y DholeSystem 1.115.0 → 1.115.1.
- Otros componentes conservan sus versiones; no hay cambios de esquema, endpoints REST ni arquitectura SignalR/Redis Streams. Integración selectiva por ramas intermedias con CI y staging previos a master.

## [1.115.0] - 2026-11-22 · DH-20261122-OPERATIONS-OPENING-POLISH-406 (selective master candidate)

- MINOR: apertura manual con autoguardado local recuperable, seleccionadores de naturaleza y bultos, tarjetas FCL/FTL similares a Pricing con control de duplicados, cantidad y peso, y contactos operativos de CRM activos por defecto con opción de desmarcar.
- Crear IDTRA y asignar validadores de Aperturas mediante el pool existente solo al confirmar; reintentos no duplican el registro. Sin leyenda de Coordinación Origen.
- DholeWeb y DholeSystem 1.114.0 → 1.115.0; 15 componentes restantes sin modificaciones. Conserva REST, SignalR, audit, borradores y expedientes anteriores.
- Promoción selectiva y coordinada con staging y CI; solicitud del usuario autoriza integrar master, no otros despliegues de infraestructura.

## [1.114.0] - 2026-11-22 · DH-20261122-OPERATIONS-OPENING-UX-405 (master candidate)

- MINOR: operaciones apertura manual con selección solo marítimo, aéreo y terrestre; tarjetas de botones accesibles y mejora del ejecutivo comercial CRM, incluidos contactos operativos reales por ID.
- Histórico de modalidad Multimodal y borradores preservados. División CRM de solo lectura hasta disponer de contrato. Documento v1.2 de brechas en DholeWeb.
- DholeWeb/DholeSystem 1.113.1 → 1.114.0; los otros quince componentes no cambian. REST, SignalR y Outbox/Inbox sin cambios.
- Release selectivo desde master, sin merge general develop. Staging y CI son obligatorios; producción sin autorización en DH-405.

## [1.113.1] - 2026-11-22 · DH-20261122-OPERATIONS-NO-SERVICES-404 (master: selective operations opening promotion)

- PATCH sobre 1.113.0: eliminar por completo la pantalla 5 de Servicios de la apertura manual y sus campos de recolecta, entrega, agentes, naviera y merchant; conservar el WHS obligatorio en Cliente y ruta para FCA con LCL/LTL.
- Promoción coordinada de DholeSystem y DholeWeb a 1.113.1 desde master 1.112.1, sin fusionar miles de commits ajenos de develop ni modificar los otros 15 componentes.
- El usuario autorizó subir DH-404 a master. DholeWeb auto-despliega ante push a master; sin cambios a infraestructura de despliegue ni despliegue de backend.
- Validado en develop: Web CI, política SemVer, tests de Operaciones, build y despliegue de staging exitoso (run 45038067759). QA manual autenticado en producción por verificar.

## [1.113.0] - 2026-11-22 · DH-20261122-OPERATIONS-UX-403 (base funcional incluida)

- MINOR: paso a un wizard de tres etapas para aperturas manuales con selector de clientes de Pricing, búsquedas CABYS, documentos en Storage, países derivados de ruta, borradores e IDTRA automático sin campo editable.
- El release 1.113.1 elimina la pantalla de servicios que inicialmente estaba incluida en el paso 1 de 1.113.0.

## [1.112.1] - 2026-11-22 · DH-20261122-PRICING-OPERATIONS-STEPPER-402 (DholeWeb / DholeSystem · visual Pricing)

- PATCH: Coordinación del encabezado y navegación de Pricing con el componente compartido de Aperturas, conservando borradores múltiples, descarte y autoguardado existentes.
- DholeSystem y DholeWeb 1.112.0 → 1.112.1; restantes microservicios sin cambios, incluidos DholeOperationsService 0.15.1, DholePricingService 1.26.24 y DholeApiGateway 1.11.0.
- No modifica REST ni SignalR. CI y staging obligatorios antes de integrar master; producción sin autorización de despliegue.

## [1.112.0] - 2026-11-22 · DH-20261122-OPERATIONS-PARITY-401

- MINOR: release coordinado de apertura manual alineada con Pricing, con DholeWeb 1.112.0 y DholeOperationsService 0.15.1.
- Conserva versiones de otros microservicios en el manifiesto global, sin modificar main. CI y staging deben pasar antes de master; producción no autorizada para despliegue.

## [1.111.1] - 2026-11-21 · DH-20261121-OPERATIONS-STEPPER-400 (patch visual del wizard compartido)

- PATCH Web/System 1.111.0 → 1.111.1. El componente compartido PricingWizardStepper usa la cantidad real de pasos: 4 columnas para Pricing y 5 para Aperturas en escritorio, sin crear una segunda fila artificial. Móvil conserva su disposición desplazable.
- Operations 0.15.0 y los otros 14 componentes sin cambios. Pruebas de UI y políticas de versión requeridas antes del batch master.

## [1.111.0] - 2026-11-21 · DH-20261121-OPERATIONS-PRICING-UI-399 (Operations UI comparte componentes de Pricing)

- MINOR coordinado DholeWeb/DholeSystem 1.110.6 → 1.111.0; Operations conserva 0.15.0, Pricing conserva su versión y los otros 15 componentes sus versiones actuales.
- Apertura manual en cinco etapas con navegación visual de Pricing y controles compartidos: PricingWizardStepper extraído del editor de tarifas, PricingLocationSearchSelect para POL/POE/POD/WHS, PricingCrystalMultiSelect para servicios, DhInput/DhSelect/DhCheckbox/DhTextarea y mismos catálogos de Config.
- Borradores incompletos y edición versionada conservan las referencias ya guardadas; no modifican costos ni líneas comerciales y no cambian el IDTRA generado por PostgreSQL.
- CI/staging requieren validación; integración automática de QUO aceptada a Operations se mantiene pendiente.

## [1.110.6] - 2026-11-21 · DH-20261121-PRICING-TERRESTRIAL-FREIGHT-398 (candidate master)

- PATCH: promoción del mismo DH-398 validado en develop: DholeSystem y DholeWeb 1.110.5 → 1.110.6; PricingService mantiene 1.26.24.
- Pantalla 7 FCL multimodal conserva el flete marítimo y agrega el Flete Internacional Terrestre independiente de USD 2.140 desde el conjunto applicable retornado por Pricing, reconciliado tras cargar la respuesta asíncrona.
- Protege CostId, relaciones múltiples POE/POD, importe y snapshots persistidos; la regla no duplica Bunker ni elimina cargos anteriores.
- Se conservan el manifiesto global, las 17 versiones registradas y productionDeploymentAuthorized=false; CI de master y UAT autenticado en staging pendientes.

## [1.110.5] - 2026-11-21 · DH-20261121-PRICING-VGM-FCL-FINAL-397 (candidate master)

- PATCH global System/Web 1.110.4 → 1.110.5; PricingService 1.26.23 → 1.26.24; resto de versiones sin cambios.
- Cierre de la validación Incoterm para VGM Miami y FCL Panamá independiente, mismo release para staging y master después de CI.


## [1.110.4] - 2026-11-21 · DH-20261121-PRICING-MISSING-LINES-396 (candidate master)

- PATCH global System/Web 1.110.3 → 1.110.4 y Pricing 1.26.22 → 1.26.23. Las versiones de los demás componentes permanecen iguales.
- Reparación de persistencia de VGM LCL Miami y flete terrestre FCL Panamá separados de Bunker y flete marítimo. Pruebas de regresión y promoción develop → staging → master.

\n## [1.110.3] - 2026-11-21 · DH-20261121-PRICING-FINAL-POLISH-395 (candidate master)

- PATCH coordinado: DholeSystem y DholeWeb 1.110.2 → 1.110.3; DholePricingService 1.26.21 → 1.26.22. Resto de componentes mantiene su versión.
- Tres pendientes finales de Pricing: VGM Miami, FCL Freight independiente de Bunker y días de tránsito editables en LTL. CI y staging obligatorios.

## [1.110.2] - 2026-11-21 · DH-20261121-PRICING-LAST-THREE-FIXES-394 (candidate master)

- Coordinación PATCH System/Web 1.110.1 → 1.110.2 y Pricing 1.26.20 → 1.26.21. Los demás componentes mantienen su versión.
- Entrega cerrada de tres pendientes: cuatro cargos LTL Panamá, flete terrestre FCL multimodal independiente, y conceptos comerciales LCL Miami.
- Promoción selectiva en ramas intermedias con manifiesto central, sin importar cambios ajenos de develop.

## [1.110.1] - 2026-11-21 (DH-20261121-PRICING-TRANCHE-MIAMI-PANAMA-393 · Promoción de costos logísticos)

- PATCH coordinado de DholeWeb 1.109.3 → 1.110.1, DholeSystem 1.109.3 → 1.110.1 y DholePricingService 1.26.19 → 1.26.20.
- Costos por tramo en creación y modificación, LCL comercial Miami según cotizador HTML, FCL multimodal marítimo/terrestre y cuatro cargos de LTL Panamá → Costa Rica.
- Backport selectivo a master debido a divergencia con develop, sin incluir cambios operativos DH-392 que no pertenecen a este release. Producción condicionada a CI, staging y validaciones del manifiesto central.

## [1.109.3] - 2026-11-21 · DH-20261121-P7-COSTS-391 (candidato master)

- Release PATCH coordinado de DholeWeb 1.109.3 y DholeSystem 1.109.3 (DholePricingService 1.26.19 sin cambios).
- Se corrigen costos LTL Panamá por peso y la agencia aduanal LCL, separación de flete terrestre en multimodal, selección de sobrepeso al modificar y denominación del flete según modalidad.
- Se actualiza manifiesto central, rutas de integración y escenarios de QA; sin migración de BD ni cambio incompatible en REST/SignalR.
- CI/staging pendientes, despliegue a producción no autorizado para DH-391.

## [1.109.2] - 2026-11-21 · DH-20261121-WIZARD-COSTS-390 (candidato master)

- Release coordinado: DholePricingService 1.26.19 y DholeWeb 1.109.2; corrección de costos 0/0 legítimos, sobrepeso Panamá con tarifas LTL y cambio explícito de muellaje durante edición.
- Actualiza manifiesto de componentes y versiones; conserva contratos REST/realtime existentes; sin migración de base de datos.
- Integración develop, CI, staging y batch master pendientes; no autorizado el despliegue de producción.

## [1.109.1] - 2026-11-21 · DH-20261121-PRICING-EDIT-BUNDLE-389

- PATCH coordinado DholeWeb 1.109.1 / DholeSystem 1.109.1; PricingService conserva 1.26.18 y el contrato GET /api/pricing/costs/wizard-bundle.
- La edición de cotizaciones consulta costos aplicables en Pantalla 6 (Naviera/Merchant) y Pantalla 7 (solo delta solicitado), sin recalcular RateDetails persistidos, importar opcionales ajenos ni eliminar flete marítimo.
- La carga del catálogo no se omite por existir RateId; la carga protege contexto vigente, solicitudes tardías y selection de Inland. REST/SignalR sin cambios incompatibles.
- Despliegues a staging y producción sujetos a CI, validación de pantalla 6/7 y revisión coordinada de ramas.

## [1.109.0] - 2026-11-21 · DH-20261121-BLOBATAR-ACCESSORIES-388

- MINOR: manifiesto global coordinado con DholeWeb 1.109.0 para accesorios combinables de Blobatar.
- Nuevas colecciones: Navidad, Halloween, Mes Patrio de Costa Rica y diversión (gorrito de bufón). Persistencia local migrada sin alterar los demás servicios.
- Las versiones de los otros 15 componentes permanecen registradas sin cambios. CI y staging obligatorios; despliegue de producción requiere autorización expresa.

## [1.108.20] - 2026-11-21 · DH-20261121-QUO-EDIT-DELTA-387

- PATCH: edición diferencial de QUO. Los RateDetails originales se conservan salvo cambios de contexto solicitados; Servicio de Aduanas y Seguro crean únicamente sus propias líneas y mantienen los valores pactados en las restantes.
- PATCH: candidato master agrupa 1.108.19 DH-386 (wizard-bundle como catálogo único y flete internacional terrestre independiente) y 1.108.20 DH-387 (comparación de contexto y servicios), reduciendo el despliegue de producción a un solo release coordinado.
- DholeWeb/DholeSystem 1.108.20, PricingService 1.26.18. Historial y versiones intermedias conservadas en CHANGELOG. Verificaciones CI, staging y producción exigidas.

## [1.108.19] - 2026-11-21 · DH-20261121-WIZARD-BUNDLE-ONLY-386

- PATCH coordinado: DholeSystem y DholeWeb 1.108.18 → 1.108.19, DholePricingService 1.26.17 → 1.26.18; los 14 componentes restantes mantienen sus versiones.
- Fuente definitiva de costos del asistente QUO: /api/pricing/costs/wizard-bundle, sin mezclas desde /costs/select ni inserción de cargos ajenos a data.applicable.
- FCL multimodal: conserva Flete Internacional Terrestre como línea independiente del flete marítimo por equipo. Edición conserva RateDetails guardados y no reincorpora líneas eliminadas.
- CI y despliegues de staging aprobados, prueba manual autenticada pendiente. Master se integra mediante ramas de backport, despliegue de producción requiere autorización específica.

## [1.108.18] - 2026-11-21 · DH-20261121-PRICING-EDIT-TIERS-LAND-385

- PATCH coordinado: DholeSystem/DholeWeb 1.108.17 → 1.108.18, DholePricingService 1.26.16 → 1.26.17; los demás servicios mantienen sus versiones individuales.
- Garantizar que la edición de QUO no reincorpora cargos eliminados, que se aplican tramos por contenedor/peso/bultos/días y que el flete internacional terrestre aparece en multimodal cuando corresponde.
- CI y pruebas staging pendientes; ningún despliegue a producción autorizado. REST y SignalR compatibles.

## [1.108.17] - 2026-11-21 · DH-20261121-PRICING-P7-RESTORE-384

- PATCH: persistir las eliminaciones de cargos en Pantalla 7 y recuperar la revisión original mediante confirmación explícita.
- PATCH: permitir actualizar costos en cotizaciones guardadas y evitar cargos de proveedores ajenos.
- Release coordinado DholeSystem/DholeWeb 1.108.17, PricingService 1.26.16; restantes 14 sin cambios.

## [1.108.16] - 2026-11-21 · DH-20261121-PRICING-P7-EDIT-SAFETY-383

- PATCH: edición de RateDetails existentes sin generar cargos de catálogo no seleccionados.
- PATCH: Pricing omite importes 0/0 por ausencia de tramo y conserva catálogo.
- Versiones DholeWeb y DholeSystem 1.108.16, PricingService 1.26.15; resto sin cambios.

## [1.108.15] - 2026-11-21 · DH-20261121-PRICING-P7-SNAPSHOT-TIERS-382

- PATCH: DholeSystem y DholeWeb 1.108.14→1.108.15; DholePricingService 1.26.13→1.26.14; otros 14 servicios mantienen versión.
- PATCH: Pricing calcula cargos elegibles de Wizard Bundle a partir de las reglas por contenedor, peso, bultos y días adicionales en lugar de devolver el cero del catálogo.
- PATCH: DholeWeb conserva detalle y precios de las cotizaciones ya guardadas y no agrega opcionales del catálogo a Pantalla 7 durante edición.
- Pruebas y CI coordinadas en ramas release; staging pendiente. Sin cambios incompatibles de API, base de datos o SignalR.

## [1.108.14] - 2026-11-21 (DH-20261121-PRICING-TIERS-381 · costos por tramos)

- PATCH coordinado DholeSystem y DholeWeb 1.108.13 → 1.108.14; DholePricingService permanece 1.26.13 y los otros catorce servicios no cambian.
- Costos por condiciones: contenedores, rangos de bultos y peso (incluyendo tarifa por kilogramo), y cobro por días adicionales a los incluidos en almacenamiento fiscal.
- Pantallas 6/7 de Pricing utilizan el valor de pricingRulesJson y evitan el monto cero de cabecera; invalidan los tramos cuando cambian los datos de la carga sin alterar cargos manuales ni RateDetails históricos.
- Se realiza backport selectivo desde develop/staging a master con pruebas CI, versionado y manifiesto centralizado. Sin cambios REST, realtime ni datos maestros.

## [1.108.13] - 2026-11-21 (DH-20261121-PRICING-P7-EDIT-380 · release coordinado P7 seguro/costos/edición)

- PATCH: DholeSystem y DholeWeb 1.108.12 → 1.108.13; DholePricingService 1.26.12 → 1.26.13. Los 14 componentes restantes conservan sus versiones.
- Web: seguro desde creación con valor declarado; no líneas variables ficticias; edición conserva RateDetails, importes y orden pantalla 7.
- PricingService: endpoint wizard-bundle unificado del catálogo y cargos, backportado a master sin eliminar REST.
- Actualizados metadatos y manifiesto central del release. Compilación, CI y staging pendientes; producción sin autorización.

## [1.108.12] - 2026-11-21 (DH-20261121-FOB-FCL-MASTER-379 · master alineado con develop)

- PATCH DholeSystem y DholeWeb 1.108.10 → 1.108.12; DholePricingService permanece 1.26.12. Cambio selectivo de hotfixes Incoterm y FCL, no integración masiva de ramas divergentes.
- Web: conserva las funciones de Incoterms tras Vite, diferencia fletes FCL generados automáticamente de tarifas manuales, excluye de facturación el flete de FOB Exportación salvo selección explícita y acotada de «Cotizar por acuerdo». Mantiene montos de inventario, RateDetails históricos e Inland.
- Sin cambios de endpoints backend, Redis, SignalR ni base de datos. Manifiesto de 17 componentes actualizado. Producción habilitada por solicitud del usuario de promoción a master; CI y smoke postdeploy obligatorios.

## [1.108.11] - 2026-11-21 (DH-20261121-INCOTERM-RUNTIME-SCOPE-378 · promocionado junto al 1.108.12)

- Evita transformaciones de Vite que borraban applyIncotermAutomaticChargeGuard del wizard, añade comprobaciones de bindings y tests en Web.

## [1.108.10] - 2026-11-21 (DH-20261121-INCOTERMS-MODIFICATIONS-MASTER-378 · backport master Incoterms y modificaciones)

- PATCH coordinado DholeWeb/DholeSystem 1.107.5 → 1.108.10 y Pricing 1.26.9 → 1.26.12, versiones presentes en develop; sin merge masivo ni nuevos servicios.
- Incoterms: 11 marítimo/multimodal, 7 aéreo/terrestre, operación compacta manual, categorías de responsabilidad en P7, cargos de contraparte no precotizados, acuerdo explícito por línea.
- Modificaciones: no eliminar RateDetail históricos por ausencia en snapshot y no hacer resync del catálogo sobre QUOs guardadas; el flete importado solo se cobra si P7 lo envía.
- CI, prueba autenticada en staging y gate de despliegue a producción obligatorios; no hay solicitud de workflow_dispatch de producción.

## [1.107.5] - 2026-11-20 (DH-20261120-PRICING-WIZARD-RUNTIME-366 · restaurar formulario Pricing y evitar errores runtime)

- PATCH coordinado Web/System 1.107.4 → 1.107.5: corrige `automaticOperationType is not defined` después de la promoción de la resolución mundial de países, sin revertirla.
- Validación de presencia de identificadores en los transforms del wizard y comprobación del JavaScript minificado; mantiene import/export manual, IVA según POD, inland y la arquitectura realtime.
- DholePricingService permanece en 1.26.9. Sin cambios en API, Auth, Config, base de datos, despliegues de backend ni SignalR. CI y pruebas de staging/productivas obligatorias.

## [1.107.4] - 2026-11-20 (DH-20261120-PRICING-UNIVERSAL-COUNTRY-365 · países y rutas universales de Pricing)

- PATCH coordinado DholeSystem/DholeWeb 1.107.3 → 1.107.4 para resolver países de todas las rutas con ISO 3166-1, códigos ISO2/3, UN/LOCODE y nombres ES/EN/PT/FR, sin listas manuales de destinos.
- La perspectiva comercial se determina con el país real del cliente frente al origen/destino final; cuando falta evidencia, continúa disponible el selector manual de Importación/Exportación/Tránsito.
- VAT por POD, Incoterms, cargos, contratos REST y SignalR sin cambios. DholePricingService 1.26.9 se mantiene.
- CI y staging autenticado obligatorios antes de producción. El 20 de noviembre de 2026 se recibió autorización explícita de promoción a master; CI aprobada en develop y verificación autenticada staging aún por confirmar.

## [1.107.3] - 2026-11-20 (DH-20261120-PRICING-PERSPECTIVE-364 · perspectiva comercial de Pricing)

- PATCH Web/System coordinado 1.107.2 → 1.107.3: identifica El Salvador en los destinos antiguos aunque falte ISO en Config, amplía el ISO-2 de países CRM y permite seleccionar Importación/Exportación manualmente.
- El asistente de Pricing guarda la selección en borradores y preserva la operación existente; no se modifica la lógica de IVA, contratos REST, SignalR ni Redis Streams.
- DholePricingService 1.26.9 sin cambios. Validación de compilación, CI, pruebas y staging pendiente; producción no autorizada para este release.

## [1.107.2] - 2026-11-20 (DH-20261120-PRICING-INLAND-RESTORE-363 · restauración de cargos en pantallas 6 y 7)

- PATCH de contención coordinado con DholeWeb 1.107.2; revierte mutaciones prematuras del inland y de los costos durante la carga asíncrona, preservando la rama master actual (1.107.1).
- Conserva las notificaciones de actualizaciones de 1.107.1, las aprobaciones de tarifas vencidas de 1.106.18 y el desbloqueo temporal de Incoterms. DholePricingService sigue en 1.26.9 y los otros componentes no cambian.
- Sin cambios en infraestructura, bases de datos, REST ni SignalR. Validaciones de CI y posteriores al despliegue obligatorias.

## [1.107.1] - 2026-11-20 (DH-20261120-VERSION-NOTICE-500-362 · hotfix del guardado de avisos de versión)

- PATCH coordinado: corrige HTTP 500 global/personal mediante Npgsql execution strategy que agrupa la transacción y los eventos Outbox atómicamente.
- Auth 1.17.0 → 1.17.1; DholeSystem y DholeWeb 1.107.0 → 1.107.1; resto de componentes sin cambios.
- Implementado y compilado en develop; promoción aislada sobre master sin arrastrar cambios no relacionados.

## [1.107.0] - 2026-11-20 (DH-20261120-VERSION-NOTICES-361 · control de avisos de nuevas versiones)

- MINOR coordinado: DholeWeb 1.106.18 → 1.107.0, DholeAuthService 1.16.2 → 1.17.0, DholeNotificationsService 1.7.0 → 1.8.0 y DholeSystem 1.106.18 → 1.107.0.
- Preferencias globales e individuales, persistencia Auth, Outbox/Redis Streams y SignalR con reconciliación REST y aislamiento por usuario.
- Promoción aislada desde rama master y no desde develop (evita 1.000+ commits no relacionados); CI, migración y staging E2E obligatorios antes de merge a master.

## [1.106.18] - 2026-11-20 (DH-20261120-PRICING-EXPIRED-MASTER-361 · aprobación de vencidas exclusiva para vendedores)

- PATCH coordinado Pricing/Web/System: Master recibe corrección de roles aplicada originalmente en develop como 354. Vendedores solicitan autorización a Roy/José Pablo; Pricing y Superadmin editan tarifas vencidas directamente, sin el modal de solicitud ni el bloqueo HTTP 409.
- Pricing 1.26.8 → 1.26.9, Web/System 1.106.16 → 1.106.18; versión por encima de develop 1.106.17. Resto de componentes sin cambios, preservando funcionalidades del master actual.
- No hay migraciones, se mantienen auditoría, REST, SignalR/Outbox e idempotencia. La promoción a master está solicitada explícitamente; CI y validación posdespliegue obligatorias.

## [1.106.16] - 2026-11-20 (DH-20261120-PRICING-INLAND-QA-358 · control de calidad del inland 6→7)

- PATCH de DholeWeb/DholeSystem 1.106.15 → 1.106.16: rectifica la prueba aislada del guardado de Merchant/Carrier en Pantalla 6, tras la incorporación del nuevo autoguardado por POE/naviera; Pricing 1.26.8 sin cambios.
- Conserva la corrección funcional de 1.106.15 sin alterar REST, SignalR, base de datos ni permisos. Pruebas CI/staging aún obligatorias; producción no autorizada.

## [1.106.15] - 2026-11-20 (DH-20261120-PRICING-INLAND-STEP67-357 · inland y cargos se mantienen de pantalla 6 a 7)

- PATCH coordinado de DholeWeb 1.106.14 → 1.106.15, DholePricingService 1.26.7 → 1.26.8 y DholeSystem 1.106.11 → 1.106.15. Los demás 14 repositorios mantienen versión.
- El inland Naviera/Merchant y los recargos configurados se transfieren por CostId al entrar a Pantalla 7, se conservan en borradores por POE/naviera y no se pierden por carreras de consultas asíncronas.
- Misma API REST, permisos, SignalR y esquema de datos. CI, staging y despliegue a producción pendientes; producción no autorizada.

## [1.106.10] - 2026-11-20 (DH-20261120-PRICING-VAT-TOTAL-353 · IVA de tarifas en el resumen de oferta)

- PATCH coordinado en DholePricingService 1.26.5 y DholeWeb/DholeSystem 1.106.10: IVA comercial por línea agregado en USD/CRC aunque Config guarde códigos de moneda opacos.
- En tarifas persistidas, el frontend recupera el IVA comercial por renglón cuando la API histórica devuelve cero, evitando total incorrecto; subtotal, utilidad y margen permanecen sin IVA.
- Pruebas para rubros gravados y no gravados, con paridad de PDF. Sin migración, cambios REST ni SignalR; CI y staging pendientes, producción no autorizada.

## [1.106.8] - 2026-11-20 (DH-20261120-INCOTERM-SAVE-351 · Guardado Incoterm FOB importación)

- PATCH de Web/System: el transformador de edición de tarifas ya no introduce `freightNotRequiredByIncoterm`, variable inexistente que bloqueaba la operación antes de llamar al API Pricing.
- Conserva el flete cuando el servicio Transporte Internacional está seleccionado, independientemente del Incoterm, y concilia los detalles persistidos cuando no se contrató transporte. Regresión FOB Shanghái → Caldera → San José.
- Versiones DholeWeb/DholeSystem 1.106.7 → 1.106.8; DholePricingService permanece en 1.26.4. Actualizado manifiesto de 17 repositorios; compatibilidad REST y SignalR sin cambios. Validaciones de CI/staging necesarias.

## [1.106.7] - 2026-11-20 (DH-20261120-INCOTERM-IMPORT-350 · Incoterms importación China a Costa Rica)

- PATCH coordinado Pricing/Web/System: los Incoterms aplican las obligaciones desde el país real del cliente, POL China y POD Costa Rica; importaciones no heredan el punto de vista exportador. Resolución de los 11 códigos ICC, con identificadores Config opacos y flete internacional expresamente contratado.
- DholePricingService 1.26.3 → 1.26.4; DholeWeb y DholeSystem 1.106.6 → 1.106.7. Los otros 14 componentes no cambian binarios; se preservan REST, SignalR, Outbox e Inbox.
- Release en ramas intermedias; compilación y pruebas CI, staging autenticado y aprobación de producción pendientes. Sin migración de datos ni despliegue autorizado.

## [1.106.6] - 2026-11-20 (DH-20261120-MERCHANT-OPTIONS-348 · Merchant/Carrier comparte opciones entre Pantalla 6 y 7)

- PATCH coordinado Web/System 1.106.5 → 1.106.6: opciones Optional de ruta confirmadas para Pantalla 7 no se descartan en Pantalla 6 por el segundo filtro de tramos. El cargo Balboa → Colon Free Zone (Merchant) queda disponible para comparar si cumple su contexto de Pricing.
- El catálogo opcional validado se asocia a la alternativa actual, con protección de solicitudes atrasadas y consulta opcional independiente ante fallo del contexto general. Precios, CostIds, cantidades y cargos comunes se conservan.
- Regresiones actualizadas para simular eliminación de todos los Optional por `applicableConfiguredCosts()` sin perder los costos de la pantalla siguiente.
- Manifiesto de 17 componentes actualizado; 15 sin cambios de binarios. Infraestructura realtime mantiene bloqueo de producción independiente. CI y staging previos a publicación.

## [1.106.5] - 2026-11-20 (DH-20261120-MERCHANT-OPTIONAL-SCREEN6-347 · selección Merchant/Naviera Pantalla 6)

- PATCH coordinado DholeSystem/DholeWeb 1.106.4 → 1.106.5. Los cargos opcionales de transporte disponibles en Pantalla 7 se consultan previamente en Pantalla 6, resolviendo el Inland Balboa → Colon Free Zone (Merchant) que no se ofrecía en la alternativa.
- La carga combina CostIds por ruta y descarta solicitudes obsoletas entre cambios de POE/POD, naviera, agente y servicios. Se preservan cargos fijos comunes, bases por contenedor, contexto comercial CRM y las APIs REST/SignalR actuales.
- Se agregaron pruebas de regresión para carga de catálogo opcional en Pantalla 6, sincronización de elección y protección ante respuestas antiguas.
- Manifiesto global de 17 componentes actualizado. DholePricingService y otros 14 servicios sin cambios binarios. CI y staging obligatorios antes de producción.

## [1.106.4] - 2026-11-20 (DH-20261120-PRICING-MERCHANT-HAULAGE-346 · Merchant Haulage FCL)

- Promoción selectiva de 1.106.4 a master en DholeWeb y DholeSystem desde ramas intermedias, sin fusionar cambios ajenos acumulados en develop.
- Los cargos Inland Fixed, Variable y Optional configurados para Merchant o Naviera se reconocen según proveedor y POE/POD; las líneas fijas compartidas no se duplican ni se convierten en transporte alternativo.
- 15 servicios adicionales permanecen en sus versiones actuales. Manifiesto de 17 componentes actualizado y sincronizado con Web; REST y SignalR sin modificación.
- Pruebas de Pricing y CI de develop aprobadas; validar CI del candidato de master y comprobar staging antes de autorizar producción.

## [1.106.3] - 2026-11-20 (DH-20261120-PRICING-IMPORT-COSTS-345 · costos FCL importación por contexto válido)

- PATCH coordinado DholeWeb/DholeSystem 1.106.2 → 1.106.3. Se muestran costos activos que ya pasaron la verificación real de Pricing por ruta, proveedor, modalidad, servicios e Incoterm, sin descartarlos por snapshots legados de un único puerto.
- El filtro de respaldo sobre catálogo general conserva coincidencias estrictas para evitar cargos de otras rutas. En Pantalla 7, cargos de origen, documentación y destino no desaparecen por la responsabilidad del comprador según el Incoterm; la selección de Transporte Internacional sigue controlando el flete.
- Soporte de etapas manuales en ambos asistentes y pruebas de regresión para CIF importación con cargos heterogéneos. DholePricingService continúa en 1.26.3 sin cambios de código; restantes 14 componentes sin cambios.
- Manifiesto global de 17 componentes actualizado, sin migraciones ni cambios REST/SignalR. CI y staging pendientes; producción no autorizada.

## [1.106.2] - 2026-11-20 (DH-20261120-INCOTERM-QUOTED-FREIGHT-344 · flete internacional contratado bajo cualquier Incoterm)

- PATCH coordinado para LTL/LCL/FTL/FCL/aéreo. CPT y demás Incoterms permiten agregar cargos de Transporte Internacional cuando el servicio está contratado; no se confunde responsabilidad comercial con prohibición del rubro.
- DholePricingService 1.26.2 → 1.26.3: validación de distribución por contenedores únicamente para flete FCL explícito, preservando cotizaciones de sólo cargos aduaneros y el flete en ediciones.
- DholeWeb/DholeSystem 1.106.1 → 1.106.2: UI conserva las líneas seleccionadas por servicio en todos los Incoterms; se mantiene la compatibilidad REST/SignalR y la composición de cargos terrestres.
- Manifiesto de los 17 repositorios actualizado; 14 restantes sin cambios binarios. Pruebas CI/staging pendientes y sin despliegue autorizado a producción.

## [1.106.1] - 2026-11-20 (DH-20261120-CRM-PRICING-PREFERRED-ALIAS-343 · tarifas preferenciales CRM por identidad de cuenta y ruta)

- PATCH coordinado DholeSystem/DholeWeb 1.106.0 → 1.106.1. Pricing utiliza identidad de cuenta CRM en sus cachés e identifica equivalencias de catálogo por ID real (POL, POE, POD y naviera) sin aplicar preferencias ajenas.
- Precio de venta preferencial y cargos manuales se recalculan por alternativa al reconciliar el contexto, preservando costos proveedor, cantidad, unidades, impuestos y cotizaciones persistidas; rechazo de respuestas CRM malformadas.
- Manifiesto y pruebas regresivas del caso de seis ítems FCL CIF 40HC/ONE/Caldera/San José; servicios CRM/Pricing no cambian binarios y conservan REST/SignalR.
- CI del PR Web y deploy de staging completados; pruebas UAT autenticadas con cliente real pendientes. Release a master solicitado por usuario.

## [1.106.0] - 2026-11-20 (DH-20261120-OPERATIONS-TRAMITES-UX-332 · Trámites, drawer y expediente completo)

- MINOR coordinado Web/System/Operations: Trámites es entrada única para listar, buscar, crear apertura manual con cuenta CRM y ver un resumen en drawer.
- Cada IDTRA abre expediente de pantalla completa con ocho tabs, permisos por sección/equipo calculados por backend, QUO persistida, etapas, hitos, tareas, doble validación y bitácora privada autorizada.
- Modificaciones a Aperturas requieren versionado, scope y relación con el trámite; cambios auditados y propagados mediante Outbox/SignalR con reconsulta REST y recuperación ante desconexión.
- Versiones Web/System 1.105.2 → 1.106.0, Operations 0.13.0 → 0.14.0; restantes 14 componentes se conservan.
- La apertura automática desde QUO aceptada, importación de IDTRA históricos Dynamics y workflows avanzados de áreas aún no están implementados.
- CI y staging pendientes. Producción no autorizada para este release.

## [1.105.2] - 2026-11-20 (DH-20261120-CRM-PREFERRED-BLOCKS-342 · consolidación de bloques preferenciales CRM)

- PATCH: DholeWeb 1.105.2 reconcilia acuerdos CRM con líneas de Pricing por servicios seleccionados y CostId/identidad del cargo, conserva costos y cotizaciones históricas, y presenta los seis ítems preferenciales de una misma ruta como bloque comercial editable, incluidos los manuales.
- Pruebas para CIF/40HC/ONE/Caldera/San José, unidades comerciales, moneda y matching seguro; API, SignalR y microservicios sin cambios. CI y staging requeridos antes de master.

## [1.105.1] - 2026-11-20 (DH-20261120-PRICING-CRM-PREFERRED-RUNTIME-331 · restaurar beneficios preferenciales CRM en Pricing)

- PATCH: reparación en DholeWeb del cargador efectivo de costos generado por Vite: ahora recupera los acuerdos de la cuenta CRM y aplica la venta preferencial por CostId, ruta, naviera, servicio, equipo e Incoterm, sin cambiar el costo del proveedor ni las cotizaciones emitidas.
- Se agrega comprobación automática del resultado final de transformaciones, prueba de regresión y contador de líneas preferenciales efectivamente aplicadas. System/Web 1.105.0 → 1.105.1; CRM 1.42.8 y demás componentes sin cambios. CI/staging obligatorios.

## [1.105.0] - 2026-11-20 (DH-20261120-OPERATIONS-APERTURES-330 · Aperturas manuales, Dashboard y Trámites)

- MINOR coordinado DholeSystem/Web/Operations: formularios de Aperturas asistidos por CRM, consultas paginadas y seguras, indicadores por origen y navegación de expediente con ocho tabs.
- Web/System 1.104.5 → 1.105.0; Operations 0.12.0 → 0.13.0. Se conservan las versiones de los otros 14 microservicios y componentes en el manifiesto central.
- La integración definitiva Pricing → Operations para crear automáticamente un IDTRA requiere evento durable, snapshot de la opción aceptada, resolución segura de CRM e Inbox idempotente; **pendiente**, no simulada.
- CI, staging, política de ramas y autorizaciones de producción por validar. No desplegar automáticamente a master.

## [1.104.5] - 2026-11-20 (DH-20261120-PRICING-CRM-PREFERRED-324 · precios preferenciales de CRM)

- PATCH: Pricing aplica automáticamente ventas preferenciales CRM en cargos coincidentes del cliente. Mantiene costo proveedor y cotizaciones persistidas.
- Web/System 1.104.5; CRM 1.42.8. Release coordinado con manifiesto, CI/staging pendientes.

## [1.104.4] - 2026-11-20 (DH-20261120-EXPIRED-APPROVAL-SELLER-ACCESS-312 · aprobador nominal desde ventas)

- PATCH: José Pablo, vendedor con autorización nominal, puede revisar y aprobar solicitudes de tarifas vencidas desde Inicio → Dashboard de Ventas; Roy accede desde Inicio. Sin permisos de Pricing ni SuperUsuario adicionales.
- Contador en tiempo real vía SignalR y notificaciones con enlace seguro. DholeSystem/Web 1.104.3 → 1.104.4; Pricing 1.26.1 → 1.26.2.

## [1.104.3] - 2026-11-20 (DH-20261120-CRM-INVITEE-VISIBILITY-323 · promoción a master de invitados en agenda CRM)

- PATCH selectivo de CRM, Web y System: nombres reales de participantes internos, visibilidad de actividades en calendarios de invitados y recarga SignalR tras notificaciones o desconexiones.
- Global Web/System master 1.103.24 → 1.104.3 y CRM 1.42.6 → 1.42.7, en sincronía con develop. Sin cambios en los otros 14 componentes.
- CI, despliegue y validación real de staging son obligatorios antes de merge a master; producción solicitada por el usuario pero no desplegada sin gates.

## [1.103.24] - 2026-11-20 (DH-20261120-PRICING-COUNTRY-OPTIONS-310 · corrección del wizard de tarifas en blanco)

- PATCH: reparar TypeError pricingQuoteCountryOptions undefined al abrir Crear tarifa; la vista consume las opciones de países desde el catálogo reactivo de Config en ambas pantallas, sin acceso a computed susceptible a transformaciones Vite.
- Añade regresión de selector de país y comprobación del bundle minificado que falla si reaparece el símbolo sin enlace. Se conservan países CRM, país de POL/POD, impuestos, los contratos REST y SignalR sin cambios.
- Web/System 1.103.23 → 1.103.24; demás 15 componentes permanecen en sus versiones previas. CI y validación de staging antes de master.

## [1.103.23] - 2026-11-20 (DH-20261120-PRICING-CLIENT-COUNTRY-298 · corrección de país CRM en cotizaciones FCL)

- PATCH: promoción selectiva del fix probado en develop: permitir seleccionar en la pantalla 3 el país del cliente si CRM no lo proporciona; el país de la cotización no modifica el registro CRM.
- Resolver país de POL Ho Chi Minh, Vietnam explícitamente como VN incluso con metadata Config incompleta. Se conserva el país del POD para IVA; sin cambios en los contratos REST/SignalR ni backend.
- DholeSystem 1.103.22 → 1.103.23; DholeWeb master 1.103.20 → 1.103.23 en release coordinado; 15 componentes más permanecen en sus versiones actuales. CI y staging requeridos antes de producción.

## [1.103.22] - 2026-11-20 (DH-20261120-CRM-INVITEE-SYNC-309 · persistencia de invitados CRM)

- PATCH: versión coordinada DholeSystem/DholeWeb 1.103.20 → 1.103.22; DholeCRMService 1.42.6. Propaga nuevos invitados a acuerdos pendientes y confirma guardado desde Web.
- Manifiesto de 17 componentes, sin modificar los no afectados; mantiene outbox, SignalR y REST. Se conserva lo previamente integrado de Pricing/CRM y la autorización de master para producción.

## [1.103.20] - 2026-11-20 (DH-20261120-CRM-MANUAL-AMOUNT-297 · reparación guardado manual CRM)

- PATCH: corrige TypeError en el formulario manual de tarifas preferenciales ocasionado por manual.amount.trim() después de v-model type=number.
- Valida importes numéricos y texto con pruebas de regresión; guarda sin bloqueos silenciosos de HTML. Versiones DholeWeb y DholeSystem 1.103.18→1.103.20, resto sin modificaciones.
- REST, CRM, realtime y Pricing compatibles. CI/staging previo a producción.

## [1.103.18] - 2026-11-19 (DH-20261119-SELLER-DASHBOARD-PARITY-295 · dashboards comerciales consistentes)

- PATCH: los indicadores, estados e importes de supervisión con vendedor seleccionado comparten la misma cartera comercial del vendedor, incluyendo asignaciones directas y la última revisión publicada. Corrige discrepancias de 72 vs 31 tarifas; conserva el cálculo del desempeño y el control de permisos.
- Pricing 1.25.3→1.25.4, Web/System 1.103.17→1.103.18; otras 14 versiones inalteradas, sin migraciones o incompatibilidad REST/SignalR. CI y staging antes de la publicación.

## [1.103.17] - 2026-11-19 (DH-20261119-CRM-TIERED-CHECK-293 · corregir 409 de tarifas preferenciales)

- PATCH selectivo System/Web 1.103.15→1.103.17 y CRM 1.42.2→1.42.3. CRM amplía CHECK para TIERED_SALE y conserva todos los datos; Web no reenvía cargos ya guardados.
- Validación de migración en staging completada. CI y staging del frontend antes del master. REST/SignalR permanecen compatibles.

## [1.103.15] - 2026-11-19 (DH-20261119-DASHBOARD-TABLE-293 · backport master dashboard de ventas)

- PATCH: backport aislado de DholeWeb/DholeSystem 1.103.14→1.103.15, sin fusionar ramas divergentes.
- Las tarjetas comerciales seleccionan el estado de la tabla del dashboard y desplazan a su encabezado. El selector de cliente solo usa nombres de registros visibles y autorizados; la paginación se reinicia.
- Conserva los otros 15 servicios, APIs REST, eventos SignalR y permisos. CI del backport y validación de staging previas al merge; no autorizado el despliegue a producción.

## [1.103.14] - 2026-11-19 (DH-20261119-DASHBOARD-PERFORMANCE-292 · fórmula comercial corregida)

- PATCH: las abiertas se excluyen del total de cotizaciones entregadas; las rechazadas sí permanecen en el denominador y las vencidas restan en el numerador. Desempeño = (aceptadas − vencidas) / (total cotizadas − abiertas) × 100.
- Incluye reporte general de Ventas 1.103.13, filtros por fecha/vendedor/modalidad y categorías monetarias. Se conservan versiones de los otros 15 componentes, REST y SignalR. Requiere staging previo a master.

## [1.103.13] - 2026-11-19 (DH-20261119-DASHBOARD-GLOBAL-FILTER-291 · dashboard comercial global)

- PATCH DholeWeb/DholeSystem 1.103.12 → 1.103.13. Filtros globales de fecha, vendedor y modalidad en dashboard de Ventas y reportería.
- Desempeño = (abiertas + aceptadas − vencidas) / cotizadas no canceladas × 100. Importes por moneda: aceptadas, abiertas, enviadas + vencidas, rechazadas, total cotizado.
- Conserva la funcionalidad de vencimientos de Pricing 1.25.3 y otros 14 componentes. Sin nuevos contratos ni permisos, requiere CI y staging previos a master.

## [1.103.12] - 2026-11-19 (DH-20261119-PRICING-EXPIRY-1D-SYSTEM-291 · aviso de vencimiento al vendedor)

- PATCH coordinado de DholeSystem y DholeWeb 1.103.11→1.103.12, Pricing 1.25.2→1.25.3. Las otras 14 versiones no cambian.
- Se añade recordatorio System/SignalR un día antes del vencimiento de una tarifa enviada, con destinatario vendedor autorizado, enlace, cliente y fecha. El correo existente sigue activo, con idempotencia separada por canal.
- Migración compatible de marcador PostgreSQL y outbox transaccional. Se mantienen REST, seguridad e infraestructura realtime. CI y staging requeridos; despliegue de producción no autorizado.

## [1.103.11] - 2026-11-19 (DH-20261119-CRM-INVITATIONS-SAVE-290 · guardado de invitados CRM)

- PATCH: DholeSystem y DholeWeb 1.103.10 → 1.103.11, DholeCRMService 1.42.1 → 1.42.2. Manifiesto de 17 componentes, incrementando únicamente los tres repositorios afectados.
- Backend usa directorio Auth autorizado y conserva invitaciones/realtime individuales durables; REST y SignalR compatibles.
- Requiere CI, staging y aprobación explícita de producción antes de master; no desplegar automáticamente aún.

## [1.103.10] - 2026-11-19 (DH-20261119-CRM-FOLLOWUP-EDIT-PROMOTION-286 · promoción de editor de seguimientos CRM)

- PATCH: promueve el editor de seguimientos/recordatorios validado en staging, con cambios de asunto, responsable, fechas, invitados y avisos, auditados y versionados.
- Release coordinado DholeSystem/DholeWeb 1.103.9 → 1.103.10 y DholeCRMService 1.42.0 → 1.42.1. Conserva los cambios del release de tarifas preferenciales 285 ya integrado en master.
- REST y SignalR existentes se mantienen; se respetan los permisos y la infraestructura de recordatorios durables. CI de master obligatorio.

## [1.103.9] - 2026-11-19 (DH-20261119-CRM-MANUAL-BENEFITS-285 · backport del guardado de cargos manuales CRM)

- PATCH: sincroniza DholeSystem/DholeWeb 1.103.8→1.103.9; conserva las correcciones posteriores del wizard Pricing y resto del ecosistema.
- Web muestra los ítems manuales guardados y confirma su persistencia a través de la API CRM antes de limpiar el formulario, sin modificaciones en el servicio CRM ni SignalR.
- Release en rama intermedia sobre master; validación CI y despliegue automático tras merge a master.

## [1.103.8] - 2026-11-19 (DH-20261119-PRICING-LTL-DDP-FREIGHT-284 · DDP LTL/FTL a producción)

- PATCH de promoción selectiva Web/System 1.103.7→1.103.8 y DholePricingService 1.25.1→1.25.2: el flete internacional explícito de LTL/FTL bajo DDP no debe rechazarse como distribución FCL. Caso corregido: USD 50/CBM, 33.33 CBM, equipo terrestre 24.
- Se conserva el esquema, los contratos REST y SignalR, la exclusión marítima CIF/FCL y todos los módulos preexistentes de master. Los otros 14 componentes mantienen su SemVer en el manifiesto; CRM master 1.42.0 no se reemplaza por develop.
- Pruebas CI y despliegues staging de Pricing/Web aprobados; promoción master autorizada por usuario con validaciones y despliegue de producción automatizado sujetos a workflows.

## [1.103.7] - 2026-11-19 (DH-20261119-PRICING-LTL-MANUAL-ENDTOEND-278 · reparación integral de LTL propio manual)

- PATCH DholeWeb/DholeSystem 1.103.6→1.103.7: la fuente propia manual LTL es válida en pantalla 5 y 6 y se mantiene en borradores; los importes de flete se conservan.
- Recupera el país desde la cuenta CRM al retomar solicitudes de Ventas. Cuando el cliente no tiene país, Pricing puede seleccionarlo para la QUO sin cambiar el CRM ni presumir dirección comercial.
- Pruebas Pricing y CI/staging antes de master. Los 15 restantes componentes, contratos REST, SignalR, permisos y bases de datos se mantienen.

## [1.103.6] - 2026-11-19 (DH-20261119-PRICING-LTL-STEP6-277 · pantalla 6 LTL manual)

- PATCH coordinado DholeWeb/DholeSystem 1.103.5→1.103.6. El botón Continuar acepta flete LTL/FTL terrestre con moneda, costo y venta válidos sin exigir naviera oculta; mantiene el agente obligatorio de coloader manual.
- El resumen de validaciones coincide con campos visibles. Se preservan los otros 15 componentes, permisos, APIs REST y SignalR.
- Ramas intermedias, compilación CI y staging antes de master, validación del despliegue de producción posterior.

## [1.103.5] - 2026-11-19 (DH-20261119-PRICING-COUNTRY-LTL-276 · promoción aislada de país CRM y LTL manual)

- PATCH master 1.103.2→1.103.5 en DholeWeb y DholeSystem. No arrastra releases de CRM 1.103.3/1.103.4 ni altera las versiones de otros 15 componentes. La versión global coincide con staging 1.103.5.
- Pricing corrige selección de países CRM desde Config/countries y mantiene tasas IVA de country-vat-rates. LTL incorpora captura propia manual separada de coloaders.
- Sin migraciones, scopes ni cambios REST/SignalR. CI de master y staging confirmados antes del release.

## [1.103.2] - 2026-11-19 (DH-20261119-WIZARD-ROUTE-RUNTIME-274 · corrección de runtime de wizard)

- PATCH: sincroniza DholeSystem y DholeWeb 1.103.1→1.103.2 para reparar la referencia `resolveClientRouteOperation` no definida en el bundle productivo. Web calcula operación desde CRM/POL/POD en variables existentes, sin helper intermedio.
- Nueva validación del bundle minificado y prueba de regresión; se conservan los 15 componentes restantes y las APIs REST/SignalR.
- CI y staging obligatorios previos a promoción master. Release coordinado sin cambios de infraestructura.

## [1.103.1] - 2026-11-19 (DH-20261119-WIZARD-ROUTE-REF-273 · corrección de error de apertura Pricing)

- PATCH: release coordinado System/Web 1.103.0→1.103.1 para eliminar la referencia de runtime `routeOperation` en el wizard «Crear tarifa».
- Sin modificaciones a servicios backend, APIs, datos ni eventos SignalR; componentes restantes conservan versiones existentes y se documentan en manifiesto.
- Cambios sobre ramas intermedias aisladas; CI, pruebas funcionales y staging obligatorios antes de master. La autorización de despliegue productivo permanece false.

## [1.103.0] - 2026-11-19 (DH-20261119-PRICING-RETURN-PROMOTION-272 · promoción devolución Pricing)

- MINOR: DholeWeb/System 1.102.0→1.103.0, Pricing 1.25.0→1.25.1, el manifiesto incluye los tres componentes incrementados y conserva los demás 14.
- Promover el flujo de devolución con motivo obligatorio, notificaciones System/Email y reenvío de Ventas. No modificar archivos de infraestructura ni deploy.
- CI y staging completados para la implementación previa; verificar la promoción coordinada. Solicitud expresa de master recibida; la bandera de autorización para despliegues generales de infraestructura permanece desactivada.

## [1.102.0] - 2026-11-19 (DH-20261119-PRICING-CLIENT-COUNTRY-PROD-271 · Incoterms según país CRM)

- MINOR: incorpora en master la perspectiva de cliente para cargas POL/POD, con la API CRM countryId y la adaptación de responsabilidad de Incoterms/flete en Web.
- Global System 1.101.0 → 1.102.0, Web 1.100.1 → 1.102.0, CRM 1.41.0 → 1.42.0; servicios no afectados mantienen versión, compatibilidad REST/SignalR, sin migraciones.
- Se conserva el cambio CRM-PREFERENTIAL-ROUTE-271; ramas aisladas, CI y staging antes de despliegue productivo expresamente autorizado.

## [1.100.1] - 2026-11-19 (DH-20261119-CRM-PREFERENTIAL-ROUTE-271 · Backport de filtro de puertos)

- PATCH: registro de la corrección Web que impide listar costos con POE/POD diferentes de los seleccionados aunque esté activo mostrar todos los ítems.
- Conserva las versiones de servicios y demás funcionalidades existentes en master; CRM se mantiene en 1.41.0.
- Web/System 1.100.0 → 1.100.1; manifiesto central actualizado; producción manual requiere autorización separada.

## [1.100.0] - 2026-11-19 (DH-20261119-CRM-PREFERENTIAL-MATCH-270 · manifiesto del backport preferencial)

- MINOR: versión Web/System 1.98.0 → 1.100.0 y CRM 1.39.0 → 1.41.0 para el matching por servicio e ítems manuales.
- Conserva versionado de los 17 componentes no modificados y cambios de master preexistentes.
- Migración aditiva de ServiceCodes en CRM sin modificar los costos de Pricing ni la infraestructura realtime.
- CI y staging antes de producción; no ejecuta despliegue manual.

## [1.98.0] - 2026-11-19 (DH-20261119-CRM-PREFERENTIAL-SCOPE-267 · backport scope CRM)

- MINOR: sincroniza Web/System 1.97.9 → 1.98.0 y CRM 1.38.0 → 1.39.0 por la persistencia de naviera e Incoterm en tarifas preferenciales.
- Mantiene release previo de CIF y componentes no incluidos; manifiesto completo de servicios conservado.
- Incluir verificación de CI y staging antes de integrar en master; producción sin autorización expresa de despliegue.

## [1.97.9] - 2026-11-19 (DH-20261119-GCF-CIF-268-MASTER · GCF mundial y CIF sin flete)

- PATCH coordinado: DholeWeb y DholeSystem master 1.97.8 → 1.97.9. Backport del release develop 1.98.1, sin integrar funcionalidades nuevas de CRM.
- Metadata de Grupo Castro Fallas materializa los 249 países ISO 3166-1 y habilita el agente global en cualquier POL.
- El control de nueva tarifa duplicada FCL no exige flete marítimo si la importación CIF/CFR ya lo incluye. FOB/EXW importación y CIF exportación siguen validados.
- Otros servicios conservan versiones, contratos REST y arquitectura realtime. Integración y despliegue automático sujetos a verificaciones CI de master.

## [1.97.8] - 2026-11-19 (DH-20261119-DHOLE-REBRAND-266 · Identidad Dhole System en master)

- PATCH: coordina DholeWeb master 1.97.8 para adoptar el nombre e icono Dhole System y eliminar Orvelum de la interfaz.
- Preserva el release previo GCF mundial 1.97.7. Staging ya validado a nivel de versión 1.97.7; sin cambios de servicios backend o contratos API.
- CI y verificación del despliegue productivo obligatorios.

## [1.97.7] - 2026-11-19 (DH-20261119-GCF-ALL-COUNTRIES-266 · Promoción GCF a master)

- PATCH: cobertura mundial de Grupo Castro Fallas; todos los países, metadatos conservados, prioridad de agentes locales.
- Cambio validado en develop versión 1.97.5, promocionado sobre master versión 1.97.6 sin alterar corrección CIF ni identidad Orvelum System.
- Versión global, DholeWeb y DholeSystem 1.97.6 → 1.97.7; demás servicios sin cambios.
- CI obligatoria; no despliegue manual.

## [1.97.6] - 2026-11-19 (DH-20261119-PRICING-CIF-NAV-265 · CIF importación: avance a costos sin alternativas marítimas)

- PATCH: DholeSystem y manifiesto universal sincronizados con la corrección de DholeWeb al avanzar CIF/CFR sin alternativas marítimas.
- Release global 1.97.6; las versiones intermedias 1.97.4 y 1.97.5 se reservaron para cambios de staging que no se promoverán junto a este parche, por lo que master pasa directamente desde 1.97.3.
- Conserva Orvelum System y todas las funcionalidades productivas existentes. Sin despliegue de producción hasta validación de staging y autorización expresa.

## [1.97.3] - 2026-11-19 (DH-20261119-PRICING-CIF-NO-FREIGHT-262 · Importación CIF sin flete marítimo adicional)

- PATCH coordinado de DholeSystem: versión global 1.97.2 → 1.97.3 junto con DholeWeb para corregir el flujo de importación CIF FCL.
- Sin cambios en contratos API, datos persistidos, roles ni arquitectura realtime; solo versionamiento y manifiesto de release.
- Mantiene Orvelum System en master/producción. CI y staging obligatorios antes de master.

## [1.97.3] - 2026-11-19 (DH-20261119-PRICING-CIF-NO-FREIGHT-262 · Importación CIF sin flete marítimo adicional)

- PATCH coordinado de DholeSystem: actualización de manifiesto y versión global 1.97.2 → 1.97.3 junto con DholeWeb para el ajuste CIF FCL.
- Importación CIF no debe exigir ni crear un nuevo flete marítimo; no se cambian contratos API, realtime, roles ni datos persistidos.
- Mantener Orvelum System en master/producción. Validar CI/staging antes de integrar a master y desplegar producción.

## [1.97.2] - 2026-11-19 (DH-20261119-ORVELUM-TRANSPARENT-261 · Orvelum adaptable al tema)

- PATCH de producción: icono Orvelum transparente en sidebar/login, sin superficie azul oscuro; adaptado a variables del tema actual.
- Favicon Orvelum transparente. Las versiones comerciales Web/System quedan coordinadas sin afectar el Dashboard de Operaciones 1.97.1.
- En develop/staging se conserva el nombre visible Dhole; no se alteran APIs, servicios ni scopes.

## [1.97.1] - 2026-11-19 (DH-20261119-OPS-DASHBOARD-UX-257 · Rediseño de Dashboard de Operaciones)

- PATCH: Web integra una cabecera compacta, selector de rol/equipo, cuatro KPI y listado de Aperturas con estado vacío reducido y sin ceros aparentes durante la carga.
- System/Web 1.97.0 → 1.97.1, sin actualizar otros componentes ni afectar el cambio de marca Orvelum 1.97.0. Preparado para master, producción sin autorización.

## [1.97.0] - 2026-11-19 (DH-20261119-ORVELUM-BRAND-256 · Orvelum System)

- MINOR: identidad comercial Orvelum System; imagen orbital y favicon integrados en DholeWeb.
- Versiones comerciales Web/System sincronizadas en 1.97.0, sin renombrar repositorios, APIs, servicios ni permisos internos.
- Título de las pestañas del navegador con versión real y textos localizados.

## [1.96.1] - 2026-11-19 (DH-20261119-OPS-SIDEBAR-255 · Navegación de Operaciones)

- PATCH: DholeWeb retira solo «Aperturas» del sidebar bajo Operaciones. Conserva el módulo, los permisos y el acceso desde Dashboard.
- DholeSystem/DholeWeb 1.96.0 → 1.96.1; otros componentes sin cambios y con sus versiones existentes. Promoción a master pendiente de staging/CI y autorización.

## [1.96.0] - 2026-11-19 (DH-20261119-OPS-ROLE-TEAM-DASHBOARD-254 · Dashboard operativo por rol y equipo)

- MINOR: Promoción coordinada desde develop, con staging validado: DholeSystem y DholeWeb 1.95.1 → 1.96.0; DholeOperationsService 0.11.0 → 0.12.0.
- Dashboard por rol/Equipo, Aperturas y doble validación; acceso por scopes, pertenencia y tenant. Diseño de Equipos y Pricing actualizado.
- Los restantes componentes conservan sus versiones; promoción selectiva para no incorporar cambios no relacionados con master.

## [1.95.1] - 2026-11-19 (DH-20261119-DH-MULTISELECT-OVERLAY-253 · overlay sólido DhMultiSelect)

- PATCH: versionado global System/Web 1.95.1, compatible con el release Blobatar 1.95.0 y la arquitectura de Operaciones.
- Cambios visuales únicamente en DholeWeb; Auth, Operations y el resto de servicios permanecen sin cambios.

## [1.95.0] - 2026-11-19 (DH-20261119-BLOBATAR-TRANSPARENT-252 · Mascota Blobatar permanente)

- MINOR: DholeWeb presenta mascota siempre disponible sin foto, personalización de seis accesorios, fondo transparente y nombre/emoción visibles solo al pasar el cursor o enfocar con teclado.
- Coordinación de DholeWeb y DholeSystem 1.95.0; restantes componentes mantienen sus versiones propias sin modificar código.
- CI/staging antes de master y promoción productiva sujeta a autorización expresa.

## [1.94.0] - 2026-11-19 (DH-20261119-OPS-TEAM-BULK-251 · asignación múltiple en Operations)

- MINOR: release coordinado: Web/System 1.94.0, Operations 0.11.0 y Auth 1.16.2.
- El directorio de Auth admite variantes históricas del rol Operativo Logístico; la pantalla asigna múltiples integrantes con DhMultiSelect y el backend valida/audita un lote atómico.

## [1.93.0] - 2026-11-19 (DH-20261119-BLOBATAR-MASCOT-250 · Blobatar como mascota del sistema)

- MINOR: DholeWeb incorpora cinco emociones adicionales (58 en total), foto local de perfil y mascota Blobatar con nombre, movimiento fijo/libre, posición persistente, accesibilidad y configuración ES/EN.
- Release unificado Web/System 1.93.0, sin incrementar los restantes 15 servicios del manifiesto al no cambiar su código.
- Pruebas CI, verificación de staging y autorización de despliegue productivo obligatorias.

## [1.91.1] - 2026-11-19 (DH-20261119-OPS-ROLE-NAME-248 · rol Operativo Logístico)

- PATCH: paridad System/Web 1.91.1 y Auth 1.16.1. El pool de Operaciones usa el rol existente «Operativo Logístico», sin crear roles adicionales.
- Conserva Operations 0.10.0 y el release funcional DH-247 con su auditoría y DhSelect.

## [1.91.0] - 2026-11-19 (DH-20261119-OPS-AUDIT-ROLE-247 · Operaciones, auditoría y roles)

- MINOR: manifiesto global de 17 componentes actualizado para coordinación de Auth, Operations y Web; Web/System conservan la misma versión y comprobación de actualizaciones.
- Release coordinado DholeWeb/DholeSystem 1.89.0→1.91.0; Auth 1.15.0→1.16.0; Operations 0.9.0→0.10.0. Ecosistema 1.91.0. CI/staging y comprobación de producción obligatorias.

## [1.89.0] - 2026-11-18 (Sincronización Web/System y actualización de pestañas)

- MINOR DH-20261118-WEB-VERSION-SYNC-236: DholeWeb y DholeSystem pasan a compartir la versión 1.89.0 como contrato obligatorio para todos los releases posteriores.
- El manifiesto central y los validadores impiden publicar una versión de Web diferente de System; la web comprueba /version.json y notifica actualizaciones sin recargar formularios automáticamente.
- Componentes: DholeSystem 1.88.0 → 1.89.0; DholeWeb 1.84.0 → 1.89.0. CI y staging pendientes; producción no autorizada.

## [1.88.0] - 2026-11-18 (CRM Prospectos: contactos, zonas y fuentes comerciales)

- MINOR DH-20261118-CRM-PROSPECT-235: captura comercial con nombre y razón social independiente, catálogo de captación, referido y notas iniciales.
- Alta y gestión de contactos y ubicaciones jerárquicas antes de convertir a Cuenta.
- Conversión transaccional de contactos y direcciones, con scopes y realtime Outbox existentes.
- DholeWeb 1.84.0, DholeCRMService 1.38.0, DholeConfigService 1.12.0, DholeSystem 1.88.0.
- Cambios en rama master candidata: solo promover tras CI, staging y autorización de producción.

## [1.87.4] - 2026-11-18 (Ventas: retiro de cancelación de cotizaciones a vendedores)

- PATCH DH-20261118-SELLER-CANCEL-HIDE-234: botón «Cancelar cotización» eliminado del dashboard comercial en móvil/escritorio y del detalle de vendedores; el modal de ventas ya solo admite aceptación o rechazo.
- La cancelación de cotizaciones aceptadas permanece en Pricing con permisos y auditoría. No se alteran servicios backend, contratos REST, SignalR, Outbox ni scopes.
- DholeWeb 1.83.0 → 1.83.1; DholeSystem/ecosistema 1.87.3 → 1.87.4. Los 15 componentes restantes conservan sus versiones en el manifiesto.
- CI y staging autenticado son obligatorios antes de master. No se autoriza despliegue productivo.

## [1.87.3] - 2026-11-18 (Fix PostgreSQL 22001 al actualizar IDTRA múltiples)

- PATCH DH-20261118-RATE-REVISION-IDTRA-232: persistencia histórica de revisiones RateRevisions.IdtraNumber amplía de varchar(100) a varchar(2000), igual que cabecera para soportar múltiples IDTRA en la misma QUO. Caso reproducible: 366 caracteres para QUO-00000-000552.
- Migration no destructiva y pruebas de largo de IDTRA, mapeo EF y compatibilidad con datos existentes. No altera contratos REST, scopes, realtime, Outbox ni auditoría.
- Versiones: DholePricingService 1.24.8→1.24.9, DholeSystem/ecosistema 1.87.2→1.87.3. CI y staging antes de producción.

## [1.87.2] - 2026-11-18 (Diagnóstico seguro de error 500 al guardar Pricing)

- PATCH DH-20261118-PRICING-SAVE-DIAG-231: diagnóstico de solo lectura de categorías de excepción y códigos PostgreSQL en los logs del contenedor de Pricing, sin volcar solicitudes, datos de clientes ni secretos.
- DholeSystem/ecosistema 1.87.1→1.87.2; microservicios permanecen con su versión anterior. No se modifica producción, migraciones, REST, scopes, realtime ni auditoría. La corrección funcional se abordará según la excepción concreta.

## [1.87.1] - 2026-11-18 (Pricing: backport guardar fechas comerciales sin error UTC)

- PATCH DH-20261118-PRICING-SAVE-500-230: guardado de cotizaciones nuevas/editadas normaliza fechas comerciales YYYY-MM-DD a medianoche UTC, evitando rechazo de Npgsql frente a PostgreSQL timestamptz.
- Pricing 1.24.7→1.24.8, DholeSystem/ecosistema 1.87.0→1.87.1. Sin migraciones; contratos REST, SignalR/Outbox, AuditLogs y scopes conservados.
- CI, staging y prueba de guardado autenticada obligatorios antes de master; la promoción de master auto-despliega y requiere autorización productiva expresa.

## [1.87.0] - 2026-11-18 (CRM · agenda comercial compartida e invitados internos)

- MINOR DH-20261118-CRM-SHARED-AGENDA-229: invitados de Auth a actividades, llamadas, citas y seguimientos; evento único visible en las agendas de responsable y asistentes, recordatorios individuales Email/System idempotentes, revocación y auditoría.
- DholeSystem/ecosistema 1.86.1 → 1.87.0; DholeWeb 1.82.1 → 1.83.0 y DholeCRMService 1.36.0 → 1.37.0. Los otros 14 componentes conservan la versión correspondiente de master.
- CI y despliegues de ambos servicios en staging superados; promoción a master en revisión antes de los despliegues productivos.

## [1.86.1] - 2026-11-18 (LCL/LTL: peso unitario × cantidad · master)

- PATCH DH-20261118-CARGO-WEIGHT-PER-UNIT-229: promoción selectiva de la corrección integrada y compilada en develop. El peso por unidad se multiplica por cantidad, se refleja en resumen de Ventas y Pricing, y la recarga de cotizaciones evita duplicar el peso persistido.
- Versiones master: DholeWeb 1.82.0→1.82.1, DholePricingService 1.24.5→1.24.7, DholeSystem/ecosistema 1.86.0→1.86.1. Los restantes componentes conservan versiones y comportamiento existentes.
- Staging Web y Pricing desplegados, smoke autenticado aún pendiente. No se modifica REST, SignalR, scopes ni AuditLogs; el despliegue de producción requiere aprobación expresa.

## [1.86.0] - 2026-11-18 (Blobatar: tres emociones personalizadas)

- MINOR DH-20261118-BLOBATAR-MOODS-228: el ecosistema incorpora expresiones Estresado, Cansado y Resignado en DholeWeb, con geometría nativa, transiciones, persistencia por usuario, sincronización de Apariencia y traducciones ES/EN.
- DholeSystem/ecosistema → 1.86.0 y DholeWeb → 1.82.0; los otros 15 componentes mantienen sus versiones del manifiesto de cada rama, sin tocar APIs REST, permisos, realtime o bases de datos.
- Integración primero a develop, CI y pruebas de staging obligatorios antes de promocionar master. Sin autorización de despliegue a producción.

## [1.84.4] - 2026-11-18 (Pricing: recolecta EXW LCL propio, master backport)

- PATCH DH-20261118-PRICING-EXW-PICKUP-226: promoción coordinada a master desde backport de la corrección EXW de LCL propio. Recupera recolecta editable, conserva importes manuales y limita cargos del catálogo a los aplicables a ruta.
- Actualiza manifiesto central Web 1.80.4, Pricing 1.24.5 y System 1.84.4; las demás versiones se mantienen en el manifiesto de master. Este backport no incluye los cambios divergentes de los otros módulos en develop.
- Web/Pricing staging develop desplegados con workflows correctos; compilaciones, CI de backport y smoke autenticado pendientes. Producción expresamente autorizada por solicitud del usuario de master.
- Staging comprobado: Pricing https://github.com/CustomCodeCR/DholePricingService/actions/runs/44381748194 y Web https://github.com/CustomCodeCR/DholeWeb/actions/runs/44381755824 (ambos success). CI de backport debe superar controles propios de master antes de integrar.

## [1.83.6] - 2026-11-18 (MultiQUO: identidad comercial consolidada)

- PATCH DH-20261118-MULTIQUO-SINGLE-223: una QUO base en listado, búsqueda y reportes, con alternativas A/B dentro del detalle y aceptación única del grupo. La opción no elegida permanece en historial sin rechazo comercial independiente.
- master: DholeSystem 1.83.5 → 1.83.6, Pricing 1.23.9 → 1.23.10, Web 1.79.4 → 1.79.5; otros 14 componentes conservan versión. Mantiene correcciones recientes de reservas, permisos, AuditLogs, REST y SignalR.
- Promoción coordinada por PR y CI; no incluye despliegue manual a producción.

## [1.83.5] - 2026-11-18 (Pricing: corregir transacciones de reservas)

- PATCH DH-20261118-PRICING-LEASE-TX-222: se corrige el HTTP 503 confirmado por el trace 0HNQ5JP78QTL4:00000009. Las transacciones de claim, heartbeat y release-own se ejecutan íntegramente en la estrategia de reintentos Npgsql/EF Core.
- master: DholeSystem 1.83.4 → 1.83.5; DholePricingService → 1.23.9; DholeWeb y restantes 14 componentes sin cambio. Mantiene scopes, AuditLogs y SignalR; CI/staging obligatorios antes de producción.

## [1.83.4] - 2026-11-18 (Pricing: evitar error inesperado al abrir solicitud)

- PATCH DH-20261118-PRICING-LEASE-220: reserva de Pricing con lock transaccional PostgreSQL tipado, errores 409/503 identificables y consulta de reserva inactiva traducible por EF; Web muestra por separado error de claim/lectura y evita reintentos concurrentes.
- master: Web 1.79.4, Pricing 1.23.8, DholeSystem 1.83.3→1.83.4. Los demás 14 componentes mantienen sus versiones actuales. Sin cambios de REST existentes, scopes, auditoría ni SignalR.
- CI, staging autenticado y validación de producción pendientes.

## [1.83.3] - 2026-11-18 (Pricing: recuperación segura de reservas huérfanas)

- PATCH DH-20261118-PRICING-LEASE-219: permite liberar la propia reserva sin volver a reclamarla; reserva ajena solo tras 45 segundos sin heartbeat en el servidor y acción expresa de Pricing. Se preservan bloques realmente activos y el estado de trabajo.
- Versiones coordinadas: DholeSystem 1.83.2 → 1.83.3; DholeWeb 1.79.2 → 1.79.3; DholePricingService 1.23.6 → 1.23.7; los otros 14 componentes sin cambios. REST compatible, SignalR intacto, auditoría de acciones registrada.
- CI, staging y prueba con dos sesiones obligatorios antes de master.

## [1.83.2] - 2026-11-18 (Pricing: detener reapertura automática de bloqueos)

- PATCH DH-20261118-PRICING-LEASE-218: Web elimina claim automático al fallar heartbeat, ofrece liberación de reserva propia y aísla tokens por identidad; Pricing deja una sola reserva por operador y libera antiguas exclusivamente del mismo usuario bajo transacción.
- Versiones coordinadas: System 1.83.1 → 1.83.2, Web 1.79.1 → 1.79.2, Pricing 1.23.5 → 1.23.6; otros 14 componentes preservados. CI, pruebas y staging obligatorios.

## [1.83.1] - 2026-11-18 (MultiQUO: 672-A/B comerciales, sin 673)

- PATCH DH-20261118-MULTIQUO-IDENTITY-217: una sola base de cotización FCL y opciones con sufijo persistente. PricingService 1.23.5 incluye migración para recuperar los números históricos y Web 1.79.1 actualiza listados, búsqueda global y wizard.
- DholeSystem/ecosistema 1.83.0 → 1.83.1; DholeWeb 1.79.0 → 1.79.1; PricingService 1.23.4 → 1.23.5. Demás servicios conservan versiones; se mantienen autorización, auditoría, Outbox y SignalR.
- Validaciones de CI y despliegues staging aprobados en develop; promoción master autorizada expresamente por el usuario.

## [1.83.0] - 2026-11-18 (Apariencia: vista previa grande y modos de Blobatar)

- MINOR DH-20261118-BLOBATAR-APPEARANCE-216: mueve los controles Auto/Fijo al módulo Apariencia con vista previa grande e interactiva del avatar. Pinia sincroniza la expresión del avatar del encabezado y de la vista previa; un único ciclo de 30 s, guardado por usuario, sincronización entre pestañas y respeto a movimiento reducido.
- DholeWeb 1.78.1 → 1.79.0 y DholeSystem/ecosistema 1.82.1 → 1.83.0. Mantiene las versiones de los otros 15 servicios y Gateway de esta rama, incluido el release previo de Pricing, sin alterar REST, SignalR, Auth, permisos ni bases de datos.
- CI, regresiones, build y despliegue de staging requeridos antes de promover a master; no desplegar a producción sin autorización explícita.

## [1.82.1] - 2026-11-18 (Pricing: liberación definitiva de solicitudes)

- PATCH DH-20261118-PRICING-LEASE-214: cierre de solicitudes sin bloqueos fantasma; Web detiene heartbeat y espera release; Pricing rechaza el claim tardío con token obsoleto.
- DholeWeb 1.78.0 → 1.78.1 y Pricing 1.23.3 → 1.23.4; ecosistema DholeSystem 1.82.0 → 1.82.1; otros 14 componentes permanecen en sus versiones actuales.
- Se conservan las preferencias Blobatar del release 215, APIs REST, scopes, auditoría y SignalR. Staging de develop aprobado; validación E2E de dos usuarios pendiente.

## [1.82.0] - 2026-11-18 (Blobatar: expresión guardada y modo automático)

- MINOR DH-20261118-BLOBATAR-PREFERENCES-215: DholeWeb 1.77.2 → 1.78.0 y DholeSystem/ecosistema 1.81.1 → 1.82.0. Persistencia de expresión y modo Auto/Fijo por usuario en almacenamiento local. Auto rota cada 30 segundos mientras la pestaña está activa y no hay reduced-motion; Fijo mantiene la cara escogida.
- Se conserva sin modificar la versión del manifiesto maestro de DholePricingService (1.23.1), así como las de los otros 14 servicios. Pricing 213/214 se versiona de forma independiente, sin mezclarlo en el release de Blobatar. No afecta REST, Auth, SignalR ni permisos.
- CI, SSR, build y staging antes de master. Despliegue de producción solo bajo autorización.

## [1.81.1] - 2026-11-18 (DholeWeb: corrección de modo claro en avatar)

- PATCH DH-20261118-LIGHT-MODE-AVATAR-212: el tema oscuro de Tailwind obedece la clase html.dark de Dhole. La tarjeta del usuario, nombre/correo y la etiqueta de expresión son claros y contrastados en modo claro; el modo oscuro mantiene fondo negro y letras blancas.
- DholeWeb 1.77.0 → 1.77.1; DholeSystem/ecosistema 1.81.0 → 1.81.1. Mantiene intactos los cambios de Operations DH-20261118-OPS-DH-UI-211 y las versiones de los otros 15 componentes. REST, permisos, realtime y datos intactos.
- CI, compilación y staging obligatorios. No desplegar producción sin autorización expresa.

## [1.81.0] - 2026-11-18 (Operations: interfaz Dh para Aperturas y Equipos)

- MINOR DH-20261118-OPS-DH-UI-211: promoción de DholeWeb 1.76.0 → 1.77.0 con componentes Dh, tablas y filtros, modales, asignaciones y trazabilidad; versión global DholeSystem/ecosistema 1.80.0 → 1.81.0.
- Preserva versiones de los demás 15 componentes, servicios REST, scopes, pool de dos validadores, audit log y realtime. Validación de CI/develop aprobada; staging y autorización productiva aún requeridos.

## [1.80.0] - 2026-11-18 (Blobatar: probador interactivo de expresiones)

- MINOR DH-20261118-BLOBATAR-EXPRESSIONS-210: DholeWeb 1.75.0 → 1.76.0, DholeSystem/ecosistema 1.79.0 → 1.80.0. Al pulsar el avatar del usuario muestra cara enojada y permite recorrer las 14 expresiones de Blobatar 2.7.0, manteniendo la pose y mostrando la etiqueta hasta el siguiente clic.
- Conserva modo oscuro negro, seguimiento de ojos, fotografía/prioridad, status, animación ambiental, acceso por teclado y prefers-reduced-motion. El componente genérico mantiene animaciones existentes. No hay cambios de API, realtime, bases ni permisos.
- Se preservan las versiones de los otros 15 componentes de este manifiesto. Validar CI, build, staging y autorización de producción.

## [1.79.0] - 2026-11-18 (Blobatar: fondo negro y animación al tocar)

- MINOR DH-20261118-BLOBATAR-DARK-TAP-209: DholeWeb 1.73.0 → 1.75.0, DholeSystem/ecosistema 1.78.0 → 1.79.0. En modo oscuro, tarjeta y fondo del avatar negros; clic, toque o teclado activan sorpresa, guiño y sonrisa con rebote repetible, respetando movimiento reducido.
- Preserva íntegramente Operations Dual Validation 208: DholeAuthService 1.14.0, DholeOperationsService 0.7.0, además de todas las otras versiones del manifiesto y sus registros históricos. No hay cambios en REST, SignalR, Outbox/Inbox, permisos ni base de datos.
- CI y staging aprobados para DholeWeb; usuario autorizó expresamente promoción a master el 2026-11-18. Validar workflow de producción tras merge; UAT visual autenticado pendiente.

## [1.78.0] - 2026-11-17 (DH-20261117-OPS-DUAL-VALIDATION-208 · Aperturas doble validación)

- MINOR: backend Operations 0.7.0 con pool ponderado de dos validadores independientes, equipos, asignación, decisiones y auditoría persistente local + AuditLogs por Redis Outbox.
- Auth 1.14.0 publica usuarios internos elegibles y scopes para asignación manual; Web 1.74.0 implementa administración de equipos y Aperturas iniciales.
- Ecosistema 1.77.1 → 1.78.0 en 17 componentes; CI y staging obligatorios antes de releases maestros; producción no autorizada.

## [1.77.1] - 2026-11-17 (DH-20261117-OPS-FOUNDATION-205-PROMOTION · Operations a master)

- PATCH: promoción coordinada de DholeOperationsService 0.5.0 → 0.6.0, validado en develop y staging; despliegue a producción autorizado explícitamente.
- Versiones globales DholeSystem 1.77.0 → 1.77.1; preserva Blobatar y los 17 componentes del ecosistema.
- Funcionalidad de Operations v1.2 parcial; las navieras permanecen sin conexión externa y las integraciones pendientes no se anuncian como completas.

## [1.77.0] - 2026-11-17 (Blobatar: expresiones, animación y gaze)

- MINOR DH-20261117-BLOBATAR-MOTION-207: actualización coordinada de DholeWeb 1.72.0 → 1.73.0; DholeSystem y ecosistema 1.75.0 → 1.77.0. Se añaden animación continua de cabeza de usuario, ojos que siguen el puntero en escritorio, expresiones al hover/ocupado/desconectado y halo suave, respetando preferencias de movimiento reducido.
- Manifiesto de los 17 componentes conserva la versión de los 15 microservicios restantes. No hay cambios en REST, SignalR, Outbox/Inbox, bases de datos ni permisos. CI, staging y validación visual pendientes antes de promover a master.

## [1.75.0] - 2026-11-17 (DholeWeb: sistema de avatares Blobatar)

- MINOR DH-20261117-BLOBATAR-206: integra Blobatar 2.7.0 en el componente compartido DhAvatar, reutilizado por los módulos Dhole. Foto primero; fallback SVG local determinístico por ID; iniciales opcionales; estados SignalR sin cambios.
- Versiones coordinadas: DholeSystem/ecosistema 1.74.0 → 1.75.0, DholeWeb 1.71.0 → 1.72.0. Resto de microservicios conservan sus versiones, reflejadas en el manifiesto de 17 componentes.
- Instalación frozen-lockfile, regresión SSR, CI, staging y autorización de producción pendientes; no hay migraciones, API REST ni cambios de eventos realtime.

## [1.74.0] - 2026-11-17 (CRM / Operations: responsables de operaciones por cliente)

- MINOR DH-20261117-CRM-OPS-CONTACTS-204: campos independientes para contacto principal único y múltiples responsables operativos por cuenta CRM. API Operations obtiene sus datos por expediente autorizado, sin replicar contactos; se conserva realtime.
- Versiones: DholeSystem/ecosistema 1.73.2 → 1.74.0, DholeWeb 1.70.1 → 1.71.0, DholeCRMService 1.35.0 → 1.36.0, DholeOperationsService 0.4.1 → 0.5.0.
- Integración develop validada por CI; staging operativo y autorización de producción por confirmar antes del master release.

## [1.73.2] - 2026-11-17 (Ventas: cancelación solo de QUO aceptada)

- PATCH DH-20261117-SELLER-CANCEL-ACCEPTED-203: se corrige el release de cancelación para que únicamente las cotizaciones comerciales con estado AcceptedByClient puedan pasar a Cancelled, tanto en Web como en el dominio de Pricing.
- Coordinación de versiones: DholeWeb 1.70.0 → 1.70.1, DholePricingService 1.23.0 → 1.23.1, DholeSystem/ecosistema 1.72.0 → 1.73.2. Motivo, auditoría, idempotencia y contrato REST/realtime preservados.
- Verificaciones de compilación, CI y staging pendientes; no hay migraciones de base de datos.

## [1.72.0] - 2026-11-17 (Ventas: cancelación de QUO)

- MINOR DH-20261117-SELLER-CANCEL-202: release coordinado DholeWeb 1.69.0 y DholePricingService 1.23.0 para cancelación auditada de cotizaciones por su vendedor.
- Estado Cancelled persistente, motivo obligatorio, autorización por vendedor, idempotencia y compatibilidad con REST/realtime existentes. Se actualiza manifiesto central.
- DholeSystem y ecosistema 1.71.3 → 1.72.0. CI y validación staging pendientes; sin despliegue a producción.

## [1.71.3] - 2026-11-17 (Pricing LCL: no cargar rubros de navieras)

- PATCH DH-20261117-PRICING-LCL-CARRIER-200: Web 1.67.8 → 1.67.9 agrega control universal de cargos navieros para LCL marítimo; evita costos MAERSK y de otras navieras, aun con IDs legacy y respuesta contextual incorrecta.
- System/ecosistema 1.71.2 → 1.71.3; no altera REST, SignalR, Outbox/Inbox ni otros servicios. Revisar CI y staging antes de master; producción no autorizada.

## [1.71.2] - 2026-11-17 (Hacienda: Nginx 400 Request Header Or Cookie Too Large)

- PATCH DH-20261117-HACIENDA-HEADER-BUFFERS-199: DholeWeb 1.67.7 → 1.67.8 corrige rechazo de JWT de 9.5 KB en el servidor Nginx antes del Gateway; buffers acotados (16 KB inicial, 4 × 32 KB para cabeceras grandes).
- Conserva autenticación JWT, scopes, API REST, SignalR, Outbox/Inbox, seguridad y bases de datos. Se reprodujo localmente el 400 con Authorization sintética de 11 KB y se verificó 204 tras ampliar los buffers.
- DholeSystem/ecosistema 1.71.1 → 1.71.2. Validar CI y staging con respuestas autenticadas antes de promover master.


## [1.71.1] - 2026-11-17 (Pricing: sincronizar rubros Ver/Editar)

- PATCH DH-20261117-PRICING-EDIT-ITEMS-198: Web 1.67.6 → 1.67.7 evita que el catálogo agregue cargos extra a las cotizaciones existentes al editar. Refresco explícito en contexto sin cambios solo modifica cargos guardados; conserva seguro, Manejos, HBL y recolecciones.
- DholeSystem/ecosistema 1.71.0 → 1.71.1. Backend, REST, SignalR, Outbox/Inbox, PricingService y base de datos sin modificaciones.
- Staging: despliegue Web run 44187573454 y /health correctos, pruebas CI Pricing y compilación correctas. Autorización expresa para master recibida; smoke autenticado de QUO pendiente.

## [1.71.0] - 2026-11-17 (Hacienda CRM: consulta POST sin identificación en URL)

- MINOR DH-20261117-HACIENDA-POST-197: CRM 1.34.2 → 1.35.0 incorpora POST JSON autenticado para consultas de Hacienda y conserva GET compatible; Web 1.67.5 → 1.67.6 utiliza el nuevo transporte y elimina cookies innecesarias del proxy Nginx.
- El rechazo HTML 400 se diferencia de las validaciones fiscales del backend. No se modifican tablas, datos, permisos, Outbox ni SignalR.
- Ecosistema 1.70.6 → 1.71.0. Release coordinado con ramas intermedias; tests, CI y smoke staging pendientes; producción no autorizada.


## [1.70.5] - 2026-11-17 (MultiQUO: alternativas reales y PDF conjunto en correo)

- PATCH DH-20261117-MULTIQUO-VISIBLE-GROUP-PDF-195: Pricing 1.22.4 y Web 1.67.4 exponen las sub-QUO 672-A y 672-B separadas del RateCode interno, unifican descarga PDF, envío y cierre de solicitud en un único PDF con ambas rutas, y preservan auditoría/realtime.
- No elimina datos históricos de QUO-00000-000673; las coincidencias duplicadas requieren conciliación controlada. Validar email y PDF con registro real en staging antes de promoción. Versión global 1.70.4 → 1.70.5.

## [1.70.4] - 2026-11-17 (MultiQUO: aprobación de alternativas y PDF)

- PATCH DH-20261117-MULTIQUO-APPROVAL-PDF-194: release coordinado DholePricingService 1.22.3 y DholeWeb 1.67.3. El margen de todas las sub-QUO se aprueba conjuntamente; solo una alternativa puede ser aceptada comercialmente.
- Normalización visual QUO-A/QUO-B y exclusión de duplicados huérfanos en el listado agrupado sin eliminación de datos. Requiere CI, smoke en staging, conciliación de duplicados históricos y autorización antes de producción.

## [1.70.3] - 2026-11-17 (DH-193: Hacienda reverse proxy Web-Gateway)
- PATCH DH-20261117-HACIENDA-SAME-ORIGIN-193: mismo origen de Web para Hacienda CRM/SRM, con autenticación/impersonación intactas y Nginx limitado a GET, sin registro de identificaciones fiscales en el access log. Evita el salto del navegador al subdominio API con 502 generado por Cloudflare.
- DholeWeb 1.67.1 → 1.67.2; DholeSystem/ecosistema 1.70.2 → 1.70.3; CRM y los demás servicios conservan versiones y contratos existentes.
- Sin migraciones ni cambios SignalR/Outbox. CI y prueba real de conectividad DNS Web→Gateway + consulta de Hacienda en staging antes de master/producción.

## [1.70.2] - 2026-11-17 (DH-20261117-CRM-HACIENDA-NETWORK-192 · Consulta Hacienda CRM)

- PATCH: DholeWeb 1.67.0 → 1.67.1 y DholeCRMService 1.33.1 (master)/1.34.1 (develop) → 1.34.2; DholeSystem/ecosistema 1.70.1 → 1.70.2. Los demás componentes conservan su versión.
- CRM oculta la identificación y URLs en los errores de red; reintenta una falla de transporte sin repetir HTTP 4xx/5xx y rechaza respuestas incompletas o de otra identificación. El backend permite concurrencia acotada hacia Hacienda y devuelve 503 controlado cuando se satura.
- Sin migraciones, cambio de permisos, REST, SignalR ni Outbox. Validar compilación, pruebas, CI y staging antes de promover a master/producción.

## [1.70.1] - 2026-11-17 (DH-20261117-CONFIG-APT-DEPLOY-191 · Config: evitar Docker build atascado)

- PATCH: Config 1.9.0 → 1.9.1 y DholeSystem/ecosistema 1.70.0 → 1.70.1. DholeWeb 1.67.0 y los otros microservicios conservan sus versiones.
- La imagen de Config y workers aplica límites de 180/300 s y reintentos APT, DNS por red del host durante el build, salida detallada y timeout del job. Un nuevo deploy reemplaza el build de producción atascado sin sustituir contenedores hasta disponer de imágenes completas.
- DH-20261117-CONFIG-APT-DEPLOY-191: sin cambios de base de datos, funciones SRM, REST, SignalR o permisos. Requiere CI y prueba de health posterior al deploy.

## [1.70.0] - 2026-11-17 (DH-190 · SRM: eliminación lógica de proveedores)

- MINOR DH-20261117-SRM-SUPPLIER-DELETE-190: nuevo DELETE SRM autenticado con srm.supplier.archive, comprobación de relaciones antes de archivar y auditoría de la eliminación.
- Modal de confirmación y botón eliminar en directorio y ficha de proveedores; validaciones y mensaje específico si existen contratos/evaluaciones vinculados.
- Release coordinado: DholeWeb 1.66.1 → 1.67.0; DholeConfigService 1.8.1 → 1.9.0; DholeSystem y ecosistema 1.69.2 → 1.70.0; versiones restantes sin modificaciones.
- Realtime de invalidación SRM por Outbox sin publicar datos bancarios; CI y validación de staging pendientes; producción no autorizada.

## [1.69.2] - 2026-11-17 (DH-187 · Operations esquema propio y mensajería framework)

- PATCH coordinado sobre DH-186 SRM (1.69.1): registra Operations 0.4.1 y respeta todas las versiones y configuraciones del release SRM simultáneo.
- DholeOperationsService migra sus 18 tablas de public al esquema operations sin pérdida de información y aplica las entidades y mapeos Inbox/Outbox del mismo CustomCodeFramework que usa DholeConfigService.
- PostgreSQL conserva los eventos, índices y claves foráneas; las pruebas de migración de datos heredados aprobaron 4 tests unitarios y 6 integraciones. No se autoriza producción sin validar staging.

## [1.69.1] - 2026-11-17 (DH-186 · SRM: selects de crédito e IBAN)

- PATCH coordinado: DholeWeb 1.66.0 → 1.66.1; DholeSystem/ecosistema 1.69.0 → 1.69.1. Los otros componentes conservan su versión registrada.
- Los selects de cobertura de crédito no se superponen con campos posteriores. Las cuentas bancarias explican la causa de un IBAN inválido sin omitir checksum MOD-97, cambiar contratos REST/realtime o permisos.
- Candidato de release desde ramas intermedias; CI, pruebas en staging y autorización explícita antes de producción.

## [1.69.0] - 2026-11-17 (DH-185 · Primeras tablas de Operations)

- MINOR: seis nuevas tablas operativas para vinculación de cotización, snapshot informativo de costos y proveedores, hitos, tareas, notas y auditoría.
- Integridad mediante FK al expediente, índices de búsqueda, restricciones de moneda/prioridad, QUO principal único e idempotencia de snapshots.
- DholeOperationsService 0.3.1 → 0.4.0; DholeSystem/ecosistema 1.68.0 → 1.69.0; versiones de los demás microservicios sin alteración.
- Las migraciones son aditivas y se verifican en PostgreSQL real (18 tablas); no se eliminan datos existentes. No se conectan aún los snapshots con un consumidor de Pricing.

## [1.68.0] - 2026-11-17 (DH-184 · Gateway Operations, estados y base de datos)

- MINOR: integración de DholeOperationsService con API Gateway `/api/operations` y el Hub SignalR `/hubs/operations`; health `/api/health/operations` consulta dependencia PostgreSQL/Redis vía `/ready`.
- Estado técnico Operations visible en DholeWeb con versión real, registro, HTTP, latencia y actualización manual.
- Configuración predeterminada OPERATIONS_DB/HTTP/GRPC en las copias de runtime staging y producción; el workflow de Operations asegura de modo idempotente la base `dhole_operations` en la instancia PostgreSQL de cada entorno antes de migrar.
- Release coordinado: DholeApiGateway 1.11.0, DholeWeb 1.66.0, DholeOperationsService 0.3.1, DholeSystem/ecosistema 1.68.0. No modifica otros componentes.

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

## [1.66.0] - 2026-11-16 · CRM/SRM interfaz y Hacienda unificados (DH-179)

- MINOR Web 1.65.0 + System 1.66.0: interfaz de CRM con pestañas funcionales como SRM para alta y edición de clientes; navegación responsive y permisos intactos.
- Hacienda CR automática para CRM, con razón social y tipo de identificación aplicados en el formulario, reconsulta y actividades oficiales; proteger contra respuesta obsoleta y sincronizar antes de guardar. Prospectos incluidos.
- No requiere versiones nuevas de Config ni Auth; sin cambios en la arquitectura realtime/REST. Validar CI y staging antes de master, que despliega producción.

## [1.65.0] - 2026-11-16 · SRM/Hacienda alineado con CRM (DH-178)

- MINOR: DholeWeb 1.64.0 y DholeSystem 1.65.0. Identificación válida de Costa Rica consulta Hacienda y aplica automáticamente razón social y actividad principal disponible, sin segundo botón.
- UI de proveedores por pestañas, navegación adaptable, errores por sección y sincronización de consulta antes de guardar. Datos bancarios siguen restringidos en Config; servicios REST/realtime existentes sin cambios.
- Desarrollo sobre rama intermedia; CI, staging y autorización explícita antes de producción.

## [1.64.1] - 2026-11-16 (CRM: estado de actividad sincronizado tras finalizar)

- PATCH DH-20261116-CRM-COMPLETION-STATE-SYNC-177: DholeWeb 1.63.1 verifica en CRM el estado real de la actividad después de un error en POST y al recuperar foco de la pestaña; limpia alertas obsoletas únicamente cuando el GET confirma finalización, y muestra fecha real, tipo de gestión legible y verificación manual.
- Se preservan condiciones y validaciones de DholeCRMService, permisos, historial, recordatorios y realtime. Ecosistema Dhole 1.64.0 → 1.64.1; CI y validación multiusuario en staging antes de promover master.

## [1.64.0] - 2026-11-16 · SRM proveedores y seguridad financiera (DH-176)

- MINOR: coordinación de Auth 1.13.0, Config 1.8.0 y Web 1.63.0 para ficha de proveedor, Hacienda CR, cuenta principal y múltiples cuentas cifradas.
- Requiere `DHOLE_SRM_BANK_KEY_BASE64` en Config, scopes `srm.supplier.bank.read/manage` y migración de base de datos antes de habilitar cuentas bancarias.
- Estado: rama intermedia, CI/staging y autorización de producción pendientes; no desplegado a producción.

## [1.63.10] - 2026-11-16 (Completar actividad comercial desde seguimiento y visita)

- PATCH DH-20261116-CRM-ACTIVITY-COMPLETE-175: Web 1.62.8 muestra códigos activos del catálogo Config para el resultado de completar y delega al backend CRM el timestamp de ocurrencia; CRM acepta la fecha real opcional y normaliza Completed a COMPLETED si ese resultado está activo.
- Actualización de CRM master a 1.33.1 (manifiesto anterior referenciaba 1.33.0 aunque master compilaba 1.32.0) y develop a 1.34.1. DholeSystem/ecosistema 1.63.9 → 1.63.10. Pruebas de regresión y compatibilidad REST/SignalR, validar staging antes de promover a producción.

## [1.63.9] - 2026-11-16 (Bitácora comercial y fecha de realización UTC)

- PATCH DH-20261116-CRM-BITACORA-SERVER-CLOCK-174: Web 1.62.7 usa occurredAt=null para que el backend CRM determine con su reloj UTC la realización de bitácoras sin cita y las actividades históricas inferidas por el servidor, evitando rechazos por desfase horario del navegador.
- Los acuerdos futuros mantienen tareas y recordatorios separados; las fechas históricas programadas, acceso CRM, contratos REST, SignalR y Outbox permanecen intactos. DholeSystem/ecosistema 1.63.8 → 1.63.9. Validar pruebas, build, CI y staging antes de cualquier master/producción.

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

- PATCH DH-20261116-GATEWAY-DEPLOY-DNS-168: Gateway 1.10.3 añade recuperación acotada de descargas de DholeSystem en los workflows develop y master, evitando la interrupción de deploy por DNS transitorio.
- Clones validados y atómicos con error explícito para DNS persistente; sin cambios en APIs REST, SignalR, infraestructura runtime ni credenciales. DholeSystem/global 1.63.3 y manifiesto coordinado.
- Requiere CI Gateway/System y staging previo a la promoción a master.

## [1.63.2] - 2026-11-16 (Publicación segura de solicitudes externas)

- PATCH DH-20261116-API-PRICING-IDENTITY-167: DholeApiGateway 1.10.2 incorpora JWT técnico restringido al POST de solicitud de tarifas; DholePricingService 1.22.1 valida actor de integración y vendedor fijo, compatible con ejecutivo institucional Castro Fallas.
- Mantiene vendedor fijado desde CRM para ejecutivos reales, controles de Auth, scopes, API Keys, idempotencia y auditoría, sin flags ni credenciales en Git.
- DholeSystem y ecosistema 1.63.2; pruebas de CI y staging requeridas para la promoción coordinada a master.

## [1.63.1] - 2026-11-16 (API Manager: clientes, prospectos y vendedor Castro Fallas)

- PATCH DH-20261116-API-CRM-166: Web 1.62.1 selecciona cuentas o prospectos del directorio comercial unificado de CRM y conserva la distinción institucional.
- Gateway 1.10.1 permite omitir sellerUserId: Pricing utiliza la identidad técnica autenticada como actor operativo; el ejecutivo comercial se mantiene como Castro Fallas. No se utilizan GUID ficticios.
- DholeSystem/global 1.63.1, manifiesto coordinado y CI/staging obligatorios antes de producción.

## [1.63.0] - 2026-11-16 (API Manager: descubrimiento y valores predeterminados)

- MINOR DH-20261116-API-MANAGER-165: Dhole global 1.63.0; Gateway 1.10.0, Web 1.62.0 y System 1.63.0.
- Permite almacenar campos fijos en APIs POST/PUT/PATCH y seleccionar una cuenta real de CRM con su ejecutivo para solicitud de tarifas. El consumidor no puede reemplazar los valores bloqueados.
- Agrega fallback de rutas aprobadas cuando el inventario remoto no responde; conserva controles de credenciales y API Keys. CI, pruebas y staging previos a producción.

## [1.62.1] - 2026-11-16 (API Manager: edición y publicación segura)

- PATCH DH-20261116-API-MANAGER-164: versión global 1.62.1, Gateway 1.9.1, Web 1.61.1 y System 1.62.1; otros microservicios mantienen sus versiones.
- Corrige la edición de APIs guardadas y habilita identidad técnica de solo lectura para los ocho catálogos Config sin reutilizar permisos de superadmin. Otros endpoints requieren identidades propias.
- Registra manifiesto coordinado de los componentes modificados, conserva API Keys y controles de autorización, con validación CI/staging previa a la promoción a producción.

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

## [1.56.0] - 2026-11-14 (API Manager: descubrimiento y rutas dinámicas)

- MINOR: coordina versión global 1.56.0, Gateway 1.7.0, Web 1.56.0 y manifiesto central. Los demás microservicios conservan sus versiones actuales.
- El inventario usa rutas Gateway registradas y OpenAPI cuando está disponible; no expone rutas sin permiso ni habilita credenciales externas.
- Pendiente cobertura universal de metadatos para servicios sin OpenAPI de producción; no promover a master hasta validar CI, funcionalidad y staging.

## [1.55.0] - 2026-11-14 (Dhole API Manager coordinated release)

- MINOR: sincroniza el manifiesto central con Gateway 1.6.2, Web 1.55.0 y System 1.55.0; preserva versiones de todos los demás servicios.
- Reutiliza los tokens técnicos de los ocho catálogos Config existentes en develop, sin habilitar ThirdParty por defecto.
- Requiere CI, pruebas de staging y verificación previa a master.

## [1.54.0] - 2026-11-14

- MINOR DH-20261114-CRM-CALENDAR-SPANS-142: el calendario CRM muestra barras continuas entre días y bloques de duración real entre horas, y los seguimientos comerciales admiten fecha/hora de inicio y finalización. Los recordatorios mantienen su disparador de vencimiento, permisos y compatibilidad con los registros anteriores.
- Incremento coordinado desde Web 1.53.0 → 1.54.0, CRM 1.31.0 → 1.32.0 y DholeSystem/ecosistema 1.53.0 → 1.54.0. Migración aditiva StartAt; validación CI y staging antes de master.

## [1.53.0] - 2026-11-14

- MINOR DH-20261114-CRM-RECORD-FOLLOWUPS-142: release coordinado de nueva pestaña «Seguimientos» en fichas CRM de Prospectos y Clientes, con actividades, bitácoras y recordatorios históricos, filtros y acceso al detalle; incluye cuentas agrupadas y respeta los permisos CRM existentes.
- DholeWeb 1.52.1 → 1.53.0; DholeSystem/ecosistema 1.52.1 → 1.53.0; DholeCRMService mantiene 1.31.0. Sin cambios de API REST ni transporte SignalR. CI, staging y aprobación expresa antes de publicar en master.

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
