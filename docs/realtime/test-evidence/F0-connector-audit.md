# Evidencia F0 — GitHub / rama intermedia

Fecha: 2026-11-07. Release: `rt-20261107-01`.

| Comprobación | Resultado |
|---|---|
| GitHub get_repo x16 | 16 accesibles, 16 permiso push, 0 archivados |
| GitHub search_branches | develop/master presentes en 16; main default CRM/System |
| GitHub fetch_commit + compare_commits | SHAs develop/master obtenidos para 16; todas comparaciones `diverged`; detalle en release-manifest.yaml |
| Búsqueda de la rama exacta antes de crearla | 16/16 sin coincidencia |
| GitHub create_branch | 16/16 creadas desde SHA exacto de develop |
| Ficheros version.json | 16/16 leídos; ecosistema heterogéneo |
| Muestra de código | CRM Program y FollowupEndpoints, Web package, README System/Content/Dynamics; no inventario completo |
| Compilación/tests unitarios/integración | **NO_EJECUTADO** |
| Mediciones p95/p99/E2E/C01–C14 | **NO_EJECUTADO** |
| Auditoría WSS/Traefik/Redis en servidores | **NO_VERIFICADO** |
| F0 gate | **RECHAZADO** |

El entorno de archivos auxiliar no dispone de resolución DNS a github.com para `git ls-remote`; la inspección remota usó la conexión oficial a GitHub, no un checkout local. Esta limitación NO equivale a falla de CI ni a ejecución de pruebas. Prohibido declarar CIs, branches protegidas, ambiente de staging o métricas como validados.
