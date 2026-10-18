# Dynamics Connector vía Dhole API Gateway (staging y producción)

## Arquitectura efectiva

`https://<DHOLE_API_HOST>/api/dynamics-connector/<ruta>` → Dhole API Gateway → `http://dynamics-api:8080/api/v1/<ruta>`.
La ruta Gateway de índice 13 tiene `StripPrefix=true`: sólo entrega endpoints de ejecución M2M `/api/v1`, no expone API Admin/OIDC. Ejemplos:
- `GET https://dhole-api.customcodecr.com/api/dynamics-connector/quotes/{guid}?connectionCode=X`
- `POST https://dhole-api.customcodecr.com/api/dynamics-connector/dhole/quotes`
- `GET https://api.logisticacastrofallas.com/api/health/dynamics-connector`

**NO** reemplaza JWT OAuth2 de Microsoft Entra con JWT de DholeAuth. El gateway reenvía la cabecera Authorization y el conector valida criptográficamente issuer, audience, client grants y campos. No compartir passwords/keys/DB con DholeSystem. El navegador de Admin independiente no queda publicado por esta ruta: requiere un diseño adicional de callback OIDC/host HTTPS que NO debe exponerse de forma accidental.

## Variables exactas a agregar a ambos archivos de entorno

Copiar claves en [plantilla](../../deploy/dynamics.env.example), sustituir `ENV` por `staging` o `production` y establecer `DYNAMICS_IMAGE_TAG=staging` o `latest`. Mantener `DYNAMICS_HTTP_URL=http://dynamics-api:8080` en ambos. Estos archivos contienen *rutas* a secretos, no sus contenidos.

En cada host crear con `0600` secretos totalmente **distintos entre staging y producción**:
- `postgres_password`: contraseña aleatoria para usuario `connector_app` de **dynamics-postgres**, no del `postgres` compartido.
- `database_connection`: `Host=dynamics-postgres;Port=5432;Database=dhole_dynamics_connector;Username=connector_app;Password=<MISMA_CLAVE_DEL_ARCHIVO_POSTGRES>`.
- `encryption_key` y `cursor_key`: dos claves nuevas distintas de 32 bytes generadas con fuente criptográfica y codificadas Base64.
- `oidc_client_secret`: secreto de App Registration OIDC de Administradores.
- `data_protection.pfx` / `data_protection_password`: certificado PFX con private key de duración/rotación controlada.

Los valores `DYNAMICS_ADMIN_OIDC_AUTHORITY`, `DYNAMICS_ADMIN_OIDC_CLIENT_ID`, `DYNAMICS_M2M_AUTHORITY`, `DYNAMICS_M2M_AUDIENCE` corresponden a *nuevos recursos Entra* por ambiente y no deben inventarse ni derivarse de JWT DholeAuth. En Microsoft Entra, provisionar app API, app consumidor con permisos app-only, roles admin y Dataverse Application User en la organización correcta.

## Compose

No añadir Dynamics a `docker-compose.services.yml` existente: lanzar **Compose independiente** `deploy/docker-compose.dynamics.yml` con el proyecto `dhole-dynamics-staging` o `dhole-dynamics-production`; así el stack original no recrea Postgres, AUTH ni CRM. La única red compartida es `dhole-staging` o `dhole` y el alias `dynamics-api` del contenedor API. DB y llaves están en volúmenes exclusivos del proyecto. Nunca usar `docker compose down -v`.

En `deploy/docker-compose.services.yml` se añade la ruta Gateway índice 13; requiere **recrear sólo el contenedor api-gateway** con la configuración del Compose de su ambiente (no reconstruir imagen Gateway). No basta con editar el archivo .env y reiniciar el conector: gateway debe cargar el nuevo índice.

## Despliegue

El workflow manual del repositorio `CustomCodeCR/DholeDynamicsConnectorService` compila las imágenes .NET Tools y API en el runner de Dhole y las etiqueta por rama (staging/latest), consulta `DholeSystem/deploy/docker-compose.dynamics.yml`, valida archivos de secretos host y arranca DB, migración, API, worker; luego recrea solo API Gateway para aplicar el nuevo índice. Primero staging, revisar smoke y M2M/Entra real, luego producción con permiso explícito del Environment y backup validado.

`DYNAMICS_JOBS_ENABLED=false`, `DYNAMICS_PRODUCTION_WRITES_APPROVED=NO` y `DYNAMICS_PRODUCTION_DELETES_APPROVED=NO` son los valores por defecto. No habilitar escrituras hasta autorización operativa explícita y separado control para DELETE.

## Verificaciones

`curl -fSs https://dhole-api.customcodecr.com/api/health/dynamics-connector` debe devolver un objeto `ready` si la DB propia ya migró. `curl -s -o /dev/null -w '%{http_code}' https://dhole-api.customcodecr.com/api/dynamics-connector/quotes/00000000-0000-0000-0000-000000000001?connectionCode=demo` debe responder 401 si no hay JWT válido (en vez de 502). Lo mismo para dominio producción tras go-live.

El host debe tener acceso a Internet para Microsoft Entra/Dataverse, sin exponer 5432 ni 8080; el firewall solo admite los puertos públicos existentes detrás de Traefik/Cloudflare. Los certificados públicos siguen siendo responsabilidad del ingress Dhole existente.

**Seguridad de credenciales**: reemplazar inmediatamente todos los secretos que fueron pegados en conversaciones o archivos compartidos: contraseñas PostgreSQL/Mongo/MinIO, JWT, SMTP, API keys, contraseñas iniciales y Maersk. Reemplazo coordinado para no interrumpir servicios. No introducirlos en GitHub ni logs.
