# ADR 0001 — Arquitectura objetivo Realtime Universal (PROPUESTA)

- Release: `rt-20261107-01`
- Plan: 2.1.0
- Estado: **PROPUESTA / PENDIENTE F0**, NO ADOPTADA COMO INFRAESTRUCTURA PROBADA

## Contexto

Dhole mantiene REST como fuente de verdad para lecturas/escrituras y debe cubrir S01–S13, Gateway, Web y futuras mutaciones. La configuración concreta de Redis, proxy, autorizaciones y bases de datos no se ha auditado completamente. No se puede decidir el host del Hub sin esta evidencia.

## Diseño candidato sujeto a verificación

Escritura REST → commit BD con Outbox (o alternativa duradera documentada) → publisher con reintentos → Redis Streams → bridge e Inbox idempotente → SignalR central → invalidación mínima dirigida → GET REST autoritativo en Vue. WebSocket con fallback de transporte; si falla realtime, seguir por REST/polling de recursos visibles. Sin efectos de negocio provocados directamente por notificaciones del navegador.

## Invariantes de seguridad y consistencia

- Audiencia resuelta/autorizada en servidor por recurso y scope; no grupos elegidos libremente en Vue.
- EventId, schemaVersion, aggregateVersion y deduplicación; reentregas/out-of-order seguros.
- Resuscripción y reautenticación al reconectar; evitar escrituras duplicadas y no sobrescribir formularios con cambios.
- Feature flags OFF mientras exista un servicio fuera del batch; rollback inmediato a REST.
- Un Hub y un cliente lógico por instancia Vue, salvo ADR futura fundamentada.
- PR único por repo a develop solo F9 y PR único por repo a master solo F10 con autorización explícita.

## Decisiones pendientes de evidencia

Host exacto Hub/backplane, topología de streams, persistence/AOF, estrategia multidispositivo, claves de permisos y ownership SRM/System, estrategia de migraciones por motor, medición de carga y requerimientos de CORS/proxy. Estas decisiones deberán cerrarse antes de implementar F1/F2/F3.
