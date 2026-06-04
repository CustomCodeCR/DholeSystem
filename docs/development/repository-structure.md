# Estructura de Repositorios - Dhole Microservices

## 1. Objetivo

Este documento define la estrategia de organización de repositorios para Dhole Microservices.

El objetivo es mantener una separación clara entre la documentación general del ecosistema y el código fuente de cada microservicio.

El repositorio actual será utilizado únicamente para documentación.

Cada microservicio tendrá su propio repositorio independiente.

---

## 2. Estrategia recomendada

Para Dhole Microservices se utilizará una estrategia de múltiples repositorios.

La documentación general del ecosistema vivirá en un repositorio central de documentación.

El código fuente de cada microservicio vivirá en su propio repositorio.

Esta estrategia permite:

- Mantener la documentación centralizada.
- Evitar mezclar documentación general con código fuente.
- Mantener independencia real entre servicios.
- Facilitar despliegues independientes.
- Permitir versionamiento independiente por servicio.
- Evitar que un cambio en un servicio afecte directamente a los demás.
- Mantener una estructura más limpia y alineada con una arquitectura de microservicios.

---

## 3. Repositorio de documentación

El repositorio de documentación será el punto central para consultar la información general del ecosistema Dhole Microservices.

Nombre sugerido:

```text
dhole-microservices-docs
```

Este repositorio no debe contener código fuente de servicios.

Debe contener únicamente:

- Levantamientos de requerimientos.
- Historias de usuario.
- Backlog inicial.
- Diagramas de arquitectura.
- Diagramas de base de datos.
- Decisiones técnicas.
- Estándares de desarrollo.
- Convenciones API.
- Modelo de permisos y scopes.
- Catálogo de eventos.
- Estrategia de pruebas.
- Estrategia de despliegue.
- Roadmap de desarrollo.
- Estimación por HU.

---

## 4. Estructura general del repositorio de documentación

```text
dhole-microservices-docs
  /docs
    /architecture
    /backlog
    /requirements
    /standards
    /api
    /security
    /events
    /database
    /testing
    /deployment
    /development
    /estimation
    /roadmap
    /decisions
  README.md
```

---

## 5. Carpeta docs

La carpeta `docs` contiene toda la documentación técnica, funcional y de planificación del ecosistema.

```text
/docs
  /architecture
    architecture-diagram.md
    database-overview.md
    database-diagram.md

  /backlog
    user-stories.md

  /requirements
    auth-requirements.md
    config-requirements.md
    crm-requirements.md
    pricing-requirements.md
    storage-requirements.md
    notifications-requirements.md
    auditlogs-requirements.md
    reports-requirements.md
    ai-requirements.md

  /standards
    development-standards.md

  /api
    api-conventions.md

  /security
    technical-security.md
    permissions-scopes.md

  /events
    event-catalog.md

  /database
    database-overview.md
    auth-database.md
    config-database.md
    crm-database.md
    pricing-database.md
    storage-database.md
    notifications-database.md
    auditlogs-database.md
    reports-database.md
    ai-database.md

  /testing
    testing-strategy.md

  /deployment
    deployment-strategy.md
    environment-variables.md
    docker-compose-local.md
    migrations-and-seeds.md

  /development
    repository-structure.md

  /estimation
    hu-time-estimation.md

  /roadmap
    development-roadmap.md

  /decisions
    technical-decisions.md
```

---

## 6. Repositorios por servicio

Cada microservicio tendrá su propio repositorio.

Repositorios esperados:

```text
dhole-building-blocks
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

Cada repositorio debe ser independiente y contener únicamente el código, pruebas, configuración y documentación específica de ese servicio.

---

## 7. Repositorio DholeBuildingBlocks

Repositorio sugerido:

```text
dhole-building-blocks
```

Responsabilidad:

Contener la base técnica compartida del ecosistema.

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
- Contratos de paginación
- Respuestas estándar
- Errores estándar

No debe contener reglas de negocio de ningún servicio.

Estructura sugerida:

```text
dhole-building-blocks
  /src
    /Dhole.BuildingBlocks
  /tests
    /Dhole.BuildingBlocks.UnitTests
  README.md
  .gitignore
```

---

## 8. Estructura base por microservicio backend

Cada microservicio backend debe seguir una estructura similar.

Ejemplo usando Auth:

```text
dhole-auth-service
  /src
    /Dhole.AuthService.Api
    /Dhole.AuthService.Application
    /Dhole.AuthService.Domain
    /Dhole.AuthService.Infrastructure
    /Dhole.AuthService.Contracts
    /Dhole.AuthService.Workers
  /tests
    /Dhole.AuthService.UnitTests
    /Dhole.AuthService.IntegrationTests
  /deploy
    /docker
  README.md
  Dockerfile
  docker-compose.override.yml
  .gitignore
```

Esta misma estructura aplica para:

```text
dhole-config-service
dhole-crm-service
dhole-pricing-service
dhole-storage-service
dhole-notifications-service
dhole-auditlogs-service
dhole-reports-service
dhole-ai-service
```

---

## 9. Responsabilidad de proyectos internos por servicio

Cada servicio puede dividirse internamente en proyectos.

| Proyecto       | Responsabilidad                                                      |
| -------------- | -------------------------------------------------------------------- |
| Api            | Endpoints, controllers, middlewares, filtros y configuración HTTP    |
| Application    | Casos de uso, servicios de aplicación, validaciones y orquestación   |
| Domain         | Entidades, value objects, reglas de negocio y lógica de dominio      |
| Infrastructure | Persistencia, Redis, providers, clientes externos y repositorios     |
| Contracts      | Requests, responses, eventos públicos y contratos externos           |
| Workers        | Procesos en segundo plano, Outbox, consumidores y tareas programadas |

---

## 10. Estructura por servicio

### Auth Service

Repositorio:

```text
dhole-auth-service
```

Estructura:

```text
dhole-auth-service
  /src
    /Dhole.AuthService.Api
    /Dhole.AuthService.Application
    /Dhole.AuthService.Domain
    /Dhole.AuthService.Infrastructure
    /Dhole.AuthService.Contracts
    /Dhole.AuthService.Workers
  /tests
    /Dhole.AuthService.UnitTests
    /Dhole.AuthService.IntegrationTests
  README.md
```

Responsabilidad:

```text
Usuarios, roles, scopes, tokens, refresh tokens y sesiones.
```

---

### Config Service

Repositorio:

```text
dhole-config-service
```

Estructura:

```text
dhole-config-service
  /src
    /Dhole.ConfigService.Api
    /Dhole.ConfigService.Application
    /Dhole.ConfigService.Domain
    /Dhole.ConfigService.Infrastructure
    /Dhole.ConfigService.Contracts
    /Dhole.ConfigService.Workers
  /tests
    /Dhole.ConfigService.UnitTests
    /Dhole.ConfigService.IntegrationTests
  README.md
```

Responsabilidad:

```text
Configuración general del ecosistema.
```

---

### CRM Service

Repositorio:

```text
dhole-crm-service
```

Estructura:

```text
dhole-crm-service
  /src
    /Dhole.CrmService.Api
    /Dhole.CrmService.Application
    /Dhole.CrmService.Domain
    /Dhole.CrmService.Infrastructure
    /Dhole.CrmService.Contracts
    /Dhole.CrmService.Workers
  /tests
    /Dhole.CrmService.UnitTests
    /Dhole.CrmService.IntegrationTests
  README.md
```

Responsabilidad:

```text
Clientes, contactos y seguimiento comercial.
```

---

### Pricing Service

Repositorio:

```text
dhole-pricing-service
```

Estructura:

```text
dhole-pricing-service
  /src
    /Dhole.PricingService.Api
    /Dhole.PricingService.Application
    /Dhole.PricingService.Domain
    /Dhole.PricingService.Infrastructure
    /Dhole.PricingService.Contracts
    /Dhole.PricingService.Workers
  /tests
    /Dhole.PricingService.UnitTests
    /Dhole.PricingService.IntegrationTests
  README.md
```

Responsabilidad:

```text
Cotizaciones, ofertas, tarifas, costos, precios de venta y márgenes.
```

---

### Storage Service

Repositorio:

```text
dhole-storage-service
```

Estructura:

```text
dhole-storage-service
  /src
    /Dhole.StorageService.Api
    /Dhole.StorageService.Application
    /Dhole.StorageService.Domain
    /Dhole.StorageService.Infrastructure
    /Dhole.StorageService.Contracts
    /Dhole.StorageService.Workers
  /tests
    /Dhole.StorageService.UnitTests
    /Dhole.StorageService.IntegrationTests
  README.md
```

Responsabilidad:

```text
Archivos, metadata, versiones, referencias y proveedores de almacenamiento.
```

---

### Notifications Service

Repositorio:

```text
dhole-notifications-service
```

Estructura:

```text
dhole-notifications-service
  /src
    /Dhole.NotificationsService.Api
    /Dhole.NotificationsService.Application
    /Dhole.NotificationsService.Domain
    /Dhole.NotificationsService.Infrastructure
    /Dhole.NotificationsService.Contracts
    /Dhole.NotificationsService.Workers
  /tests
    /Dhole.NotificationsService.UnitTests
    /Dhole.NotificationsService.IntegrationTests
  README.md
```

Responsabilidad:

```text
Plantillas, mensajes, destinatarios, adjuntos, envíos y reintentos.
```

---

### AuditLogs Service

Repositorio:

```text
dhole-auditlogs-service
```

Estructura:

```text
dhole-auditlogs-service
  /src
    /Dhole.AuditLogsService.Api
    /Dhole.AuditLogsService.Application
    /Dhole.AuditLogsService.Domain
    /Dhole.AuditLogsService.Infrastructure
    /Dhole.AuditLogsService.Contracts
    /Dhole.AuditLogsService.Workers
  /tests
    /Dhole.AuditLogsService.UnitTests
    /Dhole.AuditLogsService.IntegrationTests
  README.md
```

Responsabilidad:

```text
Auditoría genérica del ecosistema.
```

---

### Reports Service

Repositorio:

```text
dhole-reports-service
```

Estructura:

```text
dhole-reports-service
  /src
    /Dhole.ReportsService.Api
    /Dhole.ReportsService.Application
    /Dhole.ReportsService.Domain
    /Dhole.ReportsService.Infrastructure
    /Dhole.ReportsService.Contracts
    /Dhole.ReportsService.Workers
  /tests
    /Dhole.ReportsService.UnitTests
    /Dhole.ReportsService.IntegrationTests
  README.md
```

Responsabilidad:

```text
Reportes, solicitudes de generación, exportaciones CSV, Excel y PDF.
```

---

### AI Service

Repositorio:

```text
dhole-ai-service
```

Estructura:

```text
dhole-ai-service
  /src
    /Dhole.AiService.Api
    /Dhole.AiService.Application
    /Dhole.AiService.Domain
    /Dhole.AiService.Infrastructure
    /Dhole.AiService.Contracts
    /Dhole.AiService.Workers
  /tests
    /Dhole.AiService.UnitTests
    /Dhole.AiService.IntegrationTests
  README.md
```

Responsabilidad:

```text
Tareas de IA, análisis, sugerencias, resultados e historial de procesamiento.
```

---

## 11. Repositorio frontend

Repositorio sugerido:

```text
dhole-web-app
```

Estructura sugerida:

```text
dhole-web-app
  /src
    /app
    /features
    /shared
    /core
    /routes
    /assets
  /public
  README.md
  package.json
  vite.config.ts
  tsconfig.json
  .gitignore
```

Responsabilidad:

```text
Aplicación web principal del ecosistema Dhole.
```

---

## 12. README principal por repositorio de servicio

Cada repositorio de servicio debe tener su propio README.md.

Contenido mínimo:

```text
# Dhole.{ServiceName}

## Responsabilidad

## Módulos

## Arquitectura interna

## Endpoints

## Tablas

## Eventos publicados

## Eventos consumidos

## Variables de entorno

## Workers

## Cómo ejecutar localmente

## Cómo probar

## Decisiones específicas del servicio
```

---

## 13. Relación entre repositorios

El repositorio de documentación funciona como fuente central de reglas y decisiones.

Cada repositorio de servicio debe consultar este repositorio para:

- Estándares de desarrollo.
- Convenciones API.
- Modelo de permisos.
- Catálogo de eventos.
- Estrategia de pruebas.
- Estrategia de despliegue.
- Decisiones técnicas generales.

Cada repositorio de servicio puede tener documentación propia, pero no debe duplicar innecesariamente la documentación general.

---

## 14. Referencia a DholeBuildingBlocks

DholeBuildingBlocks tendrá su propio repositorio.

Los servicios podrán utilizarlo como:

```text
Paquete NuGet interno
```

O temporalmente como referencia directa durante desarrollo local, si fuera necesario.

La opción recomendada para mantener independencia entre servicios es publicarlo como paquete interno versionado.

Ejemplo:

```text
Dhole.BuildingBlocks 1.0.0
```

Reglas:

- DholeBuildingBlocks no debe depender de ningún servicio.
- Los servicios sí pueden depender de DholeBuildingBlocks.
- DholeBuildingBlocks no debe contener reglas de negocio.
- Cambios en DholeBuildingBlocks deben versionarse.
- Los servicios deben actualizar la versión cuando corresponda.

---

## 15. Soluciones .NET

Cada microservicio debe tener su propia solución `.sln`.

Ejemplos:

```text
Dhole.AuthService.sln
Dhole.ConfigService.sln
Dhole.CrmService.sln
Dhole.PricingService.sln
Dhole.StorageService.sln
Dhole.NotificationsService.sln
Dhole.AuditLogsService.sln
Dhole.ReportsService.sln
Dhole.AiService.sln
```

No se usará una solución principal con todos los servicios, porque no se trabajará como monorepo.

---

## 16. Pruebas por repositorio

Cada repositorio de servicio debe contener sus propias pruebas.

Ejemplo:

```text
dhole-pricing-service
  /tests
    /Dhole.PricingService.UnitTests
    /Dhole.PricingService.IntegrationTests
```

Cada servicio es responsable de validar:

- Casos de uso.
- Endpoints.
- Reglas de negocio.
- Persistencia.
- Eventos publicados.
- Eventos consumidos.
- Workers.
- Permisos.

---

## 17. Despliegue por repositorio

Cada repositorio de servicio debe contener su propia configuración de despliegue.

Ejemplo:

```text
dhole-pricing-service
  /deploy
    /docker
  Dockerfile
  docker-compose.override.yml
```

Cada servicio debe poder desplegarse de forma independiente.

---

## 18. Reglas finales

- El repositorio principal será solo de documentación.
- No se usará monorepo para código fuente.
- Cada microservicio tendrá su propio repositorio.
- Cada microservicio tendrá su propia solución `.NET`.
- Cada microservicio tendrá sus propias pruebas.
- Cada microservicio tendrá su propio README.
- Cada microservicio tendrá su propio Dockerfile.
- Cada microservicio tendrá sus propias migraciones.
- Cada microservicio tendrá sus propias variables de entorno.
- DholeBuildingBlocks tendrá su propio repositorio.
- DholeBuildingBlocks debe versionarse como paquete interno.
- Ningún servicio debe depender directamente del dominio de otro servicio.
- Ningún servicio debe acceder directamente a la base de datos de otro servicio.
- La documentación general debe vivir en `dhole-microservices-docs`.
