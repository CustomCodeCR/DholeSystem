# Evidencia F2 — piloto CRM durable Redis/PostgreSQL (candidato NO liberado)

**Plan:** v2.1.0. **Batch:** `rt-20261107-01`.  
**Ramas finales:** sin cambios de este batch. **Gate formal F2:** `NO APROBADO`.

## Pipeline CRM 1000 operaciones + inbox/recovery

- [CI CRM run 42444887589](https://github.com/CustomCodeCR/DholeCRMService/actions/runs/42444887589)
- SHA probado: `5258689266e660f65d602c8d325bc7b3c54cd4ce`.
- Resultado: **SUCCESS**; build .NET 10 `0 warnings / 0 errors`.
- **8 PASSED, 0 FAILED, 0 SKIPPED**.
- Contiene 1000 operaciones PostgreSQL confirmadas, publicación de 1000 eventos, Inbox con 1000 efectos exactamente una vez, reentregas duplicadas sin segundo efecto, rollback de transacción, reintento tras Redis indisponible simulado, DLQ tras 5 intentos, replay pre-ACK, recuperación supervisada tras pérdida total de clave Redis y reclamación `XAUTOCLAIM` de PEL abandonada.
- Artifact TRX: `rt-20261107-01-f2-crm-durability` (id `13602109860`).

## Persistencia Redis AOF

- [CI DholeSystem run 42444816160](https://github.com/CustomCodeCR/DholeSystem/actions/runs/42444816160)
- SHA probado: `deb99f1d242be8381b814db1440b4fb2245ee895`.
- Resultado **SUCCESS**: AOF en staging Compose (rama intermedia solamente) verificado estáticamente; entrada Redis Streams visible tras eliminar/recrear un contenedor con mismo volumen temporal.
- **NO** prueba Redis en servidores reales ni RPO/RTO, backups, fallos de energía abruptos ni lag de consumidores.

## Ejecución final de la variante F2 con seguridad ampliada

- [CI CRM run 42444994037](https://github.com/CustomCodeCR/DholeCRMService/actions/runs/42444994037), SHA probado: `b28ae8278ea28b05624ec30021ada38ad3d8ca21`.
- Resultado **SUCCESS**: .NET 10 `0 warnings / 0 errors`, **10 PASSED / 0 FAILED / 0 SKIPPED** (MSTest).
- Incluye la suite anterior de 8 pruebas, más 2 casos de rechazo de campos PII y `schemaVersion` inválida sin insertar eventos en PostgreSQL.
- Archivo TRX: `rt-20261107-01-f2-crm-durability`, artifact ID `13603795163`.
- Este SHA fue comprobado **solo en rama intermedia**; no debe llamarse release, staging o producción.

## Bloqueos

- F0/F1 no tienen gates formales aprobados.
- Validar 100% mutaciones, scopes y ownership, infraestructura real de dhole-staging y producción, estrategia de purga/retención y alertas.
- El productor todavía no se integra a operaciones CRM REST reales; falta adaptador de contratos versionados compartidos sin publicar paquete prematuramente.
- La prueba XAUTOCLAIM y recovery es CI efímera, no dos instancias reales en staging.
- Ninguna promoción, no producción, no activación de flags.
