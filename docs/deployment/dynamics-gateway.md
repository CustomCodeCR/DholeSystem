# Dynamics Connector integrado con el PostgreSQL y DholeAuth existentes

**No colocar Tenant ID, Client ID ni Client Secret de Dataverse en `.env`.**

## Base y autenticación

Se usa el PostgreSQL ya existente en cada red Dhole (`POSTGRES_HOST`, `POSTGRES_PORT`, `POSTGRES_USER`, `POSTGRES_PASSWORD`). El nombre de la base exclusiva para Dynamics es `DYNAMICS_DB=dhole_dynamics_connector`. El workflow manual crea la base solamente si falta, sin tocar las existentes, y ejecuta migraciones del conector.

DholeAuth firma los JWT mediante `JWT_ISSUER`, `JWT_AUDIENCE` y `JWT_SECRET`. El conector valida esos parámetros y solo permite entrar en su administración a quien tenga scope `dynamics.admin` o `dynamics.security.admin`, otorgados en DholeAuth. Las escrituras administrativas sensibles usan `dynamics.security.admin`. No se atribuyen scopes por defecto.

### Variables requeridas (ambos entornos)

```dotenv
DYNAMICS_DB=dhole_dynamics_connector
DYNAMICS_HTTP_URL=http://dynamics-api:8080
DYNAMICS_IMAGE_TAG=latest
DYNAMICS_JOBS_ENABLED=false
DYNAMICS_PRODUCTION_WRITES_APPROVED=NO
DYNAMICS_PRODUCTION_DELETES_APPROVED=NO
```

En staging cambiar `DYNAMICS_IMAGE_TAG=staging`. Las restantes variables PostgreSQL/JWT/red ya existen en DholeSystem. **No añadir rutas de archivos secretos inexistentes ni IDs ficticios de Entra.**

## Cómo registrar los IDs reales en la base

1. Acceder primero a DholeAuth con un usuario autorizado para `dynamics.admin`.
2. Enviar `POST https://api.logisticacastrofallas.com/api/dynamics-admin/connections` con Authorization bearer de DholeAuth y este JSON, sustituyendo valores por los identificadores reales:
```json
{
  "code": "principal",
  "dataverseUrl": "https://ORGANIZACION.crm.dynamics.com",
  "tenantId": "TENANT_GUID_REAL",
  "clientId": "CLIENT_GUID_REAL",
  "clientSecret": "CLIENT_SECRET_VALUE_REAL",
  "defaultCurrencyId": null
}
```
3. El backend valida la URL y GUID, cifra `clientSecret` con AES-256-GCM y almacena el registro en `dynamics.connections`. Las respuestas devuelven solo la vista resumida (sin secreto), jamás el texto original.
4. Consultar `GET /api/dynamics-admin/connections` y ejecutar `POST /api/dynamics-admin/connections/principal/test`. Esto requiere que la aplicación de Microsoft tenga permisos reales como Application User en ese Dataverse.
5. En staging la base pública es `https://dhole-api.customcodecr.com`.

**No insertar secretos directamente con SQL**, porque el backend genera IV/nonce, GCM tag y versión de clave. El `clientId` y `tenantId` de esta conexión son los de Microsoft Dataverse, distintos del JWT de DholeAuth.

El nombre de la base NO implica que ya exista: solo el workflow inicial manual crea `dhole_dynamics_connector` cuando no está presente. Se crea dentro del PostgreSQL de la red correcta, sin ejecutar SQL en `dhole_auth`, `dhole_pricing` ni `dhole_crm`.

## Seguridad y acceso

`/api/dynamics-admin/*` se dirige al `/api/admin/v1/*` del conector, protegido con bearer DholeAuth y scopes explícitos. La ruta `/api/dynamics-connector/*` permanece para la API machine-to-machine y conserva la validación OAuth app-only original: no confundir el JWT de usuario DholeAuth con credenciales de máquina. Este despliegue permite administración y conexión Dataverse con DholeAuth; para consumidores automáticos M2M todavía se requiere una integración adicional de identidad de servicio.

La clave simétrica que cifra las credenciales y la clave de paginación se generan automáticamente la primera vez en un volumen exclusivo de cada ambiente (`dynamics_runtime_keys`), no se derivan del JWT ni de PostgreSQL. Si ese volumen se pierde, no se pueden descifrar los secretos guardados: hacer copia cifrada de la BD y del volumen de claves **antes de registrar credenciales reales**. Nunca ejecutar `docker compose down -v`. El deploy es manual y producción conserva los permisos de escritura/borrado deshabilitados.

GitHub Actions debe tener Environments `staging` y `production` protegidos con reviewers. El workflow no da de alta registros Dataverse ficticios ni inicia sesión sin autorización. El único modo de completar la conexión es proporcionar los identificadores reales en la petición administrativa.
