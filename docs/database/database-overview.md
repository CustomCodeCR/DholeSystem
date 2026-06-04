# Diagrama de Base de Datos - Dhole Microservices

## 1. Objetivo

Este documento define el modelo inicial de base de datos para Dhole Microservices.

El objetivo es representar las tablas principales por servicio, respetando la arquitectura de microservicios donde cada servicio es dueño de sus propios datos.

---

## 2. Regla principal

Cada microservicio tendrá su propia base de datos independiente.

No se permite que un servicio consulte directamente la base de datos de otro servicio.

La comunicación entre servicios debe realizarse mediante:

- HTTP.
- gRPC.
- Eventos asíncronos.
- Redis Streams.
- Outbox.
- Inbox.

---

## 3. Bases de datos por servicio

```text
dhole_auth_db
dhole_config_db
dhole_crm_db
dhole_pricing_db
dhole_storage_db
dhole_notifications_db
dhole_auditlogs_db
dhole_reports_db
dhole_ai_db
```

---

## 4. Tablas comunes por servicio

Cada servicio que publique o consuma eventos debe tener tablas técnicas para Outbox e Inbox.

Tablas estándar:

```text
OutboxMessages
InboxMessages
```

### OutboxMessages

Se usa para guardar eventos pendientes de publicación.

Flujo:

```text
1. El servicio ejecuta una operación de negocio.
2. Guarda los cambios en su base.
3. Guarda el evento en OutboxMessages.
4. Confirma la transacción.
5. Un worker publica el evento en Redis Streams.
6. El evento se marca como publicado.
```

### InboxMessages

Se usa para registrar eventos consumidos y evitar reprocesamiento.

Flujo:

```text
1. El servicio consume un evento desde Redis Streams.
2. Valida si ya existe en InboxMessages.
3. Si no existe, procesa el evento.
4. Registra el evento como procesado.
```

---

## 5. Auth Database

Responsabilidad:

```text
Usuarios, roles, scopes, sesiones, refresh tokens y control de acceso.
```

Tablas principales:

```text
Users
Roles
Scopes
UserRoles
RoleScopes
RefreshTokens
Sessions
OutboxMessages
InboxMessages
```

---

## 6. Config Database

Responsabilidad:

```text
Configuración general, módulos y feature flags del ecosistema.
```

Tablas principales:

```text
ConfigurationSettings
ConfigurationModules
FeatureFlags
OutboxMessages
InboxMessages
```

---

## 7. CRM Database

Responsabilidad:

```text
Clientes, contactos, direcciones, notas y seguimientos comerciales.
```

Tablas principales:

```text
Customers
Contacts
CustomerAddresses
CustomerNotes
CustomerFollowUps
OutboxMessages
InboxMessages
```

---

## 8. Pricing Database

Responsabilidad:

```text
Cotizaciones, ofertas, costos, cargos, tarifas, precios de venta y márgenes.
```

Tablas principales:

```text
Quotes
QuoteItems
QuoteCosts
QuoteCharges
QuoteMargins
Offers
OfferDocuments
Rates
OutboxMessages
InboxMessages
```

---

## 9. Storage Database

Responsabilidad:

```text
Metadata de archivos, versiones, referencias y proveedores de almacenamiento.
```

Tablas principales:

```text
Files
FileVersions
FileReferences
StorageProviders
OutboxMessages
InboxMessages
```

---

## 10. Notifications Database

Responsabilidad:

```text
Plantillas, mensajes, destinatarios, adjuntos, intentos de envío y estados.
```

Tablas principales:

```text
NotificationTemplates
NotificationMessages
NotificationRecipients
NotificationAttachments
NotificationDeliveryAttempts
OutboxMessages
InboxMessages
```

---

## 11. AuditLogs Database

Responsabilidad:

```text
Auditoría genérica del ecosistema.
```

Tablas principales:

```text
AuditEvents
AuditEventDetails
OutboxMessages
InboxMessages
```

Regla:

```text
AuditLogs no debe permitir modificación o eliminación de eventos registrados.
```

---

## 12. Reports Database

Responsabilidad:

```text
Definiciones de reportes, solicitudes, archivos generados, programación y logs de ejecución.
```

Tablas principales:

```text
ReportDefinitions
ReportRequests
ReportFiles
ScheduledReports
ReportExecutionLogs
OutboxMessages
InboxMessages
```

---

## 13. AI Database

Responsabilidad:

```text
Tareas de IA, mensajes, resultados, proveedores, errores e historial de procesamiento.
```

Tablas principales:

```text
AiTasks
AiTaskMessages
AiTaskResults
AiProviders
OutboxMessages
InboxMessages
```

---

## 14. Reglas de diseño

```text
1. Cada servicio tiene su propia base de datos.
2. No existen foreign keys entre bases de datos de distintos servicios.
3. Las relaciones entre servicios son lógicas, no físicas.
4. Las referencias externas se guardan como IDs simples.
5. Los eventos deben incluir CorrelationId.
6. Las tablas deben estar en inglés.
7. Las columnas deben estar en inglés.
8. Las fechas deben guardarse en UTC.
9. Las tablas transaccionales deben tener campos de auditoría.
10. Outbox e Inbox deben existir donde haya eventos.
```

---

## 15. Diagrama DBML

El diagrama completo está en:

```text
docs/database/database-diagram.dbml
```

Ese archivo puede copiarse directamente en:

```text
https://dbdiagram.io
```
