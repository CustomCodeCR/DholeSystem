# F3 — Traefik HTTPS/WSS sin configuración manual de QA

**Release:** rt-20261107-01  
**Fecha:** 2026-11-08  
**Rama:** `feature/dhole-realtime-universal-rt-20261107-01`  
**Ejecutado:** [GitHub Actions #42538238853](https://github.com/CustomCodeCR/DholeApiGateway/actions/runs/42538238853)  
**SHA probado:** `09fc6435e4df93bce05fc5a4c4c3de6a375f1a6b`  
**Estado:** CI aislada PASS; F3 staging formal NO APROBADO.

## Qué se verificó

- Proyecto .NET del Gateway compilado, tests previos de seguridad y migración PostgreSQL validados en el workflow.
- Traefik Docker con certificado TLS temporal válido para localhost y Gateway Kestrel por HTTP interno.
- Negociación HTTPS de `/hubs/realtime/negotiate` y upgrade WebSocket `wss://` usando ticket de un solo uso.
- `Subscribe("crm.account", guid)` permitido para dos JWT efímeros autorizados, denegado para otro JWT válido.
- Revalidación de permiso a través de un servidor propietario REST que responde 200 o 403 según token.
- Sin secrets QA manuales, SSH, datos de negocio reales ni despliegue.

## Qué NO se verificó

- WSS a través del Traefik y la cadena TLS de `dhole-staging`.
- Autorización real CRM, Pricing y otros recursos con identidades efectivas.
- Revocaciones reales de Auth, flujos end-to-end comerciales y los 14 escenarios F7.
- Redis AOF/backup/restauración real de staging.

Esta evidencia mejora la prueba F3 sin atribuirle el alcance de una certificación de staging ni autorizar F9/F10.
