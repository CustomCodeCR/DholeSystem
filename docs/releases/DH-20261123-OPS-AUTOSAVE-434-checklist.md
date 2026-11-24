# DHOLE — Prioridad 1: Aperturas — estado técnico del release candidato DH-20261123-OPS-AUTOSAVE-434

**Corte de revisión:** 2026-11-23. **Target único:** `develop`; no tocar `master`, staging no probado, despliegue no autorizado. Este documento registra código preparado en ramas, **NO una implementación validada en staging**.

**PRs coordinados (candidatos para integración en `develop`):** Operations #51, Web #1067, Pricing #361, CRM #202, System #831.

## Matriz de los 18 puntos

| Nº | Requerimiento | Código y validación actual |
|---|---|---|
| 1 | IDTRA al aceptar QUO definitivamente | Pricing `pricing.quote.accepted.v1`; Operations consumidor y creación transaccional con CRM. CI de unidad/PG verde; integración Redis/CRM real **sin probar**. |
| 2 | Alternativa A/B aceptada | `quoteId` padre y `acceptedOptionId` derivado del vínculo server-side en Pricing, único snapshot de opción aceptada. CI de Pricing multiselección verde. |
| 3 | Evitar IDTRA duplicados | Unique index en `source_quote_id` para automática; advisory lock, Inbox, clave evento; prueba PostgreSQL de eventos repetidos y opción alternativa. |
| 4 | Pricing↔Operations Outbox/Inbox | Outbox transaccional Pricing y consumidores Inbox idempotentes Operations; pruebas de Redis entre procesos **pendientes**. |
| 5 | Heredar información comercial/logística | Snapshot JSON inmutable, ruta, carga, unidad kg/CBM, datos de proveedores y referencias. Verificar exhaustividad real con distintas modalidades en staging. |
| 6 | Servicios, costos, proveedores sin mutar QUO | Services `QUOTED`, tabla de costos por QuoteLink, múltiples equipos, referencias de documentos en snapshot; Dynamics/Storage cross-validation pendiente. |
| 7 | Continuar consecutivo histórico IDTRA | Reutiliza migración `OperationsReconcileIdtraSequence416` y `NextSequenceAsync`, sin `MAX+1` en runtime. CI PG verde; contra contador staging no validado. |
| 8 | Autoguardado real PostgreSQL | `operations_manual_opening_drafts`, GET/PUT/DELETE autenticados, optimistic version, cache local fallback y recuperador. CI verde. |
| 9 | Borradores incompletos sin equipo | Workspace independiente de Case, no asigna persona ni consume IDTRA al autoguardar. CI PG verde. |
| 10 | Validación modalidad/Incoterm/tipo | Reutiliza `OperationsOpeningDraftValidator` + completitud 416; matriz de todas las combinaciones requiere UAT. |
| 11 | 4 estados de campo | Backend completitud `CONFIRMADO`, `PENDIENTE_PERMITIDO`, `PENDIENTE_BLOQUEANTE`, `NO_APLICA` de 416; revalidación UAT pendiente. |
| 12 | FCA WHS y EXW recolecta | Reutiliza regla 416 y formularios de Apertura; comprobar casos FCA LCL/LTL y EXW reales en staging. |
| 13 | Peso real solo Origen en manual | Captura manual excluida también del payload de borrador y heredado Pricing separado; confirmar permisos de registro Origen en UAT. |
| 14 | kg/lb CBM/CFT y originales | Reutiliza normalizador decimal de Operations y origen guardando valor original; regresiones unitarias existentes, UAT pendiente. |
| 15 | Equipos y cantidades múltiples | `operations_case_equipment_lines` y datos de la apertura; prueba 2 × 40HC + 1 × 20GP = 3; edición manual requiere UAT. |
| 16 | Semáforo amarillo servicios adicionales | API idempotente `POST /cases/{id}/services`, tabla de alertas, respuesta GET, banner y editor DH en Web; CI verde. |
| 17 | Revisión Operations→Pricing | Outbox a stream Pricing, Inbox idempotente, bandeja Pricing, decisión autorizada, regreso y conciliación Operations; integración de tres servicios Redis y notificación funcional UAT pendiente. |
| 18 | Transferencia automática a Origen | Tras 2 aprobaciones crea Origin stage, Outbox, pool por carga y worker para recuperar asignaciones; PG pruebas CI verde. |

## Responsabilidades por servicio

- **Operations 0.18.0→0.19.0:** dominio, migraciones 434/435/436, Inbox/Outbox, validación, alertas, revisiones, IDTRA, pool, auditoría y estado realtime.
- **Pricing 1.27.1→1.28.0:** aceptación comercial definitiva, grupo A/B, snapshot, bandeja de revisiones y decisiones.
- **CRM 1.43.1→1.44.0:** contrato seguro `GET /api/internal/crm/operations/accounts/{accountId}` y lector Auth real sin crear cuentas.
- **Web/System 1.120.11→1.122.0:** UI DH, autoguardado, alertas, Pricing review y manifiesto de 17 componentes.
- **Auth, Notifications, Storage y AuditLogs:** **no hubo cambio de código** en estas ramas; se usan contratos/scopes/Outbox/auditoría existentes. No declarar validado el circuito real de avisos/Storage/auditoría o crear permisos nominales automáticamente.

## Validaciones antes de dar por completadas las pruebas en staging

1. **Pricing CI RESUELTO:** se alineó el snapshot EF Core con el modelo vigente y se corrigió el nombre de la clave primaria en la nueva tabla de revisiones. `Validate Average Import Recovery`, pruebas .NET, multiselección y política de versiones en verde. No se añadió una migración de borrado de tablas existentes.
2. **Entorno por configurar:** `Crm:OperationsAcceptance:BaseAddress`, `Crm:OperationsAcceptance:InternalServiceKey`, `OperationsIntegration:ReaderUserId`, `PricingAcceptance:CompanyId`, Redis Streams y API Gateway. Identidades de Auth se asignan manualmente tras comprobarlas, nunca por email hardcoded.
3. **E2E sin ejecutar:** aceptación por comercial o Pricing, subQUO A/B; duplicados/eventos reordenados; workflow QUO→CRM→IDTRA→2 validadores→Origen; conflicto de borrador, sin equipo; alerta/revisión/resolución; SignalR desconectado; auditoría; seguridad por roles, notas privadas y contactos. Validar en staging.
4. **Integración a `develop` pendiente en este corte:** requiere fusionar los cinco PR y comprobar su despliegue en staging. `master` y producción sin modificaciones.

## Pruebas verificadas

- Operations: workflow **Dhole Operations Build and Test** verde en el último código de integración antes del corte de documentación, incluye pruebas PostgreSQL de IDTRA, Inbox y asignación Origen.
- Web: **Dhole Web CI**, versionado y suites de UI verde tras incorporar interfaces DH de revisiones.
- CRM: dotnet CI/contratos y versionado verdes.
- Pricing: dotnet build/tests, Pricing rate multi-select, versionado y gate EF Core VERDES.
- System: manifiesto y políticas de versionamiento verdes.
- Staging: **NO EJECUTADO**. Master y despliegue: **NO AUTORIZADOS**.

**Regla para cierre:** ningún ítem debe marcarse completado al 100% hasta CI completo verde, UAT de integración y revisión en `develop`/staging. El alcance preparado requiere evaluación funcional de operaciones y Pricing.
