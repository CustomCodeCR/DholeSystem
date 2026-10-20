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


## API para aplicaciones externas (Pangolin u otros consumidores)

El endpoint público de PRODUCCIÓN usa exclusivamente `https://api.logisticacastrofallas.com`,
no `https://sistema.logisticacastrofallas.com`. Por ejemplo:

```http
POST https://api.logisticacastrofallas.com/api/dynamics-connector/saved-queries/ofertas_abiertas/execute
Authorization: Bearer <TOKEN_DE_APLICACION>
Content-Type: application/json

{"connectionCode":"principal","parameters":{}}
```

Abrir este enlace desde un navegador no ejecuta la consulta: es una ruta POST con
autenticación M2M, no una página ni una sesión DholeAuth.

La API M2M está protegida mediante Microsoft Entra, con token **app-only**, no
mediante el JWT de un usuario Dhole. Para activarla de manera explícita en el
entorno correspondiente, agregar **únicamente** estos valores no secretos al
archivo de entorno de despliegue, una vez configurados en Entra:

```dotenv
DYNAMICS_M2M_AUTHORITY=https://login.microsoftonline.com/<TENANT_GUID_REAL>/v2.0
DYNAMICS_M2M_AUDIENCE=api://<ID_REAL_DE_LA_APLICACION_API_EN_ENTRA>
```

El Compose pasa estas variables como `M2m:Authority` y `M2m:Audience` a
Dynamics, y mantiene la API de máquina cerrada si faltan. El público puede
consultar si el servicio está activo solo a través del diagnóstico administrativo
`/api/dynamics-admin/console/diagnostics`, protegido por DholeAuth.

1. Registrar en Microsoft Entra una **aplicación recurso API** y definir app roles
   como `dynamics.records.read`, `dynamics.records.create`, `dynamics.records.update`
   y `dynamics.records.delete`, habilitados para aplicaciones. Configurar su URI
   de aplicación como el audience esperado.
2. Registrar la aplicación cliente externa (Pangolin si es el consumidor). Asignarle
   únicamente el app role que necesita sobre la aplicación API; otorgar consentimiento
   administrativo y guardar su secreto/certificado **solo en el backend seguro**.
3. En Dynamics 365 de Dhole, pestaña **Seguridad**, registrar el cliente M2M con
   el `issuer` exacto del token y el `client_id` de la aplicación consumidora.
   Crear un grant habilitado para `principal`, la tabla lógica (por ejemplo
   `quote`, NO el nombre de colección `quotes`), `read`, las columnas
   autorizadas y una cuota razonable.
4. Guardar y activar una consulta en Query Builder y seleccionar su nombre desde
   **API / Integraciones**. Allí se copia el endpoint de API y el ejemplo cURL.
5. Desde el **servidor** de Pangolin obtener un token OAuth2 client_credentials:

```http
POST https://login.microsoftonline.com/<TENANT_GUID_REAL>/oauth2/v2.0/token
Content-Type: application/x-www-form-urlencoded

grant_type=client_credentials
&client_id=<CLIENT_ID_REAL>
&client_secret=<SECRET_GUARDADO_EN_SERVIDOR>
&scope=api%3A%2F%2F<APP_ID_URI_REAL>%2F.default
```

   Usar `Authorization: Bearer <access_token>` en cada llamada al gateway.
   El token debe incluir la identidad de aplicación y el app role correspondiente,
   y su `aud` e `iss` deben coincidir con la configuración del servidor. Si
   Pangolin es solamente un *reverse proxy* o túnel, debe preservar el método,
   cuerpo y cabecera Authorization al reenviar al gateway, sin redirigir al
   frontend. Para aplicaciones web externas, priorizar un backend propio para
   evitar exponer credenciales o depender de CORS del navegador.

Nunca agregar secretos a las URLs ni habilitar M2M con tokens de usuarios.
Los grants por tabla/campo, el rate limiting y las políticas de escrituras
de producción continúan vigentes. No hay nuevas credenciales reales configuradas
automáticamente con este cambio.

## Seguridad y acceso

`/api/dynamics-admin/*` se dirige al `/api/admin/v1/*` del conector, protegido con bearer DholeAuth y scopes explícitos. La ruta `/api/dynamics-connector/*` permanece para la API machine-to-machine y conserva la validación OAuth app-only original: no confundir el JWT de usuario DholeAuth con credenciales de máquina. Este despliegue permite administración y conexión Dataverse con DholeAuth; para consumidores automáticos M2M todavía se requiere una integración adicional de identidad de servicio.

La clave simétrica que cifra las credenciales y la clave de paginación se generan automáticamente la primera vez en un volumen exclusivo de cada ambiente (`dynamics_runtime_keys`), no se derivan del JWT ni de PostgreSQL. Si ese volumen se pierde, no se pueden descifrar los secretos guardados: hacer copia cifrada de la BD y del volumen de claves **antes de registrar credenciales reales**. Nunca ejecutar `docker compose down -v`. El deploy es manual y producción conserva los permisos de escritura/borrado deshabilitados.

GitHub Actions debe tener Environments `staging` y `production` protegidos con reviewers. El workflow no da de alta registros Dataverse ficticios ni inicia sesión sin autorización. El único modo de completar la conexión es proporcionar los identificadores reales en la petición administrativa.
