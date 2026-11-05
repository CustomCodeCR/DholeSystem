# Release candidato Dhole 1.2.0 — correos de tarifas

Fecha: 2026-11-05.

- DholeAIService PR #4: lotes de hasta 32, 4 slots concurrentes, timeout total de 900 s y por proveedor de 600 s.
- DholeDataExtractionService PR #23: lotes de hasta 100, 4 slots y reconciliación de solicitudes AI en una sola consulta.
- Compatibilidad: Redis Streams, Outbox/Inbox, PostgreSQL SKIP LOCKED e identificadores por correo conservados.
- Requisitos de aceptación: CI verde en ambos servicios, pruebas en staging, verificación del backlog real, manifiesto con versiones de todos los componentes comprobadas, integración coordinada a master solo con aprobación.
- No autoriza ni realiza despliegues a producción.
