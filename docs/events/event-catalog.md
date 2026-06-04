# Catálogo de Eventos - Dhole Microservices

## 1. Objetivo

Este documento define el catálogo inicial de eventos para Dhole Microservices.

Los eventos permiten comunicación asíncrona entre servicios mediante Outbox, Redis Streams e Inbox.

---

## 2. Reglas generales

Todo evento debe representar un hecho que ya ocurrió.

Los nombres deben estar en pasado.

Correcto:

```text
CustomerCreated
QuoteApproved
FileUploaded
ReportGenerated
```

Incorrecto:

```text
CreateCustomer
ApproveQuote
UploadFile
GenerateReport
```

---

## 3. Estructura base de evento

Todo evento debe incluir:

```json
{
  "eventId": "00000000-0000-0000-0000-000000000000",
  "eventType": "CustomerCreated",
  "version": 1,
  "sourceService": "DholeCrmService",
  "occurredAt": "2026-06-04T18:30:00Z",
  "correlationId": "00000000-0000-0000-0000-000000000000",
  "payload": {}
}
```

---

## 4. Eventos de Auth

### UserCreated

Publicador:

```text
DholeAuthService
```

Cuándo se publica:

```text
Cuando se crea un usuario.
```

Consumidores:

```text
DholeAuditLogsService
DholeNotificationsService
```

Payload mínimo:

```json
{
  "userId": "uuid",
  "email": "user@company.com",
  "displayName": "User Name"
}
```

### UserUpdated

Se publica cuando se actualiza un usuario.

Consumidores:

```text
DholeAuditLogsService
```

### UserLocked

Se publica cuando un usuario es bloqueado.

Consumidores:

```text
DholeAuditLogsService
DholeNotificationsService
```

### RoleCreated

Se publica cuando se crea un rol.

Consumidores:

```text
DholeAuditLogsService
```

### ScopeAssignedToRole

Se publica cuando se asigna un scope a un rol.

Consumidores:

```text
DholeAuditLogsService
```

---

## 5. Eventos de Config

### ConfigurationChanged

Publicador:

```text
DholeConfigService
```

Cuándo se publica:

```text
Cuando se modifica una configuración del sistema.
```

Consumidores:

```text
DholeAuditLogsService
```

Payload mínimo:

```json
{
  "configurationId": "uuid",
  "key": "pricing.defaultCurrency",
  "oldValue": "CRC",
  "newValue": "USD"
}
```

---

## 6. Eventos de CRM

### CustomerCreated

Publicador:

```text
DholeCrmService
```

Cuándo se publica:

```text
Cuando se crea un cliente.
```

Consumidores:

```text
DholeAuditLogsService
DholePricingService
DholeReportsService
```

Payload mínimo:

```json
{
  "customerId": "uuid",
  "legalName": "Customer Legal Name",
  "taxIdentification": "000000000"
}
```

### CustomerUpdated

Se publica cuando se actualiza un cliente.

Consumidores:

```text
DholeAuditLogsService
DholePricingService
DholeReportsService
```

### ContactCreated

Se publica cuando se crea un contacto asociado a un cliente.

Consumidores:

```text
DholeAuditLogsService
DholeReportsService
```

### FollowUpCreated

Se publica cuando se registra un seguimiento comercial.

Consumidores:

```text
DholeAuditLogsService
DholeReportsService
DholeNotificationsService
```

---

## 7. Eventos de Pricing

### QuoteCreated

Publicador:

```text
DholePricingService
```

Cuándo se publica:

```text
Cuando se crea una cotización.
```

Consumidores:

```text
DholeAuditLogsService
DholeReportsService
```

Payload mínimo:

```json
{
  "quoteId": "uuid",
  "customerId": "uuid",
  "quoteNumber": "Q-000001",
  "status": "Draft"
}
```

### QuoteUpdated

Se publica cuando se actualiza una cotización.

Consumidores:

```text
DholeAuditLogsService
DholeReportsService
```

### QuoteApproved

Se publica cuando una cotización es aprobada.

Consumidores:

```text
DholeAuditLogsService
DholeNotificationsService
DholeReportsService
```

### QuoteRejected

Se publica cuando una cotización es rechazada.

Consumidores:

```text
DholeAuditLogsService
DholeNotificationsService
DholeReportsService
```

### OfferGenerated

Se publica cuando se genera una oferta formal.

Consumidores:

```text
DholeAuditLogsService
DholeStorageService
DholeReportsService
```

---

## 8. Eventos de Storage

### FileUploaded

Publicador:

```text
DholeStorageService
```

Cuándo se publica:

```text
Cuando se registra un archivo en Storage.
```

Consumidores:

```text
DholeAuditLogsService
```

Payload mínimo:

```json
{
  "fileId": "uuid",
  "fileName": "document.pdf",
  "contentType": "application/pdf",
  "relatedEntityType": "Quote",
  "relatedEntityId": "uuid"
}
```

### FileDeleted

Se publica cuando un archivo es eliminado o marcado como eliminado.

Consumidores:

```text
DholeAuditLogsService
```

### FileVersionCreated

Se publica cuando se registra una nueva versión de archivo.

Consumidores:

```text
DholeAuditLogsService
```

---

## 9. Eventos de Notifications

### NotificationRequested

Publicador:

```text
Cualquier servicio que solicite una notificación.
```

Consumidor principal:

```text
DholeNotificationsService
```

Payload mínimo:

```json
{
  "templateCode": "quote-approved",
  "recipientType": "User",
  "recipientId": "uuid",
  "data": {}
}
```

### NotificationSent

Publicador:

```text
DholeNotificationsService
```

Consumidores:

```text
DholeAuditLogsService
DholeReportsService
```

### NotificationFailed

Se publica cuando falla el envío de una notificación.

Consumidores:

```text
DholeAuditLogsService
DholeReportsService
```

---

## 10. Eventos de Reports

### ReportRequested

Publicador:

```text
Cualquier servicio que solicite un reporte.
```

Consumidor principal:

```text
DholeReportsService
```

Payload mínimo:

```json
{
  "reportCode": "pricing-summary",
  "requestedBy": "uuid",
  "parameters": {}
}
```

### ReportGenerated

Publicador:

```text
DholeReportsService
```

Consumidores:

```text
DholeAuditLogsService
DholeNotificationsService
```

### ReportFailed

Se publica cuando falla la generación de un reporte.

Consumidores:

```text
DholeAuditLogsService
DholeNotificationsService
```

---

## 11. Eventos de AI

### AiTaskRequested

Publicador:

```text
Cualquier servicio que solicite una tarea de IA.
```

Consumidor principal:

```text
DholeAiService
```

Payload mínimo:

```json
{
  "taskType": "AnalyzeQuote",
  "requestedBy": "uuid",
  "sourceEntityType": "Quote",
  "sourceEntityId": "uuid"
}
```

### AiTaskCompleted

Publicador:

```text
DholeAiService
```

Consumidores:

```text
DholeAuditLogsService
DholeReportsService
```

### AiTaskFailed

Se publica cuando falla una tarea de IA.

Consumidores:

```text
DholeAuditLogsService
```

---

## 12. Eventos de AuditLogs

### AuditEventRegistered

Publicador:

```text
DholeAuditLogsService
```

Cuándo se publica:

```text
Cuando se registra un evento de auditoría.
```

Consumidores:

```text
DholeReportsService
```

---

## 13. Streams sugeridos

Streams recomendados:

```text
dhole.auth.events
dhole.config.events
dhole.crm.events
dhole.pricing.events
dhole.storage.events
dhole.notifications.events
dhole.reports.events
dhole.ai.events
dhole.auditlogs.events
```

---

## 14. Reglas finales

- Todo evento se publica mediante Outbox.
- Todo consumidor registra el evento en Inbox.
- Todo evento debe incluir CorrelationId.
- Todo evento debe tener versión.
- Los eventos deben ser idempotentes.
- El payload debe ser mínimo y estable.
- No se deben enviar datos sensibles innecesarios en eventos.
