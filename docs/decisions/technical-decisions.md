# Decisiones Técnicas - Dhole Microservices

## 1. Objetivo

Este documento define las decisiones técnicas principales para el desarrollo de Dhole Microservices.

Su objetivo es dejar claras las reglas base del ecosistema antes de iniciar el desarrollo, evitando decisiones improvisadas o inconsistentes entre servicios.

Estas decisiones aplican para:

- Arquitectura general.
- Repositorios.
- Backend.
- Frontend.
- Bases de datos.
- Comunicación entre servicios.
- Seguridad.
- Eventos.
- Reportes.
- Storage.
- Notificaciones.
- Auditoría.
- IA.
- Despliegue.
- Observabilidad.
- Pruebas.

---

## 2. Estrategia de repositorios

### Decisión

Dhole Microservices utilizará una estrategia de **repositorio por servicio**.

Cada microservicio tendrá su propio repositorio independiente.

Repositorios esperados:

```text
dhole-auth-service
dhole-config-service
dhole-crm-service
dhole-pricing-service
dhole-storage-service
dhole-notifications-service
dhole-auditlogs-service
dhole-reports-service
dhole-ai-service
dhole-web-app
```

El repositorio actual será utilizado únicamente para documentación:

```text
dhole-microservices-docs
```

### Motivo

Se decide usar un repositorio por servicio para tener mayor control sobre:

- Despliegues independientes.
- Rollbacks independientes.
- Versionamiento por servicio.
- Trabajo aislado por servicio.
- Reducción de impacto entre cambios.
- Separación real de responsabilidades.

Esta decisión se alinea con el enfoque de microservicios, donde cada servicio puede evolucionar y desplegarse sin afectar directamente a los demás.

---

## 3. Building Blocks

### Decisión

No existirá un repositorio global para `DholeBuildingBlocks`.

Cada servicio tendrá sus propios building blocks internos.

### Motivo

La decisión busca evitar acoplamiento innecesario entre servicios.

Cada microservicio podrá definir sus propios contratos técnicos reutilizables de forma interna, sin depender de un paquete compartido global que pueda afectar a todo el ecosistema cuando cambie.

### Regla

Cada servicio puede tener una base técnica interna para:

- Result.
- Error.
- PagedResult.
- CorrelationId.
- Contratos internos.
- Helpers técnicos.
- Contratos Outbox.
- Contratos Inbox.

Pero esos elementos no deben contener reglas de negocio compartidas entre servicios.

---

## 4. Repositorio de documentación

### Decisión

El repositorio actual será únicamente para documentación.

No contendrá código fuente de servicios.

### Motivo

El repositorio de documentación funcionará como fuente central de:

- Levantamientos.
- Historias de usuario.
- Arquitectura.
- Decisiones técnicas.
- Roadmap.
- Modelo de permisos.
- Catálogo de eventos.
- Estándares.
- Diagramas.
- Estimaciones.

El código fuente vivirá en los repositorios independientes de cada servicio.

---

## 5. Backend

### Decisión

El backend será desarrollado con:

```text
.NET 10 LTS
```

### Motivo

Se utilizará una versión LTS para priorizar estabilidad, soporte a largo plazo y mantenimiento del ecosistema.

---

## 6. Estilo de API

### Decisión

Los servicios backend utilizarán:

```text
Minimal APIs
```

### Motivo

Minimal APIs permite construir endpoints más ligeros, directos y simples, reduciendo la cantidad de estructura innecesaria en servicios que estarán separados por dominio.

Esto facilita:

- Menos boilerplate.
- Endpoints más explícitos.
- Mejor organización por módulos.
- Arranque más rápido de servicios.
- Código más simple para APIs pequeñas y medianas.

---

## 7. CQRS

### Decisión

Se utilizará CQRS, pero sin MediatR.

### Motivo

CQRS permitirá separar operaciones de lectura y escritura, manteniendo mejor orden dentro de cada servicio.

No se utilizará MediatR para evitar dependencias innecesarias y reducir complejidad.

La separación se hará mediante clases, handlers o servicios de aplicación propios.

Ejemplo conceptual:

```text
CreateCustomerCommand
CreateCustomerHandler

SearchCustomersQuery
SearchCustomersHandler
```

### Regla

Cada servicio podrá organizar sus casos de uso en:

```text
Commands
Queries
Handlers
Application Services
```

Sin depender de MediatR.

---

## 8. Mapeo de objetos

### Decisión

No se utilizará AutoMapper.

El mapeo será manual o mediante un paquete alternativo que no requiera licencia.

### Motivo

Se evita depender de paquetes con restricciones de licencia o comportamientos implícitos difíciles de depurar.

El mapeo manual permite mayor control sobre:

- Requests.
- Responses.
- Entidades.
- DTOs.
- Eventos.
- Modelos de persistencia.

### Regla

Se permite usar un paquete de mapeo alternativo si:

- No requiere licencia comercial.
- No agrega complejidad innecesaria.
- Permite control explícito del mapeo.
- No oculta reglas importantes de transformación.

---

## 9. Validaciones

### Decisión

No se utilizará FluentValidation.

Las validaciones se implementarán de forma explícita dentro de cada servicio.

### Motivo

Se busca reducir dependencias externas y mantener control directo sobre las reglas de validación.

### Regla

Las validaciones podrán organizarse en:

```text
Request validators propios
Application validations
Domain validations
Guard clauses
```

Las validaciones deben ser claras, testeables y fáciles de mantener.

---

## 10. Arquitectura interna por servicio

### Decisión

Cada microservicio tendrá una estructura interna separada por responsabilidades.

Estructura base recomendada:

```text
/src
  /Dhole.ServiceName.Api
  /Dhole.ServiceName.Application
  /Dhole.ServiceName.Domain
  /Dhole.ServiceName.Infrastructure
  /Dhole.ServiceName.Contracts
  /Dhole.ServiceName.Workers

/tests
  /Dhole.ServiceName.UnitTests
  /Dhole.ServiceName.IntegrationTests
```

### Motivo

Esta estructura permite separar:

- Entrada HTTP.
- Casos de uso.
- Dominio.
- Persistencia.
- Contratos.
- Workers.
- Pruebas.

---

## 11. Independencia del dominio

### Decisión

El proyecto `Domain` debe ser independiente de `Infrastructure`.

### Motivo

El dominio no debe depender de detalles técnicos como:

- Base de datos.
- Redis.
- MongoDB.
- HTTP clients.
- Storage providers.
- Frameworks externos.

Esto permite mantener reglas de negocio limpias y testeables.

### Regla

Dependencias permitidas:

```text
Api -> Application
Api -> Infrastructure
Application -> Domain
Infrastructure -> Application
Infrastructure -> Domain
Contracts -> Independiente o compartido según necesidad interna
```

El dominio no debe depender de infraestructura.

---

## 12. Shared Kernel interno

### Decisión

Cada servicio puede tener su propio Shared Kernel interno.

No existirá un Shared Kernel global de dominio.

### Motivo

Cada servicio tendrá reglas, value objects, constantes o estructuras internas propias.

Estas no deben compartirse globalmente porque podrían generar acoplamiento entre servicios.

Ejemplo:

```text
DholePricingService puede tener value objects propios de Pricing.
DholeCrmService puede tener value objects propios de CRM.
```

### Regla

El Shared Kernel interno de un servicio no debe ser consumido por otro servicio.

---

## 13. Base de datos principal

### Decisión

La base de datos principal será:

```text
PostgreSQL
```

### Motivo

PostgreSQL será utilizado como base relacional principal por su estabilidad, robustez y buen soporte para sistemas transaccionales.

---

## 14. Separación de bases de datos

### Decisión

Cada servicio tendrá su base de datos separada.

No se utilizará una única base compartida con schemas por servicio.

### Motivo

Esta decisión refuerza la independencia real entre microservicios.

Cada servicio será dueño de sus datos.

### Regla

Ningún servicio debe consultar directamente la base de datos de otro servicio.

La comunicación entre servicios debe realizarse mediante:

```text
HTTP
gRPC
Eventos
```

---

## 15. Uso de MongoDB

### Decisión

MongoDB se utilizará en todos los casos donde sea posible y tenga sentido desde el inicio.

### Motivo

MongoDB permitirá manejar datos flexibles, documentos, snapshots, payloads, resultados de IA, auditoría extendida o información que no requiera estructura relacional estricta.

### Uso esperado

MongoDB puede ser utilizado en servicios como:

```text
DholeAuditLogsService
DholeAiService
DholeReportsService
DholeNotificationsService
DholeStorageService
```

Y en cualquier otro servicio donde el modelo documental aporte valor.

### Regla

PostgreSQL seguirá siendo la base principal para información transaccional.

MongoDB se usará para datos flexibles, históricos, documentos lógicos, snapshots o payloads variables.

---

## 16. Redis

### Decisión

Redis se utilizará desde el inicio para:

```text
Cache
Sesiones
Permisos cacheados
Redis Streams
Locks distribuidos
Rate limit
Idempotencia temporal
```

### Motivo

Redis será una pieza central para mejorar rendimiento, manejar comunicación asíncrona y controlar operaciones distribuidas.

### Usos principales

```text
Cache de consultas frecuentes
Sesiones de usuario
Cache de scopes por usuario
Redis Streams para eventos
Locks para operaciones críticas
Rate limit para endpoints sensibles
Idempotencia temporal para operaciones repetidas
```

---

## 17. Acceso a datos

### Decisión

Se utilizarán ambos:

```text
EF Core
Dapper
```

### Motivo

EF Core será útil para operaciones CRUD, transacciones y manejo normal de entidades.

Dapper será útil para consultas optimizadas, reportes, lecturas complejas o escenarios donde se requiera mayor control sobre SQL.

### Regla

Uso recomendado:

```text
EF Core -> Escrituras, transacciones, CRUD principal
Dapper -> Consultas optimizadas, reportes, lecturas complejas
```

---

## 18. Migraciones

### Decisión

Cada servicio manejará sus propias migraciones.

### Motivo

Cada servicio será dueño de su base de datos y debe controlar su propio esquema.

### Regla

Un servicio no debe ejecutar migraciones de otro servicio.

---

## 19. Comunicación síncrona

### Decisión

La comunicación síncrona será mediante:

```text
HTTP
gRPC entre servicios
WebSockets para el frontend cuando aplique
```

### Motivo

HTTP será usado para operaciones normales de API.

gRPC se utilizará entre servicios cuando se requiera comunicación eficiente, contratos estrictos y mejor rendimiento interno.

WebSockets se usarán para comunicación en tiempo real con el frontend cuando sea necesario.

---

## 20. gRPC entre servicios

### Decisión

Sí se utilizará gRPC entre servicios.

### Motivo

gRPC permite comunicación eficiente y fuertemente tipada entre microservicios.

Se usará cuando un servicio necesite comunicarse con otro de forma síncrona y controlada.

### Regla

gRPC debe usarse para comunicación interna entre servicios, no como API pública principal para el frontend.

---

## 21. Comunicación asíncrona

### Decisión

La comunicación asíncrona se realizará mediante:

```text
Redis Streams
```

### Motivo

Redis Streams permite implementar eventos asíncronos sin introducir inicialmente infraestructura adicional como RabbitMQ o Kafka.

---

## 22. RabbitMQ y Kafka

### Decisión

Por el momento no se utilizarán RabbitMQ ni Kafka.

### Motivo

Se evita agregar configuración e infraestructura adicional desde el inicio.

Si la operación crece y Redis Streams deja de ser suficiente, se evaluará implementar RabbitMQ o Kafka.

### Regla

La arquitectura debe evitar acoplarse completamente a Redis Streams para permitir una posible migración futura.

---

## 23. Outbox Pattern

### Decisión

Todos los eventos deben publicarse mediante Outbox.

### Motivo

Outbox permite asegurar que los eventos no se pierdan si ocurre un error entre la operación de negocio y la publicación del evento.

### Regla

Un servicio no debe publicar eventos directamente sin registrarlos primero en su tabla `OutboxMessages`.

---

## 24. Inbox Pattern

### Decisión

Todos los consumidores de eventos deben usar Inbox para idempotencia.

### Motivo

Inbox permite evitar que un evento duplicado se procese más de una vez.

### Regla

Todo consumidor debe registrar los eventos procesados en `InboxMessages`.

---

## 25. Servicio de autenticación

### Decisión

Auth será un microservicio separado.

Servicio:

```text
DholeAuthService
```

### Motivo

La autenticación, autorización, roles, scopes, tokens y sesiones deben manejarse de forma centralizada.

---

## 26. Permisos

### Decisión

Los permisos serán por scopes.

### Formato

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

### Motivo

Los scopes permiten control granular sobre las acciones del sistema.

---

## 27. Roles dinámicos

### Decisión

Los roles serán dinámicos.

### Motivo

La empresa podrá crear roles según su operación sin depender de roles quemados en código.

---

## 28. Roles seed

### Decisión

Los únicos roles creados por seed serán:

```text
Administrador
Superusuario
```

El resto de roles deben ser creados desde el sistema.

---

## 29. Tokens

### Decisión

Se utilizarán:

```text
Access token
Refresh token
```

### Motivo

El access token permite autenticación de corta duración.

El refresh token permite renovar sesión de forma controlada.

---

## 30. Sesiones

### Decisión

Las sesiones se guardarán en Redis.

### Motivo

Redis permite manejar sesiones con acceso rápido, expiración y revocación eficiente.

---

## 31. Scopes y JWT

### Decisión

Los scopes no se enviarán completos dentro del JWT.

Los scopes se cachearán en Redis.

### Motivo

Se evita generar JWT demasiado grandes.

Los servicios podrán validar permisos consultando los scopes cacheados en Redis.

### Regla

El JWT debe contener información mínima necesaria para identificar usuario y sesión.

Los permisos efectivos deben obtenerse desde cache.

---

## 32. Frontend

### Decisión

El frontend será desarrollado con:

```text
Vue
TypeScript
Vite
Tailwind
Pinia
```

### Motivo

Este stack permite construir una aplicación moderna, modular y mantenible.

---

## 33. Permisos en frontend

### Decisión

El frontend validará visibilidad por scopes.

### Motivo

La interfaz debe ocultar opciones, botones y rutas para las cuales el usuario no tiene permiso.

### Regla

La validación en frontend mejora UX, pero no reemplaza la validación obligatoria en backend.

---

## 34. Repositorio frontend

### Decisión

El frontend tendrá su propio repositorio.

Repositorio sugerido:

```text
dhole-web-app
```

---

## 35. Reportes

### Decisión

DholeReportsService generará:

```text
CSV
Excel
PDF
```

### Librerías definidas

```text
ClosedXML
DinkToPdf
CsvHelper
```

### Motivo

Estas librerías permiten cubrir los formatos principales de exportación requeridos.

---

## 36. Storage

### Decisión

Storage será genérico.

Servicio:

```text
DholeStorageService
```

### Motivo

Todos los archivos deben gestionarse desde un servicio centralizado para evitar duplicación de lógica y dependencia directa de proveedores físicos.

---

## 37. Proveedores de storage

### Decisión

Se soportarán todos los proveedores definidos:

```text
Local Storage
S3
Azure Blob
Firebase Storage
```

### Motivo

El sistema debe ser flexible para cambiar el proveedor de almacenamiento según necesidad.

---

## 38. Restricción de archivos

### Decisión

Los demás servicios no pueden guardar archivos directamente.

Todo archivo debe pasar por:

```text
DholeStorageService
```

### Motivo

Esto centraliza:

- Metadata.
- Versiones.
- Seguridad.
- Auditoría.
- Proveedor físico.
- Descarga.
- Referencias.

---

## 39. Notificaciones

### Decisión

DholeNotificationsService será genérico.

Cualquier servicio podrá solicitar una notificación mediante eventos o solicitud directa.

### Alcance inicial

```text
Email
Notificaciones internas del sistema
```

### Motivo

Se inicia con canales esenciales y se deja abierta la posibilidad de agregar más canales en el futuro.

---

## 40. Envío de notificaciones

### Decisión

Las notificaciones se enviarán mediante workers.

### Motivo

El envío de notificaciones no debe bloquear operaciones principales.

---

## 41. Auditoría

### Decisión

DholeAuditLogsService será genérico.

Consumirá eventos de todos los servicios.

### Motivo

La auditoría debe funcionar de forma desacoplada y centralizada.

---

## 42. Inmutabilidad de auditoría

### Decisión

AuditLogs no debe permitir modificar ni eliminar eventos registrados.

### Motivo

La auditoría debe conservar la trazabilidad histórica del sistema.

### Regla

AuditLogs será principalmente de:

```text
Lectura
Consulta
Exportación
```

---

## 43. Inteligencia Artificial

### Decisión

DholeAiService será un servicio complementario, no un servicio central.

### Motivo

La IA se usará como apoyo al sistema, no como dependencia crítica.

El servidor disponible tiene limitaciones para modelos de IA debido a la falta de GPU y a la imposibilidad de agregar una GPU por el modelo del servidor.

Por esta razón, el enfoque será híbrido:

```text
Análisis estático cuando sea suficiente.
IA local cuando sea posible.
Apoyo humano cuando el análisis automático no sea suficiente.
```

---

## 44. Procesamiento de IA

### Decisión

La IA trabajará por tareas asíncronas.

### Motivo

Las tareas de IA pueden ser pesadas o tardar más que una operación normal.

El procesamiento asíncrono evita bloquear el sistema principal.

---

## 45. Fuentes de análisis de IA

### Decisión

DholeAiService podrá analizar:

```text
Reportes
Eventos
Documentos
Datos internos permitidos
```

### Regla

No se deben enviar datos sensibles innecesarios al procesamiento de IA.

---

## 46. Proveedor de IA

### Decisión

El proveedor inicial de IA será local.

### Motivo

Se busca reducir dependencia de tokens externos y mantener control sobre costos.

---

## 47. Despliegue

### Decisión

El despliegue será on-premise.

### Motivo

El sistema se ejecutará sobre infraestructura propia.

---

## 48. Contenedores

### Decisión

Todos los servicios correrán con Docker.

### Motivo

Docker facilita empaquetado, despliegue, rollback y consistencia entre ambientes.

---

## 49. Docker Compose

### Decisión

Se utilizará Docker Compose al inicio.

### Motivo

Docker Compose permite levantar el ecosistema de forma controlada sin introducir Kubernetes desde el inicio.

---

## 50. Kubernetes

### Decisión

Kubernetes se evaluará más adelante.

### Motivo

No se utilizará desde el inicio para evitar complejidad operativa adicional.

Si el ecosistema crece y se requiere orquestación avanzada, se considerará su implementación.

---

## 51. Secretos y variables sensibles

### Decisión

Los secretos se manejarán con Vault.

### Motivo

Vault permite centralizar y proteger secretos como:

- Connection strings.
- Signing keys.
- API keys.
- Credenciales.
- Tokens internos.

---

## 52. Logs

### Decisión

Se utilizará Serilog para logging.

### Motivo

Serilog permite logs estructurados y facilita trazabilidad entre servicios.

---

## 53. CorrelationId

### Decisión

Se utilizará CorrelationId en todo el ecosistema.

### Motivo

CorrelationId permite rastrear una operación entre:

- Frontend.
- API.
- Servicios.
- Eventos.
- Workers.
- Logs.

---

## 54. Métricas, tracing y monitoreo

### Decisión

Se utilizarán métricas, tracing y monitoreo desde el inicio.

### Motivo

Un ecosistema de microservicios requiere visibilidad operativa para detectar errores, latencia, fallos de workers y problemas entre servicios.

---

## 55. Pruebas

### Decisión

Todas las pruebas serán obligatorias por servicio.

Tipos esperados:

```text
Unit tests
Integration tests
API tests
Event tests
Worker tests
Security tests
```

### Motivo

Cada servicio debe poder validarse de forma independiente y también dentro del ecosistema.

---

## 56. Cierre de HU

### Decisión

No se permite cerrar una HU sin pruebas.

### Regla

Cada HU debe tener al menos:

```text
Prueba de caso exitoso
Prueba de validación
Prueba de permisos si aplica
Prueba de error esperado
Prueba de eventos si aplica
Prueba de worker si aplica
```

---

## 57. Idioma del código

### Decisión

Todo el código debe estar en inglés.

Esto incluye:

- Variables.
- Clases.
- Métodos.
- Interfaces.
- Tablas.
- Columnas.
- Eventos.
- Comentarios técnicos.
- Mensajes técnicos.

---

## 58. Idioma de documentación

### Decisión

La documentación funcional puede estar en español.

### Motivo

La documentación funcional debe ser fácil de entender para las personas involucradas en el negocio y levantamiento de requerimientos.

---

## 59. Tablas y columnas

### Decisión

Las tablas y columnas estarán en inglés.

Ejemplos:

```text
Users
Roles
Scopes
Customers
Contacts
Quotes
QuoteItems
OutboxMessages
InboxMessages
```

---

## 60. Eventos

### Decisión

Los eventos estarán en inglés y en pasado.

Ejemplos correctos:

```text
CustomerCreated
CustomerUpdated
QuoteCreated
QuoteApproved
FileUploaded
ReportGenerated
NotificationSent
AiTaskCompleted
```

Ejemplos incorrectos:

```text
CreateCustomer
UpdateCustomer
ApproveQuote
UploadFile
GenerateReport
SendNotification
```

---

## 61. Resumen de decisiones

| Área                         | Decisión                                                           |
| ---------------------------- | ------------------------------------------------------------------ |
| Repositorios                 | Un repositorio por servicio                                        |
| Repo actual                  | Solo documentación                                                 |
| Building Blocks              | Internos por servicio                                              |
| Backend                      | .NET 10 LTS                                                        |
| API                          | Minimal APIs                                                       |
| CQRS                         | Sí, sin MediatR                                                    |
| AutoMapper                   | No                                                                 |
| FluentValidation             | No                                                                 |
| Base principal               | PostgreSQL                                                         |
| Separación de datos          | Base separada por servicio                                         |
| MongoDB                      | Para todo lo posible desde el inicio                               |
| Redis                        | Cache, sesiones, scopes, streams, locks, rate limit e idempotencia |
| Datos                        | EF Core + Dapper                                                   |
| Migraciones                  | Por servicio                                                       |
| Comunicación frontend        | HTTP y WebSockets                                                  |
| Comunicación entre servicios | gRPC y eventos                                                     |
| Eventos async                | Redis Streams                                                      |
| RabbitMQ/Kafka               | No por ahora                                                       |
| Outbox                       | Obligatorio                                                        |
| Inbox                        | Obligatorio                                                        |
| Auth                         | Servicio separado                                                  |
| Permisos                     | Scopes                                                             |
| Roles                        | Dinámicos                                                          |
| Roles seed                   | Administrador y Superusuario                                       |
| Tokens                       | Access token + refresh token                                       |
| Sesiones                     | Redis                                                              |
| Scopes                       | Cacheados en Redis                                                 |
| Frontend                     | Vue + TypeScript                                                   |
| Frontend tooling             | Vite, Tailwind, Pinia                                              |
| Reports                      | CSV, Excel y PDF                                                   |
| Reports libraries            | ClosedXML, DinkToPdf, CsvHelper                                    |
| Storage                      | Genérico                                                           |
| Storage providers            | Local, S3, Azure Blob, Firebase Storage                            |
| Notifications                | Genérico                                                           |
| Canales iniciales            | Email e internas                                                   |
| AuditLogs                    | Genérico e inmutable                                               |
| AI                           | Complementario, híbrido y local                                    |
| Deploy                       | On-premise                                                         |
| Contenedores                 | Docker                                                             |
| Orquestación inicial         | Docker Compose                                                     |
| Kubernetes                   | Más adelante                                                       |
| Secretos                     | Vault                                                              |
| Logs                         | Serilog                                                            |
| CorrelationId                | Obligatorio                                                        |
| Monitoreo                    | Desde el inicio                                                    |
| Pruebas                      | Todas obligatorias                                                 |
| Código                       | Inglés                                                             |
| Documentación funcional      | Español                                                            |
| Eventos                      | Inglés y en pasado                                                 |
