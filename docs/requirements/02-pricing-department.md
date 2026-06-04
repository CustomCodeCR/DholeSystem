# Documento Funcional — Pricing, Ofertas, Tarifas y Tarifarios

## 1. Información general del documento

**Nombre del documento:** Documento Funcional — Pricing, Ofertas, Tarifas y Tarifarios  
**Nombre del módulo:** Pricing  
**Nombre del servicio:** DholePricingService  
**Tipo de servicio:** Servicio principal de pricing y cotización formal  
**Departamento responsable:** Pricing  
**Servicios relacionados:** Auth Service, CRM Comercial Service, Notification Service, Audit Log Service, Report Service, AI Service, Storage Service  
**Versión:** 1.0  
**Estado del documento:** Borrador funcional estandarizado

---

## 2. Objetivo del documento

Este documento define el alcance funcional del módulo de Pricing, Ofertas, Tarifas y Tarifarios.

El objetivo es dejar claro cómo debe funcionar el servicio encargado de crear ofertas formales, administrar tarifarios, validar costos, calcular venta, controlar margen, generar PDFs, manejar versiones, enviar ofertas y convertir ofertas aceptadas en trámites.

Este documento servirá como base para análisis, diseño técnico, creación de historias de usuario, modelado de base de datos, definición de scopes, integraciones y desarrollo del servicio.

---

## 3. Objetivo del módulo o servicio

El servicio de Pricing será el encargado de administrar la lógica formal de tarifas, ofertas, costos, líneas de venta, utilidad, margen, vigencia, tarifarios y generación de propuestas formales.

Su objetivo principal es que el departamento de Pricing pueda recibir solicitudes de cotización, validar información, consultar proveedores o tarifarios, construir tarifas, registrar costos, calcular precios de venta, generar ofertas formales, controlar versiones y mantener trazabilidad completa del proceso.

Pricing también genera información base que puede ser utilizada por Ventas, CRM Comercial, Apertura, Logística, Facturación, Gerencia y otros departamentos.

---

## 4. Alcance funcional

El servicio de Pricing debe cubrir los siguientes bloques funcionales:

1. Gestión de solicitudes de cotización formal.
2. Gestión de ofertas.
3. Gestión de spots.
4. Gestión de tarifarios.
5. Validación de información mínima.
6. Separación de método de envío, modalidad operativa y tipo de equipo.
7. Registro de costos.
8. Registro de líneas de venta.
9. Cálculo de venta, utilidad y margen.
10. Configuración de margen por cliente.
11. Validación de margen mínimo.
12. Duplicación de ofertas y tarifarios.
13. Manejo de cambios y versiones.
14. Generación automática de consecutivo y nombre de tarifa.
15. Plantillas por incoterm y modalidad.
16. Automatización de costos y líneas de venta.
17. Automatización de correos.
18. Revisión humana antes del envío.
19. Conversión de oferta aceptada a trámite.
20. Estandarización y versionado de PDF.
21. Archivo digital centralizado.
22. Auditoría completa.
23. IA como asistente de Pricing.

---

## 5. Situación actual identificada

Actualmente el proceso de Pricing depende de correo, Dynamics, tarifarios externos, proveedores, archivos digitales, consultas manuales y revisión humana.

El departamento recibe solicitudes de cotización, valida información, consulta proveedores o sistemas externos, registra costos, genera líneas de venta, valida utilidad, genera PDF y envía la oferta.

Se identificaron problemas como:

- Solicitudes con información incompleta.
- Mucho llenado manual.
- Campos que no se utilizan.
- Categorías que no aportan valor.
- Falta de nomenclatura estándar.
- Copia manual del número Q al nombre de la tarifa.
- Reutilización manual de cotizaciones anteriores.
- Tarifarios dispersos.
- Costos consultados fuera del sistema.
- Falta de separación clara entre método, modalidad y equipo.
- Falta de trazabilidad sobre cambios.
- PDFs descargados, guardados y enviados manualmente.
- Falta de control claro sobre versiones enviadas al cliente.
- Margen no configurado de forma estructurada por cliente.
- Conversión manual de oferta aceptada a trámite.

---

## 6. Necesidad principal

El sistema debe ayudar al departamento de Pricing a crear ofertas de forma más ordenada, rápida, trazable y estandarizada.

Debe permitir:

- Validar información mínima.
- Detectar datos faltantes.
- Separar método, modalidad y equipo.
- Consultar o reutilizar tarifarios.
- Registrar costos.
- Registrar venta.
- Calcular utilidad y margen.
- Alertar cuando una oferta genera pérdida.
- Validar margen mínimo por cliente.
- Generar nombres automáticos.
- Duplicar ofertas y tarifarios.
- Controlar versiones.
- Generar y guardar PDFs.
- Saber qué PDF fue enviado.
- Convertir ofertas aceptadas en trámites.
- Mantener auditoría completa.

---

## 7. Usuarios principales

Los usuarios principales del servicio de Pricing son:

- Analistas de Pricing.
- Jefatura de Pricing.
- Gerencia comercial.
- Vendedores.
- Ejecutivos comerciales.
- CRM Comercial.
- Apertura.
- Logística.
- Facturación.
- Gerencia general.
- Administrador.
- Superusuario.

Cada usuario debe tener acceso de acuerdo con los scopes asignados por el Auth Service.

Ejemplos:

- Pricing puede crear, editar, revisar y enviar ofertas.
- Jefatura puede aprobar márgenes bajos o condiciones especiales.
- Vendedores pueden consultar ofertas relacionadas con sus clientes.
- CRM Comercial puede enviar cotizaciones express que requieren revisión formal.
- Gerencia puede consultar indicadores, utilidad, margen y conversión.

---

## 8. Responsabilidad del módulo

Pricing administra la lógica formal de cotización.

Este servicio debe manejar:

- Solicitudes de cotización formal.
- Ofertas.
- Spots.
- Tarifarios.
- Costos.
- Líneas de venta.
- Utilidad.
- Margen.
- Vigencia formal.
- Revisión interna.
- Aprobaciones de margen.
- PDFs de oferta.
- Versiones de oferta.
- Conversión de cotización express a oferta formal.
- Conversión de oferta aceptada a trámite.
- Auditoría de cambios.
- Historial documental.

---

## 9. Separación de responsabilidades con otros servicios

### Este servicio maneja

- Tarifas.
- Tarifarios.
- Costos.
- Venta.
- Margen.
- Utilidad.
- Vigencia formal.
- Condiciones especiales.
- Revisión de Pricing.
- Oferta formal.
- PDF formal de oferta.
- Conversión de cotización express a oferta formal.
- Conversión de oferta aceptada a trámite.

### Este servicio no maneja

- Seguimiento diario del vendedor.
- Cartera comercial.
- Actividades comerciales.
- Agenda del vendedor.
- Prospectos.
- Objeciones comerciales generales.
- Próximas acciones comerciales.
- Cotización express preliminar creada por vendedor.

### Servicio responsable de lo excluido

El servicio responsable del proceso comercial, seguimiento del vendedor y cotización express preliminar es **DholeCrmCommercialService**.

Pricing participa cuando una cotización express requiere validación formal, revisión de costos, margen, condiciones especiales o conversión a oferta formal.

---

## 10. Flujo funcional principal

1. Se recibe una solicitud de cotización.
2. El sistema registra la solicitud.
3. Se valida si la información mínima está completa.
4. Si falta información, el sistema cambia el estado a pendiente de información.
5. El sistema permite generar respuesta solicitando datos faltantes.
6. Si el cliente no existe, se registra como cliente o prospecto según corresponda.
7. Se crea la oferta en estado borrador.
8. Se selecciona el tipo de propuesta.
9. Se completan datos de carga, ruta, modalidad, incoterm, equipo y vigencia.
10. Se consultan tarifarios, proveedores o sistemas externos.
11. Se registran costos.
12. Se registran líneas de venta.
13. El sistema calcula venta total, costo total, utilidad y margen.
14. El sistema valida margen mínimo esperado.
15. Si requiere aprobación, se envía a revisión interna.
16. Se genera vista previa del PDF.
17. El usuario revisa la oferta.
18. Se aprueba la oferta.
19. Se genera PDF final.
20. Se envía al cliente o vendedor.
21. Se guarda evidencia del envío.
22. Si el cliente acepta, la oferta pasa a estado aceptada.
23. El sistema permite convertir la oferta aceptada en trámite.
24. Se notifica al área correspondiente.

---

## 11. Subflujos funcionales

### 11.1 Flujo de solicitud con información incompleta

1. Se recibe la solicitud.
2. El sistema valida los datos mínimos.
3. Detecta información faltante.
4. Cambia el estado a pendiente de información.
5. Genera correo o notificación con datos requeridos.
6. El usuario completa la información.
7. La oferta puede continuar el flujo.

### 11.2 Flujo de creación de tarifario

1. El usuario crea un tarifario.
2. Define vigencia.
3. Asocia método de envío.
4. Asocia modalidad operativa.
5. Asocia origen, destino y vía.
6. Asocia proveedor, si aplica.
7. Registra costos base.
8. Registra reglas de venta.
9. Guarda el tarifario.
10. El tarifario queda disponible para ofertas futuras.

### 11.3 Flujo de actualización de oferta

1. El usuario modifica datos relevantes.
2. El sistema solicita motivo del cambio.
3. Se guardan valores anteriores.
4. Se guardan valores nuevos.
5. Se recalcula costo, venta, utilidad y margen.
6. Se determina si requiere nueva aprobación.
7. Se genera nueva versión, si aplica.
8. Se genera nuevo PDF, si aplica.

### 11.4 Flujo de duplicación

1. El usuario selecciona una oferta o tarifario existente.
2. Presiona duplicar.
3. El sistema copia estructura, costos, líneas de venta y condiciones.
4. Se genera nuevo consecutivo.
5. Se mantiene referencia al registro origen.
6. El usuario actualiza cliente, ruta, vigencia o precios.
7. Se guarda como nueva oferta o tarifario independiente.

### 11.5 Flujo de conversión a trámite

1. El cliente acepta la oferta.
2. El usuario cambia el estado a aceptada.
3. El sistema valida que la información esté completa.
4. El sistema prepara los datos para apertura o trámite.
5. Se crea evento hacia el servicio correspondiente.
6. Se notifica al área operativa.
7. Se conserva trazabilidad de la oferta origen.

---

## 12. Entidades o conceptos principales

### Oferta

Cotización formal creada para una solicitud puntual de cliente, vendedor o departamento interno.

### Spot

Tarifa de vigencia corta, usualmente válida por el mismo día o por un periodo muy limitado.

### Tarifario

Lista estructurada de tarifas con vigencia definida, utilizada como base para ofertas.

### Método de envío

Medio principal por el cual se transporta la carga.

Ejemplos:

- Marítimo.
- Aéreo.
- Terrestre.
- Multimodal.

### Modalidad operativa

Forma en que se mueve la carga dentro del método seleccionado.

Ejemplos:

- FCL.
- LCL.
- FTL.
- LTL.
- Aéreo consolidado.
- Aéreo directo.
- Multimodal FCL.
- Multimodal LCL.

### Tipo de equipo

Equipo físico utilizado para transportar la carga.

Ejemplos:

- Contenedor 20.
- Contenedor 40.
- Contenedor 40 HC.
- Flat Rack.
- Open Top.
- Reefer.
- Furgón.
- Camión.
- Equipo especial.

### Costo

Monto interno o proveedor asociado a la operación.

### Línea de venta

Concepto facturable que será presentado al cliente.

### Margen

Relación entre costo, venta y utilidad esperada.

### PDF de oferta

Documento formal generado para enviar al cliente.

---

## 13. Datos requeridos

### Datos generales de la solicitud

- Cliente o prospecto.
- Persona solicitante.
- Correo de contacto.
- Vendedor o ejecutivo.
- Origen.
- Destino.
- Puerto de salida.
- Puerto de destino.
- Vía.
- Método de envío.
- Modalidad operativa.
- Tipo de equipo.
- Tipo de carga.
- Commodity.
- Incoterm.
- Cantidad de equipos.
- Peso.
- CBM.
- Dimensiones.
- Estibable.
- Carga peligrosa / IMO / Hazmat.
- Servicios adicionales.
- Dirección de recolección.
- Vigencia requerida.
- Moneda.
- Observaciones.

### Datos de oferta

- Consecutivo.
- Tipo de propuesta.
- Cliente.
- Solicitante.
- Ruta.
- Método de envío.
- Modalidad.
- Tipo de equipo.
- Vigencia.
- Estado.
- Costo total.
- Venta total.
- Utilidad.
- Margen.
- Margen mínimo esperado.
- Usuario creador.
- Usuario revisor.
- Usuario aprobador.

### Datos de tarifario

- Nombre.
- Código.
- Vigencia inicial.
- Vigencia final.
- Método de envío.
- Modalidad.
- Origen.
- Destino.
- Vía.
- Proveedor.
- Costo base.
- Regla de venta.
- Moneda.
- Estado.
- Versión.

### Datos de cambio o versión

- Oferta relacionada.
- Motivo del cambio.
- Usuario.
- Fecha y hora.
- Campos modificados.
- Valor anterior.
- Valor nuevo.
- Afecta costo.
- Afecta venta.
- Afecta utilidad.
- Requiere aprobación.
- Requiere nuevo PDF.

---

## 14. Estados del proceso

### Estados de oferta

| Estado                            | Descripción                                      |
| --------------------------------- | ------------------------------------------------ |
| Borrador                          | Oferta creada, pero no completada.               |
| Pendiente de información          | Faltan datos para poder cotizar.                 |
| Tarifa solicitada a proveedor     | Se espera respuesta de proveedor.                |
| Pendiente de revisión interna     | Oferta lista para revisión.                      |
| Pendiente de aprobación de margen | Requiere aprobación por margen bajo o pérdida.   |
| Aprobada internamente             | Oferta validada internamente.                    |
| Enviada al cliente                | Oferta enviada al cliente o vendedor.            |
| Actualizada                       | Oferta modificada después de su creación.        |
| Aceptada                          | Cliente aceptó la oferta.                        |
| Rechazada                         | Cliente rechazó la oferta.                       |
| Vencida                           | La vigencia expiró.                              |
| Cancelada                         | Oferta cancelada manualmente.                    |
| Convertida a trámite              | Oferta aceptada convertida en proceso operativo. |

### Estados de tarifario

| Estado      | Descripción                        |
| ----------- | ---------------------------------- |
| Borrador    | Tarifario en creación.             |
| Vigente     | Tarifario disponible para uso.     |
| Vencido     | Tarifario fuera de vigencia.       |
| Reemplazado | Existe una versión más reciente.   |
| Cancelado   | Tarifario desactivado manualmente. |

---

## 15. Reglas funcionales

### Regla 1: Información mínima obligatoria

El sistema no debe permitir enviar una oferta formal si faltan datos mínimos según modalidad.

### Regla 2: Separación de conceptos operativos

Método de envío, modalidad operativa y tipo de equipo deben manejarse como campos separados.

### Regla 3: Validación de margen

Si la venta no cubre los costos o queda por debajo del margen mínimo configurado, el sistema debe alertar y solicitar aprobación interna.

### Regla 4: Revisión humana

Las ofertas generadas automáticamente o asistidas por IA deben quedar pendientes de revisión antes de enviarse al cliente.

### Regla 5: Versionado de cambios

Cada cambio relevante debe guardar historial o generar nueva versión.

### Regla 6: PDF versionado

Cada PDF generado debe quedar almacenado con su versión correspondiente.

### Regla 7: Trazabilidad de envío

El sistema debe saber qué versión de PDF fue enviada, cuándo y a quién.

### Regla 8: Conversión a trámite

Una oferta aceptada debe poder convertirse en trámite sin redigitar la información ya capturada.

### Regla 9: Duplicación controlada

Cuando se duplique una oferta, se debe generar nuevo consecutivo y mantener referencia al origen.

### Regla 10: Tarifarios con vigencia

Todo tarifario debe tener una vigencia definida.

---

## 16. Automatizaciones recomendadas

El sistema debería automatizar o semiautomatizar:

- Validación de información mínima.
- Detección de datos faltantes.
- Generación de correo solicitando información.
- Generación automática de consecutivo.
- Generación automática de nombre de tarifa.
- Sugerencia de costos por modalidad.
- Sugerencia de líneas de venta.
- Sugerencia de incluidos, no incluidos y sujetos a.
- Cálculo de costo total.
- Cálculo de venta total.
- Cálculo de utilidad.
- Cálculo de margen.
- Alerta por pérdida.
- Alerta por margen bajo.
- Solicitud de aprobación interna.
- Generación de PDF.
- Guardado automático de PDF.
- Envío de oferta por correo.
- Notificación de oferta aceptada.
- Notificación para iniciar trámite.
- Vencimiento automático de ofertas.
- Versionado automático de cambios relevantes.

---

## 17. Integraciones con otros servicios

### Auth Service

Controla autenticación, autorización y scopes de acceso.

### CRM Comercial Service

Envía cotizaciones express que requieren revisión formal y recibe la referencia de la oferta formal generada.

### Notification Service

Envía notificaciones sobre aprobaciones, vencimientos, ofertas enviadas, ofertas aceptadas y solicitudes pendientes.

### Audit Log Service

Registra acciones críticas, cambios de estado, modificaciones de costos, aprobaciones y envíos.

### Report Service

Genera reportes de ofertas, utilidad, margen, tarifarios, productividad y conversión.

### AI Service

Apoya con extracción de datos, sugerencias, borradores y análisis de ofertas.

### Storage Service

Guarda PDFs, adjuntos, versiones y documentos relacionados.

---

## 18. Auditoría requerida

Deben auditarse las siguientes acciones:

- Crear oferta.
- Editar oferta.
- Duplicar oferta.
- Cambiar estado de oferta.
- Crear tarifario.
- Editar tarifario.
- Versionar tarifario.
- Agregar costo.
- Editar costo.
- Agregar línea de venta.
- Editar línea de venta.
- Aprobar margen bajo.
- Rechazar margen bajo.
- Generar PDF.
- Enviar PDF.
- Reenviar oferta.
- Convertir oferta a trámite.
- Crear versión.
- Cancelar oferta.
- Vencer oferta manualmente.

Cada auditoría debe guardar:

- Usuario.
- Acción.
- Fecha y hora.
- Entidad afectada.
- Identificador de entidad.
- Valor anterior.
- Valor nuevo.
- Motivo, si aplica.
- Metadata adicional.

---

## 19. Scopes requeridos

La seguridad debe manejarse mediante scopes por servicio, recurso y acción.

Formato recomendado:

```txt
service.resource.action
```

Ejemplos para Pricing:

```txt
pricing.offers.read
pricing.offers.create
pricing.offers.update
pricing.offers.duplicate
pricing.offers.change-status
pricing.offers.send-customer
pricing.offers.convert-operation

pricing.spots.read
pricing.spots.create
pricing.spots.update
pricing.spots.change-status

pricing.tariffs.read
pricing.tariffs.create
pricing.tariffs.update
pricing.tariffs.version
pricing.tariffs.deactivate

pricing.costs.read
pricing.costs.create
pricing.costs.update

pricing.sale-lines.read
pricing.sale-lines.create
pricing.sale-lines.update

pricing.margins.read
pricing.margins.approve-low-margin
pricing.margins.reject-low-margin

pricing.approvals.read
pricing.approvals.create
pricing.approvals.resolve

pricing.pdf.read
pricing.pdf.generate
pricing.pdf.send
pricing.pdf.download

pricing.customer-margin-rules.read
pricing.customer-margin-rules.create
pricing.customer-margin-rules.update

pricing.dashboard.read
pricing.manager-view.read
pricing.reports.read
```

Los scopes deben ser administrados desde el Auth Service y asignados a roles creados dinámicamente. Únicamente los roles Administrador y Superusuario deben existir como seed inicial.

---

## 20. Consideraciones técnicas generales

El servicio debe diseñarse bajo arquitectura de microservicios.

Debe contemplar:

- PostgreSQL para información relacional.
- MongoDB para historial, snapshots, correos y documentos semiestructurados.
- Redis para cache, locks y consultas rápidas.
- Outbox Pattern para comunicación asíncrona entre servicios.
- Background worker para procesar eventos pendientes.
- Integración con Auth Service para scopes.
- Integración con Audit Log Service para trazabilidad.
- Integración con Notification Service para alertas.
- Integración con Report Service para indicadores.
- Integración con AI Service para asistencia de Pricing.
- Integración con Storage Service para PDFs y adjuntos.

---

## 21. Entidades sugeridas en PostgreSQL

### pricing_offers

Tabla principal de ofertas.

Campos sugeridos:

- id.
- offer_number.
- offer_name.
- offer_type.
- customer_id.
- prospect_id.
- requester_name.
- requester_email.
- seller_id.
- origin.
- destination.
- departure_port.
- destination_port.
- route_via.
- shipping_method.
- modality.
- equipment_type.
- cargo_type.
- commodity.
- incoterm.
- validity_date.
- currency.
- status.
- total_cost.
- total_sale.
- profit.
- margin_percentage.
- minimum_margin_percentage.
- created_at.
- updated_at.
- created_by.
- updated_by.
- is_active.

### pricing_offer_versions

Tabla para versiones de oferta.

Campos sugeridos:

- id.
- offer_id.
- version_number.
- change_reason.
- snapshot_data.
- created_at.
- created_by.

### pricing_offer_costs

Tabla para costos de oferta.

Campos sugeridos:

- id.
- offer_id.
- concept.
- provider_id.
- cost_amount.
- currency.
- quantity.
- total_cost.
- applies_to.
- created_at.
- updated_at.
- created_by.
- updated_by.

### pricing_offer_sale_lines

Tabla para líneas de venta.

Campos sugeridos:

- id.
- offer_id.
- concept.
- sale_amount.
- currency.
- quantity.
- total_sale.
- included_type.
- created_at.
- updated_at.
- created_by.
- updated_by.

### pricing_tariffs

Tabla principal de tarifarios.

Campos sugeridos:

- id.
- tariff_number.
- tariff_name.
- customer_id.
- provider_id.
- shipping_method.
- modality.
- origin.
- destination.
- route_via.
- validity_start_date.
- validity_end_date.
- currency.
- status.
- created_at.
- updated_at.
- created_by.
- updated_by.
- is_active.

### pricing_tariff_versions

Tabla para versiones de tarifarios.

Campos sugeridos:

- id.
- tariff_id.
- version_number.
- change_reason.
- snapshot_data.
- created_at.
- created_by.

### pricing_customer_margin_rules

Tabla para reglas de margen por cliente.

Campos sugeridos:

- id.
- customer_id.
- shipping_method.
- modality.
- route.
- minimum_margin_percentage.
- suggested_margin_percentage.
- requires_approval_below_minimum.
- allows_special_margin.
- observations.
- created_at.
- updated_at.
- created_by.
- updated_by.

### pricing_offer_documents

Tabla para documentos de oferta.

Campos sugeridos:

- id.
- offer_id.
- document_type.
- version_number.
- storage_provider.
- storage_path.
- file_name.
- file_url.
- sent_to_customer.
- sent_at.
- sent_by.
- created_at.
- created_by.

### pricing_offer_approvals

Tabla para aprobaciones internas.

Campos sugeridos:

- id.
- offer_id.
- approval_type.
- requested_by.
- approved_by.
- status.
- reason.
- comments.
- requested_at.
- resolved_at.

### pricing_outbox_messages

Tabla para eventos pendientes.

Campos sugeridos:

- id.
- event_type.
- aggregate_type.
- aggregate_id.
- payload.
- status.
- retry_count.
- error_message.
- created_at.
- processed_at.

---

## 22. Colecciones sugeridas en MongoDB

### pricing_offer_snapshots

Colección para snapshots completos de oferta.

Documento sugerido:

- offerId.
- versionNumber.
- offerData.
- costs.
- saleLines.
- marginData.
- createdAt.
- createdBy.

### pricing_email_history

Colección para historial de correos relacionados con ofertas.

Documento sugerido:

- offerId.
- emailType.
- from.
- to.
- cc.
- subject.
- body.
- attachments.
- sentAt.
- sentBy.

### pricing_ai_drafts

Colección para borradores generados por IA.

Documento sugerido:

- offerId.
- draftType.
- inputReferences.
- generatedContent.
- modelName.
- createdAt.
- createdByModel.

### pricing_change_timeline

Colección para línea de tiempo de cambios.

Documento sugerido:

- entityType.
- entityId.
- eventType.
- title.
- description.
- metadata.
- createdAt.
- createdBy.

### pricing_pdf_metadata

Colección para metadata flexible de PDFs.

Documento sugerido:

- offerId.
- documentId.
- versionNumber.
- templateUsed.
- generatedAt.
- generatedBy.
- sentAt.
- sentTo.

---

## 23. Uso recomendado de Redis

Redis puede utilizarse para:

- Cache de tarifarios vigentes.
- Cache de ofertas por estado.
- Cache de reglas de margen.
- Cache de dashboards de Pricing.
- Locks para evitar doble generación de PDF.
- Locks para evitar doble conversión a trámite.
- Estados temporales de formularios.
- Indicadores rápidos de ofertas.
- Notificaciones pendientes.

Ejemplos de claves:

```txt
pricing:tariffs:active:{modality}
pricing:offers:status:{status}
pricing:customer:{customerId}:margin-rules
pricing:offer:{offerId}:summary
pricing:dashboard:{date}
pricing:lock:pdf:{offerId}
pricing:lock:convert-operation:{offerId}
```

---

## 24. Outbox Pattern y eventos

Pricing debe utilizar Outbox Pattern para publicar eventos hacia otros servicios sin perder consistencia.

### Tabla pricing_outbox_messages

Campos sugeridos:

- id.
- event_type.
- aggregate_type.
- aggregate_id.
- payload.
- status.
- retry_count.
- error_message.
- created_at.
- processed_at.

### Eventos sugeridos

- PricingOfferCreated.
- PricingOfferUpdated.
- PricingOfferVersionCreated.
- PricingOfferSentToCustomer.
- PricingOfferAccepted.
- PricingOfferRejected.
- PricingOfferExpired.
- PricingOfferCancelled.
- PricingOfferConvertedToOperation.
- PricingTariffCreated.
- PricingTariffUpdated.
- PricingTariffVersionCreated.
- PricingMarginApprovalRequested.
- PricingMarginApprovalApproved.
- PricingMarginApprovalRejected.
- PricingPdfGenerated.
- PricingPdfSent.

---

## 25. Background worker

El background worker debe encargarse de procesar mensajes pendientes de la tabla outbox.

Responsabilidades:

- Leer mensajes pendientes.
- Publicar eventos a otros servicios.
- Reintentar mensajes fallidos.
- Registrar errores.
- Marcar mensajes como procesados.
- Evitar duplicidad.
- Controlar número de reintentos.
- Permitir reprocesamiento controlado.

Reglas:

- No debe eliminar mensajes procesados inmediatamente.
- Debe guardar historial de errores.
- Debe manejar reintentos.
- Debe ser idempotente.
- Debe permitir reprocesamiento controlado.

---

## 26. Reportes e indicadores

El Report Service debe permitir generar reportes sobre:

- Ofertas creadas.
- Ofertas por estado.
- Ofertas enviadas.
- Ofertas aceptadas.
- Ofertas rechazadas.
- Ofertas vencidas.
- Conversión de ofertas a trámites.
- Utilidad por cliente.
- Margen por cliente.
- Margen por modalidad.
- Tarifarios vigentes.
- Tarifarios vencidos.
- Ofertas con margen bajo.
- Ofertas con pérdida.
- Tiempo promedio de creación de oferta.
- Tiempo promedio de aprobación.
- Productividad por usuario.
- Ofertas generadas desde cotización express.
- Ofertas duplicadas.
- Versiones generadas.

Indicadores sugeridos:

- Total de ofertas del mes.
- Porcentaje de aceptación.
- Porcentaje de rechazo.
- Margen promedio.
- Utilidad total.
- Ofertas pendientes de revisión.
- Ofertas pendientes de aprobación.
- Ofertas próximas a vencer.
- Tarifarios próximos a vencer.
- Top clientes por utilidad.
- Top rutas por volumen de cotización.
- Top modalidades por margen.

---

## 27. IA como apoyo

La IA puede apoyar al equipo de Pricing en:

- Leer correos de solicitud.
- Extraer datos clave de cotización.
- Detectar información faltante.
- Generar borradores de oferta.
- Sugerir tarifas similares.
- Sugerir incluidos y no incluidos.
- Preparar correos de respuesta.
- Identificar ofertas repetitivas.
- Montar tarifarios automáticamente.
- Sugerir líneas de venta.
- Sugerir líneas de costo.
- Sugerir proveedores frecuentes.
- Ayudar a crear tarifarios de consolidado.
- Generar PDFs preliminares para revisión.
- Mantener trazabilidad de versiones.
- Recomendar duplicar una oferta anterior.
- Resumir cambios entre versiones.
- Detectar ofertas con riesgo de margen bajo.

Regla general:

La IA debe ser de apoyo. No debe enviar ofertas automáticamente ni tomar decisiones definitivas sin validación humana.

---

## 28. Problemas detectados

Durante el levantamiento se identificaron los siguientes problemas:

- Solicitudes con información incompleta.
- Mucho llenado manual.
- Campos en Dynamics que no se utilizan.
- Categorías que no aportan valor al proceso.
- No existe una nomenclatura estándar para nombrar tarifas.
- Se copia manualmente el número Q al nombre de la tarifa.
- Se repite información entre campos.
- Se reutilizan cotizaciones anteriores de forma manual.
- Se deben revisar tarifarios y proveedores fuera del sistema.
- Se pierde tiempo moviendo conceptos entre incluye, sujeto a y no incluye.
- No hay separación clara entre cliente final y persona que solicitó la oferta.
- No hay automatización del correo de respuesta.
- No hay conversión automática de oferta aceptada a trámite.
- No hay suficiente trazabilidad sobre quién modificó, revisó o aprobó una oferta.
- No todos los tarifarios están centralizados o estructurados.
- El mercado cambia rápido y obliga a actualizar tarifas constantemente.
- Los PDFs se descargan, guardan y envían manualmente.
- Las versiones de PDF pueden generar confusión.
- La información relacionada a ofertas, costos, gastos, facturas y documentos puede estar distribuida.
- La utilidad esperada no es igual para todos los clientes.
- No hay reglas claras en el sistema para margen mínimo por cliente.

---

## 29. Puntos de mejora identificados

1. Validar automáticamente la información mínima.
2. Separar método, modalidad y equipo.
3. Generar nombres automáticos.
4. Manejar cambios y versiones.
5. Configurar margen por cliente.
6. Duplicar ofertas y tarifarios.
7. Sugerir costos según modalidad.
8. Mantener revisión humana antes de envío.
9. Automatizar conversión a trámite.
10. Centralizar documentos.
11. Generar PDFs versionados.
12. Automatizar correos.
13. Integrar Pricing con CRM Comercial.
14. Usar IA como apoyo de Pricing.
15. Mejorar trazabilidad de costos, venta y margen.
16. Crear reportes gerenciales.
17. Controlar acceso mediante scopes.

---

## 30. Resumen final

El servicio de Pricing debe centralizar la creación de ofertas, spots, tarifas y tarifarios.

El proceso actual depende mucho del correo, Dynamics, tarifarios externos, proveedores, archivos digitales y revisión manual. Por eso, el sistema debe ayudar a capturar información, validar datos, sugerir tarifas, administrar costos, calcular venta, controlar margen, generar PDFs, versionar cambios, enviar ofertas y convertir ofertas aceptadas en trámites.

Un punto clave es separar correctamente método de envío, modalidad operativa y tipo de equipo. Esto permitirá reglas más claras, cálculos más precisos y automatizaciones más confiables.

Pricing debe seguir siendo el dueño de la validación formal de costos, tarifas, margen, utilidad y ofertas formales. CRM Comercial puede iniciar una cotización express, pero Pricing debe validar cuando se requiera formalidad comercial, financiera u operativa.

El objetivo principal es construir un flujo más ordenado, trazable y automatizado, donde el sistema apoye al equipo de Pricing sin eliminar la revisión humana.
