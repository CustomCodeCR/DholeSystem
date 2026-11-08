# Dhole Realtime Universal — Progress

Plan **2.1.0**, release **rt-20261107-01**. No habilitar funcionalidades ni publicar partes del batch.

| Fase | Estado | Gate | Observación |
|---|---|---|---|
| F0 | BLOQUEADA | RECHAZADO | 16 ramas intermedias creadas; endpoints y ambiente no verificados completamente |
| F1 | PENDIENTE | NO EVALUADO | Prohibido iniciar hasta F0 aprobado |
| F2 | PENDIENTE | NO EVALUADO | Contratos y durabilidad |
| F3 | PENDIENTE | NO EVALUADO | Gateway/Hub y grupos |
| F4 | PENDIENTE | NO EVALUADO | Frontend + fallback |
| F5 | PENDIENTE | NO EVALUADO | Piloto vertical |
| F6.01–F6.13 | PENDIENTE | NO EVALUADO | 0/13 servicios aprobados |
| F7 | PENDIENTE | NO EVALUADO | 0/14 casos ejecutados |
| F8 | PENDIENTE | NO EVALUADO | Enforcement servicios futuros |
| F9 | PENDIENTE | NO EVALUADO | Prohibido merge a develop |
| F10 | PENDIENTE | NO EVALUADO | Requiere autorización expresa master/producción |

## Evidencia F0 (2026-11-07)

- 16/16 repositorios accesibles con permiso push; 16 ramas intermedias nuevas desde el SHA exacto de develop.
- 16/16 comparaciones develop...master diverged; véase release-manifest.yaml para SHA y conteos.
- Ningún push, merge o PR hacia develop/master/main. Ningún despliegue.
- VERSIONADO: baselines inspeccionados en 16 version.json; DholeSystem sube 1.12.3 -> 1.12.4 solo en su intermedia por cambios documentales, con CHANGELOG; la versión global del batch 1.13.0 está PROPUESTA y no aplicada a servicios.
- Código inspeccionado parcialmente; CRM README está desactualizado frente a código de endpoints.
- tests de compilación, integración, staging, infraestructura y métricas: NO EJECUTADOS.
- Inventario 100% endpoints/jobs, ownership SRM/System, configuración viva de Redis/Traefik, instancias y permisos de recursos: BLOQUEADOS por falta de inspección/verificación completa.

## Gate F0

**RECHAZADO** hasta completar infraestructura, endpoints/jobs, matriz de permisos y baseline de carga medido. No iniciar F1. Próxima acción permitida: completar F0 en estas mismas ramas intermedias.
