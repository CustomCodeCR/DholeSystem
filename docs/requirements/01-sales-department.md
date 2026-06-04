# Documento Funcional — CRM Comercial y Cotización Express

## 1. Información general del documento

**Nombre del documento:** Documento Funcional — CRM Comercial y Cotización Express  
**Nombre del módulo:** CRM Comercial  
**Nombre del servicio:** DholeCrmCommercialService  
**Tipo de servicio:** Servicio principal comercial  
**Departamento responsable:** Comercial  
**Servicios relacionados:** Auth Service, Pricing Service, Notification Service, Audit Log Service, Report Service, AI Service, Storage Service  
**Versión:** 1.0  
**Estado del documento:** Borrador funcional estandarizado

---

## 2. Objetivo del documento

Este documento define el alcance funcional del módulo de CRM Comercial y Cotización Express.

El objetivo es dejar claro cómo debe funcionar el área comercial dentro del sistema, qué procesos debe cubrir, qué información debe administrar, cómo debe relacionarse con otros servicios y qué reglas debe seguir para permitir el desarrollo del servicio sin ambigüedades funcionales.

Este documento servirá como base para análisis, diseño técnico, creación de historias de usuario, modelado de base de datos, definición de scopes, integraciones y desarrollo del servicio.

---

## 3. Objetivo del módulo o servicio

El CRM Comercial será el servicio encargado de centralizar la gestión comercial de clientes, prospectos, cartera, contactos, actividades, oportunidades, agenda, recordatorios, seguimiento de cotizaciones vivas y cotizaciones express.

El objetivo principal es que el equipo comercial pueda trabajar de forma más ordenada, con mejor seguimiento, menor dependencia de archivos manuales y mayor capacidad de respuesta ante clientes y prospectos.

El servicio debe permitir que el vendedor trabaje desde oficina o desde campo, especialmente desde celular, teniendo acceso rápido a su cartera, clientes, prospectos, actividades pendientes, oportunidades y cotizaciones express.

---

## 4. Alcance funcional

El CRM Comercial debe cubrir los siguientes bloques funcionales:

1. Gestión de clientes comerciales.
2. Gestión de prospectos.
3. Gestión de cartera comercial.
4. Gestión de contactos.
5. Gestión de actividades comerciales.
6. Gestión de agenda diaria.
7. Gestión de próximas acciones.
8. Gestión de recordatorios.
9. Gestión de oportunidades comerciales.
10. Gestión de cotización express.
11. Seguimiento de cotizaciones vivas.
12. Perfil comercial del cliente.
13. Registro de objeciones comerciales.
14. Registro de motivos de pérdida.
15. Reasignación de vendedor.
16. Seguimiento de contratos o solicitudes de crédito.
17. Dashboard comercial.
18. Vista gerencial.
19. Automatizaciones comerciales.
20. IA como asistente comercial.

---

## 5. Situación actual identificada

Actualmente, parte del seguimiento comercial se realiza mediante archivos compartidos, dashboards, correos, controles manuales y comunicación directa con vendedores.

El área comercial trabaja con controles de prospectos, tareas diarias, visitas, llamadas, seguimiento de cotizaciones vivas, revisión de correos, análisis de clientes, análisis de importaciones, identificación de clientes con baja de volumen, identificación de competencia y preparación de argumentos comerciales.

El problema principal es que mucha información comercial queda dispersa, se maneja manualmente o no queda registrada de forma estructurada.

Esto genera dificultad para saber:

- Qué hizo cada vendedor durante el día.
- Qué clientes visitó.
- Qué llamadas realizó.
- Qué cotizaciones están pendientes.
- Qué prospectos están en seguimiento.
- Qué clientes necesitan contacto.
- Qué oportunidades están abiertas.
- Qué clientes están comprando menos.
- Qué clientes podrían estar usando competencia.
- Qué acciones se deben realizar después.

---

## 6. Necesidad principal

El sistema debe ayudar al equipo comercial a tener una vista clara y centralizada de su operación diaria.

Debe permitir saber:

- Qué clientes tiene cada vendedor.
- Qué prospectos está trabajando.
- Qué actividades realizó.
- Qué actividades tiene pendientes.
- Qué cotizaciones están vivas.
- Qué cotizaciones necesitan seguimiento.
- Qué oportunidades existen.
- Qué cliente necesita visita o llamada.
- Qué cliente tiene baja de actividad.
- Qué cliente está usando otros proveedores.
- Qué cotizaciones express fueron creadas desde campo.
- Qué cotizaciones express necesitan validación formal.
- Qué cotizaciones express se convirtieron en oferta formal.

La necesidad principal es reducir controles manuales y permitir que el vendedor tenga más información para vender mejor.

---

## 7. Usuarios principales

Los usuarios principales del CRM Comercial son:

- Gerencia comercial.
- Jefatura comercial.
- Vendedores.
- Ejecutivos comerciales.
- Asistentes comerciales.
- Pricing.
- Servicio al cliente.
- Gerencia general.
- Administrador.
- Superusuario.

Cada usuario debe tener acceso de acuerdo con los scopes asignados por el Auth Service.

Ejemplos:

- El vendedor puede ver su cartera, sus tareas, sus prospectos, sus oportunidades y sus cotizaciones.
- La jefatura comercial puede ver la cartera completa y el trabajo de todos los vendedores.
- Gerencia puede ver indicadores, metas, resultados y desempeño comercial.
- Pricing puede ver únicamente las cotizaciones express que requieren validación formal o conversión a oferta formal.

---

## 8. Responsabilidad del módulo

El CRM Comercial administra el proceso comercial y el seguimiento del cliente.

Este servicio debe manejar:

- Clientes.
- Prospectos.
- Cartera comercial.
- Contactos.
- Actividades comerciales.
- Agenda diaria.
- Próximas acciones.
- Recordatorios.
- Oportunidades.
- Seguimiento comercial.
- Perfil comercial del cliente.
- Objeciones.
- Motivos de pérdida.
- Cotización express inicial creada por el vendedor.
- Resultado comercial de la cotización.
- Seguimiento de cotizaciones vivas.
- Solicitudes de crédito.
- Reasignación de vendedor.
- Indicadores comerciales.

---

## 9. Separación de responsabilidades con otros servicios

### Este servicio maneja

- La gestión comercial del cliente.
- El seguimiento diario del vendedor.
- La administración de prospectos.
- La administración de actividades comerciales.
- La administración de oportunidades.
- La cotización express preliminar.
- El seguimiento de cotizaciones vivas.
- El registro de objeciones.
- El registro de motivos de pérdida.
- La agenda comercial.
- La visibilidad gerencial comercial.

### Este servicio no maneja

- Tarifas oficiales.
- Tarifarios formales.
- Costos formales.
- Margen formal.
- Utilidad formal.
- Oferta formal aprobada.
- Validación final de Pricing.
- Generación formal de oferta validada.

### Servicio responsable de lo excluido

El servicio responsable de tarifas, costos, margen, utilidad y ofertas formales es **DholePricingService**.

La cotización express nace en CRM Comercial, pero se envía a Pricing únicamente cuando requiere validación formal, revisión de margen, condiciones especiales o conversión a oferta formal.

---

## 10. Flujo funcional principal

1. El vendedor ingresa al CRM Comercial.
2. El sistema muestra su cartera, agenda diaria, tareas pendientes y cotizaciones en seguimiento.
3. El vendedor selecciona un cliente, prospecto u oportunidad.
4. El vendedor registra una actividad comercial.
5. La actividad puede generar una próxima acción.
6. El sistema crea recordatorios según la próxima acción.
7. Si existe una oportunidad, el vendedor puede crear una cotización express.
8. La cotización express queda registrada en CRM Comercial.
9. El vendedor puede enviarla al cliente o marcarla en seguimiento.
10. Si requiere validación formal, el vendedor la envía a Pricing.
11. Pricing revisa y puede convertirla en oferta formal.
12. CRM Comercial mantiene el seguimiento comercial de la cotización.
13. Si el cliente acepta, la oportunidad puede marcarse como ganada.
14. Si el cliente rechaza, el sistema solicita motivo de pérdida.
15. El historial queda disponible para análisis comercial, reportes e IA.

---

## 11. Subflujos funcionales

### 11.1 Flujo de creación de prospecto

1. El vendedor registra un prospecto.
2. El sistema valida datos mínimos.
3. El prospecto queda asignado a un vendedor.
4. El sistema permite crear actividades, oportunidades y próximas acciones.
5. Si el prospecto se convierte en cliente, se conserva el historial comercial.

### 11.2 Flujo de actividad comercial

1. El vendedor selecciona cliente o prospecto.
2. Registra tipo de actividad.
3. Agrega resultado y comentarios.
4. Define próxima acción, si aplica.
5. El sistema genera recordatorio.
6. La actividad queda en el historial comercial.

### 11.3 Flujo de oportunidad comercial

1. El vendedor crea una oportunidad.
2. Asocia cliente o prospecto.
3. Define servicio potencial, valor estimado y etapa.
4. Registra próxima acción.
5. Da seguimiento hasta ganarla, perderla o descartarla.

### 11.4 Flujo de cotización express

1. El vendedor selecciona cliente, prospecto u oportunidad.
2. Presiona “Crear cotización express”.
3. El sistema muestra formulario móvil.
4. El vendedor ingresa datos mínimos.
5. El sistema genera cotización preliminar.
6. El vendedor puede mostrarla o enviarla al cliente.
7. Si requiere validación formal, la envía a Pricing.
8. Pricing puede convertirla en oferta formal.

### 11.5 Flujo de rechazo o pérdida

1. El cliente rechaza la cotización u oportunidad.
2. El sistema solicita motivo de pérdida.
3. El vendedor registra comentario.
4. El sistema guarda competidor si se conoce.
5. La información queda disponible para reportes e IA.

---

## 12. Entidades o conceptos principales

### Cliente

Empresa o persona que mantiene relación comercial con la organización.

### Prospecto

Empresa o persona con potencial comercial que todavía no se ha convertido en cliente.

### Contacto

Persona relacionada con un cliente o prospecto. Puede ser contacto operativo, financiero, comercial, de compras, logística o gerencia.

### Cartera comercial

Conjunto de clientes y prospectos asignados a un vendedor.

### Actividad comercial

Registro de una interacción comercial como llamada, visita, correo, WhatsApp, reunión o seguimiento.

### Próxima acción

Acción futura que debe realizar un vendedor como resultado de una actividad comercial.

### Oportunidad comercial

Posibilidad de venta identificada con un cliente o prospecto.

### Cotización express

Cotización preliminar creada por el vendedor desde CRM Comercial, usualmente desde celular, para dar respuesta rápida al cliente.

### Oferta formal

Documento validado por Pricing con costos, margen, utilidad, vigencia y condiciones formales.

---

## 13. Datos requeridos

### Datos del cliente

- Nombre comercial.
- Razón social.
- Identificación.
- Vendedor asignado.
- Estado comercial.
- Prioridad.
- Servicios actuales.
- Comentarios comerciales.
- Estado activo/inactivo.

### Datos del prospecto

- Empresa.
- Contacto principal.
- Teléfono.
- Correo.
- Ubicación.
- Actividad económica.
- Fuente del prospecto.
- Vendedor responsable.
- Servicio de interés.
- Estado.
- Próxima acción.

### Datos del contacto

- Nombre completo.
- Cargo.
- Área.
- Teléfono.
- Correo.
- WhatsApp.
- Preferencia de comunicación.
- Nivel de influencia.
- Toma decisiones.
- Comentarios.

### Datos de la actividad comercial

- Cliente o prospecto.
- Contacto relacionado.
- Vendedor responsable.
- Tipo de actividad.
- Fecha y hora.
- Resultado.
- Comentarios.
- Próxima acción.
- Estado.
- Archivos adjuntos, si aplica.

### Datos de la oportunidad

- Cliente o prospecto.
- Vendedor responsable.
- Servicio potencial.
- Valor estimado.
- Probabilidad.
- Etapa.
- Fecha estimada de cierre.
- Fuente.
- Comentarios.

### Datos de la cotización express

- Cliente o prospecto.
- Contacto.
- Vendedor.
- Origen.
- Destino.
- Método de envío.
- Modalidad.
- Tipo de equipo, si aplica.
- Peso.
- CBM.
- Dimensiones, si aplica.
- Incoterm.
- Tipo de carga.
- Servicios requeridos.
- Observaciones.
- Vigencia estimada.
- Moneda.
- Monto estimado.
- Estado.

---

## 14. Estados del proceso

### Estados de prospecto

| Estado                    | Descripción                                    |
| ------------------------- | ---------------------------------------------- |
| Nuevo                     | Prospecto registrado, sin contacto inicial.    |
| Contactado                | Ya se realizó el primer contacto.              |
| En seguimiento            | Se mantiene gestión comercial activa.          |
| Reunión agendada          | Existe reunión programada.                     |
| Cotización express creada | Ya tiene cotización preliminar.                |
| En negociación            | Existe negociación comercial activa.           |
| Ganado                    | Se convirtió en cliente u oportunidad cerrada. |
| Perdido                   | No se logró concretar.                         |
| Descartado                | No continuará en gestión comercial.            |

### Estados de oportunidad

| Estado                    | Descripción                      |
| ------------------------- | -------------------------------- |
| Detectada                 | Oportunidad identificada.        |
| Contactada                | Cliente o prospecto contactado.  |
| En análisis               | Se está revisando la necesidad.  |
| Cotización express creada | Se generó cotización preliminar. |
| Oferta formal requerida   | Necesita validación de Pricing.  |
| Oferta formal creada      | Pricing creó la oferta formal.   |
| En negociación            | El cliente está evaluando.       |
| Ganada                    | La oportunidad fue aceptada.     |
| Perdida                   | La oportunidad fue rechazada.    |
| Descartada                | Ya no aplica continuar.          |

### Estados de cotización express

| Estado                       | Descripción                              |
| ---------------------------- | ---------------------------------------- |
| Borrador express             | Cotización iniciada, pero no finalizada. |
| Creada por vendedor          | Cotización registrada por el vendedor.   |
| Enviada al cliente           | Cotización compartida con el cliente.    |
| En seguimiento               | El vendedor está dando seguimiento.      |
| Aceptada preliminarmente     | El cliente aceptó de forma preliminar.   |
| Rechazada                    | El cliente no aceptó.                    |
| Requiere revisión de Pricing | Necesita validación formal.              |
| En revisión de Pricing       | Pricing está revisando.                  |
| Convertida a oferta formal   | Pricing la convirtió en oferta formal.   |
| Descartada                   | No continuará.                           |

---

## 15. Reglas funcionales

### Regla 1: Creación desde CRM Comercial

Toda cotización express debe poder crearse desde CRM Comercial.

### Regla 2: Optimización móvil

La pantalla de cotización express debe estar optimizada para celular.

### Regla 3: No requiere Pricing inicialmente

El vendedor puede crear una cotización express sin solicitar primero una validación de Pricing.

### Regla 4: Relación obligatoria

Toda cotización express debe estar relacionada con un cliente o prospecto.

### Regla 5: Creación o relación de oportunidad

Cuando se crea una cotización express, el sistema puede crear o relacionar una oportunidad comercial.

### Regla 6: Seguimiento obligatorio

La cotización express debe aparecer en agenda, cartera y seguimiento comercial.

### Regla 7: Escalamiento a Pricing

Si requiere validación formal, el vendedor debe poder enviarla a Pricing.

### Regla 8: Historial de cambios

Todo cambio de estado debe quedar registrado.

### Regla 9: Motivo de pérdida

Si la cotización, oportunidad o gestión se pierde, debe registrarse un motivo.

### Regla 10: Conversión a oferta formal

Cuando Pricing valida una cotización express, puede convertirla en oferta formal.

---

## 16. Automatizaciones recomendadas

El sistema debería automatizar o semiautomatizar:

- Recordatorios de llamadas.
- Recordatorios de visitas.
- Seguimiento de cotizaciones express.
- Seguimiento de ofertas formales.
- Alertas de tareas vencidas.
- Alertas de clientes sin seguimiento.
- Alertas de cotizaciones próximas a vencer.
- Alertas de clientes con baja de actividad.
- Generación de próxima acción desde una actividad.
- Conversión de prospecto a cliente.
- Creación de oportunidad desde una cotización rechazada.
- Creación de oportunidad desde análisis externo.
- Sugerencia de próximos pasos con IA.
- Resumen previo a visita.
- Notificaciones a vendedores y jefatura.
- Notificación a Pricing cuando una cotización express requiera revisión.

---

## 17. Integraciones con otros servicios

### Auth Service

Controla autenticación, autorización y scopes de acceso.

### Pricing Service

Recibe cotizaciones express que requieren revisión formal y devuelve ofertas formales convertidas.

### Notification Service

Envía alertas, recordatorios y notificaciones comerciales.

### Audit Log Service

Registra acciones importantes del usuario.

### Report Service

Genera reportes comerciales, dashboards e indicadores.

### AI Service

Apoya con resúmenes, sugerencias, análisis comercial y recomendaciones.

### Storage Service

Administra documentos, adjuntos, evidencias y archivos relacionados.

---

## 18. Auditoría requerida

Deben auditarse las siguientes acciones:

- Crear cliente.
- Editar cliente.
- Crear prospecto.
- Editar prospecto.
- Convertir prospecto a cliente.
- Crear contacto.
- Crear actividad.
- Crear próxima acción.
- Crear oportunidad.
- Cambiar etapa de oportunidad.
- Crear cotización express.
- Editar cotización express.
- Cambiar estado de cotización express.
- Enviar cotización express al cliente.
- Enviar cotización express a Pricing.
- Registrar motivo de pérdida.
- Reasignar vendedor.
- Crear solicitud de crédito.

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

Ejemplos para CRM Comercial:

```txt
crm.customers.read
crm.customers.create
crm.customers.update
crm.customers.reassign

crm.prospects.read
crm.prospects.create
crm.prospects.update
crm.prospects.convert

crm.contacts.read
crm.contacts.create
crm.contacts.update

crm.activities.read
crm.activities.create
crm.activities.update

crm.next-actions.read
crm.next-actions.create
crm.next-actions.update
crm.next-actions.complete

crm.opportunities.read
crm.opportunities.create
crm.opportunities.update
crm.opportunities.change-stage

crm.express-quotes.read
crm.express-quotes.create
crm.express-quotes.update
crm.express-quotes.send-customer
crm.express-quotes.send-pricing
crm.express-quotes.change-status

crm.commercial-profile.read
crm.commercial-profile.update

crm.objections.read
crm.objections.create

crm.loss-reasons.read
crm.loss-reasons.create

crm.credit-requests.read
crm.credit-requests.create
crm.credit-requests.update

crm.dashboard.read
crm.manager-view.read
crm.reports.read
```

Los scopes deben ser administrados desde el Auth Service y asignados a roles creados dinámicamente. Únicamente los roles Administrador y Superusuario deben existir como seed inicial.

---

## 20. Consideraciones técnicas generales

El servicio debe diseñarse bajo arquitectura de microservicios.

Debe contemplar:

- PostgreSQL para información relacional.
- MongoDB para historial, notas, comentarios, eventos comerciales y snapshots.
- Redis para cache, sesiones, indicadores rápidos y listas de trabajo.
- Outbox Pattern para comunicación asíncrona entre servicios.
- Background worker para procesar eventos pendientes.
- Integración con Auth Service para scopes.
- Integración con Audit Log Service para trazabilidad.
- Integración con Notification Service para alertas.
- Integración con Report Service para dashboards.
- Integración con AI Service para asistencia comercial.
- Integración con Storage Service para adjuntos.

---

## 21. Entidades sugeridas en PostgreSQL

### crm_customers

Tabla para clientes comerciales.

Campos sugeridos:

- id.
- external_customer_id.
- customer_name.
- legal_name.
- identification_number.
- assigned_seller_id.
- commercial_status.
- priority.
- created_at.
- updated_at.
- created_by.
- updated_by.
- is_active.

### crm_prospects

Tabla para prospectos.

Campos sugeridos:

- id.
- company_name.
- contact_name.
- phone.
- email.
- location.
- economic_activity.
- source.
- assigned_seller_id.
- status.
- next_action_date.
- created_at.
- updated_at.
- created_by.
- updated_by.
- is_active.

### crm_contacts

Tabla para contactos.

Campos sugeridos:

- id.
- customer_id.
- prospect_id.
- full_name.
- position.
- area.
- phone.
- email.
- whatsapp.
- communication_preference.
- decision_maker.
- influence_level.
- notes.
- created_at.
- updated_at.
- is_active.

### crm_activities

Tabla para actividades comerciales.

Campos sugeridos:

- id.
- customer_id.
- prospect_id.
- contact_id.
- seller_id.
- activity_type.
- activity_date.
- result.
- comments.
- next_action_id.
- status.
- created_at.
- updated_at.
- created_by.
- updated_by.

### crm_next_actions

Tabla para próximas acciones.

Campos sugeridos:

- id.
- customer_id.
- prospect_id.
- opportunity_id.
- activity_id.
- seller_id.
- action_type.
- due_date.
- priority.
- status.
- comments.
- completed_at.
- created_at.
- updated_at.

### crm_opportunities

Tabla para oportunidades comerciales.

Campos sugeridos:

- id.
- customer_id.
- prospect_id.
- seller_id.
- potential_service.
- estimated_value.
- probability.
- stage.
- expected_close_date.
- source.
- express_quote_id.
- formal_offer_id.
- closing_reason_id.
- created_at.
- updated_at.
- created_by.
- updated_by.

### crm_express_quotes

Tabla para cotizaciones express.

Campos sugeridos:

- id.
- customer_id.
- prospect_id.
- contact_id.
- seller_id.
- opportunity_id.
- origin.
- destination.
- shipping_method.
- modality.
- equipment_type.
- weight.
- cbm.
- dimensions.
- incoterm.
- cargo_type.
- required_services.
- estimated_amount.
- currency.
- estimated_validity_date.
- observations.
- status.
- pricing_required.
- pricing_request_id.
- formal_offer_id.
- created_at.
- updated_at.
- created_by.
- updated_by.

### crm_quote_followups

Tabla para seguimiento de cotizaciones.

Campos sugeridos:

- id.
- express_quote_id.
- formal_offer_id.
- seller_id.
- followup_date.
- result.
- next_action_date.
- comments.
- created_at.
- created_by.

### crm_objections

Tabla para objeciones comerciales.

Campos sugeridos:

- id.
- customer_id.
- prospect_id.
- opportunity_id.
- express_quote_id.
- formal_offer_id.
- seller_id.
- objection_type.
- comments.
- created_at.
- created_by.

### crm_loss_reasons

Tabla para motivos de pérdida.

Campos sugeridos:

- id.
- customer_id.
- prospect_id.
- opportunity_id.
- express_quote_id.
- formal_offer_id.
- seller_id.
- reason_type.
- competitor_name.
- comments.
- created_at.
- created_by.

### crm_seller_reassignments

Tabla para reasignación de vendedor.

Campos sugeridos:

- id.
- customer_id.
- prospect_id.
- previous_seller_id.
- new_seller_id.
- reason.
- comments.
- created_at.
- created_by.

### crm_credit_requests

Tabla para solicitudes de crédito.

Campos sugeridos:

- id.
- customer_id.
- prospect_id.
- seller_id.
- status.
- requested_amount.
- comments.
- created_at.
- updated_at.
- created_by.
- updated_by.

---

## 22. Colecciones sugeridas en MongoDB

### commercial_customer_profile

Colección para perfil comercial extendido del cliente.

Documento sugerido:

- customerId.
- communicationPreferences.
- negotiationStyle.
- priceSensitivity.
- knownCompetitors.
- strategicNotes.
- relationshipLevel.
- decisionMakers.
- relevantInterests.
- serviceOpportunities.
- commercialRisks.
- updatedAt.
- updatedBy.

### commercial_activity_timeline

Colección para línea de tiempo comercial.

Documento sugerido:

- entityType.
- entityId.
- eventType.
- title.
- description.
- relatedUserId.
- metadata.
- createdAt.

### express_quote_snapshots

Colección para snapshots de cotización express.

Documento sugerido:

- expressQuoteId.
- status.
- quoteData.
- sellerId.
- customerId.
- prospectId.
- createdAt.

### ai_commercial_summaries

Colección para resúmenes generados por IA.

Documento sugerido:

- entityType.
- entityId.
- summaryType.
- summary.
- inputReferences.
- createdAt.
- createdByModel.

---

## 23. Uso recomendado de Redis

Redis puede utilizarse para:

- Cache de dashboard comercial.
- Cache de agenda diaria.
- Cache de cotizaciones vivas por vendedor.
- Cache de tareas pendientes.
- Cache de indicadores gerenciales.
- Locks temporales para evitar doble procesamiento.
- Estados temporales de formularios móviles.
- Notificaciones pendientes.

Ejemplos de claves:

```txt
crm:seller:{sellerId}:daily-agenda
crm:seller:{sellerId}:open-opportunities
crm:seller:{sellerId}:express-quotes
crm:manager:dashboard:{date}
crm:customer:{customerId}:summary
```

---

## 24. Outbox Pattern y eventos

El CRM Comercial debe utilizar Outbox Pattern para publicar eventos hacia otros servicios sin perder consistencia.

### Tabla crm_outbox_messages

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

- CustomerCreated.
- ProspectCreated.
- ProspectConvertedToCustomer.
- CommercialActivityCreated.
- NextActionCreated.
- OpportunityCreated.
- ExpressQuoteCreated.
- ExpressQuoteSentToCustomer.
- ExpressQuoteRequiresPricingReview.
- ExpressQuoteRejected.
- ExpressQuoteAcceptedPreliminarily.
- ExpressQuoteConvertedToFormalOffer.
- SellerReassigned.
- CreditRequestCreated.

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

- Actividades por vendedor.
- Cotizaciones express por vendedor.
- Cotizaciones express aceptadas.
- Cotizaciones express rechazadas.
- Motivos de pérdida.
- Prospectos por etapa.
- Oportunidades por etapa.
- Clientes sin seguimiento.
- Productividad comercial.
- Dashboard gerencial.
- Seguimiento de tareas.
- Reasignación de vendedores.
- Solicitudes de crédito.

Indicadores sugeridos:

- Meta del mes.
- Ventas del mes.
- Cumplimiento de meta.
- Cotizaciones express creadas.
- Cotizaciones vivas.
- Cotizaciones aceptadas.
- Cotizaciones rechazadas.
- Oportunidades abiertas.
- Oportunidades ganadas.
- Oportunidades perdidas.
- Prospectos por etapa.
- Actividades por vendedor.
- Visitas realizadas.
- Llamadas realizadas.
- Clientes sin seguimiento.
- Clientes con baja de actividad.
- Tareas vencidas.
- Motivos de rechazo.
- Motivos de pérdida.

---

## 27. IA como apoyo

La IA puede apoyar al equipo comercial en:

- Resumir historial del cliente.
- Preparar resumen antes de una visita.
- Sugerir próxima acción.
- Detectar clientes sin seguimiento.
- Detectar clientes con baja de actividad.
- Sugerir oportunidades.
- Analizar motivos de rechazo.
- Comparar cotizaciones aceptadas contra rechazadas.
- Sugerir argumentos comerciales.
- Sugerir manejo de objeciones.
- Analizar datos externos importados.
- Identificar patrones de pérdida.
- Recomendar qué cliente visitar.
- Ayudar a preparar correos comerciales.
- Resumir cotizaciones express.
- Sugerir cuándo escalar una cotización express a Pricing.

Regla general:

La IA debe ser de apoyo. No debe tomar decisiones definitivas sin validación humana.

---

## 28. Problemas detectados

Durante el levantamiento se identificaron los siguientes problemas:

- Mucho control en archivos compartidos.
- Seguimiento manual de tareas.
- Dificultad para saber qué hizo cada vendedor durante el día.
- Alto volumen de correos.
- Muchas cotizaciones vivas que requieren revisión.
- Falta de recordatorios automáticos.
- Riesgo de olvidar contactar clientes.
- Prospectos sin seguimiento oportuno.
- Cotizaciones rechazadas sin análisis suficiente.
- Falta de registro formal de objeciones.
- Información comercial dispersa.
- Información útil del cliente no queda centralizada.
- Análisis externo no queda conectado a oportunidades.
- No existe una agenda comercial automatizada.
- No existe un perfil comercial completo del cliente.
- Cotizaciones en campo no se capturan de forma estructurada.
- Solicitudes de crédito se siguen de forma manual o dispersa.
- Dificultad para identificar cuándo un cliente baja actividad.
- Dificultad para saber si un cliente se está yendo con competencia.
- Dependencia de Pricing para respuestas que el vendedor podría iniciar desde campo.

---

## 29. Puntos de mejora identificados

1. Centralizar cartera comercial.
2. Automatizar seguimiento.
3. Registrar actividades comerciales.
4. Controlar prospectos por etapa.
5. Permitir cotización express desde celular.
6. Conectar CRM con Pricing.
7. Dar seguimiento a cotizaciones vivas.
8. Analizar rechazos.
9. Crear perfil comercial del cliente.
10. Gestionar oportunidades.
11. Usar IA como apoyo comercial.
12. Generar reportes gerenciales.
13. Reducir controles manuales.
14. Mejorar trazabilidad.
15. Proteger información estratégica mediante scopes.

---

## 30. Resumen final

El CRM Comercial debe funcionar como el servicio principal para administrar la operación comercial diaria.

No debe ser únicamente un módulo para registrar ventas, sino una herramienta para administrar clientes, prospectos, cartera, actividades, oportunidades, cotizaciones express, seguimiento comercial, recordatorios, agenda diaria, objeciones, motivos de pérdida y análisis comercial.

La cotización express debe permitir que el vendedor cree una cotización rápida desde celular, sin depender inicialmente de Pricing. Pricing participa únicamente cuando se requiere validación formal, revisión de margen, tarifas especiales o conversión a oferta formal.

El objetivo principal es que el sistema ayude al vendedor a vender mejor, centralizando información, automatizando seguimiento, dando visibilidad a gerencia y evitando que los clientes se pierdan por falta de atención.
