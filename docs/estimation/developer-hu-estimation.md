# Estimación Técnica por HU - Dhole Microservices

## 1. Objetivo

Este documento presenta la estimación técnica de desarrollo por historia de usuario y por fase.

Está dirigido a la planificación interna del desarrollo.

El objetivo es servir como guía para organizar trabajo, priorizar tareas, identificar dependencias y estimar carga real de implementación.

---

## 2. Ubicación del documento

Este documento debe guardarse en:

```text
docs/estimation/developer-hu-estimation.md
```

---

## 3. Supuestos técnicos

La estimación contempla:

```text
Backend
Frontend
Base de datos
Migraciones
Seeds
Pruebas
Permisos por scopes
Eventos
Workers
Integración
CI/CD
Servidor
Vault
Migración de datos
```

La documentación base no se carga a cada HU, porque se realiza antes del desarrollo.

Solo se contempla documentación adicional cuando sea necesaria por cambios, ajustes o decisiones nuevas.

---

## 4. Capacidad de trabajo

## 4.1 Solo una persona

```text
Capacidad nominal semanal: 40 horas
Capacidad efectiva semanal: 32 horas
```

La diferencia corresponde a:

```text
Reunión con gerente general
Levantamientos adicionales
Revisión funcional
Correcciones no planificadas
Coordinación
Despliegue
Validación
```

---

## 4.2 Persona líder + persona desarrolladora

```text
Persona líder: 28 horas efectivas semanales
Persona desarrolladora: 40 horas efectivas semanales
Total: 68 horas efectivas semanales
```

La persona desarrolladora se dedica principalmente a implementación.

La persona líder asume:

```text
Arquitectura
Revisión
Integración
Reuniones
Validación
Decisiones técnicas
Control de calidad
Bloqueos técnicos
```

---

## 5. Escala de complejidad

```text
XS = 4 a 6 horas
S  = 8 a 12 horas
M  = 16 a 24 horas
L  = 32 a 40 horas
XL = 48 a 64 horas
```

Se aplica un 15% adicional por:

```text
5% revisión/refactor
10% colchón general
```

---

# 6. Estimación por HU

| HU     | Nombre                                              | Fase           | Servicio      | Complejidad | Horas base | Horas con colchón | Prioridad  | Riesgo | Dependencias                   |
| ------ | --------------------------------------------------- | -------------- | ------------- | ----------- | ---------: | ----------------: | ---------- | ------ | ------------------------------ |
| HU-001 | Base técnica interna por servicio                   | Base técnica   | Todos         | L           |         40 |                46 | Crítica    | Alto   | Ninguna                        |
| HU-002 | Plantilla base de microservicio                     | Base técnica   | Todos         | M           |         24 |                28 | Crítica    | Medio  | HU-001                         |
| HU-003 | Configuración inicial de repositorios por servicio  | Base técnica   | Todos         | M           |         24 |                28 | Crítica    | Medio  | HU-001                         |
| HU-004 | Estructura base de Minimal APIs                     | Base técnica   | Todos         | M           |         24 |                28 | Crítica    | Medio  | HU-002                         |
| HU-005 | Manejo estándar de respuestas, errores y paginación | Base técnica   | Todos         | M           |         24 |                28 | Crítica    | Medio  | HU-001                         |
| HU-006 | CorrelationId, logging base y middleware común      | Base técnica   | Todos         | M           |         24 |                28 | Crítica    | Medio  | HU-001                         |
| HU-007 | Auth: usuarios                                      | Seguridad      | Auth          | L           |         40 |                46 | Crítica    | Alto   | HU-001, HU-002                 |
| HU-008 | Auth: roles dinámicos                               | Seguridad      | Auth          | L           |         40 |                46 | Crítica    | Alto   | HU-007                         |
| HU-009 | Auth: scopes y asignación de permisos               | Seguridad      | Auth          | L           |         40 |                46 | Crítica    | Alto   | HU-008                         |
| HU-010 | Auth: login, access token y refresh token           | Seguridad      | Auth          | XL          |         64 |                74 | Crítica    | Alto   | HU-007                         |
| HU-011 | Auth: sesiones en Redis                             | Seguridad      | Auth          | L           |         40 |                46 | Crítica    | Alto   | HU-010                         |
| HU-012 | Auth: cache de scopes en Redis                      | Seguridad      | Auth          | L           |         40 |                46 | Crítica    | Alto   | HU-009, HU-011                 |
| HU-013 | Auth: validación de permisos en backend             | Seguridad      | Auth          | L           |         40 |                46 | Crítica    | Alto   | HU-009, HU-012                 |
| HU-014 | Config Service base                                 | Configuración  | Config        | M           |         24 |                28 | Alta       | Medio  | HU-001, HU-002                 |
| HU-015 | Config: módulos, settings y feature flags           | Configuración  | Config        | M           |         24 |                28 | Alta       | Medio  | HU-014                         |
| HU-016 | Outbox Pattern por servicio                         | Eventos        | Todos         | XL          |         64 |                74 | Crítica    | Alto   | HU-001, HU-006                 |
| HU-017 | Inbox Pattern e idempotencia                        | Eventos        | Todos         | XL          |         64 |                74 | Crítica    | Alto   | HU-016                         |
| HU-018 | Redis Streams y consumidores base                   | Eventos        | Todos         | XL          |         64 |                74 | Crítica    | Alto   | HU-016, HU-017                 |
| HU-019 | gRPC interno entre servicios                        | Comunicación   | Todos         | L           |         40 |                46 | Alta       | Medio  | HU-001, HU-002                 |
| HU-020 | CRM: clientes                                       | CRM            | CRM           | L           |         40 |                46 | Alta       | Medio  | HU-013, HU-014                 |
| HU-021 | CRM: contactos y direcciones                        | CRM            | CRM           | L           |         40 |                46 | Alta       | Medio  | HU-020                         |
| HU-022 | CRM: notas y seguimientos                           | CRM            | CRM           | M           |         24 |                28 | Alta       | Medio  | HU-020, HU-021                 |
| HU-023 | CRM: frontend completo con permisos                 | CRM            | Web App       | XL          |         64 |                74 | Alta       | Alto   | HU-020, HU-021, HU-022, HU-013 |
| HU-024 | Storage: proveedores y configuración                | Storage        | Storage       | L           |         40 |                46 | Alta       | Medio  | HU-013, HU-014                 |
| HU-025 | Storage: carga, descarga y metadata                 | Storage        | Storage       | XL          |         64 |                74 | Alta       | Alto   | HU-024                         |
| HU-026 | Storage: versiones y referencias de archivos        | Storage        | Storage       | L           |         40 |                46 | Alta       | Medio  | HU-025                         |
| HU-027 | Pricing: cotización express                         | Pricing        | Pricing       | XL          |         64 |                74 | Alta       | Alto   | HU-020, HU-013                 |
| HU-028 | Pricing: costos, cargos y márgenes                  | Pricing        | Pricing       | XL          |         64 |                74 | Alta       | Alto   | HU-027                         |
| HU-029 | Pricing: aprobación, rechazo y estados              | Pricing        | Pricing       | L           |         40 |                46 | Alta       | Alto   | HU-027, HU-028                 |
| HU-030 | Pricing: oferta formal y documentos                 | Pricing        | Pricing       | XL          |         64 |                74 | Alta       | Alto   | HU-025, HU-026, HU-029         |
| HU-031 | Pricing: frontend completo con permisos             | Pricing        | Web App       | XL          |         64 |                74 | Alta       | Alto   | HU-027, HU-028, HU-029, HU-030 |
| HU-032 | AuditLogs: consumo y registro de auditoría          | Auditoría      | AuditLogs     | L           |         40 |                46 | Alta       | Medio  | HU-016, HU-017, HU-018         |
| HU-033 | AuditLogs: consultas y exportación                  | Auditoría      | AuditLogs     | M           |         24 |                28 | Alta       | Medio  | HU-032                         |
| HU-034 | Notifications: plantillas y mensajes                | Notificaciones | Notifications | L           |         40 |                46 | Media-Alta | Medio  | HU-013, HU-014                 |
| HU-035 | Notifications: envío por worker y reintentos        | Notificaciones | Notifications | XL          |         64 |                74 | Media-Alta | Alto   | HU-018, HU-034                 |
| HU-036 | Notifications: internas y email                     | Notificaciones | Notifications | L           |         40 |                46 | Media-Alta | Medio  | HU-034, HU-035                 |
| HU-037 | Reports: definiciones y solicitudes                 | Reportes       | Reports       | L           |         40 |                46 | Media-Alta | Medio  | HU-013, HU-014                 |
| HU-038 | Reports: CSV y Excel                                | Reportes       | Reports       | L           |         40 |                46 | Media-Alta | Medio  | HU-037, HU-025                 |
| HU-039 | Reports: PDF                                        | Reportes       | Reports       | XL          |         64 |                74 | Media-Alta | Alto   | HU-037, HU-025                 |
| HU-040 | Reports: programados y workers                      | Reportes       | Reports       | L           |         40 |                46 | Media-Alta | Alto   | HU-018, HU-037                 |
| HU-041 | AI: configuración local y proveedores               | IA             | AI            | XL          |         64 |                74 | Media      | Alto   | HU-014                         |
| HU-042 | AI: tareas asíncronas, análisis estático e híbrido  | IA             | AI            | XL          |         64 |                74 | Media      | Alto   | HU-018, HU-041                 |
| HU-043 | AI: pruebas con servidor y límites operativos       | IA             | AI            | L           |         40 |                46 | Media      | Alto   | HU-041, HU-042                 |
| HU-044 | Frontend base: login, layout, rutas y scopes        | Frontend       | Web App       | XL          |         64 |                74 | Alta       | Alto   | HU-010, HU-012, HU-013         |
| HU-045 | CI/CD, Docker, Vault y servidor on-premise          | DevOps         | Todos         | XL          |         64 |                74 | Crítica    | Alto   | Servicios principales creados  |
| HU-046 | Pruebas end-to-end, hardening y despliegue inicial  | Cierre         | Todos         | XL          |         64 |                74 | Crítica    | Alto   | HU-001 a HU-045                |

---

# 7. Resumen por fase

| Fase                      | Horas base | Horas con colchón | Prioridad  |
| ------------------------- | ---------: | ----------------: | ---------- |
| Base técnica              |        160 |               186 | Crítica    |
| Seguridad / Auth          |        304 |               350 | Crítica    |
| Configuración             |         48 |                56 | Alta       |
| Eventos / Outbox / Inbox  |        192 |               222 | Crítica    |
| Comunicación interna      |         40 |                46 | Alta       |
| CRM                       |        168 |               194 | Alta       |
| Storage                   |        144 |               166 | Alta       |
| Pricing                   |        296 |               342 | Alta       |
| Auditoría                 |         64 |                74 | Alta       |
| Notificaciones            |        144 |               166 | Media-Alta |
| Reportes                  |        184 |               212 | Media-Alta |
| IA                        |        168 |               194 | Media      |
| Frontend base             |         64 |                74 | Alta       |
| DevOps / CI/CD / Servidor |         64 |                74 | Crítica    |
| Cierre / E2E / Hardening  |         64 |                74 | Crítica    |
| **Total**                 |  **2,104** |         **2,430** |            |

---

# 8. Migración de datos

Además de las HU, se debe contemplar migración de datos desde sistemas existentes.

## 8.1 Migración inicial para octubre

```text
Clientes activos
Contactos activos
Datos mínimos de Pricing
Usuarios iniciales
Roles y scopes iniciales
Documentos necesarios para operación inicial
```

Estimación:

```text
80 a 160 horas
```

Valor recomendado para planificación:

```text
120 horas
```

---

## 8.2 Migración general realista

Incluye:

```text
Clientes
Contactos
Cotizaciones
Ofertas
Tarifas
Documentos
Usuarios
Roles
Permisos
Historial comercial
Datos operativos
Datos financieros si aplica
Archivos adjuntos
```

Reserva recomendada:

```text
400 horas
```

---

# 9. Escenarios de duración

## 9.1 Solo una persona

```text
Capacidad efectiva: 32 horas por semana
Horas HU con colchón: 2,430 horas
```

Resultado:

```text
2,430 / 32 = 75.9 semanas
```

Duración estimada:

```text
76 semanas
18 a 19 meses
```

Con migración realista:

```text
2,430 + 400 = 2,830 horas
2,830 / 32 = 88.4 semanas
21 a 22 meses
```

---

## 9.2 Persona líder + persona desarrolladora

```text
Capacidad efectiva: 68 horas por semana
Horas HU con colchón: 2,430 horas
```

Resultado:

```text
2,430 / 68 = 35.7 semanas
```

Duración estimada:

```text
36 semanas
8 a 9 meses
```

Con migración realista:

```text
2,430 + 400 = 2,830 horas
2,830 / 68 = 41.6 semanas
10 meses aproximadamente
```

---

# 10. Objetivo octubre

## 10.1 Solo una persona

Para octubre, trabajando solo, el alcance debe ser MVP recortado.

Incluye:

```text
Auth mínimo
Config mínimo
CRM básico
Pricing básico
Storage mínimo
Frontend básico
PDF básico
Deploy básico
Migración inicial mínima
```

No incluye:

```text
IA funcional
Reports avanzado
Notifications avanzado
AuditLogs avanzado
Migración histórica
```

---

## 10.2 Con persona desarrolladora adicional

Para octubre, con una persona desarrolladora adicional, el alcance puede ser más sólido.

Incluye:

```text
Auth funcional
Config funcional
CRM funcional
Pricing funcional
Storage mínimo funcional
Frontend funcional
Permisos por scopes
Outbox / Inbox base
Redis Streams base
AuditLogs básico
Reports básico
IA MVP complementaria
CI/CD básico
Servidor configurado
Vault configurado
Migración inicial mínima
Pruebas E2E principales
```

---

# 11. Reglas de planificación

```text
1. No iniciar Pricing completo sin CRM mínimo.
2. No iniciar Reports sin Storage mínimo.
3. No iniciar frontend completo sin Auth funcional.
4. No cerrar HU sin pruebas.
5. No publicar eventos sin Outbox.
6. No consumir eventos sin Inbox.
7. No incluir migración histórica en octubre.
8. No hacer IA dependencia central.
9. No avanzar con módulos pendientes sin levantamiento.
10. No comprometer fechas cerradas sin alcance cerrado.
```

---

# 12. Riesgos técnicos

```text
Auth puede atrasar todo.
Outbox e Inbox pueden requerir retrabajo.
Pricing puede crecer por reglas de negocio.
PDF puede consumir más tiempo por formato.
IA local puede estar limitada por servidor.
CI/CD y servidor pueden consumir más tiempo.
Migración de datos puede crecer por inconsistencias.
Frontend puede crecer por permisos y validaciones.
```

---

# 13. Estado del documento

```text
Estado: Borrador inicial
Pendiente: Alinear con las 46 HU exactas de GitHub
Pendiente: Ajustar cuando se cierren requerimientos faltantes
Pendiente: Separar estimación por departamento
Pendiente: Validar alcance exacto de migración
Pendiente: Validar alcance final de IA
```
