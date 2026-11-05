# Dhole — recuperación de la cola de correos tarifarios (release 1.2.0)

Fecha: 2026-11-05. Estado: candidato, no desplegado.

## Diagnóstico observado
- La interfaz mostraba 148 correos y hasta 26 en proceso por página, incluyendo algunos recibidos en octubre.
- Última ejecución exitosa publicada para DholeAIService (master): 2026-10-14.
- Última ejecución exitosa publicada para DholeDataExtractionService (master): 2026-11-02.
- `deploy/docker-compose.services.yml` **incluye** `/opt/dhole/docker-compose.services.yml`. Las definiciones base de `ai-workers` y `dataextraction-workers` pertenecen a ese archivo externo del servidor. No es correcto concluir que los servicios estén ausentes solo porque no aparezcan en el override de GitHub.

## Comprobaciones de producción, solo lectura
Ejecutar en el runner/servidor autorizado; no reiniciar contenedores ni reencolar trabajos antes de validar.

```bash
docker ps --filter 'label=com.docker.compose.project=dhole' \
  --format 'table {{.Names}}\t{{.Status}}\t{{.Image}}' \
  | grep -E 'NAMES|ai-|dataextraction-|pricing-|postgres|redis'
docker stats --no-stream $(docker ps -q --filter 'label=com.docker.compose.project=dhole' \
  --filter 'label=com.docker.compose.service=ai-workers')
docker compose --env-file /opt/dhole/.env -f /opt/dhole/docker-compose.services.yml \
  -p dhole config --services | grep -E 'ai-(api|workers)|dataextraction-(api|workers)'
```

## Validaciones del flujo
1. Verificar que AI y DataExtraction usan el mismo Redis Streams (stream, consumer group, ACK y pending).
2. Verificar en los logs **sin compartir payloads**: Dispatcher activo, trabajo reclamado, heartbeat, timeout, resultado en outbox y ACK de completion.
3. Consultar health checks: conteos `aged_pending`, `oldest_pending_age_minutes`, `completed_last_hour`, fallos de inbox/outbox, proveedor activo.
4. Contrastar estados entre `EmailExtractionJobs` y `AiEmailAnalysisJobs` por `EmailExtractionJobId` y `RequestId` sin exponer correos, asuntos ni secretos.
5. Priorizar extracción determinística completa de XLS(X), CSV, PDF y cuerpo HTML/texto; enviar a IA solo los casos estructuralmente complejos o incompletos.
6. No reemplazar una matriz completa por un resultado IA con menos filas; conservar e incluir advertencia si debe revisarse.

## Estrategia de procesamiento
- DataExtraction: hasta 100 jobs por despacho, cuatro slots con DbContext propio y `FOR UPDATE SKIP LOCKED`.
- AI: hasta 32 jobs por despacho, cuatro slots de análisis independientes. `MaxConcurrentJobs` limita la presión contra Ollama; ajustarlo solo según CPU/RAM/VRAM observadas.
- Timeout por ejecución 900 s; por intento de proveedor 600 s.
- Si un correo lleva más de 30 min pendiente, health se degrada aunque no supere el umbral de cantidad.
- Recovery DataExtraction reencola solo trabajos sin solicitud IA activa; nunca resetea un análisis legítimo en progreso.
- Outbox/Inbox y claves idempotentes deben impedir duplicados.

## Criterios para validar staging y luego producción
- Ambos workflows CI y pruebas de regresión de lote verdes, sin nuevos errores.
- Procesar al menos 30 correos de prueba con mezclas de CSV/XLSX/PDF/HTML en paralelo.
- Confirmar que el atraso se reduce, que los estados pasan a Pricing o revisión y que no se duplican importaciones.
- Confirmar memoria y latencia de Ollama bajo carga y tasas de fallo/reintento.
- Verificar versión de todos los componentes, changelog y manifiesto global.
- Integrar primero a `develop`, validar staging, y solo después desplegar a producción con autorización expresa.

**No reencolar manualmente todas las filas `Processing` con un UPDATE masivo.** Eso produciría ejecuciones duplicadas o descartaría resultados válidos que aún están en vuelo.
