# Modelo de Permisos y Scopes - Dhole Microservices

## 1. Objetivo

Este documento define el modelo de permisos para Dhole Microservices.

El sistema manejará permisos de forma granular mediante scopes.

Los roles no serán permisos en sí mismos. Los roles serán agrupadores de scopes.

---

## 2. Principio base

La autorización se basa en scopes.

Un usuario puede ejecutar una acción únicamente si tiene el scope requerido.

Ejemplo:

```text
pricing.quotes.approve
```

Este scope permite aprobar cotizaciones.

---

## 3. Formato de scopes

Formato estándar:

```text
service.resource.action
```

Ejemplo:

```text
crm.customers.create
```

Partes:

| Parte     | Significado      |
| --------- | ---------------- |
| crm       | Servicio         |
| customers | Recurso o módulo |
| create    | Acción           |

---

## 4. Acciones estándar

Acciones base:

```text
read
create
update
delete
approve
reject
assign
download
upload
generate
send
retry
export
import
execute
cancel
lock
unlock
revoke
```

No se deben crear acciones duplicadas con el mismo significado.

Ejemplo incorrecto:

```text
view
list
get
read
```

Se debe usar:

```text
read
```

---

## 5. Roles seed

Solo se crearán por seed los siguientes roles:

```text
Administrador
Superusuario
```

El resto de roles serán creados desde el sistema.

---

## 6. Administrador

El rol Administrador representa un usuario con acceso administrativo funcional.

Puede administrar usuarios, roles, configuración y operación general según los scopes asignados.

---

## 7. Superusuario

El rol Superusuario representa un usuario con acceso técnico o máximo nivel operativo.

Debe usarse con cuidado.

Su uso debe ser auditado.

---

## 8. Roles dinámicos

Los roles adicionales deben ser creados desde el sistema.

Ejemplos:

```text
Pricing Manager
CRM Agent
Reports Viewer
Storage Manager
```

Cada rol puede tener uno o varios scopes.

---

## 9. Permisos efectivos

Los permisos efectivos de un usuario se calculan por:

```text
Usuario -> Roles -> Scopes
```

Un usuario puede tener múltiples roles.

Si cualquiera de sus roles contiene el scope requerido, el usuario tiene permiso.

---

## 10. Cache de permisos

Los permisos efectivos pueden guardarse en Redis.

Key recomendada:

```text
dhole:auth:user-permissions:{userId}
```

Debe invalidarse cuando:

- Cambian los roles del usuario.
- Cambian los scopes de un rol.
- Se desactiva un usuario.
- Se bloquea un usuario.
- Se elimina un rol.
- Se elimina un scope.

---

## 11. Scopes de Auth

```text
auth.users.read
auth.users.create
auth.users.update
auth.users.delete
auth.users.lock
auth.users.unlock

auth.roles.read
auth.roles.create
auth.roles.update
auth.roles.delete
auth.roles.assign

auth.scopes.read
auth.scopes.create
auth.scopes.update
auth.scopes.delete
auth.scopes.assign

auth.sessions.read
auth.sessions.revoke
```

---

## 12. Scopes de Config

```text
config.settings.read
config.settings.create
config.settings.update
config.settings.delete

config.modules.read
config.modules.update
```

---

## 13. Scopes de CRM

```text
crm.customers.read
crm.customers.create
crm.customers.update
crm.customers.delete

crm.contacts.read
crm.contacts.create
crm.contacts.update
crm.contacts.delete

crm.followups.read
crm.followups.create
crm.followups.update
crm.followups.delete
```

---

## 14. Scopes de Pricing

```text
pricing.quotes.read
pricing.quotes.create
pricing.quotes.update
pricing.quotes.delete
pricing.quotes.approve
pricing.quotes.reject

pricing.offers.read
pricing.offers.create
pricing.offers.generate
pricing.offers.send

pricing.rates.read
pricing.rates.create
pricing.rates.update
pricing.rates.delete
```

---

## 15. Scopes de Storage

```text
storage.files.read
storage.files.upload
storage.files.download
storage.files.delete
storage.files.update

storage.providers.read
storage.providers.create
storage.providers.update
storage.providers.delete
```

---

## 16. Scopes de Notifications

```text
notifications.templates.read
notifications.templates.create
notifications.templates.update
notifications.templates.delete

notifications.messages.read
notifications.messages.send
notifications.messages.retry

notifications.settings.read
notifications.settings.update
```

---

## 17. Scopes de AuditLogs

```text
auditlogs.events.read
auditlogs.events.export
auditlogs.details.read
```

AuditLogs normalmente no debe permitir update ni delete sobre eventos históricos.

---

## 18. Scopes de Reports

```text
reports.definitions.read
reports.definitions.create
reports.definitions.update
reports.definitions.delete

reports.requests.read
reports.requests.create
reports.requests.execute

reports.exports.read
reports.exports.generate
reports.exports.download

reports.schedules.read
reports.schedules.create
reports.schedules.update
reports.schedules.delete
```

---

## 19. Scopes de AI

```text
ai.tasks.read
ai.tasks.create
ai.tasks.execute
ai.tasks.cancel

ai.results.read
ai.results.delete

ai.settings.read
ai.settings.update
```

---

## 20. Validación por endpoint

Cada endpoint debe declarar el scope requerido.

Ejemplo:

```text
POST /api/v1/customers
Scope requerido: crm.customers.create
```

```text
POST /api/v1/quotes/{id}/approve
Scope requerido: pricing.quotes.approve
```

---

## 21. Auditoría de permisos

Se debe auditar:

- Creación de roles.
- Actualización de roles.
- Eliminación de roles.
- Asignación de scopes.
- Remoción de scopes.
- Asignación de roles a usuarios.
- Remoción de roles a usuarios.
- Acceso denegado por falta de scope.

---

## 22. Reglas finales

- Los permisos se validan por scope.
- Los roles no se queman en código.
- Solo Administrador y Superusuario son seed.
- Los demás roles se crean desde el sistema.
- Los scopes deben estar en inglés.
- Los scopes deben ser consistentes entre servicios.
- Los scopes deben ser auditables.
