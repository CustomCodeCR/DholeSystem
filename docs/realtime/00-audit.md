# F0 — Auditoría inicial y baseline (Dhole Realtime Universal)

- Plan: CODEX_DHOLE_REALTIME_PLAN_POR_FASES_MEDIBLES.md **v2.1.0**, recibido como archivo adjunto el 2026-11-07.
- Release ID: `rt-20261107-01`.
- Estado: **BLOQUEADA** (auditoría remota de ramas lograda, inspección técnica incompleta).
- Alcance: S01–S13, API Gateway, Web, DholeSystem; SRM/System lógicos por identificar.
- Cambios funcionales: **ninguno**. F1/F9/F10: **NO INICIADAS**.

## Ramas y permiso

Los 16 repositorios `CustomCodeCR/{DholeCRMService,DholePricingService,DholeNotificationsService,DholeAuthService,DholeConfigService,DholeAuditLogsService,DholeStorageService,DholeDataExtractionService,DholeReportsService,DholeDynamicsConnectorService,DholeAIService,DholeAgentService,DholeContentService,DholeApiGateway,DholeWeb,DholeSystem}` fueron consultados mediante conector GitHub y reportaron permiso push. Se verificó ausencia de la rama exacta antes de crearla y se creó en los 16 la rama `feature/dhole-realtime-universal-rt-20261107-01` a partir del SHA de `develop` auditado, **no de la rama default**. Las ramas `develop` y `master` existen en los 16.

Ramas default: DholeCRMService y DholeSystem usan `main`; los otros 14 usan `master`. **Nunca se escribirá en main**. Las comparaciones `develop...master` devolvieron `diverged` para los 16; difieren mucho DholeWeb (master-only 3089, develop-only 3457), Pricing (1330/1444) y Agent (763/705). No reconciliar automáticamente ni sobrescribir cambios. Detalles: `release-manifest.yaml` (SHAs completos y merge base).

Los SHAs del manifiesto son **baseline de F0**, no snapshot congelado ni promoción autorizada. Se revisará drift previo a F9.

## Versiones verificadas (desde `version.json` en la intermedia recién creada)

| Repo | Componente | Ecosistema declarado |
|---|---:|---:|
| DholeCRMService | 1.3.1 | 1.12.3 |
| DholePricingService | 1.5.7 | 1.12.4 |
| DholeNotificationsService | 1.2.1 | 1.3.1 |
| DholeAuthService | 1.2.1 | 1.3.1 |
| DholeConfigService | 1.2.1 | 1.3.1 |
| DholeAuditLogsService | 1.2.1 | 1.3.1 |
| DholeStorageService | 1.2.2 | 1.3.2 |
| DholeDataExtractionService | 1.3.5 | 1.3.12 |
| DholeReportsService | 1.4.2 | 1.11.2 |
| DholeDynamicsConnectorService | 1.2.1 | 1.3.1 |
| DholeAIService | 1.3.9 | 1.3.12 |
| DholeAgentService | 1.2.2 | 1.3.2 |
| DholeContentService | 1.2.1 | 1.3.1 |
| DholeApiGateway | 1.3.1 | 1.3.12 |
| DholeWeb | 1.12.4 | 1.12.4 |
| DholeSystem | 1.12.3 | 1.12.3 |

**Cambio documental en F0:** `DholeSystem` elevó `version.json` de 1.12.3 a 1.12.4 en esta rama intermedia y actualizó `CHANGELOG.md`. Las cifras de la tabla son **baselines anteriores**; ningún otro componente ni rama final recibió incremento en esta fase. La versión del batch completo no ha sido aplicada.

**Inconsistencia existente:** `ecosystemVersion` no es globalmente uniforme. Propuesta pendiente: versión funcional de batch `1.13.0` (MINOR desde máximo observado 1.12.4), sin aplicar ni declarar release. La numeración final debe reevaluarse contra cambios concurrentes antes de F9. Bumps por componente y CHANGELOG obligatorios.

## Evidencia de lectura de código (parcial, NO inventario completo)

- `DholeCRMService@develop:src/Dhole.Crm.Api/Program.cs`: configuraciones Auth, autorización, gRPC, health PostgreSQL/Redis. Tiene endpoints reales (el README del mismo repo afirma incorrectamente que todavía no existen endpoints comerciales).
- `DholeCRMService@develop:src/Dhole.Crm.Api/Endpoints/CrmFollowupEndpoints.cs`: mutaciones relativas a grupo `PUT /accounts/{accountId}/followup-policy`, `POST /followups`, `POST /followups/{id}/reschedule`, `POST /followups/{id}/complete`, `POST /followups/{id}/cancel`, `POST /followups/{id}/archive`, `POST /reminders/{id}/replay`. Revisar prefijo MapGroup, transacciones y workers antes de introducirlas en matriz como rutas absolutas.
- `DholeWeb@develop:package.json`: Vue `^3.5.38`, Node `^22.18.0 || >=24.12.0`, tests modulares y script de versionado; no aparece `@microsoft/signalr` como dependencia directa. Esto NO descarta wrappers o implementaciones existentes.
- `DholeDynamicsConnectorService@develop:README.md`: describe .NET 10, PostgreSQL, jobs y Vue de administración; no prueba configuración de producción.
- `DholeContentService@develop:README.md`: declara CMS con Postgres, Redis, Outbox/Inbox y worker programado; no se han inspeccionado tablas ni workflows de eventos en ejecución.
- `DholeSystem@develop:README.md`: define arquitectura objetivo Redis Streams, Outbox e Inbox; es documentación, NO evidencia de infraestructura viva.
- Para varios otros repos no existe README.md en la raíz. No inferir estado de tecnología o cobertura a partir de la ausencia de README.

## Baseline de infraestructura y medición (NO VERIFICADOS)

- Infraestructura real de `dhole-staging` / `dhole`, Compose, Traefik/proxy, JWT, CORS, WSS/negociación, Redis Streams/AOF/retención, redes, instancias y backups: no auditados en ambiente vivo.
- Usuarios simultáneos, instancias, frecuencia y tamaño de mensajes, carga REST y p95/p99: no medidos.
- Dependencias y permisos del Gateway, código completo de workers, servicios dueños de SRM/System: no identificados con evidencia definitiva.
- Inventario completo de endpoints mutables/jobs de S01–S13, Gateway y vistas Web: **NO COMPLETADO**. Cobertura 100%: NO DEMOSTRADA.
- Esquema de sincronización de Redis/Outbox existente y documentación complementaria detallada: pendiente de contrastar contra código en develop.

## Riesgos y política de no liberación

1. Historia muy divergente entre develop/master; posibles conflictos funcionales en futuras promociones. Reconciliación exclusivamente en ramas intermedias/temporal y pruebas, nunca reset/force.
2. Repos default main; escribir siempre ref explícita en conectores GitHub.
3. Versiones de ecosistema ya desalineadas; fijar versión global al congelar batch y verificar metadatos, manifest y CHANGELOG.
4. Cobertura incompleta y falta de acceso a runtime: **gate F0 RECHAZADO**.
5. Migraciones y features no ejecutadas; todos los flags nuevos deben permanecer apagados hasta batch completo.

## Criterio para reabrir el gate F0

Verificar 100% endpoints/jobs por repo y vistas/audiencias, ownership SRM/System, infraestructura real y baseline con mediciones reproducibles; guardar evidencia anonimizada. Antes de F1, registrar status de branches, protecciones, CI, dependencias y divergencias contra SHAs iniciales. Hasta entonces, **detenerse en F0**.
