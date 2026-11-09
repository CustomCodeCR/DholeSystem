# F4 — evidencia de CI para Vue universal y contingencia

**Release:** rt-20261107-01 · **plan:** 2.1.0 · **estado:** piloto candidato, gate F4 NO APROBADO.

## GitHub Actions verificado

- Repositorio: `CustomCodeCR/DholeWeb`.
- Rama: `feature/dhole-realtime-universal-rt-20261107-01`.
- SHA exacto probado: `ed6271db6b32fb33accc1dec2c106e66672ef923`.
- [Workflow F4 — run 42447931191](https://github.com/CustomCodeCR/DholeWeb/actions/runs/42447931191): **SUCCESS**.
- Pruebas unitarias del gestor F4: **11/11 aprobadas, 0 fallidas y 0 omitidas**. Incluyen 100 ciclos de registro/desregistro de observadores, 30 cierres de WebSocket con reconexión y resuscripción, 30 fallos de conexión inicial, único socket lógico por instancia de app, ausencia de JWT en URL WSS, restauración REST, eventos duplicados/fuera de orden, protección de formulario sucio, offline, pestaña oculta, sesión vencida y cambio de usuario.
- Regresiones CRM/Pricing: **91/91 PASS** (71 CRM, 3 multi-POE, 17 multi-QUO).
- `pnpm install --frozen-lockfile`: **PASS**.
- `pnpm run version:check`: **PASS**, candidato `DholeWeb 1.13.0` y changelog/package-lock consistentes.
- `pnpm run type-check`: **PASS**.
- `pnpm run build`: **PASS**, artefactos frontend compilados con `VITE_DHOLE_REALTIME_ENABLED=false`, `VITE_DHOLE_REALTIME_BATCH_APPROVED=false`.
- Archivo de evidencia del run: `rt-20261107-01-f4-vue-gate`, artifact ID `13604711151` (tsbuildinfo). Los logs del workflow son evidencia de resultados de tests, no se afirma que el artifact contenga un TRX.

## Limitaciones importantes para la aprobación formal

- Los 100 ciclos miden registro/desregistro de observadores y timers del manager puro, **no** 100 montajes Vue reales en navegador midiendo listeners/heap; ello queda pendiente.
- Las 30 reconexiones y 30 fallas iniciales son simulaciones deterministas de transporte, **no** 30 reinicios de host real, TLS/Traefik o escenarios multiusuario en `dhole-staging`.
- Las 2 vistas piloto usan REST verdadero cuando el frontend se ejecuta, pero el test puro usa snapshots simulados, por lo que no demuestra aún 100% de reconciliación con backend real en staging.
- Los componentes CRM/Pricing de prueba de F4 y Gateway F3 están feature-flagged OFF; no hay comprobación real conjunta end-to-end hasta F5/F9.
- El cambio de `develop` y `master` posterior a crear ramas requiere reconciliación segura sin force push ni sobreescritura. No se ha hecho merge.
- No hay deploy, PR, activación del Hub ni publicación de versión; F0–F3 todavía no tienen gates formales aprobados.

**Decisión:** gate F4 `BLOQUEADO / NO APROBADO`; F5 no iniciada.


## Evidencia de cierre de la implementación F4 en navegador real

- [GitHub Actions DholeWeb #42448772988](https://github.com/CustomCodeCR/DholeWeb/actions/runs/42448772988) — **SUCCESS** (SHA `0ac843361b51446967b2f8706a62cf137dce3785`), sin jobs/skips/fallos.
- Node 24: gestor **12/12 PASS**, incluyendo regresión de carrera: una invalidación que llega durante un GET antiguo se procesa con un segundo GET serializado; ninguna escritura es reintentada desde realtime.
- Regresiones de CRM/Pricing **91/91 PASS**: 71 CRM, 3 multi-POE, 17 multi-QUO.
- `pnpm --frozen-lockfile`, `pnpm run version:check` (DholeWeb candidato **1.13.0**), `pnpm run type-check` y `pnpm run build` — **todos PASS**, con flags realtime OFF.
- **Navegador Chromium de GitHub Actions (Playwright 1.56.1 instalado fuera del proyecto)**, con componentes reales Vue 3 montados mediante `createApp` y composable `useResourceRealtime` inyectado con transporte de pruebas:
  - **200 montajes y desmontajes reales** (dos lotes de 100); **0 observers** restantes, **0 crecimiento neto de listeners de `window/document`**, **0 crecimiento de sockets**; un WebSocket lógico por pestaña.
  - 2 usuarios autorizados (A/B) en 3 pestañas (A1/A2/B1) y una cuarta pestaña C denegada HTTP **403** correctamente, sin entrega de datos a C. ACL de la prueba simulada mediante intercepción HTTP, NO Auth real.
  - CRM `crm.account` cambió de versión 1→2 en todas las vistas autorizadas mediante GET REST; una edición sucia mantuvo la versión 1, levantó conflicto y luego convergió a versión 2 después de liberar el editor.
  - Pricing `pricing.rate` cambió de versión 1→3 vía GET REST en 3 pestañas. El productor real Pricing aún no ha sido conectado al bridge; se simuló invalidación mínima, sin fingir evento durable real.
  - Pérdida y recuperación de red de una pestaña: al reconectar, cuenta CRM llegó a versión 5 por GET aun **sin** recepción del evento.
  - **218 lecturas REST, 0 escrituras por cliente realtime**, 0 errores de JS en consola inesperados.
  - Heap tras GC: baseline **7,032,045 B**, tras primer lote **8,621,770 B**, tras segundo lote **7,866,582 B**; diferencia segundo lote **−755,188 B**. No se observó crecimiento sostenido; no es prueba de carga real.
- Artefacto del workflow: `rt-20261107-01-f4-vue-gate` ID **13605140347**: resultados JSON del navegador y metadata de typecheck. Logs del run son la fuente de los contadores de tests.
- La ejecución anterior #42448616037 mostró los mismos resultados funcionales de browser pero falló únicamente por tratar como error inesperado la línea HTTP 403 del lector rechazado; se corrigió el filtro y el run final **SUCCESS** aprobó sin suprimir errores no esperados.

### Distinción obligatoria

**Implementación F4 y suite aislada: COMPLETAS / PASS. Gate formal global F4: NO APROBADO.** No existe evidencia de WSS real con Traefik y Auth, autorizaciones por scopes reales, aplicación de F3/CRM en staging, 100% de inventario F0, pruebas reales de dos usuarios en servidores ni aprobaciones previas de F0–F3. Ningún despliegue se realizó, ningún flag fue activado, ninguna rama final se modificó y F5 no puede iniciarse de acuerdo con el plan.
