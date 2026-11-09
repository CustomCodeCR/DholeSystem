# Dynamics 365 — Activación de CRUD general sin ticket manual

**Entorno:** Producción, Argos (AlmaLinux).
**Objetivo:** permitir CREATE, UPDATE, UPSERT y, si se autoriza, DELETE y acciones en las APIs publicadas del conector Dynamics. Los permisos por tabla, campo, usuario y clave siguen siendo obligatorios.

## Registro de aprobación automático

El workflow [Deploy Dynamics Connector via existing Dhole PostgreSQL and Gateway](https://github.com/CustomCodeCR/DholeDynamicsConnectorService/actions/workflows/deploy-dhole-gateway.yml) registra una referencia `GH-ACTIONS-<run_id>-<sha>` como prueba de procedencia de la ejecución de despliegue.

**No hay que escribir `DYNAMICS_PRODUCTION_WRITES_TICKET` ni `DYNAMICS_PRODUCTION_DELETES_TICKET` en `/opt/dhole/.env`.** La acción de GitHub los genera al desplegar con el modo autorizado.

El run de GitHub **no reemplaza la autorización humana**: configurar el Environment `production` con *required reviewers* y restricciones de ramas en GitHub Settings → Environments antes de usar modo `DEPLOY_FULL_CRUD`. Una persona con autoridad debe aprobar ese despliegue.

## Configuración de Argos

Editar el archivo existente:

```bash
sudo nano /opt/dhole/.env
```

Dejar estas variables **sin copiar ni subir el archivo de secretos al repositorio**:

```dotenv
DYNAMICS_PRODUCTION_WRITES_APPROVED=YES
DYNAMICS_PRODUCTION_DELETES_APPROVED=YES
```

No agregues referencias inventadas ni copies aquí las claves `DynamicsQuoteSync__ApiKey`. Si la organización no autoriza eliminaciones, dejar `DYNAMICS_PRODUCTION_DELETES_APPROVED=NO`. Para deshabilitar todas las escrituras, poner ambas en `NO`.

## Aplicar en producción

1. Confirmar que el código revisado está en la rama `master` y que los tests pasaron.
2. En GitHub Actions abrir el workflow **Deploy Dynamics Connector via existing Dhole PostgreSQL and Gateway**.
3. Elegir *Run workflow* con rama `master`, `target=production`, `production_confirmation=DEPLOY_FULL_CRUD`.
4. Aprobar la solicitud en el GitHub Environment protegido `production` por el revisor autorizado.
5. El workflow inspeccionará `/opt/dhole/.env`, generará la referencia de auditoría de forma automática, recreará `dynamics-api` / `dynamics-worker` y comprobará readiness.
6. En Dhole → Dynamics 365 → Incidencias de ofertas seleccionar **Comprobar autorización**. Deberá responder `DYNAMICS_QUOTE_WRITES_READY` si la clave de Pricing está vigente y las escrituras están permitidas.
7. Reintentar solo las sincronizaciones sin escritura confirmada y comprobar `quote`, `quotedetail`, `totalamount` y el estado de conciliación.

**Atención:** los despliegues normales por `push` no pueden habilitar CRUD si el archivo solicita `YES`: fallan cerrados hasta ejecutar un despliegue manual aprobado. Cualquier despliegue posterior con escrituras habilitadas también debe aprobarse de esta manera.

## Reversión

1. Poner ambas variables de `/opt/dhole/.env` en `NO`.
2. Ejecutar workflow de producción manual con `production_confirmation=DEPLOY_READ_ONLY` y autorización de Environment.
3. Confirmar que **Comprobar autorización** informa política de solo lectura y que las API keys siguen sometidas a su alcance.

## Riesgos y permisos

La habilitación general no da acceso administrativo anónimo ni cambia los permisos de Dataverse. **DELETE puede eliminar información irreversible**; habilitarlo solo después de tener copias, auditoría y responsable de aprobación. Los errores por nombres ambiguos, campos no autorizados, credenciales vencidas o privilegios de Dataverse deben corregirse separadamente de esta política.
