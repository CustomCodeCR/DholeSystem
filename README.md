# Dhole Microservices

Repositorio principal para el desarrollo de **Dhole Microservices**, un ecosistema de microservicios orientado a centralizar procesos comerciales, pricing, configuración, autenticación, auditoría, reportes, almacenamiento, notificaciones e inteligencia artificial.

---

## Objetivo del proyecto

Dhole Microservices tiene como objetivo construir una plataforma modular, escalable y mantenible, donde cada servicio tenga una responsabilidad clara y pueda evolucionar de forma independiente.

El sistema está diseñado para:

- Separar responsabilidades por servicio.
- Evitar acoplamiento entre módulos.
- Centralizar autenticación y permisos.
- Manejar permisos granulares mediante scopes.
- Usar comunicación asíncrona mediante eventos.
- Mantener trazabilidad con CorrelationId.
- Registrar auditoría genérica.
- Generar reportes en CSV, Excel y PDF.
- Manejar archivos mediante un servicio de storage genérico.
- Integrar procesos de IA como servicio complementario.

---

## Arquitectura general

El sistema se basa en una arquitectura de microservicios.

Cada microservicio tiene:

- Su propia responsabilidad.
- Su propia base de datos.
- Sus propios contratos.
- Sus propios endpoints.
- Sus propias migraciones.
- Sus propios workers cuando aplique.
- Sus propias pruebas.

La comunicación entre servicios se realizará mediante:

- HTTP para operaciones síncronas.
- Redis Streams para eventos asíncronos.
- Outbox Pattern para publicación confiable.
- Inbox Pattern para consumo idempotente.

---

## Servicios del ecosistema

| Servicio                  | Responsabilidad                                    |
| ------------------------- | -------------------------------------------------- |
| DholeBuildingBlocks       | Base técnica compartida                            |
| DholeAuthService          | Usuarios, roles, scopes, tokens y sesiones         |
| DholeConfigService        | Configuración general del ecosistema               |
| DholeCrmService           | Clientes, contactos y seguimiento comercial        |
| DholePricingService       | Cotizaciones, ofertas, tarifas, costos y márgenes  |
| DholeStorageService       | Archivos, metadata y proveedores de almacenamiento |
| DholeNotificationsService | Plantillas, mensajes, envíos y reintentos          |
| DholeAuditLogsService     | Auditoría genérica del sistema                     |
| DholeReportsService       | Reportes, exportaciones CSV, Excel y PDF           |
| DholeAiService            | Tareas de IA, análisis y resultados                |

---

## Stack técnico base

| Área                       | Tecnología     |
| -------------------------- | -------------- |
| Backend                    | .NET           |
| Base de datos principal    | PostgreSQL     |
| Cache / Streams            | Redis          |
| Datos flexibles opcionales | MongoDB        |
| Comunicación asíncrona     | Redis Streams  |
| Patrón de publicación      | Outbox Pattern |
| Patrón de consumo          | Inbox Pattern  |
| Documentación              | Markdown       |
| Contenedores               | Docker         |
| Control de versiones       | Git / GitHub   |

---

## Estructura del repositorio

```text
dhole-microservices
  /docs
  /src
  /tests
  /deploy
  /scripts
  /tools
  README.md
  docker-compose.yml
  .gitignore
```

---

## Estructura de documentación

```text
/docs
  /architecture
    architecture-diagram.md
    database-overview.md
    technical-decisions.md

  /standards
    development-standards.md

  /api
    api-conventions.md

  /security
    technical-security.md
    permissions-scopes.md

  /events
    event-catalog.md

  /testing
    testing-strategy.md

  /deployment
    deployment-strategy.md

  /development
    repository-structure.md

  /estimation
    hu-time-estimation.md
    roadmap.md

  /backlog
    user-stories.md
```

---

## Documentos principales

| Documento                   | Ruta                                        |
| --------------------------- | ------------------------------------------- |
| Estándares de desarrollo    | `docs/standards/development-standards.md`   |
| Seguridad técnica           | `docs/security/technical-security.md`       |
| Modelo de permisos y scopes | `docs/security/permissions-scopes.md`       |
| Convenciones API            | `docs/api/api-conventions.md`               |
| Estrategia de despliegue    | `docs/deployment/deployment-strategy.md`    |
| Catálogo de eventos         | `docs/events/event-catalog.md`              |
| Estrategia de pruebas       | `docs/testing/testing-strategy.md`          |
| Estructura de repositorios  | `docs/development/repository-structure.md`  |
| Historias de usuario        | `docs/backlog/user-stories.md`              |
| Diagrama de arquitectura    | `docs/architecture/architecture-diagram.md` |
| Diagrama de base de datos   | `docs/architecture/database-overview.md`    |
| Estimación de tiempo        | `docs/estimation/hu-time-estimation.md`     |
| Roadmap                     | `docs/estimation/roadmap.md`                |

---

## Estructura sugerida de servicios

```text
/src
  /BuildingBlocks
    /Dhole.BuildingBlocks

  /Services
    /Auth
      /Dhole.AuthService.Api
      /Dhole.AuthService.Application
      /Dhole.AuthService.Domain
      /Dhole.AuthService.Infrastructure
      /Dhole.AuthService.Contracts
      /Dhole.AuthService.Workers

    /Config
      /Dhole.ConfigService.Api
      /Dhole.ConfigService.Application
      /Dhole.ConfigService.Domain
      /Dhole.ConfigService.Infrastructure
      /Dhole.ConfigService.Contracts
      /Dhole.ConfigService.Workers

    /CRM
      /Dhole.CrmService.Api
      /Dhole.CrmService.Application
      /Dhole.CrmService.Domain
      /Dhole.CrmService.Infrastructure
      /Dhole.CrmService.Contracts
      /Dhole.CrmService.Workers

    /Pricing
      /Dhole.PricingService.Api
      /Dhole.PricingService.Application
      /Dhole.PricingService.Domain
      /Dhole.PricingService.Infrastructure
      /Dhole.PricingService.Contracts
      /Dhole.PricingService.Workers

    /Storage
      /Dhole.StorageService.Api
      /Dhole.StorageService.Application
      /Dhole.StorageService.Domain
      /Dhole.StorageService.Infrastructure
      /Dhole.StorageService.Contracts
      /Dhole.StorageService.Workers

    /Notifications
      /Dhole.NotificationsService.Api
      /Dhole.NotificationsService.Application
      /Dhole.NotificationsService.Domain
      /Dhole.NotificationsService.Infrastructure
      /Dhole.NotificationsService.Contracts
      /Dhole.NotificationsService.Workers

    /AuditLogs
      /Dhole.AuditLogsService.Api
      /Dhole.AuditLogsService.Application
      /Dhole.AuditLogsService.Domain
      /Dhole.AuditLogsService.Infrastructure
      /Dhole.AuditLogsService.Contracts
      /Dhole.AuditLogsService.Workers

    /Reports
      /Dhole.ReportsService.Api
      /Dhole.ReportsService.Application
      /Dhole.ReportsService.Domain
      /Dhole.ReportsService.Infrastructure
      /Dhole.ReportsService.Contracts
      /Dhole.ReportsService.Workers

    /AI
      /Dhole.AiService.Api
      /Dhole.AiService.Application
      /Dhole.AiService.Domain
      /Dhole.AiService.Infrastructure
      /Dhole.AiService.Contracts
      /Dhole.AiService.Workers
```

---

## Base técnica compartida

`DholeBuildingBlocks` contiene contratos técnicos reutilizables por todos los servicios.

Debe incluir:

- Result
- Result<T>
- Error
- PagedResult<T>
- IntegrationEvent
- EventEnvelope
- CorrelationId
- Contratos base de Outbox
- Contratos base de Inbox
- Respuestas estándar
- Errores estándar
- Contratos de paginación

`DholeBuildingBlocks` no debe contener reglas de negocio de ningún servicio.

---

## Seguridad

La seguridad será gestionada por `DholeAuthService`.

El sistema usará:

- Usuarios
- Roles
- Scopes
- Access tokens
- Refresh tokens
- Sesiones
- Cache de permisos en Redis

Los permisos se validan mediante scopes.

Formato estándar:

```text
service.resource.action
```

Ejemplos:

```text
auth.users.create
crm.customers.read
pricing.quotes.approve
storage.files.download
reports.exports.generate
```

Los únicos roles creados por seed son:

```text
Administrador
Superusuario
```

El resto de roles deben ser creados desde el sistema.

---

## Comunicación entre servicios

La comunicación síncrona se usará solo cuando el servicio necesite una respuesta inmediata.

Ejemplos:

- Validar token.
- Consultar configuración.
- Consultar información necesaria para completar una operación directa.

La comunicación asíncrona se usará para procesos desacoplados.

Ejemplos:

- Auditoría.
- Notificaciones.
- Reportes.
- Procesamiento de IA.
- Proyecciones.
- Eventos de negocio.

---

## Eventos

Los eventos deben representar hechos ocurridos.

Correcto:

```text
CustomerCreated
QuoteApproved
FileUploaded
ReportGenerated
NotificationSent
AiTaskCompleted
```

Incorrecto:

```text
CreateCustomer
ApproveQuote
UploadFile
GenerateReport
SendNotification
CompleteAiTask
```

Todo evento debe incluir:

```text
EventId
EventType
Version
SourceService
OccurredAt
CorrelationId
Payload
```

---

## Outbox e Inbox

Cada servicio que publique eventos debe usar Outbox.

Cada servicio que consuma eventos debe usar Inbox.

### Outbox

Permite publicar eventos de forma confiable después de confirmar una operación de negocio.

Flujo:

```text
1. Ejecutar operación de negocio.
2. Guardar cambios en base de datos.
3. Guardar evento en OutboxMessages.
4. Confirmar transacción.
5. Worker publica evento.
6. Evento se marca como publicado.
```

### Inbox

Permite consumir eventos de forma idempotente.

Flujo:

```text
1. Consumir evento desde Redis Streams.
2. Verificar si el evento ya fue procesado.
3. Si no fue procesado, ejecutar lógica.
4. Registrar evento en InboxMessages.
5. Marcar evento como procesado.
```

---

## Bases de datos

Cada servicio debe tener su propia base de datos o esquema lógico independiente.

No se permite que un servicio acceda directamente a las tablas de otro servicio.

Base principal:

```text
PostgreSQL
```

Uso complementario:

```text
Redis
MongoDB cuando aplique
```

Tablas técnicas comunes por servicio:

```text
OutboxMessages
InboxMessages
```

---

## Redis

Redis se usará para:

- Cache
- Sesiones
- Permisos cacheados
- Locks distribuidos
- Redis Streams
- Idempotencia temporal

Formato recomendado de keys:

```text
dhole:{service}:{resource}:{id}
```

Ejemplos:

```text
dhole:auth:user-permissions:{userId}
dhole:auth:session:{sessionId}
dhole:pricing:quote-summary:{quoteId}
```

---

## Reportes

`DholeReportsService` será responsable de generar reportes.

Debe soportar:

- CSV
- Excel
- PDF

Los archivos generados deben guardarse mediante `DholeStorageService`.

Reports no debe guardar archivos físicos directamente.

---

## Storage

`DholeStorageService` será responsable de manejar archivos de forma genérica.

Debe manejar:

- Metadata
- Versiones
- Referencias
- Proveedor de almacenamiento
- Relación lógica entre archivo y entidad origen

El proveedor físico debe ser configurable.

Opciones esperadas:

- Local Storage
- S3
- Azure Blob

---

## Notificaciones

`DholeNotificationsService` será responsable de manejar notificaciones de forma genérica.

Debe manejar:

- Plantillas
- Destinatarios
- Mensajes
- Adjuntos
- Intentos de envío
- Estados
- Errores

Las notificaciones pueden ser solicitadas mediante eventos.

---

## Auditoría

`DholeAuditLogsService` será responsable de registrar auditoría genérica del ecosistema.

Debe auditar:

- Creación de registros
- Actualización de registros
- Eliminación lógica
- Cambios de estado
- Accesos
- Cambios de permisos
- Eventos relevantes de negocio
- Errores críticos

---

## IA

`DholeAiService` será responsable de procesar tareas de IA.

Debe manejar:

- Solicitudes de análisis
- Tareas pendientes
- Procesamiento asíncrono
- Resultados
- Errores
- Historial de tareas

La IA debe funcionar como servicio complementario, no como dependencia central del sistema.

---

## Ejecución local

La ejecución local se realizará mediante Docker Compose.

Servicios base esperados:

```text
PostgreSQL
Redis
MongoDB
DholeAuthService
DholeConfigService
DholeCrmService
DholePricingService
DholeStorageService
DholeNotificationsService
DholeAuditLogsService
DholeReportsService
DholeAiService
```

Comando sugerido:

```bash
docker compose up -d
```

---

## Variables de entorno

Cada servicio debe manejar sus propias variables.

Ejemplos:

```text
ASPNETCORE_ENVIRONMENT
ConnectionStrings__Postgres
ConnectionStrings__Redis
ConnectionStrings__Mongo
Jwt__Issuer
Jwt__Audience
Jwt__SigningKey
Storage__Provider
Storage__BasePath
```

No se deben guardar secretos directamente en el código.

---

## Pruebas

Cada servicio debe tener pruebas propias.

Tipos mínimos:

- Unit tests
- Integration tests
- API tests
- Event tests
- Worker tests
- Security tests

Estructura sugerida:

```text
/tests
  /Auth
    /Dhole.AuthService.UnitTests
    /Dhole.AuthService.IntegrationTests

  /CRM
    /Dhole.CrmService.UnitTests
    /Dhole.CrmService.IntegrationTests

  /Pricing
    /Dhole.PricingService.UnitTests
    /Dhole.PricingService.IntegrationTests
```

---

## Criterios para cerrar una HU

Una historia de usuario puede cerrarse cuando:

```text
[ ] Código implementado
[ ] Migraciones aplicadas
[ ] Endpoints funcionando
[ ] Validaciones aplicadas
[ ] Permisos aplicados
[ ] Eventos implementados si aplica
[ ] Pruebas mínimas ejecutadas
[ ] Logs incluidos
[ ] README actualizado si aplica
```

---

## Orden recomendado de desarrollo

```text
Fase 1 - Base técnica
1. DholeBuildingBlocks
2. Contratos de eventos
3. Outbox / Inbox
4. Plantilla base de microservicio

Fase 2 - Seguridad y configuración
5. DholeAuthService
6. Usuarios
7. Roles
8. Scopes
9. Tokens y sesiones
10. Cache de permisos
11. DholeConfigService

Fase 3 - Base comercial
12. DholeCrmService
13. Clientes
14. Contactos
15. Seguimientos
16. DholePricingService
17. Cotización express
18. Costos y márgenes
19. Aprobación de cotización
20. Oferta formal

Fase 4 - Servicios complementarios
21. DholeStorageService
22. DholeNotificationsService
23. DholeAuditLogsService
24. DholeReportsService
25. DholeAiService

Fase 5 - Integración
26. Eventos end-to-end
27. Workers
28. Pruebas integradas
29. Hardening
30. Despliegue inicial
```

---

## Reglas generales del repositorio

- Todo código debe estar en inglés.
- Toda documentación funcional puede estar en español.
- Cada servicio debe tener su propia responsabilidad.
- Cada servicio debe tener su propia persistencia.
- Ningún servicio debe consultar directamente la base de otro servicio.
- Los permisos se manejan por scopes.
- Los roles no se queman en código.
- Los eventos se publican mediante Outbox.
- Los eventos se consumen mediante Inbox.
- Todo evento debe incluir CorrelationId.
- Todo endpoint debe usar respuesta estándar.
- Todo servicio debe tener README propio.
- Toda HU debe tener criterios de aceptación claros.

---

## Estado actual del proyecto

```text
[x] Levantamientos de requerimientos por departamento
[x] Historias de usuario en GitHub
[x] Diagrama de arquitectura
[x] Documentación técnica base
[ ] Diagrama de base de datos
[ ] Estimación de tiempo por HU
[ ] Roadmap final
[ ] Desarrollo inicial
```

---

## Licencia

Este repositorio es privado y pertenece al proyecto Dhole Microservices.
