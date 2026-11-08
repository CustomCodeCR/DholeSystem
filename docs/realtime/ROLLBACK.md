# Rollback y política de flags — Release rt-20261107-01

Estado actual: **F0/BLOQUEADA, sin cambios runtime**. Los únicos cambios de esta tarea están confinados a ramas intermedias. No existe todavía feature flag nuevo, migración ni release desplegada que deba revertirse.

## Invariantes

- Hasta F9: sin merge a `develop` ni despliegue staging. Hasta F10: sin merge a `master` ni producción; requiere autorización explícita.
- Ninguna función realtime se habilitará durante despliegue incompleto. REST permanece fuente autoritativa.
- F9/F10: manifest con SHAs congelados, versiones y compatibilidad N/N-1; flags inicialmente OFF; rollback de flags prioritario, luego imágenes versionadas y migraciones solo reversibles verificadas.
- Si un repo falla durante batch, detener promoción; no activar flags, conservar logs y seguir runbook de rollback coordinado; evitar inconsistencias inter-servicio.
- No eliminar ramas intermedias ni resetear targets sin decisión explícita. Nunca force push.

## Evidencia

F0: no hay test operativo de rollback; `NO_EJECUTADO`. Plan de rollback de infraestructura y flags detallado y probado: pendiente de F7/F9.
