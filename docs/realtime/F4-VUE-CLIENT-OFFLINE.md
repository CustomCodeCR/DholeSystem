# F4 — Cliente Vue universal + contingencia offline

**Plan:** `CODEX_DHOLE_REALTIME_PLAN_POR_FASES_MEDIBLES.md` v2.1.0  
**Batch:** `rt-20261107-01`  
**Código:** `CustomCodeCR/DholeWeb@feature/dhole-realtime-universal-rt-20261107-01`  
**Gate:** **NO APROBADO**; los de F0–F3 aún requieren validación formal.

## Contrato cliente

- `src/core/realtime/realtimeManager.ts`: un gestor tipado compartido y un WebSocket lógico por pestaña. No instancia conexiones desde componentes.
- `src/core/realtime/universalRealtime.ts`: singleton a nivel App, integra sesión/refresh, online/offline, pestaña visible/oculta, arranque y desmontaje.
- `src/core/realtime/useResourceRealtime.ts`: observador de recurso por vista con cleanup mediante `onScopeDispose`; la suscripción no expone un nombre de grupo arbitrario. Recursos piloto `crm.account` y `pricing.rate` únicamente.
- `App.vue`: lifecycle login/logout, refresh JWT, impersonación, rutas públicas y desmontaje. No altera el sistema de notificaciones antiguo ni su Hub.
- `DholeRealtimeStatus.vue`: estado accesible no invasivo dentro del workspace: connecting, connected, reconnecting, degraded, offline y unauthorized.

## Seguridad de credenciales y transporte

1. `POST /hubs/realtime/negotiate?negotiateVersion=1` por Gateway con `Authorization: Bearer <JWT>`; `POST /hubs/realtime/ticket` con el mismo header. El navegador construye URL `wss://.../hubs/realtime?id=<opaque>&ticket=<single-use>`. Nunca pone JWT, refresh token ni `access_token` en query.
2. Solo acepta ticket opaco del tamaño esperado. Ante 401/403 de Hub, intenta renovar token **una sola vez**; si falla, entra `unauthorized` y no intenta reconectar hasta nueva sesión.
3. El backend F3 vuelve a comprobar permisos por recurso en cada mensaje, pero F4 también borra datos visibles al recibir `403/401/404` del GET REST propietario (en CRM/Pricing), no deja presentar contenido revocado.
4. En cambio de usuario/impersonación, descarta credenciales, socket, listeners, deduplicaciones y observadores del sujeto anterior.
5. Cada intento de activación requiere en **frontend** simultáneamente:
   - `VITE_DHOLE_REALTIME_ENABLED=true`
   - `VITE_DHOLE_REALTIME_BATCH_APPROVED=true`
   - `VITE_DHOLE_REALTIME_RELEASE=rt-20261107-01`
   
   Todos **desactivados o ausentes** por defecto en el branch. Además el Gateway F3 exige sus propios flags `Features:UniversalRealtimeEnabled`, `Realtime:Enabled`, `Realtime:BatchApproved` y release ID exacto. No habilitar antes de batch F9/F10, ni cambiar el estado del servidor real.

## Convergencia REST y contingencia

- Socket cerrado, error al negociar, fallo inicial, reconexión, cambio de online/offline, pestaña visible: actualiza las vistas observadas por GET REST. Mientras WS está inactivo, polling escalonado de **5 a 30 segundos**, con límite de requests concurrentes mediante inFlight por observador. Un recurso oculto no se consulta.
- Reintento WS con backoff exponencial escalonado `[0, 2s, 5s, 10s, 30s]` + jitter acotado a 25%; timeout de handshake de 8s. No inicia en una pestaña oculta/offline.
- Al confirmar handshake/resubscribe se consultan de nuevo los recursos activos por GET REST. Los eventos recibidos solo invalidan; la UI jamás asume escritura confirmada por recibir un evento.
- Dedupe LRU por `eventId` acotada a 2048. Revisión del `aggregateVersion`: se ignoran versiones antiguas y duplicadas; se solicita snapshot REST ante nueva versión o gap; no se sobreescriben versiones conocidas con snapshots más viejos.
- Formularios sucios: no ejecutar `applySnapshot` si existe edición o cambio pendiente; conservar borrador, indicar conflicto remoto y permitir resolver al guardar/descartar. Nunca reintentar automáticamente mutaciones dudosas: solo se realizan GET.
- Sin internet: estado `offline`, no hay polling ni escrituras automáticas, se conserva lectura previa salvo revocación de permisos. El flujo de Pricing offline preexistente se conserva sin tocar.

## Cobertura piloto explícita

- `CrmRecordDetailView.vue`: **cuentas**, carga REST de `/api/crm/accounts/{id}`, vista segura si una edición está sucia; relaciones revalidadas solo si no hay formulario abierto. Se avisa de conflicto sin modificar el borrador. Revocación del acceso elimina vista y relaciones.
- `PricingRateReadOnlyView.vue`: GET de tarifa `/api/pricing/rates/{id}` por `PricingService.getRate`. Refresca solo la vista de detalle, no el formulario modal de edición; revocación limpia la tarifa visible.
- No se vinculan listados/dashboards/widgets restantes en F4; corresponden a piloto F5 y cobertura F6. **No declarar cobertura del sistema 100%** por estas dos vistas.

## Pruebas F4 (CI aislado)

Workflow `DholeWeb/.github/workflows/realtime-f4-web.yml`: Node 24, instalación frozen pnpm, `version:check`, `tests/realtimeF4Manager.test.ts`, regresiones CRM/Pricing, `vue-tsc` y build frontend con flags off. Casos: **100** iteraciones de attach/detach, **30** cierres inesperados y re-suscripciones, **30** fallos iniciales simulados seguidos de recuperación, aislamiento de 1 socket/pestaña, online/offline, pestaña visible, dedupe, versión fuera de orden, conflicto de edición y token expirado. Las 100 iteraciones comprueban observadores/timers, **no sustituyen montar 100 componentes Vue reales**: falta prueba E2E del DOM y memoria en navegador real antes del gate final.

**Pendiente** la última conclusión/commit de CI, WSS público y Auth real, pruebas de reconciliación de todas las vistas piloto con 2 usuarios de staging y 0 fugas entre tenants.

## Rollback

Mantener flags frontend y Gateway OFF. El frontend original sigue ejecutando REST, la conexión a NotificationHub permanece independiente y el backend no ejecuta migraciones por F4. No hay PRs, merges, publicación de versión ni despliegues en F4.
