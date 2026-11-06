# Changelog

## [1.3.1] - 2026-11-05

- Unifica versión global Dhole 1.3.1 y manifiesto de los 16 componentes SemVer.
- Corrige job skipped de producción, activa deploy por push a master conservando preflights de volúmenes y disponibilidad del host.
- Respeta ramas intermedias, CI y staging previo a producción.

## [1.3.0] - 2026-11-05

- Release coordinado de DholeAIService y DholeDataExtractionService para procesar correos tarifarios por lotes.
- Bumps individuales de 1.2.0 a 1.3.0 y manifiesto global 1.3.0; componentes no modificados conservan 1.2.0.
- Verificación obligatoria de Semantic Versioning por componente en el release.
- No se autoriza producción sin pruebas de staging.

## [1.2.0] - 2026-11-05

- Incorporates universal Dhole SemVer policy with GitHub Actions checks.
- Synchronizes service assembly metadata with the ecosystem version.
- Adds permanent Codex instructions and coordinated release requirements.
