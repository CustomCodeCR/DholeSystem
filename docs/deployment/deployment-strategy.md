# Estrategia de Despliegue - Dhole Microservices

## 1. Objetivo

Este documento define la estrategia inicial de despliegue para Dhole Microservices.

La estrategia debe permitir ejecutar el sistema de forma ordenada en ambiente local, pruebas y producción.

---

## 2. Enfoque general

Cada microservicio debe poder ejecutarse de forma independiente.

Cada servicio debe tener:

- Dockerfile propio.
- Variables de entorno propias.
- Base de datos propia o esquema independiente.
- Migraciones propias.
- README de ejecución.
- Configuración por ambiente.

---

## 3. Ambientes

Se definen los siguientes ambientes:

```text
Local
Development
Staging
Production
```

Uso de cada ambiente:

| Ambiente    | Uso                                     |
| ----------- | --------------------------------------- |
| Local       | Desarrollo en máquina del desarrollador |
| Development | Pruebas internas técnicas               |
| Staging     | Validación previa a producción          |
| Production  | Ambiente real de operación              |

---

## 4. Docker

Cada microservicio debe tener su propio Dockerfile.

Ejemplo:

```text
Dhole.AuthService/Dockerfile
Dhole.CrmService/Dockerfile
Dhole.PricingService/Dockerfile
```

El Dockerfile debe:

- Restaurar dependencias.
- Compilar el servicio.
- Publicar la aplicación.
- Ejecutar el servicio en modo release.

---

## 5. Docker Compose local

Para desarrollo local se puede usar Docker Compose.

Debe levantar:

- PostgreSQL
- Redis
- MongoDB si aplica
- Servicios necesarios para desarrollo
- Workers necesarios

Archivos sugeridos:

```text
docker-compose.yml
docker-compose.override.yml
```

---

## 6. Variables de entorno

Cada servicio debe configurarse con variables de entorno.

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

## 7. Configuración por servicio

Cada servicio debe tener su propia configuración.

Ejemplo:

```text
Dhole.AuthService
  appsettings.json
  appsettings.Development.json
  appsettings.Production.json
```

Las configuraciones sensibles deben venir de variables de entorno.

---

## 8. Migraciones

Cada microservicio debe manejar sus propias migraciones.

Reglas:

- Un servicio solo migra su propia base de datos.
- Ningún servicio migra tablas de otro servicio.
- Las migraciones deben versionarse en el repositorio.
- Las migraciones deben ejecutarse antes de iniciar el servicio en producción o como paso controlado de despliegue.

---

## 9. Orden de despliegue inicial

Orden recomendado:

```text
1. Infraestructura base
   - PostgreSQL
   - Redis
   - MongoDB si aplica
   - Storage físico

2. DholeBuildingBlocks
   - Publicar paquete o referencia interna

3. Servicios base
   - DholeAuthService
   - DholeConfigService

4. Servicios funcionales
   - DholeCrmService
   - DholePricingService
   - DholeStorageService

5. Servicios complementarios
   - DholeAuditLogsService
   - DholeNotificationsService
   - DholeReportsService
   - DholeAiService

6. Workers
   - OutboxBackgroundService
   - RedisStreamsConsumerBackgroundService
   - ScheduledNotificationsWorker
   - ProjectionWorker
   - AiTaskWorker

7. Frontend
   - Dhole Web App
```

---

## 10. Health checks

Cada servicio debe exponer un endpoint de salud.

Endpoint recomendado:

```text
GET /health
```

Debe validar:

- Servicio activo.
- Conexión a PostgreSQL.
- Conexión a Redis si aplica.
- Conexión a MongoDB si aplica.
- Estado de workers si aplica.

---

## 11. Logs

Todos los servicios deben generar logs estructurados.

Cada log debe incluir:

- ServiceName
- Environment
- CorrelationId
- Timestamp
- Level
- Message
- Exception si aplica

Los logs deben permitir rastrear una operación entre servicios.

---

## 12. Backups

Se deben definir backups para:

- PostgreSQL
- MongoDB si aplica
- Archivos físicos de Storage

Frecuencia recomendada inicial:

```text
Base de datos: diario
Archivos: diario
Retención mínima: 7 días
```

En producción, la política de retención puede ampliarse.

---

## 13. Storage

DholeStorageService debe abstraer el proveedor físico.

Opciones soportadas por diseño:

- Local Storage
- S3
- Azure Blob

El proveedor activo debe definirse por configuración.

Ejemplo:

```text
Storage__Provider=Local
Storage__BasePath=/data/dhole/storage
```

---

## 14. Redis

Redis será requerido para:

- Cache
- Sesiones
- Permisos cacheados
- Redis Streams
- Locks
- Idempotencia temporal

Debe estar disponible antes de iniciar servicios que dependan de él.

---

## 15. Workers

Los workers deben desplegarse como procesos independientes o servicios separados.

Cada worker debe tener:

- Logs propios.
- Variables de entorno.
- Health check si aplica.
- Control de reintentos.
- Manejo de errores.

---

## 16. Rollback

Cada despliegue debe permitir rollback.

Reglas:

- No eliminar columnas de forma inmediata.
- No hacer cambios destructivos sin fase previa.
- Mantener compatibilidad temporal entre versiones.
- Respaldar base antes de cambios críticos.
- Versionar migraciones.

---

## 17. Checklist de despliegue

Antes de desplegar:

```text
[ ] Variables de entorno configuradas
[ ] Migraciones aplicadas
[ ] Redis disponible
[ ] PostgreSQL disponible
[ ] Storage disponible
[ ] Health checks correctos
[ ] Logs funcionando
[ ] Workers activos
[ ] Backups configurados
[ ] Usuario administrador seed creado
[ ] Scopes iniciales cargados
```

---

## 18. Reglas finales

- No desplegar secretos en código.
- No compartir base de datos entre servicios.
- No ejecutar migraciones de otros servicios.
- No desplegar sin health checks.
- No desplegar sin estrategia de backup.
- No iniciar workers antes de tener Redis disponible.
