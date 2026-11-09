# Dhole NotificationsHub — sincronización de ramas y estado del piloto

**Fecha:** 2026-11-09  
**Rama del batch:** `feature/rt-notificationshub-20261109-01`  
**Release ID:** `rt-20261107-01`  
**Versión global candidata:** `1.14.0`  
**Repositorios:** 16 (se excluye `CustomCodeFramework`).

## Resultado Git

Las 16 ramas candidatas se sincronizaron incorporando los commits de las ramas actuales `develop` y `master` en cada repositorio. En las 16 comparaciones realizadas después de la sincronización, `behind_by=0` respecto a ambas bases. **Esto no es un merge a las ramas destino**: todavía no se ha modificado `develop`, `master` ni `main`.

| Componente | Versión candidata |
|---|---|
| DholeSystem | 1.14.0 |
| DholeApiGateway | 1.5.0 |
| DholeAuthService | 1.4.0 |
| DholeWeb | 1.14.0 |
| DholeConfigService | 1.4.0 |
| DholeAuditLogsService | 1.4.0 |
| DholeDataExtractionService | 1.5.0 |
| DholePricingService | 1.7.0 |
| DholeAIService | 1.5.0 |
| DholeStorageService | 1.4.0 |
| DholeReportsService | 1.6.0 |
| DholeNotificationsService | 1.4.0 |
| DholeContentService | 1.4.0 |
| DholeAgentService | 1.4.0 |
| DholeDynamicsConnectorService | 1.4.0 |
| DholeCRMService | 1.6.0 |

## Trabajo A — candidato, no validado integralmente

- Reutilizar `NotificationsHub` existente en `DholeNotificationsService`, `/api/notifications/hub` y su ticket corto; preservar `notificationReceived`.
- Añadir `SubscribeResource`, `UnsubscribeResource`, `resourceChanged`, revisión REST de permisos y retransmisión de invalidaciones sin datos comerciales.
- Retirar los cinco archivos C# exclusivos del Hub universal duplicado en Gateway; mantener el proxy WebSocket.
- Adaptar `DholeWeb` a una conexión compartida; restaurar flags Vite de compilación tras sincronizar con master.
- Mantener Outbox/REST de los productores y recuperar el override de Notifications en Docker Compose. Todas las flags siguen por defecto apagadas.
- Metadatos SemVer de los 16 componentes en `version.json` y `CHANGELOG.md`; `release-manifest.json` y catálogo Gateway alineados con la versión candidata `1.14.0`.

## Evidencia de compilación

- **Notifications:** PASS en GitHub Actions run `42629920121`, después de corregir la colisión del descarte `out _` en el callback Redis.
- **Gateway:** PASS en GitHub Actions run `42630086579`, después de retirar los archivos C# del Hub duplicado.
- **Web:** FAIL en GitHub Actions run `42629475067`: type-check detectó 279 diagnósticos TypeScript, mayormente colisiones tras reconciliar grandes divergencias en pantallas de Pricing, Marketing y componentes compartidos. **El frontend no está listo para staging**.

## Pendientes antes de ejecutar B, C y D

1. Resolver sin perder hotfixes los errores de compilación Web sobre la rama ya sincronizada (no copiar masivamente código antiguo).
2. Revisar el contrato final de los productores, pruebas de compilación y reemplazar las pruebas Gateway antiguas que referencian el Hub retirado.
3. Retirar del release los workflows temporales de sincronización; congelar los SHA una vez que el código compile.
4. Preparar y ejecutar el workflow del piloto **exclusivo para staging**, preservando volúmenes e imágenes de rollback; sin exigir la auditoría exhaustiva F6–F8 antes del primer despliegue.
5. Auditar ACL, tickets WSS, eventos CRM/Pricing, reconciliación REST, reconexión y respaldos **después** del staging.
6. Solo tras resolver fallos críticos, aprobar CI del release y abrir/integrar PR coordinados a `develop`; después preparar `master` con autorización expresa de producción y rollback verificado.

**Estado final en este documento:** 16/16 ramas sincronizadas; compilación parcial; staging **NO desplegado**; PR/merges a `develop` y `master` **NO realizados**; producción **NO activada**.
