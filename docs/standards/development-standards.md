# Seguridad Técnica - Dhole Microservices

## 1. Objetivo

Este documento define la estrategia de seguridad técnica para Dhole Microservices.

La seguridad estará centralizada en DholeAuthService y será aplicada mediante tokens, sesiones, roles dinámicos y scopes.

---

## 2. Principios de seguridad

El sistema debe seguir estos principios:

- Autenticación centralizada.
- Autorización granular por scopes.
- Roles dinámicos.
- Validación de acceso en cada servicio.
- Tokens con expiración.
- Refresh tokens controlados.
- Auditoría de acciones sensibles.
- Cache controlado de permisos.
- No exponer datos sensibles.
- No confiar en datos enviados desde el frontend.

---

## 3. Servicio responsable

DholeAuthService será responsable de:

- Usuarios
- Roles
- Scopes
- Asignación de roles
- Asignación de scopes
- Inicio de sesión
- Refresh tokens
- Sesiones
- Validación de tokens
- Cache de permisos
- Bloqueo de usuarios
- Auditoría de accesos

---

## 4. Autenticación

Flujo base:

```text
1. Usuario envía credenciales.
2. Auth valida usuario y contraseña.
3. Auth valida estado del usuario.
4. Auth genera access token.
5. Auth genera refresh token.
6. Auth registra sesión.
7. Auth devuelve tokens al cliente.
```

El access token debe ser de corta duración.

El refresh token debe ser de mayor duración, pero revocable.

---

## 5. Autorización

La autorización se manejará mediante scopes.

No se deben validar permisos únicamente por nombre de rol.

Los roles solo agrupan scopes.

Ejemplo:

```text
Rol: Pricing Manager

Scopes:
- pricing.quotes.read
- pricing.quotes.create
- pricing.quotes.update
- pricing.quotes.approve
```

---

## 6. Roles seed

Solo existirán dos roles creados por seed:

```text
Administrador
Superusuario
```

El resto de roles deben ser creados desde el sistema.

Esto permite que la empresa defina sus propios roles según su operación.

---

## 7. Access token

El access token debe contener únicamente información necesaria.

Claims recomendados:

```text
sub
email
name
sessionId
tenantId
roles
scopes
iat
exp
jti
```

No se debe incluir información sensible en el token.

No se debe incluir password, refresh token ni datos privados innecesarios.

---

## 8. Refresh token

El refresh token debe almacenarse de forma segura.

Debe registrar:

```text
Id
UserId
SessionId
TokenHash
CreatedAt
ExpiresAt
RevokedAt
CreatedByIp
RevokedByIp
ReplacedByTokenId
```

El refresh token no debe guardarse en texto plano.

Debe guardarse como hash.

---

## 9. Sesiones

Cada inicio de sesión debe crear una sesión.

La sesión debe registrar:

```text
Id
UserId
StartedAt
LastActivityAt
IpAddress
UserAgent
IsActive
ClosedAt
CloseReason
```

Las sesiones permiten:

- Cerrar sesión individual.
- Cerrar todas las sesiones.
- Auditar accesos.
- Invalidar tokens por sesión.

---

## 10. Cache de permisos

Los permisos efectivos del usuario pueden cachearse en Redis.

Key recomendada:

```text
dhole:auth:user-permissions:{userId}
```

La cache debe invalidarse cuando:

- Se asigna un rol al usuario.
- Se remueve un rol al usuario.
- Se asigna un scope a un rol.
- Se remueve un scope de un rol.
- Se desactiva un usuario.
- Se bloquea un usuario.

---

## 11. Validación en API Gateway

El API Gateway puede validar:

- Existencia del token.
- Firma del token.
- Expiración del token.
- CorrelationId.
- Rate limit básico.

Sin embargo, cada servicio debe seguir validando los scopes requeridos para sus operaciones.

No se debe depender únicamente del Gateway.

---

## 12. Validación en microservicios

Cada microservicio debe validar:

- Usuario autenticado.
- Scope requerido.
- Estado del usuario si aplica.
- Tenant si aplica.
- Propiedad o acceso al recurso si aplica.

Ejemplo:

```text
pricing.quotes.approve
```

Debe ser requerido para aprobar una cotización.

---

## 13. Contraseñas

Las contraseñas deben almacenarse usando hash seguro.

No se deben guardar contraseñas en texto plano.

Reglas mínimas:

- Longitud mínima configurable.
- Bloqueo después de intentos fallidos.
- No reutilizar contraseñas recientes si se implementa historial.
- Forzar cambio si el administrador resetea contraseña.

---

## 14. Bloqueo de usuarios

Un usuario puede ser bloqueado por:

- Intentos fallidos de inicio de sesión.
- Acción administrativa.
- Inactividad prolongada si se define.
- Evento de seguridad.

Campos sugeridos:

```text
IsLocked
LockedAt
LockedReason
FailedLoginAttempts
LastFailedLoginAt
```

---

## 15. Auditoría de seguridad

Se deben auditar eventos como:

- Login exitoso.
- Login fallido.
- Logout.
- Refresh token usado.
- Refresh token revocado.
- Usuario creado.
- Usuario actualizado.
- Rol creado.
- Scope asignado.
- Scope removido.
- Usuario bloqueado.
- Usuario desbloqueado.

Estos eventos deben enviarse a DholeAuditLogsService.

---

## 16. Datos sensibles

No se deben registrar en logs:

- Passwords
- Tokens
- Refresh tokens
- OTP
- Secret keys
- Connection strings
- Datos bancarios sensibles
- Archivos privados

Los errores enviados al cliente no deben revelar detalles internos.

---

## 17. CORS

CORS debe configurarse por ambiente.

No se debe usar wildcard en producción.

Incorrecto:

```text
*
```

Correcto:

```text
https://app.dhole.local
https://dhole.company.com
```

---

## 18. Rate limit

Se debe aplicar rate limit en endpoints sensibles:

- Login
- Refresh token
- Forgot password
- Reset password
- Descarga de archivos
- Generación de reportes
- Tareas de IA

---

## 19. Seguridad en archivos

DholeStorageService debe validar:

- Usuario autenticado.
- Scope requerido.
- Tipo de archivo permitido.
- Tamaño máximo.
- Relación lógica del archivo.
- Permiso de descarga.

Los archivos no deben ser expuestos directamente sin validación.

---

## 20. Seguridad en reportes

DholeReportsService debe validar:

- Scope para generar reporte.
- Scope para descargar reporte.
- Acceso a la información incluida.
- Parámetros permitidos.
- Tamaño máximo de consulta.

---

## 21. Seguridad en IA

DholeAiService debe validar:

- Scope para crear tarea IA.
- Scope para consultar resultados.
- Límites de uso.
- Datos permitidos para análisis.

No se deben enviar datos sensibles innecesarios al motor de IA.

---

## 22. Reglas finales

- Todo endpoint privado requiere autenticación.
- Toda acción crítica requiere scope.
- Los roles no se queman en código.
- Los permisos se validan por scope.
- Los tokens deben poder revocarse por sesión.
- Toda acción sensible debe auditarse.
