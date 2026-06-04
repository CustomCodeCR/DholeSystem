# Estructura de Repositorios - Dhole Microservices

## 1. Objetivo

Este documento define la estructura recomendada para organizar los repositorios y proyectos de Dhole Microservices.

El objetivo es mantener orden, separación de responsabilidades y facilidad de mantenimiento.

---

## 2. Estrategia recomendada

Para Dhole Microservices se recomienda iniciar con un monorepo controlado.

Esto permite:

- Mantener documentación centralizada.
- Facilitar cambios coordinados.
- Compartir DholeBuildingBlocks.
- Simplificar el inicio del desarrollo.
- Mantener una visión completa del sistema.

En el futuro, si el sistema crece mucho, algunos servicios pueden separarse en repositorios independientes.

---

## 3. Estructura general del repositorio

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

## 4. Carpeta docs

La carpeta docs contiene la documentación técnica y funcional.

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
```

---

## 5. Carpeta src

La carpeta src contiene todos los servicios.

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

## 6. Carpeta tests

La carpeta tests contiene las pruebas automatizadas.

```text
/tests
  /Auth
    /Dhole.AuthService.UnitTests
    /Dhole.AuthService.IntegrationTests

  /Config
    /Dhole.ConfigService.UnitTests
    /Dhole.ConfigService.IntegrationTests

  /CRM
    /Dhole.CrmService.UnitTests
    /Dhole.CrmService.IntegrationTests

  /Pricing
    /Dhole.PricingService.UnitTests
    /Dhole.PricingService.IntegrationTests

  /Storage
    /Dhole.StorageService.UnitTests
    /Dhole.StorageService.IntegrationTests

  /Notifications
    /Dhole.NotificationsService.UnitTests
    /Dhole.NotificationsService.IntegrationTests

  /AuditLogs
    /Dhole.AuditLogsService.UnitTests
    /Dhole.AuditLogsService.IntegrationTests

  /Reports
    /Dhole.ReportsService.UnitTests
    /Dhole.ReportsService.IntegrationTests

  /AI
    /Dhole.AiService.UnitTests
    /Dhole.AiService.IntegrationTests
```

---

## 7. Carpeta deploy

La carpeta deploy contiene archivos de despliegue.

```text
/deploy
  /docker
    docker-compose.local.yml
    docker-compose.dev.yml
    docker-compose.prod.yml

  /postgres
    init.sql

  /redis
    redis.conf

  /storage
    local-storage.md
```

---

## 8. Carpeta scripts

La carpeta scripts contiene comandos útiles.

```text
/scripts
  create-service.sh
  run-all.sh
  run-auth.sh
  run-pricing.sh
  migrate-all.sh
  seed-auth.sh
```

---

## 9. README principal

El README principal debe contener:

```text
# Dhole Microservices

## Descripción

## Servicios

## Arquitectura

## Requisitos

## Ejecución local

## Documentación

## Convenciones

## Roadmap
```

---

## 10. README por servicio

Cada servicio debe tener su propio README.

Ejemplo:

```text
/src/Services/Auth/README.md
```

Contenido mínimo:

```text
# Dhole Auth Service

## Responsabilidad

## Módulos

## Endpoints

## Tablas

## Eventos publicados

## Eventos consumidos

## Variables de entorno

## Cómo ejecutar

## Cómo probar
```

---

## 11. Soluciones .NET

Se puede manejar una solución principal:

```text
Dhole.sln
```

Y soluciones por servicio:

```text
Dhole.AuthService.sln
Dhole.CrmService.sln
Dhole.PricingService.sln
```

Para iniciar, puede usarse una solución principal para facilitar desarrollo.

---

## 12. Referencia a BuildingBlocks

DholeBuildingBlocks puede manejarse inicialmente como proyecto interno del monorepo.

Los servicios pueden referenciarlo como proyecto.

En el futuro puede convertirse en paquete NuGet interno si hace falta.

---

## 13. Reglas finales

- Cada servicio debe estar separado por carpeta.
- Cada servicio debe tener sus propios proyectos.
- Cada servicio debe tener sus propias pruebas.
- Cada servicio debe tener su propio README.
- DholeBuildingBlocks no debe contener reglas de negocio.
- Ningún servicio debe depender directamente del dominio de otro servicio.
- La documentación debe vivir en docs.
