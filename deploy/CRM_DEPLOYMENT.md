# DholeCRMService — configuración de despliegue

Este repositorio incluye los contenedores `crm-api` y `crm-workers` en `deploy/docker-compose.services.yml` (para `master` / producción y `develop` / staging).

## Variables nuevas, no sensibles

Añadir estas líneas **sin eliminar ni sustituir ninguna variable existente** en ambos archivos protegidos del servidor:

- `/opt/dhole/.env`
- `/opt/dhole/.env.staging`

```dotenv
# PostgreSQL
CRM_DB=dhole_crm

# Direcciones internas (red Docker de cada ambiente)
CRM_HTTP_URL=http://crm-api:8080
CRM_GRPC_URL=http://crm-api:8081
```

`deploy/prepare-environments.sh` también agrega los mismos valores **solo si faltan** en sus copias de runtime; no modifica los archivos fuente ni las credenciales.

## Servicios

| Servicio | Imagen | Puerto interno | Uso |
|---|---|---|---|
| `crm-api` | `dhole/crm-api:${DHOLE_IMAGE_TAG}` | 8080 HTTP, 8081 gRPC (HTTP/2) | API y servidor gRPC |
| `crm-workers` | `dhole/crm-workers:${DHOLE_IMAGE_TAG}` | ninguno | BackgroundTasks, Redis Streams, Outbox/Inbox |

Ambos servicios reutilizan las variables JWT, Redis, PostgreSQL y la clave de servicios internos existentes (desde el archivo protegido de cada entorno). Se conectan a la red `dhole-runtime`, cuyo nombre real depende de `DHOLE_NETWORK` (`dhole` o `dhole-staging`). No se publican puertos del CRM al host.

Las claves `Integrations__*` y `Grpc__Clients__Config__Address` expresan el contrato de configuración esperado por el nuevo CRM: deben implementarse/validarse en el código de `DholeCRMService`. Para otros servidores gRPC, agregar solo URLs y contratos que hayan sido implementados realmente.

## API Gateway

Se envían al contenedor `api-gateway`:

```dotenv
CRM_HTTP_URL=http://crm-api:8080
Gateway__Routes__12__Destination=http://crm-api:8080
Gateway__HealthChecks__crm=http://crm-api:8080
```

**Pendiente de DholeApiGateway:** verificar que la configuración dinámica del Gateway consume el índice 12 y que se ha registrado el prefijo `/api/crm/**` con el destino `CRM_HTTP_URL`. El cambio de DholeSystem prepara las variables, pero no sustituye la implementación de enrutamiento.

## Fuentes Compose y cuidado con el include

El archivo `deploy/docker-compose.services.yml` de `master` y `develop` empieza con `include: /opt/dhole/docker-compose.services.yml`. Es distinto del Compose extenso que reside en el servidor.

- El archivo del servidor no se puede actualizar mediante un commit de GitHub.
- **No** duplicar `crm-api` / `crm-workers` en el Compose incluido del servidor: Docker Compose `include` no fusiona automáticamente definiciones de servicios con el mismo nombre.
- Mantener sin cambios las definiciones existentes, redes, credenciales y configuraciones Traefik del servidor.
- Confirmar que el Compose efectivo resuelve correctamente `api-gateway`; el servicio también aparece en el Compose incluido, por lo que pueden existir conflictos de nombre. No desplegar hasta validar su configuración efectiva y mantener todas las rutas preexistentes.
- Si alguna automatización despliega **solo** `/opt/dhole/docker-compose.services.yml`, tendrá que incorporar el CRM en ese Compose o pasar el archivo de DholeSystem; actualizar GitHub por sí solo no altera ese archivo.

## Validación previa al despliegue

Con las imágenes publicadas (primero staging) y con el archivo del repositorio disponible en el servidor:

```bash
docker compose --env-file /opt/dhole/.env.staging \
  -f deploy/docker-compose.services.yml \
  -f deploy/docker-compose.staging.yml \
  -p dhole-staging config -q

docker compose --env-file /opt/dhole/.env \
  -f deploy/docker-compose.services.yml \
  -p dhole config -q
```

Verificar **además** el Compose resuelto: rutas previas del Gateway, redes, variables, bases de datos separadas y puertos. El comando `config -q` no valida la lógica del Gateway, el aislamiento de bases, los permisos ni la existencia de las imágenes.

Crear la base de datos `dhole_crm` en el PostgreSQL correspondiente **de cada entorno** y ejecutar las migraciones EF Core del servicio antes de ponerlo en operación. No asumir que los dos archivos de ambiente apuntan a instancias PostgreSQL diferentes sin comprobarlo.

Desplegar por separado `crm-api` y `crm-workers` solo cuando estén construidas y disponibles las imágenes `dhole/crm-api:staging|latest` y `dhole/crm-workers:staging|latest`. No reiniciar servicios existentes como parte de esta adición.

## Seguridad

No subir archivos `.env` reales a GitHub. No escribir contraseñas, tokens, JWT, claves de Maersk o credenciales SMTP en Compose/documentación/versionado. Si alguna credencial se ha compartido públicamente o fuera del entorno autorizado, rotarla de manera coordinada sin interrumpir los servicios.
