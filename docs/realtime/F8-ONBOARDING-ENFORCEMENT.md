# F8 — CI de cobertura para servicios futuros (candidato sin aprobación)

**Release:** rt-20261107-01 · **global SemVer candidato:** 1.13.0.
**Rama compartida:** feature/dhole-realtime-universal-rt-20261107-01.
**Gate:** F8 NO APROBADO, F9 no autorizado, 0/14 chaos real de staging en F7.

## Entregables ya implementados

1. Un ejemplo compilable de servicio dueño con endpoint REST bajo scope + owner
   PostgreSQL, control de revisión, commit atómico de negocio y Outbox,
   publicador Redis Streams con reintento, métricas y logs, Inbox SQL:
   scaffolds/dhole-future-service/.
2. Contrato obligatorio realtime.manifest.yaml con owner, recurso, scope,
   audiencia, evento versionado, REST GET, consumidor, publicación, jobs,
   test contractual, integración/recovery y excepciones firmadas.
3. Validador fail-closed scripts/realtime/verify-f8-future-service.py.
   Descubre rutas literales MapPost/Put/Patch/Delete y workers hosted.
   Bloquea rutas dinámicas, MapMethods sin análisis, HttpPost MVC,
   GraphQL/gRPC y cualquier segundo MapHub hasta auditoría especializada.
   Compara fichero, verbo, ruta y prefijos MapGroup con el manifiesto,
   exige test files reales y comprueba registry central.
4. Generador scripts/realtime/scaffold-future-service.py: crea candidatos
   versionados y manifiesto, SQL, pruebas, CI y propuesta de registry sin
   sobreescribir directorios ni modificar Git o servidores.
5. Workflow CI en .github/workflows/realtime-f8-future-service.yml para
   la muestra. Plantilla por repositorio nuevo en
   scaffolds/realtime-future-enforcement.yml, y plantilla PR de revisión
   en scaffolds/realtime-future-PR-template.md.
6. Guard formal scripts/realtime/verify-f8-formal-gate.py y evidencia
   docs/realtime/gate-evidence.f8.yaml: no permite F9 hasta F0–F8
   aprobadas secuencialmente y 14/14 chaos con evidencia real.

## CI ejecutado

- #42511408397: 16 pruebas de contrato/política (1 positiva + 15 negativas)
  y 4 del generador = **20/20 PASS**; .NET8 compila; PostgreSQL real CI
  conserva dos Outbox confirmados (uno durante caída Redis); al recuperar
  se entregan; repetir XADD antes de ACK crea 4 entradas para 2 EventId,
  Inbox PostgreSQL aplica **exactamente 2 efectos lógicos**.
- #42511053160 y las ejecuciones recientes del guard F8: CI PASS de
  **bloqueo deliberado**, no de aprobación formal.
- La muestra S14 se registra solo como CI_SAMPLE_NOT_DEPLOYABLE; no existe
  un repositorio vivo DholeFutureSample ni servicio agregado al Compose.
  No se ha creado otro Hub.

## Cómo incorporar un servicio nuevo después del batch

- Solicitar nuevo serviceId a DholeSystem, owner responsable, scopes,
  modelo de exposición, semver y rama intermedia del mismo release.
- Generar en un directorio NUEVO:

      python scripts/realtime/scaffold-future-service.py --name DholeBillingService \
        --domain billing --service-id S15 --owner PlatformTeam \
        --version 1.14.0 --out /path/to/DholeBillingService

- Revisar el resultado y actualizar registro central con una PR
  independiente dentro del lote coordinado; registrar stream en el único
  DholeApiGateway y sumar vista REST autorizada en DholeWeb. Los IDs y
  rangos son ejemplos, no reservas oficiales para producción.
- Probar eventId idempotente, scopes reales de varios usuarios, abandono de
  sesión, OAuth/JWT, reconnect, REST offline fallback, Outbox/Inbox/DLQ,
  1000 eventos y regresiones. Un consumidor no debe efectuar efectos de
  negocio por un mensaje emitido a UI. La guía del scaffold explica los
  pasos no provistos automáticamente.
- La CI del repo futuro DEBE validar el registro central real desde
  DholeSystem/develop con token de solo lectura
  DHOLE_REGISTRY_READ_TOKEN. Sin permiso/tokens, falla el PR.
  No aceptar local central-registry.PROPOSAL.yaml como sustituto.
- Habilitar CODEOWNERS y el required status check en develop/master solo
  durante F9/F10, después del batch integrado; no modificar las ramas
  protegidas en esta fase.

## Limitaciones / riesgo que bloquea gate F8

- El parser fuente no es Roslyn ni conoce rutas generadas dinámicamente;
  las trata como desconocidas y bloquea el check. Revisión de código y
  pruebas funcionales siguen siendo requisito separado.
- El ejemplo no está conectado a un Gateway Hub real ni demuestra WSS
  multinstancia ni reautorización de JWT: **0 validaciones F8 staging**.
- Los 13 servicios existentes y las 582 filas candidatas F0 no quedan
  aprobados por el validador de servicios nuevos.
- La consulta del estado nativo de ramas GitHub devolvió HTTP 403
  Resource not accessible by integration en develop/master y rulesets
  vacíos: no se pudo acreditar enforcement real ni modificarlo.
- Redis stage último leído con aof_enabled=0; no se ha ejecutado migración
  coordinada ni restauración real. F7 mantiene 0/14 staging aprobados.
- F8 formalApproved=false y nextPhaseF9Authorized=false. Ningún merge,
  despliegue, flag del batch ni cambios en develop/master/main.

## Registro en el release

Ver también docs/realtime/gate-evidence.f8.yaml,
docs/realtime/release-manifest.yaml y docs/realtime/PROGRESS.md.
