# Roadmap de Desarrollo - Dhole Microservices

## 1. Objetivo

Este documento define el orden recomendado de desarrollo para Dhole Microservices.

El objetivo del roadmap es evitar desarrollar historias de usuario en un orden incorrecto, reducir retrabajo y asegurar que las bases técnicas estén listas antes de construir funcionalidades dependientes.

Este roadmap se basa en los servicios definidos para Dhole Microservices y en las historias de usuario existentes en GitHub.

---

## 2. Principios del roadmap

El desarrollo debe seguir estos principios:

- Primero se construye la base técnica.
- Después se construye seguridad y configuración.
- Luego se desarrollan los servicios funcionales principales.
- Después se desarrollan los servicios complementarios.
- Finalmente se integran eventos, workers, pruebas y despliegue.
- Ningún servicio debe depender directamente de la base de datos de otro servicio.
- La comunicación entre servicios debe respetar la arquitectura definida.
- Los permisos deben validarse por scopes.
- Los eventos deben publicarse mediante Outbox.
- Los eventos deben consumirse mediante Inbox.

---

## 3. Servicios incluidos

El roadmap contempla los siguientes servicios:

```text
DholeBuildingBlocks
DholeAuthService
DholeConfigService
DholeCrmService
DholePricingService
DholeStorageService
DholeNotificationsService
DholeAuditLogsService
DholeReportsService
DholeAiService
Dhole Web App
```

---

## 4. Fase 0 - Preparación documental y técnica

### Objetivo

Preparar la base documental y técnica antes de iniciar desarrollo fuerte.

### Entregables

```text
[x] Levantamientos de requerimientos por departamento
[x] Historias de usuario en GitHub
[x] Diagrama de arquitectura
[x] Backlog inicial
[x] Documentación funcional base
[x] Estándares de desarrollo
[x] Modelo de permisos/scopes
[x] Catálogo de eventos
[x] Estructura de repositorios
[x] Estrategia de pruebas
[x] Estrategia de despliegue
[x] Convenciones API
[x] Seguridad técnica
[X] Roadmap de desarrollo
[X] Decisiones técnicas
[X] Diagrama de base de datos
[X] Estimación por HU
```

### Criterio de salida

Esta fase se considera lista cuando exista una base mínima para iniciar los repositorios y desarrollar sin improvisar decisiones principales.

---

## 5. Fase 1 - Base técnica compartida

### Objetivo

Construir la base técnica común que será usada por todos los microservicios.

Esta fase debe desarrollarse primero porque los demás servicios dependerán de los contratos base, respuestas estándar, errores, eventos y estructuras compartidas.

### Servicio principal

```text
DholeBuildingBlocks
```

### Alcance

```text
- Result
- Result<T>
- Error
- PagedResult<T>
- PaginationRequest
- IntegrationEvent
- EventEnvelope
- CorrelationId
- Contratos base de Outbox
- Contratos base de Inbox
- Errores estándar
- Respuestas estándar
```

### Dependencias

```text
Ninguna
```

### Servicios bloqueados por esta fase

```text
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

### Criterio de salida

```text
[ ] DholeBuildingBlocks creado
[ ] Contratos base definidos
[ ] Respuestas estándar listas
[ ] Eventos base definidos
[ ] CorrelationId definido
[ ] Outbox contracts definidos
[ ] Inbox contracts definidos
[ ] Paquete listo para ser usado por otros servicios
```

---

## 6. Fase 2 - Seguridad y configuración base

### Objetivo

Construir la seguridad central del ecosistema y la configuración base.

Esta fase permite que los demás servicios puedan validar usuarios, roles, scopes, tokens y configuración general.

### Servicios principales

```text
DholeAuthService
DholeConfigService
```

---

### 6.1 DholeAuthService

#### Alcance

```text
- Usuarios
- Roles
- Scopes
- Asignación de roles a usuarios
- Asignación de scopes a roles
- Login
- Access token
- Refresh token
- Sesiones
- Cache de permisos en Redis
- Bloqueo de usuarios
- Validación de scopes
- Seeds iniciales
```

#### Roles seed

```text
Administrador
Superusuario
```

#### Reglas

```text
- Los roles no se queman en código.
- Solo Administrador y Superusuario son seed.
- Los demás roles se crean desde el sistema.
- Los permisos se manejan mediante scopes.
```

#### Criterio de salida

```text
[ ] Usuarios creados
[ ] Roles creados
[ ] Scopes creados
[ ] Login funcionando
[ ] Refresh token funcionando
[ ] Sesiones funcionando
[ ] Cache de permisos funcionando
[ ] Validación de scopes funcionando
[ ] Seeds iniciales aplicados
```

---

### 6.2 DholeConfigService

#### Alcance

```text
- Configuraciones generales
- Configuraciones por módulo
- Lectura de configuración
- Actualización de configuración
- Auditoría de cambios de configuración
```

#### Criterio de salida

```text
[ ] Configuraciones base creadas
[ ] Endpoints de consulta funcionando
[ ] Endpoints de actualización funcionando
[ ] Evento ConfigurationChanged definido
```

---

## 7. Fase 3 - Base de comunicación asíncrona

### Objetivo

Implementar el patrón de eventos para comunicación entre servicios.

Esta fase puede construirse después de Auth y Config, pero antes de depender de eventos en CRM, Pricing, Reports, Notifications, AuditLogs y AI.

### Componentes principales

```text
OutboxMessages
InboxMessages
Redis Streams
OutboxBackgroundService
RedisStreamsConsumerBackgroundService
```

### Alcance

```text
- Tabla OutboxMessages por servicio
- Tabla InboxMessages por servicio consumidor
- Worker de publicación de eventos
- Worker de consumo de eventos
- Control de reintentos
- Control de errores
- CorrelationId en eventos
- Idempotencia en consumidores
```

### Criterio de salida

```text
[ ] OutboxMessages definido
[ ] InboxMessages definido
[ ] Redis Streams configurado
[ ] Worker de Outbox funcionando
[ ] Worker consumidor funcionando
[ ] Eventos duplicados no se procesan dos veces
[ ] Errores quedan registrados
```

---

## 8. Fase 4 - Base comercial

### Objetivo

Construir los servicios funcionales principales para clientes, contactos, seguimiento comercial, cotizaciones y ofertas.

### Servicios principales

```text
DholeCrmService
DholePricingService
```

---

### 8.1 DholeCrmService

#### Alcance

```text
- Clientes
- Contactos
- Direcciones si aplica
- Seguimientos comerciales
- Notas comerciales
- Eventos de cliente
```

#### Eventos principales

```text
CustomerCreated
CustomerUpdated
ContactCreated
FollowUpCreated
```

#### Dependencias

```text
DholeBuildingBlocks
DholeAuthService
DholeConfigService
Outbox / Inbox
Redis Streams
```

#### Criterio de salida

```text
[ ] Clientes funcionando
[ ] Contactos funcionando
[ ] Seguimientos funcionando
[ ] Validación de scopes funcionando
[ ] Eventos CRM publicados
[ ] Auditoría integrada por eventos
```

---

### 8.2 DholePricingService

#### Alcance

```text
- Cotización express
- Cotización formal
- Costos
- Cargos
- Precios de venta
- Márgenes
- Estados de cotización
- Aprobación de cotización
- Rechazo de cotización
- Generación de oferta formal
```

#### Eventos principales

```text
QuoteCreated
QuoteUpdated
QuoteApproved
QuoteRejected
OfferGenerated
```

#### Dependencias

```text
DholeBuildingBlocks
DholeAuthService
DholeConfigService
DholeCrmService
DholeStorageService para documentos generados
Outbox / Inbox
Redis Streams
```

#### Criterio de salida

```text
[ ] Cotización express funcionando
[ ] Cotización formal funcionando
[ ] Costos definidos
[ ] Márgenes calculados
[ ] Aprobación funcionando
[ ] Rechazo funcionando
[ ] Oferta formal generada
[ ] Eventos Pricing publicados
```

---

## 9. Fase 5 - Storage y documentos

### Objetivo

Construir el servicio genérico de archivos para que otros servicios puedan guardar documentos, PDFs, adjuntos y reportes generados.

### Servicio principal

```text
DholeStorageService
```

### Alcance

```text
- Metadata de archivos
- Carga de archivos
- Descarga de archivos
- Versiones de archivos
- Referencias de archivos
- Proveedor de almacenamiento configurable
- Relación lógica con entidades origen
```

### Eventos principales

```text
FileUploaded
FileDeleted
FileVersionCreated
```

### Dependencias

```text
DholeBuildingBlocks
DholeAuthService
DholeConfigService
Outbox / Inbox
Redis Streams
```

### Servicios que dependen de Storage

```text
DholePricingService
DholeReportsService
DholeNotificationsService
```

### Criterio de salida

```text
[ ] Carga de archivos funcionando
[ ] Descarga de archivos funcionando
[ ] Metadata guardada
[ ] Versiones soportadas si aplica
[ ] Proveedor de almacenamiento abstraído
[ ] Eventos de Storage publicados
```

---

## 10. Fase 6 - Servicios complementarios base

### Objetivo

Construir los servicios que acompañan los procesos principales sin acoplarse directamente a ellos.

### Servicios principales

```text
DholeAuditLogsService
DholeNotificationsService
DholeReportsService
```

---

### 10.1 DholeAuditLogsService

#### Alcance

```text
- Registro de eventos de auditoría
- Consulta de auditoría
- Auditoría de cambios
- Auditoría de seguridad
- Auditoría de eventos de negocio
```

#### Dependencias

```text
Outbox / Inbox
Redis Streams
DholeBuildingBlocks
```

#### Criterio de salida

```text
[ ] Eventos auditables registrados
[ ] Consulta de auditoría funcionando
[ ] Eventos de seguridad registrados
[ ] Eventos de negocio registrados
```

---

### 10.2 DholeNotificationsService

#### Alcance

```text
- Plantillas
- Mensajes
- Destinatarios
- Adjuntos
- Solicitudes de envío
- Estados de envío
- Reintentos
- Worker de notificaciones programadas
```

#### Eventos principales

```text
NotificationRequested
NotificationSent
NotificationFailed
```

#### Dependencias

```text
DholeStorageService
DholeAuthService
DholeConfigService
Outbox / Inbox
Redis Streams
```

#### Criterio de salida

```text
[ ] Plantillas funcionando
[ ] Solicitud de envío funcionando
[ ] Estados de envío funcionando
[ ] Reintentos funcionando
[ ] Adjuntos soportados
[ ] Eventos de Notifications publicados
```

---

### 10.3 DholeReportsService

#### Alcance

```text
- Definición de reportes
- Solicitud de reportes
- Generación CSV
- Generación Excel
- Generación PDF
- Reportes programados
- Guardado de archivos generados mediante Storage
```

#### Eventos principales

```text
ReportRequested
ReportGenerated
ReportFailed
```

#### Dependencias

```text
DholeStorageService
DholeAuthService
DholeConfigService
Outbox / Inbox
Redis Streams
```

#### Criterio de salida

```text
[ ] Solicitudes de reporte funcionando
[ ] CSV generado
[ ] Excel generado
[ ] PDF generado
[ ] Archivos guardados en Storage
[ ] Eventos de Reports publicados
```

---

## 11. Fase 7 - Servicio de IA

### Objetivo

Construir el servicio de IA como servicio complementario y no como dependencia central del sistema.

### Servicio principal

```text
DholeAiService
```

### Alcance

```text
- Tareas de IA
- Solicitudes de análisis
- Cola de procesamiento
- Resultados
- Errores
- Historial de tareas
- Worker de procesamiento IA
```

### Eventos principales

```text
AiTaskRequested
AiTaskCompleted
AiTaskFailed
```

### Dependencias

```text
DholeAuthService
DholeConfigService
DholeReportsService si analiza reportes
Outbox / Inbox
Redis Streams
```

### Criterio de salida

```text
[ ] Tareas de IA creadas
[ ] Worker de IA funcionando
[ ] Resultados almacenados
[ ] Errores controlados
[ ] Eventos de IA publicados
```

---

## 12. Fase 8 - Frontend inicial

### Objetivo

Construir la base de la aplicación web para consumir los servicios principales.

### Servicio principal

```text
Dhole Web App
```

### Alcance inicial

```text
- Login
- Manejo de sesión
- Layout principal
- Navegación por módulos
- Validación de permisos por scopes
- Pantallas base de Auth
- Pantallas base de CRM
- Pantallas base de Pricing
- Pantallas base de Storage
- Pantallas base de Reports
```

### Dependencias

```text
DholeAuthService
DholeConfigService
DholeCrmService
DholePricingService
DholeStorageService
DholeReportsService
```

### Criterio de salida

```text
[ ] Login funcionando
[ ] Sesión funcionando
[ ] Permisos aplicados en UI
[ ] Navegación base lista
[ ] CRM consumido desde frontend
[ ] Pricing consumido desde frontend
[ ] Storage consumido desde frontend
[ ] Reports consumido desde frontend
```

---

## 13. Fase 9 - Integración end-to-end

### Objetivo

Validar que los servicios trabajen juntos correctamente.

### Flujos principales a validar

```text
Crear cliente -> Crear contacto -> Crear cotización -> Aprobar cotización -> Generar oferta -> Guardar PDF -> Auditar evento
```

```text
Solicitar reporte -> Generar Excel/PDF -> Guardar archivo -> Notificar resultado -> Auditar evento
```

```text
Evento de negocio -> Redis Streams -> Inbox -> AuditLogs / Notifications / Reports / AI
```

### Criterio de salida

```text
[ ] Flujo CRM -> Pricing funcionando
[ ] Flujo Pricing -> Storage funcionando
[ ] Flujo Reports -> Storage funcionando
[ ] Flujo Notifications -> Storage funcionando
[ ] Flujo eventos -> AuditLogs funcionando
[ ] CorrelationId propagado entre servicios
[ ] Outbox funcionando
[ ] Inbox funcionando
[ ] Redis Streams funcionando
```

---

## 14. Fase 10 - Pruebas, hardening y estabilización

### Objetivo

Preparar el ecosistema para uso controlado o despliegue inicial.

### Alcance

```text
- Pruebas unitarias
- Pruebas de integración
- Pruebas de API
- Pruebas de eventos
- Pruebas de workers
- Pruebas de seguridad
- Validación de permisos
- Validación de logs
- Validación de errores
- Validación de performance básica
```

### Criterio de salida

```text
[ ] Pruebas mínimas ejecutadas
[ ] Endpoints críticos validados
[ ] Workers validados
[ ] Permisos validados
[ ] Eventos validados
[ ] Logs validados
[ ] Errores controlados
[ ] Bugs críticos corregidos
```

---

## 15. Fase 11 - Despliegue inicial

### Objetivo

Preparar el despliegue inicial del ecosistema.

### Alcance

```text
- Variables de entorno
- Dockerfiles por servicio
- Docker Compose local
- Migraciones
- Seeds
- Health checks
- Backups
- Logs
- Documentación de ejecución
```

### Criterio de salida

```text
[ ] Variables configuradas
[ ] Servicios levantan correctamente
[ ] Bases de datos creadas
[ ] Migraciones aplicadas
[ ] Seeds aplicados
[ ] Health checks funcionando
[ ] Logs funcionando
[ ] Backups definidos
[ ] README por servicio actualizado
```

---

## 16. Orden recomendado resumido

```text
1. DholeBuildingBlocks
2. DholeAuthService
3. DholeConfigService
4. Outbox / Inbox / Redis Streams
5. DholeCrmService
6. DholeStorageService
7. DholePricingService
8. DholeAuditLogsService
9. DholeNotificationsService
10. DholeReportsService
11. DholeAiService
12. Dhole Web App
13. Integración end-to-end
14. Pruebas y hardening
15. Despliegue inicial
```

---

## 17. Dependencias principales

```text
DholeBuildingBlocks
  -> Todos los servicios

DholeAuthService
  -> Todos los servicios protegidos

DholeConfigService
  -> Servicios que requieren configuración dinámica

DholeStorageService
  -> Pricing
  -> Reports
  -> Notifications

DholeCrmService
  -> Pricing

Outbox / Inbox / Redis Streams
  -> AuditLogs
  -> Notifications
  -> Reports
  -> AI

DholeReportsService
  -> AI cuando se requiera análisis sobre reportes

Dhole Web App
  -> Depende de servicios backend ya funcionales
```

---

## 18. Roadmap por prioridad

### Prioridad crítica

```text
DholeBuildingBlocks
DholeAuthService
DholeConfigService
Outbox / Inbox
Redis Streams
```

### Prioridad alta

```text
DholeCrmService
DholePricingService
DholeStorageService
DholeAuditLogsService
```

### Prioridad media

```text
DholeNotificationsService
DholeReportsService
DholeAiService
```

### Prioridad de integración

```text
Dhole Web App
Pruebas end-to-end
Despliegue inicial
```

---

## 19. Estado del roadmap

```text
Estado: Borrador inicial
Pendiente: Alinear con las 46 HU reales en GitHub
Pendiente: Agregar estimación por HU
Pendiente: Agregar fechas tentativas
Pendiente: Validar decisiones técnicas finales
```

---

## 20. Reglas finales

- No iniciar Pricing antes de tener CRM mínimo.
- No iniciar Reports sin Storage mínimo.
- No iniciar Notifications con adjuntos sin Storage mínimo.
- No iniciar AI como dependencia central del sistema.
- No publicar eventos sin Outbox.
- No consumir eventos sin Inbox.
- No construir frontend completo antes de tener Auth funcional.
- No avanzar a despliegue sin pruebas mínimas.
- No cerrar una fase sin validar criterios de salida.
