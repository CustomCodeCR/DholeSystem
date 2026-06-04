# Convenciones API - Dhole Microservices

## 1. Objetivo

Este documento define las convenciones para diseñar APIs en Dhole Microservices.

El objetivo es que todos los servicios expongan endpoints consistentes, predecibles y fáciles de consumir.

---

## 2. Versionado

Todas las APIs deben usar versionado.

Formato:

```text
/api/v1/{resource}
```

Ejemplos:

```text
/api/v1/users
/api/v1/customers
/api/v1/quotes
/api/v1/files
/api/v1/reports
```

---

## 3. Recursos

Los recursos deben escribirse en inglés y en plural.

Correcto:

```text
/users
/customers
/contacts
/quotes
/files
/reports
```

Incorrecto:

```text
/user
/customer
/clientes
/cotizaciones
```

---

## 4. Métodos HTTP

Uso estándar:

| Método | Uso                                       |
| ------ | ----------------------------------------- |
| GET    | Consultar                                 |
| POST   | Crear o ejecutar acción                   |
| PUT    | Actualizar recurso completo o principal   |
| PATCH  | Actualización parcial o cambio específico |
| DELETE | Eliminar o desactivar                     |

---

## 5. CRUD base

Formato recomendado:

```text
GET    /api/v1/resources
GET    /api/v1/resources/{id}
POST   /api/v1/resources
PUT    /api/v1/resources/{id}
DELETE /api/v1/resources/{id}
```

Ejemplo:

```text
GET    /api/v1/customers
GET    /api/v1/customers/{id}
POST   /api/v1/customers
PUT    /api/v1/customers/{id}
DELETE /api/v1/customers/{id}
```

---

## 6. Acciones de negocio

Cuando una operación no sea CRUD simple, se permite usar una acción.

Ejemplos:

```text
POST /api/v1/quotes/{id}/approve
POST /api/v1/quotes/{id}/reject
POST /api/v1/reports/{id}/generate
POST /api/v1/notifications/{id}/retry
POST /api/v1/files/{id}/restore
```

Las acciones deben estar en inglés.

---

## 7. Filtros

Los filtros deben enviarse como query params en consultas GET.

Ejemplo:

```text
GET /api/v1/customers?search=castro&isActive=true
GET /api/v1/quotes?status=approved&customerId=123
```

Los nombres de filtros deben usar camelCase.

Ejemplos:

```text
search
status
customerId
createdFrom
createdTo
isActive
```

---

## 8. Paginación

Todas las listas deben soportar paginación.

Query params estándar:

```text
page
pageSize
```

Ejemplo:

```text
GET /api/v1/customers?page=1&pageSize=25
```

Respuesta estándar:

```json
{
  "success": true,
  "data": {
    "items": [],
    "page": 1,
    "pageSize": 25,
    "totalItems": 100,
    "totalPages": 4
  },
  "errors": [],
  "correlationId": "00000000-0000-0000-0000-000000000000"
}
```

---

## 9. Ordenamiento

El ordenamiento debe usar:

```text
sortBy
sortDirection
```

Ejemplo:

```text
GET /api/v1/customers?sortBy=legalName&sortDirection=asc
```

Valores permitidos:

```text
asc
desc
```

---

## 10. Respuesta estándar

Toda respuesta debe usar el formato estándar definido en DholeBuildingBlocks.

Respuesta exitosa:

```json
{
  "success": true,
  "data": {},
  "errors": [],
  "correlationId": "00000000-0000-0000-0000-000000000000"
}
```

Respuesta con error:

```json
{
  "success": false,
  "data": null,
  "errors": [
    {
      "code": "crm.customers.not_found",
      "message": "Customer was not found."
    }
  ],
  "correlationId": "00000000-0000-0000-0000-000000000000"
}
```

---

## 11. Códigos HTTP

Uso recomendado:

| Código | Uso                          |
| ------ | ---------------------------- |
| 200    | Consulta o acción exitosa    |
| 201    | Recurso creado               |
| 204    | Acción exitosa sin contenido |
| 400    | Request inválido             |
| 401    | No autenticado               |
| 403    | Sin permisos                 |
| 404    | Recurso no encontrado        |
| 409    | Conflicto de negocio         |
| 422    | Validación de negocio        |
| 500    | Error interno                |

---

## 12. Errores

Los errores deben tener código estable.

Formato:

```text
service.resource.reason
```

Ejemplos:

```text
auth.users.invalid_credentials
auth.scopes.denied
crm.customers.not_found
pricing.quotes.already_approved
storage.files.invalid_type
reports.exports.failed
```

---

## 13. CorrelationId

Todas las peticiones deben tener CorrelationId.

Header recomendado:

```text
X-Correlation-Id
```

Si el cliente no lo envía, el API debe generarlo.

El CorrelationId debe propagarse a:

- Logs
- Eventos
- Outbox
- Inbox
- Workers
- Respuestas API

---

## 14. Autenticación

Los endpoints protegidos deben usar Bearer Token.

Header:

```text
Authorization: Bearer {token}
```

---

## 15. Permisos

Cada endpoint debe definir el scope requerido.

Ejemplos:

```text
GET    /api/v1/customers         -> crm.customers.read
POST   /api/v1/customers         -> crm.customers.create
PUT    /api/v1/customers/{id}    -> crm.customers.update
DELETE /api/v1/customers/{id}    -> crm.customers.delete
```

---

## 16. Fechas

Todas las fechas en API deben usar ISO 8601.

Ejemplo:

```text
2026-06-04T18:30:00Z
```

Las fechas deben manejarse internamente en UTC.

---

## 17. Archivos

Carga de archivos:

```text
POST /api/v1/files
```

Descarga de archivos:

```text
GET /api/v1/files/{id}/download
```

Metadata:

```text
GET /api/v1/files/{id}
```

---

## 18. Reportes

Solicitar generación:

```text
POST /api/v1/reports/{id}/generate
```

Consultar ejecución:

```text
GET /api/v1/report-requests/{id}
```

Descargar archivo generado:

```text
GET /api/v1/report-files/{id}/download
```

---

## 19. Notificaciones

Crear plantilla:

```text
POST /api/v1/notification-templates
```

Solicitar envío:

```text
POST /api/v1/notifications
```

Reintentar envío:

```text
POST /api/v1/notifications/{id}/retry
```

---

## 20. Reglas finales

- Usar inglés en endpoints.
- Usar plural en recursos.
- Usar versionado.
- Usar CorrelationId.
- Usar respuesta estándar.
- Usar scopes por endpoint.
- No devolver excepciones internas.
- No mezclar formatos de respuesta entre servicios.
