# F0 — Revalidación de ramas antes de solicitud F1

Plan **2.1.0** · release **rt-20261107-01** · comprobación 2026-11-07 (Costa Rica).

**Estado formal: F0 BLOQUEADA.** F1 no autorizada por gate de F0. Estas verificaciones son una continuación de la F0, no constituyen ejecución de F1 ni aprobación de implementación.

## Fuentes y método

Conector GitHub: `fetch_commit` de las tres referencias por repositorio (`develop`, `master`, `feature/dhole-realtime-universal-rt-20261107-01`), y `compare_commits` en los casos con drift con respecto al baseline. Cada SHA a continuación fue obtenido de la referencia remota en esta reevaluación, no inferido.

| Repositorio | develop actual | master actual | Rama intermedia actual | Diferencia contra baseline anterior |
|---|---|---|---|---|
| DholeCRMService | `9d92b831442e3cb5427246e5756ba7e49e487b5c` | `85059c0be40ed18e24e6332cd307716edf92c250` | `9d92b831442e3cb5427246e5756ba7e49e487b5c` | OK |
| DholePricingService | `3777ac1441ed2a1d14b4b59223945065f4259fff` | `a005de6b85bbfb9b5844672098f05b921f7507fd` | `b163fbc77291998ad182c9a7b809f329c1138bb0` | DRIFT develop +2 |
| DholeNotificationsService | `ab6b683ab802b3dca6201ab6b2b31b5868c1e105` | `7fedeff9b67f5d6ca0a1831b1908f11b2349d3f4` | `ab6b683ab802b3dca6201ab6b2b31b5868c1e105` | OK |
| DholeAuthService | `da0beaee40891a8fb045f6a3501fbb6dcc312d1c` | `936f00a697262aeafbe279234c0cadfed843630c` | `da0beaee40891a8fb045f6a3501fbb6dcc312d1c` | OK |
| DholeConfigService | `c8ff28a47dfd53f018d8a7faf00448b436c9d18d` | `7ffe4bfe4b4f7eba893d6df801d545d15bf3334e` | `c8ff28a47dfd53f018d8a7faf00448b436c9d18d` | OK |
| DholeAuditLogsService | `ac12000302f52b4792b681e38e1a493501432835` | `4dcfb7608627de8adce12ef4479f8fc45f39a433` | `ac12000302f52b4792b681e38e1a493501432835` | OK |
| DholeStorageService | `6c0937c5baac96c7684660309b73d08b348c79ee` | `5ddc37d1644f1eea988d564b1d6214c4cd7aa5f2` | `6c0937c5baac96c7684660309b73d08b348c79ee` | OK |
| DholeDataExtractionService | `8bd641a8a71a009b3427b554d2a369c53234eeff` | `21b6bbf748cb44fccc0210bcdb2d7700b4c5b33f` | `8bd641a8a71a009b3427b554d2a369c53234eeff` | OK |
| DholeReportsService | `50bdd2642ebf364550b6a980165bffa0a57d55a7` | `b586596631fb0bfc84b6787ef980a4c039f789bf` | `50bdd2642ebf364550b6a980165bffa0a57d55a7` | OK |
| DholeDynamicsConnectorService | `e09ba5db60f133875fdddccc3c8d2b6ef84b9925` | `2883e903b2b4b2ee7f02614b8648ff6ad7dfe6f6` | `e09ba5db60f133875fdddccc3c8d2b6ef84b9925` | OK |
| DholeAIService | `e4f39ef9537eb13fedac6d3bc8e9f8543d4c7cd8` | `3ace8314a33710418156bb41470c33b39ead097c` | `e4f39ef9537eb13fedac6d3bc8e9f8543d4c7cd8` | OK |
| DholeAgentService | `4618d954cc4aa2b8e2e30ea040f4cc92fa3ceea0` | `d9192c97fc07611825fbea14709ee41171e06cdd` | `4618d954cc4aa2b8e2e30ea040f4cc92fa3ceea0` | OK |
| DholeContentService | `adcc9ff99243d32eb29912e62a21db8a819d5011` | `3f6365730e4e86fb54621816d781693cb5d34878` | `adcc9ff99243d32eb29912e62a21db8a819d5011` | OK |
| DholeApiGateway | `ad57459a6fc9a102863144bacc25b9b55e1ba805` | `2f3e0d2b00a0afd63884ee7f6870fdec54c26d2a` | `ad57459a6fc9a102863144bacc25b9b55e1ba805` | OK |
| DholeWeb | `9bce4d835c95cc0c34868674578a9a9f190b1764` | `0e86a8e35a24e04c2864e4074c2bc747c44564ca` | `72fa663cc0c328d956bbe510eafe563d4dffe51b` | DRIFT develop +3, master +2 |
| DholeSystem | `9040bb00df39a95bc56cf68f3334d03ce9ac25d4` | `baeb014da206c0125f5863a49c576d58e6206409` | `2420dc99ccfa9826d5153f9f12ee2abb1b3ed1a7` | F0 docs |

## Divergencia nueva detectada

- `DholePricingService`: develop `b163fbc77291998ad182c9a7b809f329c1138bb0` → `3777ac1441ed2a1d14b4b59223945065f4259fff` (fast-forward; 2 commits). Archivos: CHANGELOG, Directory.Build.targets, docs/releases/DH-20261108-FCL-VISIBLE-DEDUP-036.json y version.json.
- `DholeWeb`: develop `72fa663cc0c328d956bbe510eafe563d4dffe51b` → `9bce4d835c95cc0c34868674578a9a9f190b1764` (fast-forward; 3 commits).
- `DholeWeb`: master `a74a87a0f9e68a017a44bc543ca4f7de16abb52d` → `0e86a8e35a24e04c2864e4074c2bc747c44564ca` (fast-forward; 2 commits).
- En DholeWeb, los cambios abarcan CHANGELOG, manifiesto de release, package.json/package-lock.json, `pricingRateDisplayDedup.ts`, prueba asociada y version.json.
- Estas modificaciones pertenecen a otra línea de trabajo y deben conservarse. No rebajar, borrar, force-push, resetear, ni hacer merge directo a targets.
- Se conservan `developBaselineSha` y `masterBaselineSha` anteriores en el manifiesto: son históricos y no se reemplazan por los HEAD actuales.
- Si hay que actualizar la intermedia más adelante, documentar el cambio de base y comprobar compatibilidad primero. Ningún rebase/merge ejecutado ahora.

## F0 y política de batch

- Ramas intermedias: **16/16 existentes** y verificadas.
- Target branches: **16/16 develop y 16/16 master existentes**; ningún target fue modificado por este trabajo. `main` no se modificó.
- Rama intermedia de `DholeSystem` sí contiene los documentos F0; las otras 15 permanecen en los SHAs F0 que les dieron origen.
- F0: sin validación de 100% mutaciones/jobs, SRM/System ownership, infraestructura real, línea base de carga y permisos, pruebas ejecutables: **gate rechazado**.
- F1: contratos compilables y 20 pruebas representativas **NO INICIADAS / NO EJECUTADAS**. No se han aplicado cambios de código F1.
- F9/F10: no abiertos, no PR, no merges, no staging ni producción.
- Próxima acción permitida: finalizar F0, revalidar bases cuando corresponda, registrar pruebas y obtener aprobación formal del gate. **No continuar a F1 mientras F0 permanezca bloqueada.**
