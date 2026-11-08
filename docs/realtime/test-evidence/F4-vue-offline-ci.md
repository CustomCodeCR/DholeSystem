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
