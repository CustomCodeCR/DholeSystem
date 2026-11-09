# Rollback y política de flags — Release rt-20261107-01

Estado actual: **F0–F7 SIN APROBACIÓN FORMAL, sin despliegue del batch**. Hay flags, migraciones y código candidatos solo en ramas intermedias; todos los flags del release permanecen OFF y no requieren revertirse en servidores porque no se han desplegado.

## Invariantes

- Hasta F9: sin merge a `develop` ni despliegue staging. Hasta F10: sin merge a `master` ni producción; requiere autorización explícita.
- Ninguna función realtime se habilitará durante despliegue incompleto. REST permanece fuente autoritativa.
- F9/F10: manifest con SHAs congelados, versiones y compatibilidad N/N-1; flags inicialmente OFF; rollback de flags prioritario, luego imágenes versionadas y migraciones solo reversibles verificadas.
- Si un repo falla durante batch, detener promoción; no activar flags, conservar logs y seguir runbook de rollback coordinado; evitar inconsistencias inter-servicio.
- No eliminar ramas intermedias ni resetear targets sin decisión explícita. Nunca force push.

## Evidencia

F0: no hay test operativo de rollback; `NO_EJECUTADO`. Plan de rollback de infraestructura y flags detallado y probado: pendiente de F7/F9.

## Riesgo RDB→AOF detectado por el batch

No restaurar el mismo volumen Redis reiniciando simplemente con `appendonly=yes`.
El ensayo [#42507114616](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42507114616) perdió entradas RDB existentes. La ruta de migración ensayada
[#42507199248](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42507199248)
usa `CONFIG SET appendonly yes` sobre el proceso activo, espera el rewrite, respalda
y luego recrea con Compose. Ver `F6-REDIS-AOF-STAGING-MIGRATION.md`.
La conversión real y su rollback no están aprobados ni ejecutados en staging.
