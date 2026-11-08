# F0 — Branch protections: visibilidad insuficiente

Release **rt-20261107-01** · Fecha local 2026-11-07.

Se intentó leer de forma no destructiva los endpoints oficiales de GitHub REST:

- `GET /repos/CustomCodeCR/DholeSystem/branches/develop/protection`
- `GET /repos/CustomCodeCR/CustomCodeFramework/branches/master/protection`

Ambos devolvieron **HTTP 403 Resource not accessible by integration**. No se puede afirmar que exista o no exista protección real. Esta limitación de permisos deja pendiente verificar las reglas efectivas y configurar required checks antes de F9/F10. **No se cambiaron reglas ni se abrió PR contra targets.** El script `scripts/realtime/verify-branch-policy.py` valida el manifiesto y rechaza targets prematuros en CI, pero no sustituye las reglas nativas de GitHub. Estado `NO_VERIFICADO`; no considerar el gate aprobado.
