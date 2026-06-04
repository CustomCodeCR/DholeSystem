# Estrategia de Pruebas - Dhole Microservices

## 1. Objetivo

Este documento define la estrategia de pruebas para Dhole Microservices.

El objetivo es validar que cada microservicio funcione correctamente de forma individual y también dentro del ecosistema completo.

---

## 2. Tipos de pruebas

Se utilizarán los siguientes tipos de pruebas:

- Pruebas unitarias
- Pruebas de integración
- Pruebas de API
- Pruebas de base de datos
- Pruebas de eventos
- Pruebas de workers
- Pruebas de seguridad
- Pruebas end-to-end manuales o automatizadas

---

## 3. Pruebas unitarias

Las pruebas unitarias validan lógica aislada.

Deben cubrir:

- Reglas de negocio.
- Validaciones.
- Servicios de aplicación.
- Value objects.
- Cálculos.
- Mapeos importantes.
- Construcción de errores.
- Resultados esperados.

No deben depender de:

- Base de datos real.
- Redis real.
- Servicios externos.
- Archivos físicos.

---

## 4. Pruebas de integración

Las pruebas de integración validan interacción con infraestructura.

Deben cubrir:

- PostgreSQL.
- Redis.
- MongoDB si aplica.
- Repositorios.
- Migraciones.
- Outbox.
- Inbox.
- Storage local de prueba.

---

## 5. Pruebas de API

Las pruebas de API validan endpoints completos.

Deben cubrir:

- Códigos HTTP.
- Respuesta estándar.
- Validaciones de request.
- Permisos.
- Paginación.
- Filtros.
- Ordenamiento.
- Errores esperados.

Ejemplo:

```text
POST /api/v1/customers
- Debe crear cliente con request válido.
- Debe retornar 400 si falta legalName.
- Debe retornar 403 si falta crm.customers.create.
```

---

## 6. Pruebas de base de datos

Deben validar:

- Migraciones.
- Constraints.
- Índices.
- Relaciones.
- Soft delete si aplica.
- Fechas UTC.
- Campos auditables.
- OutboxMessages.
- InboxMessages.

---

## 7. Pruebas de eventos

Deben validar:

- Evento se guarda en Outbox.
- Evento contiene CorrelationId.
- Evento contiene EventType correcto.
- Evento contiene Payload mínimo.
- Evento se publica en Redis Streams.
- Evento se marca como publicado.
- Evento duplicado no se procesa dos veces.

---

## 8. Pruebas de workers

Los workers deben probarse como procesos independientes.

Workers principales:

```text
OutboxBackgroundService
RedisStreamsConsumerBackgroundService
ScheduledNotificationsWorker
AiTaskWorker
ProjectionWorker
```

Deben validar:

- Lectura de pendientes.
- Procesamiento exitoso.
- Reintentos.
- Manejo de errores.
- Idempotencia.
- Registro de logs.
- Actualización de estado.

---

## 9. Pruebas de seguridad

Deben validar:

- Endpoint sin token retorna 401.
- Endpoint sin scope retorna 403.
- Token expirado retorna 401.
- Refresh token revocado no funciona.
- Usuario bloqueado no puede operar.
- Permisos cacheados se invalidan correctamente.
- No se devuelven datos sensibles.
- No se registran tokens en logs.

---

## 10. Pruebas por servicio

### Auth

Debe cubrir:

- Login.
- Refresh token.
- Logout.
- Creación de usuario.
- Asignación de roles.
- Asignación de scopes.
- Validación de permisos.
- Bloqueo de usuario.
- Auditoría de accesos.

### Config

Debe cubrir:

- Lectura de configuración.
- Actualización de configuración.
- Validaciones.
- Auditoría de cambios.

### CRM

Debe cubrir:

- Clientes.
- Contactos.
- Seguimientos.
- Validaciones.
- Eventos CustomerCreated y CustomerUpdated.

### Pricing

Debe cubrir:

- Cotización express.
- Oferta formal.
- Costos.
- Margen.
- Aprobación.
- Rechazo.
- Generación de documento.

### Storage

Debe cubrir:

- Carga de archivos.
- Descarga.
- Metadata.
- Versiones.
- Eliminación lógica.
- Validación de permisos.

### Notifications

Debe cubrir:

- Plantillas.
- Solicitud de envío.
- Reintentos.
- Fallos.
- Adjuntos.

### Reports

Debe cubrir:

- Solicitud de reporte.
- Generación CSV.
- Generación Excel.
- Generación PDF.
- Almacenamiento del archivo generado.

### AuditLogs

Debe cubrir:

- Registro de evento.
- Consulta.
- Exportación.
- Inmutabilidad de registros.

### AI

Debe cubrir:

- Creación de tarea.
- Procesamiento.
- Resultado.
- Fallo.
- Consulta de resultado.

---

## 11. Datos de prueba

Los datos de prueba deben ser controlados.

No se deben usar datos reales de clientes en pruebas automatizadas.

Se deben crear seeds para pruebas cuando sea necesario.

Ejemplo:

```text
Test admin user
Test customer
Test quote
Test file
Test report
```

---

## 12. Criterio mínimo por HU

Cada historia de usuario debe tener al menos:

```text
[ ] Prueba de caso exitoso
[ ] Prueba de validación
[ ] Prueba de permisos si aplica
[ ] Prueba de error esperado
[ ] Prueba de evento si publica eventos
[ ] Prueba de worker si requiere procesamiento asíncrono
```

---

## 13. Criterio para cerrar una HU

Una HU se puede cerrar cuando:

```text
[ ] Código implementado
[ ] Migraciones aplicadas
[ ] Endpoints funcionando
[ ] Validaciones aplicadas
[ ] Permisos aplicados
[ ] Eventos implementados si aplica
[ ] Pruebas mínimas ejecutadas
[ ] Logs incluidos
[ ] README actualizado si aplica
```

---

## 14. Pruebas manuales

Las pruebas manuales deben usarse para validar flujos completos.

Ejemplos:

```text
Crear cliente -> Crear cotización -> Aprobar cotización -> Generar PDF -> Guardar archivo -> Auditar evento
```

```text
Solicitar reporte -> Generar Excel -> Guardar archivo -> Notificar resultado
```

---

## 15. Reglas finales

- No cerrar HU sin prueba mínima.
- No probar solo casos exitosos.
- No omitir pruebas de permisos.
- No omitir pruebas de eventos si hay Outbox.
- No usar datos reales sensibles.
- No depender de ejecución manual para todo.
