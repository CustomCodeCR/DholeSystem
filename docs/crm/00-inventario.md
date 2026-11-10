# DholeCRM — Fase 0: inventario técnico y decisiones de arquitectura

**Fecha de corte:** 2026-10-14 (America/Costa_Rica)  
**Fase:** 0 de 9 — diagnóstico exclusivamente; sin bootstrap, nuevas entidades, migraciones ni despliegues.  
**Especificación funcional única:** archivo proporcionado por el propietario `CODEX_DHOLECRM_IMPLEMENTACION_COMPLETA.md`.  
**Origen de evidencia:** lectura de repositorios GitHub `CustomCodeCR/*`, ramas y archivos indicados. No se inspeccionaron bases de datos activas ni el Compose efectivo del servidor.

> **Convención:** CONFIRMADO = localizado en código GitHub; DOCUMENTADO = descrito en documentación/configuración, no necesariamente ejecutado; PENDIENTE = exige validación de entorno/contrato; DECISIÓN = criterio que debe conservarse en las fases siguientes.

## 1. Resultado ejecutivo

1. **`DholeCRMService` está vacío**: metadata GitHub indica rama predeterminada `main`, tamaño 0, consulta de ramas `[]` y endpoint de contenido devuelve «This repository is empty». No existen aún solución, API, workers, gRPC ni migraciones CRM. No se debe afirmar que existe un commit `main`.
2. **La orquestación CRM ya fue preparada en `DholeSystem`**: `deploy/docker-compose.services.yml` declara `crm-api` y `crm-workers`, imágenes `dhole/crm-api` y `dhole/crm-workers`, puertos internos 8080 y 8081 y BD lógica `dhole_crm`. Esto **no demuestra** que existan imágenes, contenedores o tablas en ejecución.
3. **Existe una vía de reutilización real** para catálogos Config gRPC, scopes/roles Auth, estados y solicitudes de Pricing, Notifications gRPC y Outbox/Inbox de los servicios existentes. Cada integración deberá comprobar contrato, autenticación, endpoint, eventos, idempotencia y operación en staging antes de declararse completa.
4. **Gateway aún no publica la ruta CRM en código revisado**. `DholeSystem` inyecta `Gateway__Routes__12__Destination`, pero `DholeApiGateway/appsettings.json` presenta 12 rutas, sin prefijo `/api/crm`. Aportar sólo `Destination` no crea `Prefix`.
5. **Prioridad de seguridad:** `DholeApiGateway/Dhole.ApiGateway/appsettings.json` en repositorio público contiene valor de `Auth:Jwt:SecretKey` en claro. **No se reproduce** aquí. Evaluar exposición, rotación coordinada si la clave está en uso, eliminación del versionado de secretos y protección del historial antes de despliegues. `DholeWeb` tiene un archivo `.env` versionado en la raíz; su contenido **no** fue consultado, por lo que requiere revisión segura, no se afirma que contenga secretos.

## 2. Inventario de repositorios y ramas (GitHub)

| Repositorio | Rama predeterminada | Ramas verificadas | Evidencia / alcance fase 0 |
|---|---|---|---|
| [DholeCRMService](https://github.com/CustomCodeCR/DholeCRMService) | main (sin commits) | ninguna | Vacío; inicializar de forma controlada en fase 1 |
| [DholeWeb](https://github.com/CustomCodeCR/DholeWeb) | master | master, develop | Vue 3/TS; `src/modules` sin módulo `crm`; router y búsqueda global existentes |
| [DholeConfigService](https://github.com/CustomCodeCR/DholeConfigService) | master | master, develop | Catálogos, `.proto` y servidor Config gRPC, migraciones |
| [DholeAuthService](https://github.com/CustomCodeCR/DholeAuthService) | master | master, develop | Usuarios/roles/scopes, seeds, permisos, migraciones |
| [DholeAuditLogsService](https://github.com/CustomCodeCR/DholeAuditLogsService) | master | master, develop | API/Workers, Outbox/Inbox; integración a validar |
| [DholePricingService](https://github.com/CustomCodeCR/DholePricingService) | master | master, develop | Rates, RateRequests, estados y eventos de dominio |
| [DholeApiGateway](https://github.com/CustomCodeCR/DholeApiGateway) | master | master, develop | Proxy de rutas por prefijo; falta ruta CRM comprobada |
| [DholeNotificationsService](https://github.com/CustomCodeCR/DholeNotificationsService) | master | master, develop | Contrato Notifications gRPC, stream handlers y worker |
| [DholeSystem](https://github.com/CustomCodeCR/DholeSystem) | main | main, master, develop | Compose y workflows; ubicación del inventario Fase 0 |
| [DholeStorageService](https://github.com/CustomCodeCR/DholeStorageService) | master | master, develop | API archivos, referencias, Outbox/Inbox |
| [DholeDynamicsConnectorService](https://github.com/CustomCodeCR/DholeDynamicsConnectorService) | main | main | API Dataverse limitada a conexiones y cotizaciones |

No se modificaron los 10 repositorios de servicios leídos: el informe de fase 0 se crea **únicamente en una rama de `DholeSystem`**. No se crean ramas de trabajo vacías en repositorios que no necesitan cambios de código durante esta fase.

## 3. Inventario de contratos y patrones confirmados

### 3.1 Auth

- `src/Dhole.Auth.Domain/Shared/AuthConstants.cs`: roles reales `Administrador`, `SuperUsuario`, `Pricing`, `Mercadeo`; `DatabaseSeeder.cs` menciona además `Vendedor Supervisor`, `Vendedor Jefe` y el rol `Vendedor` usado por el directorio comercial.
- `src/Dhole.Auth.Persistence/Seed/AuthScopeCatalog.cs` agrupa scopes de módulos existentes; **no aparece un grupo CRM**. La Fase 2 debe agregar solamente los 53 scopes de la especificación, sin asumir que ya están registrados en producción.
- `DatabaseSeeder.SeedAsync` llama `AssignAllScopesToSuperUserAsync`. **Riesgo de privilegios:** comprobar efecto de los nuevos scopes financieros; no asumir que «superusuario» puede leer créditos sin autorización explícita.
- `src/Dhole.Auth.Api/Endpoints/InternalPricingRecipientEndpoints.cs` tiene directorio de vendedores/usuarios por HTTP interno con clave de servicio. **No se confirmó** contrato de directorio Auth gRPC; reutilizar o implementar contrato técnico real de forma segura cuando corresponda.
- Autorización por políticas `Scope:` y `RequireScope`. CRM debe exigir además acceso por propietario/asignación del registro.

### 3.2 Config

- `src/Dhole.Config.Contracts/Protos/config_catalog.proto` define `ConfigCatalogGrpc` y RPC `GetCatalogItemById`, `GetCatalogItemBySlug`, `GetCatalogItemByCode`, `ResolveCatalogItem`, `ValidateCatalogItem`, `GetActiveCatalogItemsByGroup`.
- Implementación localizada: `src/Dhole.Config.Api/Grpc/ConfigCatalogGrpcService.cs`; mensajes incluyen `code`, `value`, `slug` y `is_active`.
- Reutilizar estos catálogos para países, puertos, divisas, modalidades, etc. Para selects mostrar **value** y guardar identificador/código según contrato.
- Seeds nuevos CRM sólo idempotentes y tras comparar grupos reales de staging. No se inspeccionó el contenido de catálogos almacenados.

### 3.3 Pricing

- Entidades verificadas: `src/Dhole.Pricing.Domain/Rates/Entities/RateHeader.cs` y `RateRequest.cs`.
- `RateStatus` verificado en `Rates/Enums/RateStatus.cs`: `PendingApproval=0`, `ApprovedByManagement=1`, `RejectedByManagement=2`, `Open=3`, `Sent=4`, `AcceptedByClient=5`, `RejectedByClient=6`, `RequestedByClient=7`, `Closed=8`, `Expired=9`.
- `RateRequestStatus` existente: `Open=0`, `Completed=1`, `Cancelled=2`. Identificadores `RateRequest.Id`, `RateRequest.RateId`, `SellerUserId` y `RateHeader.Id` deben vincularse **lógicamente** con oportunidades, sin nuevas FKs cross-service.
- API actual: `/api/pricing/rates`, `/api/pricing/rate-requests/mine`, `/api/pricing/rate-requests/dashboard` y cambios de estado. Revisar verificaciones de visibilidad por usuario.
- Eventos de dominio localizados: `RateHeaderCreatedDomainEvent`, `RateHeaderUpdatedDomainEvent`; **no equivalen por sí solos** a eventos Redis públicos `QuoteAcceptedV1`/etc. Comprobar mapper Outbox y consumidores antes de diseñar la fase 4.
- **DECISIÓN:** `ApprovedByManagement` no significa aceptación del cliente ni oportunidad ganada; conservar cierre comercial explícito y eventos verdaderos.

### 3.4 Gateway y Web

- `Dhole.ApiGateway/Gateway/GatewayProxyMiddleware.cs` elige prefijo más específico y proxy HTTP con timeout; `Dhole.ApiGateway/appsettings.json` no contiene ruta `/api/crm` en la revisión efectuada.
- `DholeSystem/deploy/docker-compose.services.yml` inyecta el destino CRM para `Gateway__Routes__12__Destination`; crear la ruta completa con `Prefix` y validar precedencia sin afectar las rutas existentes.
- `DholeWeb/src/core/router/index.ts`, `src/core/services/globalSearchService.ts` y `src/modules`: router por scopes y búsqueda federada existente; la fase 7 podrá ampliar sin crear una segunda búsqueda global.
- La UI no debe acceder directamente a gRPC. Navegador → Gateway HTTP autorizado → CRM API; gRPC sólo servicio a servicio.

### 3.5 Notifications / AuditLogs / Storage

- `Dhole.Notifications.Contracts/Protos/notifications.proto` define `NotificationsGrpc`: `CreateNotification`, `CancelNotification`, `GetNotification`; contiene destinatarios, canal, plantilla, fecha programada e intentos. Validar límites, auth y deduplicación antes de uso real.
- `Dhole.Notifications.Workers/Streams` implementa handlers de eventos; verificar nomenclatura de streams y consumidor para no publicar eventos incompatibles.
- `Dhole.AuditLogs.Workers/Streams`, `Persistence/Messaging/InboxStore.cs` y `Dhole.Storage.Workers/Outbox` muestran patrones Outbox/Inbox y Redis existentes. No copiar tablas técnicas si `CustomCodeFramework` ya las suministra.
- `Dhole.Storage.Domain/Files/Entities/FileReference.cs`: mantener binarios en Storage y referencias lógicas en CRM; comprobar ACL y API disponible al implementarlo.

### 3.6 Dynamics / Hacienda / propiedad de clientes y contactos

- `DholeDynamicsConnectorService/src/Dhole.Dynamics.Api/Program.cs` dispone de endpoints de configuración de conexiones y operaciones `POST /api/dynamics/quotes`, `GET /api/dynamics/quotes/{id}`, `GET /api/dynamics/quotes/links/{dholeRateId}`.
- `DataverseClient.cs` implementa creación/lectura de **quotes** con Dataverse v9.2, no operaciones verificadas de cuentas, leads ni contactos ni consulta de metadatos. Estos contratos son **dependencia pendiente de la fase 8**, sin implementar clientes Dynamics paralelos.
- La documentación histórica `DholeSystem/docs/database/database-overview.md` **planea** que CRM sea propietario de `Customers`, `Contacts`, `CustomerAddresses`, `CustomerFollowUps`; no constituye prueba de tablas físicas.
- En el código inspeccionado de los repositorios enumerados **no se confirmó una implementación operativa CRM propietaria de cuentas/contactos/direcciones/preferencias**. Tampoco se validó una instancia Dataverse ni la BD real; la decisión definitiva de propiedad exige inspección de BD, registros legacy y contrato Dynamics **antes de la migración de fase 2**.
- **DECISIÓN provisional:** CRM dueño del perfil y ciclo comercial; Auth de usuarios, Config de catálogos, Pricing de tarifas y aceptación, Storage de binarios, AuditLogs del histórico y DynamicsConnector del acceso a Dataverse. Si existe registro canónico de clientes en otro servicio, usar ID lógico/read-model y **no duplicarlo**.
- **PENDIENTE:** localizar contrato/API Hacienda en despliegue y verificar campos reales Dataverse/option sets usando metadata autorizada. No inventar campos ni crear `dynamics-field-mapping.csv` con suposiciones.

## 4. Infraestructura y CI/CD: evidencia y bloqueos

- `DholeSystem/deploy/docker-compose.services.yml` incluye **`/opt/dhole/docker-compose.services.yml`**, define `crm-api`, `crm-workers` y red externa `dhole-runtime` cuyo nombre real depende de `DHOLE_NETWORK`.
- Variables **no secretas** previstas: `CRM_DB=dhole_crm`, `CRM_HTTP_URL=http://crm-api:8080`, `CRM_GRPC_URL=http://crm-api:8081`; no verificar ni volcar los `.env` reales en repositorio.
- `deploy/prepare-environments.sh` añade esos defaults sólo cuando faltan; no acredita BD existente.
- `deploy/CRM_DEPLOYMENT.md` advierte conflicto potencial de `api-gateway` y duplicación por `include`. No hay acceso comprobado al Compose **efectivo** del host ni prueba de `docker compose config` con archivos protegidos.
- En `DholeSystem/.github/workflows/deploy-staging.yml` **todo push a `develop`** dispara el workflow del runner self-hosted; en `deploy-production.yml` **todo push a `master`** dispara producción. No hay exclusión documental por rutas observada.
- **DECISIÓN de seguridad Fase 0:** crear PR de documento, **no fusionarlo automáticamente** mientras un merge de documentación pueda activar despliegue de infraestructura. Ajustar filtros/protecciones en fase adecuada con autorización previa y comprobaciones de staging; nunca activar producción al completar este inventario.
- Las imágenes `dhole/crm-api`/`dhole/crm-workers`, DB `dhole_crm`, health y contenedores son **previstos, no validados**. En fase 1 se requerirán workflows `ci.yml`, `deploy-staging.yml`, `deploy-production.yml` en el CRM una vez exista código.
- Inconsistencia nominal: `docs/database/database-overview.md` cita `dhole_crm_db`, mientras el Compose concreto utiliza `dhole_crm`. **DECISIÓN:** seguir la variable runtime `CRM_DB` y validar su valor real antes de aplicar EF migrations, sin renombrar BD existente.

## 5. Diferencias frente a la especificación actual

| Tema | Estado visto | Acción / condición |
|---|---|---|
| Bootstrap CRM | Repositorio vacío | Fase 1: preparar historia Git sin perder `main`; crear `master`/`develop` con estrategia revisada y feature branch |
| Clientes/contactos existentes | Sólo planificación histórica, sin fuente productiva verificada | Confirmar propietario y duplicados antes de tablas en fase 2 |
| Esquema CRM PostgreSQL | No hay migraciones en CRM | Fase 2: EF y migraciones versionadas, previa inspección de BD |
| 53 scopes CRM | No localizados en `AuthScopeCatalog` | Fase 2: seed idempotente y matriz de roles sin asignaciones excesivas |
| Config gRPC | Servicio y contrato reales | Reusar; validar conectividad y auth |
| Eventos comerciales Pricing | Eventos de dominio, integración Redis no demostrada | Fase 4: validar/publicar/consumir eventos V1 idempotentes |
| Notificaciones | Contrato gRPC existente | Fase 5: autenticación, retries, dedupe y canal real |
| Gateway CRM | Destino env preparado, ruta no confirmada | Fase 4: prefijo y auth; no sólo variable indexada |
| Interfaz CRM | Módulo no presente | Fase 7 sin alterar dashboard/rutas actuales |
| Dynamics cuentas/contacts | Conector de quotes únicamente comprobado | Fase 8: CRUD/metadata real y CSV de campos verificados |
| Hacienda | Contrato no confirmado | Fase 8: localizar API y definir elegibilidad para CR |
| Requisito anterior `docs/requirements/01-sales-department.md` | Describe Cotización Express y otros alcances históricos | **No ampliar funcionalidad por ese documento**; único alcance funcional vigente = MD adjunto |

## 6. Riesgos, prioridades y mitigación

| Prioridad | Riesgo comprobado o no verificado | Mitigación requerida |
|---|---|---|
| **P0** | JWT secret hardcodeado en config pública de Gateway | Inventariar consumidores, rotar si vigente, sustituir por secret de entorno, sanear historia/visibilidad siguiendo proceso seguro |
| **P0** | Integrar `DholeSystem/develop` inicia job de despliegue | Mantener PR sin merge hasta acordar mecanismo docs-only que evite despliegues |
| **P1** | `include` Compose y servicio `api-gateway` potencialmente duplicado | Verificar `docker compose config` efectivo en staging, sin mostrar `.env` |
| **P1** | Cliente canónico de CRM no verificado | Consultar fuentes de datos actuales/Dataverse antes de crear entidades |
| **P1** | Scope global `AssignAllScopesToSuperUserAsync` | Revisión de least privilege y scopes de crédito antes del seed |
| **P1** | La ruta /api/crm requiere `Prefix`, no sólo Destination | PR Gateway dedicado y smoke test de auth/routing |
| **P2** | Diferencias `main` / `master` / `develop` | Preparar historial sin force push, reglas por repositorio |
| **P2** | `DholeWeb/.env` está versionado | Auditar contenido **sin exponerlo en logs** y retirar secretos si aparecen |

## 7. Decisiones técnicas de salida de Fase 0

1. No crear estructuras CRM, scopes, datos ni endpoints en Fase 0.
2. Usar `DholeSystem/docs/crm/00-inventario.md` como inventario único; el resto de `docs/crm/*` no es prerrequisito para implementar la Fase 1 y podrá documentarse oportunamente.
3. Una base de datos **por servicio**, sin FKs entre bases; `Guid` lógico para Auth/Config/Pricing/Storage. UTC persistido.
4. Adoptar arquitectura Clean Architecture .NET 10 de servicios existentes, Minimal API/CQRS, `CustomCodeFramework` y sus patrones EF/Outbox/Inbox/Redis, sin nuevas abstracciones duplicadas.
5. Mantener API pública HTTP con scopes y autorización por registro; gRPC seguro únicamente interno; deadlines/retries/correlation.
6. Priorizar compatibilidad con Pricing, y separar explícitamente aceptación comercial de aprobación de margen.
7. Usar adaptador Dynamics existente, no un cliente Dataverse adicional dentro CRM.
8. No automatizar migraciones destructivas ni rollback SQL; respaldos antes de cambios; despliegue por servicio y promoción gated después de staging.
9. Diferir cualquier CRUD, seeds, workflow, migración, imagen y deploy a su fase correspondiente.

## 8. Comprobaciones efectuadas / no efectuadas

**Realizadas:** consulta GitHub de 11 repositorios, ramas/defaults, árboles de código, contracts Config/Notifications, roles/scopes Auth, tipos Rate/RateRequest, rutas Gateway/Web, API Dynamics, Compose, workflows y documentación existente. Verificación de inexistencia del archivo `docs/crm/00-inventario.md` en `DholeSystem/develop`.

**No realizadas:** compilación `dotnet`, `npm`, tests unitarios/integración, seguridad estática automatizada, PostgreSQL introspection, checks activos de runner, `docker compose config` efectivo con `/opt/dhole`, migraciones, verificaciones live HTTP/gRPC/health, staging o producción. Ninguna parte del diagnóstico requiere simularlas.

**Bloqueos para fase 1:** (a) esquema de ramas e inicialización de repo vacío sin commits; (b) CI/CD no puede superar a staging/prod sin disponibilidad de runner e imágenes; (c) seguridad de Gateway y ruta CRM; (d) existencia/propiedad de datos CRM y validación Compose efectiva antes de EF; (e) contrato de integración Dynamics incompleto para fases posteriores.

## 9. Cierre y siguiente paso

**Estado de la fase 0:** informe de descubrimiento preparado sobre código GitHub; PR hacia `develop` para revisión. No equivale a comprobación de producción. La integración queda sujeta a que **no dispare despliegues** involuntarios. No comenzar fase 1 hasta instrucción explícita.

**Evidencia raíz:**
- `CustomCodeCR/DholeSystem/deploy/CRM_DEPLOYMENT.md`
- `CustomCodeCR/DholeSystem/deploy/docker-compose.services.yml`
- `CustomCodeCR/DholeSystem/.github/workflows/deploy-staging.yml`
- `CustomCodeCR/DholeApiGateway/Dhole.ApiGateway/appsettings.json`
- `CustomCodeCR/DholeAuthService/src/Dhole.Auth.Persistence/Seed/DatabaseSeeder.cs`
- `CustomCodeCR/DholeConfigService/src/Dhole.Config.Contracts/Protos/config_catalog.proto`
- `CustomCodeCR/DholePricingService/src/Dhole.Pricing.Domain/Rates/Enums/RateStatus.cs`
- `CustomCodeCR/DholeNotificationsService/src/Dhole.Notifications.Contracts/Protos/notifications.proto`
- `CustomCodeCR/DholeDynamicsConnectorService/src/Dhole.Dynamics.Api/Program.cs`

_Ningún secreto, valor protegido de entorno o token se incluye en este documento._
