# F5 — Piloto CRM: implementación candidata y evidencia

**Plan:** Dhole Realtime Universal v2.1.0 | **Release:** rt-20261107-01  
**Gate F5:** BLOQUEADO (F0–F4 no aprobadas y E2E no ejecutado).  
**Rama:** feature/dhole-realtime-universal-rt-20261107-01. Sin PR, merge, flags habilitados ni despliegues.

## Flujo único

A (autorizado) hace PATCH /api/crm/accounts/{id} con ExpectedVersion. El servidor valida permisos y versión. Mediante CrmAccountRealtimeCommit confirma modificación, historial y Outbox en **la misma transacción PostgreSQL**; únicamente después del commit el worker, si flags aprobados, publica en Redis Streams. El Bridge de Gateway comprueba de nuevo la ACL y emite una invalidación SignalR mínima. La segunda sesión autorizada de Vue consulta por GET REST y reconcilia, sin repetir mutaciones.

**Estado real por componente:**
- CRM PATCH/Outbox: código conectado, compilado y probado contra PostgreSQL real.
- Redis Streams: trabajador F2 duradero probado aisladamente con Redis real, incluido retry/DLQ.
- Gateway Hub/Bridge: 100 pruebas F3 aisladas; no hay entrega end-to-end desde el mismo PATCH.
- Vue: singleton, reconciliación/contingencia y 200 ciclos Chromium probados en F4 aislado; todavía no validado con Auth/CRM real en staging.
- Flags CRM: Features:UniversalRealtimeEnabled + Realtime:Outbox:Enabled + Realtime:BatchApproved + Realtime:ReleaseId exacto rt-20261107-01. Todos apagados en despliegue actual.
- Contrato: crm.account.updated.v1, version de la cuenta y audiencia crm:account:{guid}; payload sin datos personales.

## Test real (CI de la rama)

[GitHub Actions #42489760621](https://github.com/CustomCodeCR/DholeCRMService/actions/runs/42489760621), SHA de CRM probado 12ea9f72cb7aee930c7a6e5b4b82538eb618a492:

- Compilación de API CRM real y test project .NET10: 0 errores y 0 advertencias.
- 14/14 pruebas, 0 fallidas y 0 omitidas (PostgreSQL 17 + Redis 7).
- 20 actualizaciones de una cuenta real → 20 versiones y 20 eventos durables distintos, con 20 entradas de auditoría.
- Ruta PATCH autenticada real en TestServer: usuario A escribe; usuario B con scope read-all obtiene GET 200 y dato actualizado; usuario C sin acceso obtiene 403; PATCH stale devuelve 409 y no genera un segundo evento.
- Paquetes criptográficos vulnerables del test corregidos a la familia .NET10 10.0.13 sin desactivar alertas ni --warnaserror.
- Esta prueba HTTP **no equivale** a dos navegadores reales con SignalR.

## Baseline staging leído sin modificarlo

[GitHub Actions #42489552444](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42489552444): ejecutado en runner del host de staging, sin despliegue ni cambios de datos. Se observaron 27 servicios del proyecto de Compose y 5 componentes de infraestructura. Verificación positiva de que 127.0.0.1:18080 correspondía al Gateway de staging; 100/100 GET health HTTP 200, p95=2.606 ms y p99=3.397 ms. **No** es medición commit→UI, WSS/TLS público ni Auth real.

## Gate formal F5: NO APROBADO

| Requisito de aceptación | Resultado |
|---|---|
| F0–F4 aprobadas | NO |
| 20/20 actualizaciones visibles sin refresh entre dos navegadores | NO EJECUTADO |
| 0 filtraciones a terceros reales | PARCIAL; HTTP 403 en TestServer, no WSS staging |
| 0 dobles escrituras | PASS aislado (409/Outbox), no cadena completa |
| 5/5 cortes y reconciliación total | NO EJECUTADO en cadena completa |
| Rollback de flags con backend + navegador reales | NO EJECUTADO |
| p95<=2s y p99<=5s commit→UI | NO MEDIDO |

Próximo paso: completar el inventario F0 de endpoints/jobs y permisos, verificar proxy WSS/Auth/Redis AOF/backup en entorno autorizado, cerrar gates secuenciales F1–F4 y luego ejecutar el E2E completo F5. No promover este batch a develop/master ni iniciar migración masiva F6. Versiones CRM 1.4.0 y global 1.13.0 permanecen candidatas.
