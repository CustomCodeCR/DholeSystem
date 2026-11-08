# F1 — Contratos compartidos: evidencia CI real

Release: **rt-20261107-01** · plan v2.1.0. 

- Repo: `CustomCodeCR/CustomCodeFramework`.
- Rama: `feature/dhole-realtime-universal-rt-20261107-01`.
- SHA probado: `a81447dd00d004d6a32eb28001a379ee89ddb552`.
- Workflow: [Realtime F1 contracts — run 42443081145](https://github.com/CustomCodeCR/CustomCodeFramework/actions/runs/42443081145).
- Resultado: **success**, job `contract-tests`, id `128616245130`.
- Build: **0 errores** (advertencias CS1591 por comentarios XML faltantes, no errores).
- Pruebas reales: **42 PASSED / 0 FAILED / 0 SKIPPED**, .NET 8, ~183 ms de ejecución de test reportada por runner.
- Archivo de prueba: `tests/CustomCodeFramework.Messaging.Realtime.Tests/RealtimeContractTests.cs`.
- Artifact: `rt-20261107-01-f1-contract-tests` (id `13602900251`, contiene TRX).
- Versión candidata de paquete: `0.3.0` (anterior `0.2.0`), no publicada.

## Gate formal

F1 tiene contratos compilables y más de 20 pruebas en verde, pero sigue **EN_PROGRESO** porque F0 no ha aprobado su gate; faltan revisión de implementación compartida real, resolución de permisos concreta y adopción en microservicios. No declarar F1 COMPLETADA, ni iniciar F2, ni publicar NuGet. Sin modificaciones directas a `develop`, `master`, `main`.
