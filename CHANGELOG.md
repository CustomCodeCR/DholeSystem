# Changelog

## [1.3.9] - 2026-11-06

- Cierra extracciones de octubre y meses anteriores según la fecha de recepción y calendario de Costa Rica; solo noviembre queda activo.
- Conserva correo y adjuntos históricos, solicitudes Pricing ya enviadas y filas importadas.
- DataExtraction 1.3.2 a 1.3.3: archivado gradual, prevención de reencolado, API HTTP 410 para solicitudes obsoletas.
- AIService 1.3.5 a 1.3.6: cancela tareas antiguas pendientes y trata HTTP 410 como cierre esperado.
- DholeSystem 1.3.8 a 1.3.9. Release DH-20261106-HISTORICAL-CLOSE-011.


## [1.3.8] - 2026-11-06

- Release de optimización de extracción de correos: Qwen genera filas JSON compactas y evita 22 valores null por tarifa.
- DholeAIService 1.3.4 a 1.3.5; DholeSystem 1.3.7 a 1.3.8.
- Sin borrado de colas, sin incremento de paralelismo y sin interrupción de servicios persistentes.
- Se requiere staging previo a producción. DH-20261106-AI-THROUGHPUT-010.


## [1.3.7] - 2026-11-06

- Valida servicios de infraestructura sin reiniciarlos ni borrar sus volúmenes persistentes en producción.
- Registra fallos de salud con el nombre del servicio y diagnóstico, eliminando reinicios innecesarios de Ollama.
- Coordina el cambio de AIService 1.3.4 para agilizar Qwen y mejorar salida JSON.
- Release DH-20261106-AI-RELIABILITY-009.


## [1.3.6] - 2026-11-06

- Registra el release coordinado DH-20261106-MODIFICATION-CLOSURE-008 para evitar cierre automático de modificaciones.
- DholePricingService 1.2.5 → 1.2.6 y DholeWeb 1.3.2 → 1.3.3; incrementa DholeSystem a 1.3.6.
- Separa guardar de enviar al vendedor, bloquea cierre por SLA y revisión, y protege cancelaciones auditadas.
- Requiere validación en staging antes de master y no autoriza despliegue en producción.


## [1.3.4] - 2026-11-06

- Coordina control de saturación AI y extracción de tarifas desde correos sin pérdida de fuentes.
- DholeAIService 1.3.2 → 1.3.3: recuperación de duplicados de AI y menor concurrencia.
- DholeDataExtractionService 1.3.1 → 1.3.2: MarkItDown prioritario en documentos Office, backpressure y límite de reintentos.
- Requiere pruebas de staging antes de permitir integración a master y autorización explícita antes del despliegue de producción.


## [1.3.3] - 2026-11-05

- Release coordinado para corregir Otras pestañas y mostrar versiones SemVer de servicios en monitoreo.
- Registra DholeWeb 1.3.0 y DholeApiGateway 1.3.0; conserva las versiones de los otros 13 componentes.
- Diferencia versiones del proceso en ejecución de versiones declaradas en el manifiesto.

## [1.3.2] - 2026-11-05

- Release coordinado de recuperación de GitHub Actions para AI, Storage y Agent.
- Registra la versión global y el estado de las cuatro modificaciones del lote.

## [1.3.1] - 2026-11-05

- Define release global 1.3.1 y registra versiones SemVer independientes de 16 componentes.
- Activa el deploy de infraestructura de producción por push a master sin confirmación manual; staging continúa por develop.
- Conserva validaciones de volúmenes persistentes, host, red y servicios existentes.

## [1.3.0] - 2026-11-05

- Release coordinado de DholeAIService y DholeDataExtractionService para procesar correos tarifarios por lotes.
- Bumps individuales de 1.2.0 a 1.3.0 y manifiesto global 1.3.0; componentes no modificados conservan 1.2.0.
- Verificación obligatoria de Semantic Versioning por componente en el release.
- No se autoriza producción sin pruebas de staging.

## [1.2.0] - 2026-11-05

- Incorporates universal Dhole SemVer policy with GitHub Actions checks.
- Synchronizes service assembly metadata with the ecosystem version.
- Adds permanent Codex instructions and coordinated release requirements.
