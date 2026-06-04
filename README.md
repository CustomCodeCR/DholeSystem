# Dhole Microservices Documentation

Repositorio central de documentación para **Dhole Microservices**.

Este repositorio no contiene código fuente de los microservicios. Su objetivo es centralizar la documentación funcional, técnica, arquitectónica y de planificación del ecosistema Dhole.

Cada microservicio tendrá su propio repositorio independiente.

---

## Objetivo del repositorio

Este repositorio existe para mantener en un solo lugar la documentación necesaria para diseñar, planificar y desarrollar el ecosistema Dhole Microservices.

Aquí se documenta:

- Levantamientos de requerimientos.
- Historias de usuario.
- Arquitectura general.
- Diagramas técnicos.
- Estándares de desarrollo.
- Seguridad técnica.
- Modelo de permisos y scopes.
- Catálogo de eventos.
- Estrategia de pruebas.
- Estrategia de despliegue.
- Roadmap de desarrollo.
- Estimaciones por historia de usuario.
- Decisiones técnicas generales.

---

## Alcance del repositorio

Este repositorio es únicamente para documentación.

No debe contener:

- Código fuente de microservicios.
- Proyectos `.NET`.
- Código frontend.
- Migraciones ejecutables.
- Dockerfiles de servicios.
- Tests automatizados.
- Archivos compilados.
- Secretos o variables sensibles.

Cada servicio debe tener su propio repositorio de implementación.

---

## Repositorios de servicios

La arquitectura está pensada para manejar un repositorio independiente por servicio.

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

Este repositorio funciona como fuente central de documentación para todos esos repositorios.

---

## Servicios del ecosistema

| Servicio                  | Responsabilidad                                                                                                 |
| ------------------------- | --------------------------------------------------------------------------------------------------------------- |
| DholeBuildingBlocks       | Base técnica compartida para contratos, resultados, errores, eventos, paginación, CorrelationId, Outbox e Inbox |
| DholeAuthService          | Usuarios, roles, scopes, tokens, refresh tokens y sesiones                                                      |
| DholeConfigService        | Configuración general del ecosistema                                                                            |
| DholeCrmService           | Clientes, contactos y seguimiento comercial                                                                     |
| DholePricingService       | Cotizaciones, ofertas, tarifas, costos y márgenes                                                               |
| DholeStorageService       | Archivos, metadata y proveedores de almacenamiento                                                              |
| DholeNotificationsService | Plantillas, mensajes, envíos, adjuntos y reintentos                                                             |
| DholeAuditLogsService     | Auditoría genérica del ecosistema                                                                               |
| DholeReportsService       | Reportes y exportaciones CSV, Excel y PDF                                                                       |
| DholeAiService            | Tareas de IA, análisis, sugerencias y resultados                                                                |
| Dhole Web App             | Aplicación web principal del ecosistema Dhole                                                                   |

---

## Arquitectura general

Dhole Microservices se basa en una arquitectura de microservicios.

Cada servicio debe tener:

- Su propia responsabilidad.
- Su propio repositorio.
- Su propia base de datos o esquema lógico.
- Sus propios contratos.
- Sus propios endpoints.
- Sus propias migraciones.
- Sus propios workers cuando aplique.
- Sus propias pruebas.
- Su propio README técnico.

La comunicación entre servicios se define mediante:

- HTTP para operaciones síncronas.
- Redis Streams para comunicación asíncrona.
- Outbox Pattern para publicación confiable de eventos.
- Inbox Pattern para consumo idempotente de eventos.

---

## Stack técnico base

| Área                       | Tecnología          |
| -------------------------- | ------------------- |
| Backend                    | .NET                |
| Frontend                   | Vue / TypeScript  |
| Base de datos principal    | PostgreSQL          |
| Cache / Streams            | Redis               |
| Datos flexibles opcionales | MongoDB             |
| Comunicación asíncrona     | Redis Streams       |
| Publicación de eventos     | Outbox Pattern      |
| Consumo de eventos         | Inbox Pattern       |
| Documentación              | Markdown            |
| Diagramas                  | Mermaid / Eraser.io |
| Control de versiones       | Git / GitHub        |

---

## Estructura del repositorio de documentación

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

## Estructura de carpetas

### `/docs/architecture`

Contiene la documentación de arquitectura general.

```text
/docs/architecture
  architecture-diagram.md
  database-overview.md
  database-diagram.md
```

Documentos esperados:

- Diagrama de arquitectura.
- Explicación de arquitectura.
- Diagrama general de base de datos.
- Relación entre servicios.
- Flujo de comunicación síncrona y asíncrona.

---

### `/docs/backlog`

Contiene las historias de usuario y el backlog inicial.

```text
/docs/backlog
  user-stories.md
```

Documentos esperados:

- Historias de usuario.
- Orden de implementación.
- Dependencias entre HU.
- Criterios de aceptación.
- Servicios relacionados por HU.

---

### `/docs/requirements`

Contiene los levantamientos de requerimientos por departamento o área.

```text
/docs/requirements
  crm-requirements.md
  pricing-requirements.md
  auth-requirements.md
  reports-requirements.md
  notifications-requirements.md
  storage-requirements.md
  auditlogs-requirements.md
  ai-requirements.md
```

Estos documentos funcionan como fuente funcional del proyecto.

---

### `/docs/standards`

Contiene estándares generales de desarrollo.

```text
/docs/standards
  development-standards.md
```

Define reglas para:

- Idioma del código.
- Estructura de proyectos.
- Nombres de tablas.
- Nombres de columnas.
- Respuestas estándar.
- Errores.
- Eventos.
- Workers.
- Logging.
- Redis keys.

---

### `/docs/api`

Contiene las convenciones para APIs.

```text
/docs/api
  api-conventions.md
```

Define reglas para:

- Versionado.
- Endpoints.
- Métodos HTTP.
- Paginación.
- Filtros.
- Ordenamiento.
- Respuestas estándar.
- Códigos HTTP.
- CorrelationId.

---

### `/docs/security`

Contiene documentación de seguridad.

```text
/docs/security
  technical-security.md
  permissions-scopes.md
```

Define:

- Autenticación.
- Autorización.
- Access tokens.
- Refresh tokens.
- Sesiones.
- Roles.
- Scopes.
- Cache de permisos.
- Auditoría de seguridad.
- Seguridad en archivos.
- Seguridad en reportes.
- Seguridad en IA.

---

### `/docs/events`

Contiene el catálogo de eventos.

```text
/docs/events
  event-catalog.md
```

Define:

- Eventos por servicio.
- Publicadores.
- Consumidores.
- Payload mínimo.
- Streams sugeridos.
- Reglas de Outbox.
- Reglas de Inbox.
- Versionado de eventos.

---

### `/docs/database`

Contiene documentación de base de datos.

```text
/docs/database
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
```

Define:

- Tablas por servicio.
- Relaciones internas.
- Campos principales.
- Índices recomendados.
- Tablas técnicas.
- OutboxMessages.
- InboxMessages.

---

### `/docs/testing`

Contiene la estrategia de pruebas.

```text
/docs/testing
  testing-strategy.md
```

Define:

- Pruebas unitarias.
- Pruebas de integración.
- Pruebas de API.
- Pruebas de eventos.
- Pruebas de workers.
- Pruebas de seguridad.
- Criterios mínimos para cerrar una HU.

---

### `/docs/deployment`

Contiene documentación de despliegue.

```text
/docs/deployment
  deployment-strategy.md
  environment-variables.md
  docker-compose-local.md
  migrations-and-seeds.md
```

Define:

- Ambientes.
- Variables de entorno.
- Docker.
- Docker Compose local.
- Migraciones.
- Seeds.
- Health checks.
- Backups.
- Rollback.

---

### `/docs/development`

Contiene documentación relacionada con la organización del desarrollo.

```text
/docs/development
  repository-structure.md
```

Define:

- Estrategia de repositorios.
- Estructura esperada por servicio.
- README esperado por servicio.
- Organización de soluciones.
- Relación con DholeBuildingBlocks.

---

### `/docs/estimation`

Contiene estimaciones de tiempo.

```text
/docs/estimation
  hu-time-estimation.md
```

Define:

- Estimación por HU.
- Complejidad.
- Horas.
- Dependencias.
- Riesgo técnico.
- Fase recomendada.

---

### `/docs/roadmap`

Contiene el orden de desarrollo.

```text
/docs/roadmap
  development-roadmap.md
```

Define:

- Fases de desarrollo.
- Orden recomendado.
- Servicios por fase.
- Dependencias.
- Entregables por fase.

---

### `/docs/decisions`

Contiene decisiones técnicas generales.

```text
/docs/decisions
  technical-decisions.md
```

Define:

- Decisiones de arquitectura.
- Decisiones de base de datos.
- Decisiones de comunicación.
- Decisiones de seguridad.
- Decisiones de eventos.
- Decisiones sobre repositorios.
- Decisiones sobre despliegue.

---

## Documentos principales

| Documento                   | Ruta                                        |
| --------------------------- | ------------------------------------------- |
| Diagrama de arquitectura    | `docs/architecture/architecture-diagram.md` |
| Diagrama de base de datos   | `docs/architecture/database-diagram.md`     |
| Historias de usuario        | `docs/backlog/user-stories.md`              |
| Estándares de desarrollo    | `docs/standards/development-standards.md`   |
| Convenciones API            | `docs/api/api-conventions.md`               |
| Seguridad técnica           | `docs/security/technical-security.md`       |
| Modelo de permisos y scopes | `docs/security/permissions-scopes.md`       |
| Catálogo de eventos         | `docs/events/event-catalog.md`              |
| Estrategia de pruebas       | `docs/testing/testing-strategy.md`          |
| Estrategia de despliegue    | `docs/deployment/deployment-strategy.md`    |
| Estructura de repositorios  | `docs/development/repository-structure.md`  |
| Estimación por HU           | `docs/estimation/hu-time-estimation.md`     |
| Roadmap de desarrollo       | `docs/roadmap/development-roadmap.md`       |
| Decisiones técnicas         | `docs/decisions/technical-decisions.md`     |

---

## Estado actual de documentación

```text
Hechos:
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
[x] Diagrama de base de datos
[x] Estimación por HU
[x] Roadmap de desarrollo
[x] Decisiones técnicas
```

---

## Reglas del repositorio

Este repositorio debe seguir estas reglas:

- Solo debe contener documentación.
- No debe contener código fuente de servicios.
- No debe contener secretos.
- No debe contener variables sensibles reales.
- No debe contener archivos compilados.
- No debe contener dependencias instaladas.
- Todo documento debe estar en Markdown.
- Todo diagrama debe estar en Markdown, Mermaid o Diagram as Code.
- Los documentos deben actualizarse cuando cambie una decisión técnica.
- Las historias de usuario deben mantenerse alineadas con el backlog de GitHub.

---

## Relación con los repositorios de servicios

Cada repositorio de servicio debe consultar este repositorio como fuente de documentación general.

Cada servicio debe tener su propio README técnico con:

```text
# Dhole.{ServiceName}

## Responsabilidad

## Módulos

## Endpoints

## Tablas

## Eventos publicados

## Eventos consumidos

## Variables de entorno

## Cómo ejecutar

## Cómo probar

## Decisiones específicas del servicio
```

Este repositorio no reemplaza la documentación específica de cada servicio.

---

## Flujo recomendado de trabajo

Cuando se agregue o cambie una funcionalidad:

```text
1. Actualizar levantamiento o requerimiento si aplica.
2. Actualizar historia de usuario.
3. Actualizar diagrama o documento técnico si aplica.
4. Actualizar eventos si aplica.
5. Actualizar modelo de permisos si aplica.
6. Actualizar estimación si cambia el alcance.
7. Implementar en el repositorio del servicio correspondiente.
```

---

## Licencia

Repositorio privado de documentación para el ecosistema Dhole Microservices.
