# Dhole 1.3.0 · procesamiento de correos tarifarios

DholeAIService 1.2.0 → 1.3.0: lotes acotados de IA, tiempo máximo, reintentos, recuperación de leases, métricas de cola e idempotencia.

DholeDataExtractionService 1.2.0 → 1.3.0: lotes de extracción, recuperación segura de solicitudes IA, normalización de PDFs y correos, prevención de duplicados, compatibilidad con precios, puertos y fechas.

DholeSystem 1.2.0 → 1.3.0: manifiesto central con versiones independientes; los restantes servicios permanecen en 1.2.0 sin cambio de binarios.

## Pruebas certificadas para los candidatos a master y develop
- AI: 31/31 pruebas, batch regresiones y SemVer exitosos.
- DataExtraction: 262/262 pruebas, pruebas de PDF y SemVer exitosos.

## Puertas de release
- Integrar candidatos coordinadamente a develop.
- Verificar staging y reducción real del backlog, Redis, PostgreSQL y proveedores IA.
- Promover a master solamente después de estas verificaciones.
- Ningún despliegue de producción está autorizado por este manifiesto.
