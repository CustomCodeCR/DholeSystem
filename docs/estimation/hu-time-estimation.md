# Estimación General de Horas - Dhole Microservices

## 1. Objetivo

Este documento define la estimación general inicial para el desarrollo de Dhole Microservices.

La estimación contempla las historias de usuario actuales, la arquitectura definida, los servicios principales y complementarios, el frontend, las pruebas, el servidor, CI/CD, IA y despliegue.

También considera que todavía faltan módulos y requerimientos de otros departamentos, por lo que esta estimación debe entenderse como una base inicial que deberá ajustarse conforme se completen los levantamientos faltantes.

---

## 2. Alcance actual considerado

La estimación actual contempla los siguientes servicios y módulos base:

```text
DholeAuthService
DholeConfigService
DholeCrmService
DholePricingService
DholeStorageService
DholeNotificationsService
DholeAuditLogsService
DholeReportsService
DholeAiService
Dhole Web App
```

También contempla:

```text
Base técnica por servicio
Repositorios independientes
Minimal APIs
CQRS sin MediatR
PostgreSQL por servicio
MongoDB donde aplique
Redis
Redis Streams
Outbox
Inbox
gRPC entre servicios
WebSockets para frontend cuando aplique
Docker
Docker Compose
Vault
CI/CD
Servidor on-premise
Pruebas
Monitoreo
IA local complementaria
```

---

## 3. Alcance pendiente por definir

Todavía hacen falta módulos y requerimientos de otros departamentos.

Por lo tanto, esta estimación no debe interpretarse como el cierre definitivo del proyecto completo.

Departamentos o áreas pendientes pueden incluir:

```text
Operaciones
Documentación
Coordinación de Origen
Tránsito
Coordinación de Destino
Facturación
Liquidación de trámites
Servicio al Cliente
Pedimentación
Transporte
Bodega
Contabilidad
Otros departamentos que se definan en levantamientos posteriores
```

Estos módulos podrían requerir:

```text
Nuevos microservicios
Nuevas bases de datos
Nuevas pantallas
Nuevos flujos
Nuevos eventos
Nuevos reportes
Nuevas reglas de negocio
Nuevas integraciones
Nuevos permisos/scopes
Nuevas pruebas
```

Por esta razón, se incluye una reserva de alcance pendiente.

---

## 4. Supuestos generales

La estimación se basa en los siguientes supuestos:

```text
- Desarrollo realista, no agresivo.
- Jornada ideal de 8 horas diarias.
- Se trabaja de lunes a viernes.
- Se reserva tiempo semanal para reunión con el gerente general.
- Se reserva tiempo para levantamientos adicionales.
- Se reserva tiempo para reuniones con departamentos.
- La documentación base se realiza antes del desarrollo.
- Cada HU incluye backend, frontend cuando aplique, base de datos, pruebas, permisos e integración.
- Cada servicio tendrá su propio repositorio.
- Cada servicio tendrá su propia base de datos.
- Cada servicio tendrá sus propias migraciones.
- Cada servicio tendrá sus propias pruebas.
- El frontend será Vue + TypeScript.
- El despliegue será on-premise.
- Docker será obligatorio.
- Vault será usado para secretos.
- La IA será complementaria y local.
```

---

## 5. Capacidad semanal estimada

## 5.1 Escenario A - Solo una persona

```text
Capacidad nominal semanal: 40 horas
Tiempo reservado para reuniones, gestión y ajustes: 8 horas
Capacidad efectiva semanal: 32 horas
```

La capacidad efectiva baja porque una sola persona debe encargarse de:

```text
Desarrollo backend
Desarrollo frontend
Base de datos
Pruebas
Reuniones
Levantamientos adicionales
Decisiones técnicas
CI/CD
Servidor
Revisión funcional
Corrección de errores
Despliegue
```

---

## 5.2 Escenario B - Persona líder + persona desarrolladora

La persona líder mantiene responsabilidades adicionales además del desarrollo:

```text
Reunión semanal con el gerente general
Revisión técnica
Decisiones de arquitectura
Control de calidad
Apoyo a la persona desarrolladora
Integración entre servicios
Validación funcional
Revisión de entregables
Coordinación del roadmap
Resolución de bloqueos técnicos
```

Capacidad efectiva de la persona líder:

```text
28 horas semanales
```

La persona desarrolladora se dedica principalmente a desarrollar.

Capacidad efectiva de la persona desarrolladora:

```text
40 horas semanales
```

Capacidad efectiva total:

```text
68 horas semanales
```

---

## 6. Escala de complejidad

```text
XS = 4 a 6 horas
S  = 8 a 12 horas
M  = 16 a 24 horas
L  = 32 a 40 horas
XL = 48 a 64 horas
```

Se utiliza una estimación realista, considerando:

```text
Pruebas
Integración
Permisos
Eventos
Workers
Frontend
Base de datos
CI/CD
Servidor
Ajustes funcionales
```

---

## 7. Colchones aplicados

Se aplican los siguientes colchones:

```text
5% revisión/refactor
10% colchón general
```

Total aplicado:

```text
15%
```

Además, se agrega una reserva separada por alcance pendiente de otros departamentos.

---

# 8. Estimación general base

## 8.1 Resumen por fase

| Fase                                     | Horas base | Horas con colchón | Prioridad  |
| ---------------------------------------- | ---------: | ----------------: | ---------- |
| Base técnica por servicio                |        160 |               184 | Crítica    |
| Auth y seguridad                         |        304 |               350 | Crítica    |
| Configuración                            |         48 |                55 | Alta       |
| Eventos / Outbox / Inbox / Redis Streams |        192 |               221 | Crítica    |
| Comunicación interna HTTP / gRPC / WS    |         40 |                46 | Alta       |
| CRM                                      |        168 |               193 | Alta       |
| Storage                                  |        144 |               166 | Alta       |
| Pricing                                  |        296 |               340 | Alta       |
| AuditLogs                                |         64 |                74 | Alta       |
| Notifications                            |        144 |               166 | Media-Alta |
| Reports                                  |        184 |               212 | Media-Alta |
| IA                                       |        168 |               193 | Media      |
| Frontend base                            |         64 |                74 | Alta       |
| DevOps / CI/CD / Servidor / Vault        |        120 |               138 | Crítica    |
| Pruebas E2E / Hardening / Pre-despliegue |        120 |               138 | Crítica    |
| **Total base**                           |  **2,316** |         **2,666** |            |

---

## 8.2 Observación importante

La estimación base de 2,666 horas contempla los servicios principales y complementarios actuales.

No incluye todavía el desarrollo completo de todos los módulos departamentales pendientes.

Por eso se debe agregar una reserva de alcance.

---

# 9. Reserva por módulos y requerimientos pendientes

Como todavía faltan requerimientos de otros departamentos, se agrega una reserva estimada para módulos futuros.

Esta reserva no es relleno. Representa trabajo real que probablemente aparecerá cuando se completen los levantamientos.

## 9.1 Categorías de módulos pendientes

| Tipo de módulo pendiente      | Horas estimadas por módulo |
| ----------------------------- | -------------------------: |
| Módulo simple                 |                 80 a 120 h |
| Módulo medio                  |                160 a 240 h |
| Módulo complejo               |                280 a 400 h |
| Módulo con integración fuerte |                400 a 600 h |

---

## 9.2 Departamentos pendientes probables

| Departamento / Área     | Complejidad esperada | Observación                                                  |
| ----------------------- | -------------------- | ------------------------------------------------------------ |
| Documentación           | Alta                 | Puede requerir flujos, archivos, validaciones y seguimiento  |
| Coordinación de Origen  | Alta                 | Puede requerir estados, tareas, coordinación y eventos       |
| Tránsito                | Media-Alta           | Puede requerir seguimiento operativo y alertas               |
| Coordinación de Destino | Alta                 | Puede requerir estados, documentos y coordinación            |
| Facturación             | Alta                 | Puede requerir reglas financieras, documentos y aprobaciones |
| Liquidación de trámites | Alta                 | Puede requerir cálculos, cierres y validaciones              |
| Servicio al Cliente     | Media                | Puede requerir tickets, seguimientos y notificaciones        |
| Pedimentación           | Alta                 | Puede requerir reglas específicas y documentos               |
| Transporte              | Media-Alta           | Puede requerir unidades, rutas y programación                |
| Bodega                  | Media-Alta           | Puede requerir inventario, movimientos y ubicaciones         |
| Contabilidad            | Alta                 | Puede requerir integración, reportes y cierres               |

---

## 9.3 Reserva recomendada

Para cubrir módulos pendientes, se recomienda agregar una reserva inicial de:

```text
Mínima: 800 horas
Realista: 1,200 horas
Conservadora: 1,600 horas
```

Para planificación general se recomienda usar:

```text
Reserva realista: 1,200 horas
```

---

# 10. Estimación total del proyecto

## 10.1 Total sin módulos pendientes

```text
Total base con colchón: 2,666 horas
```

Este total cubre:

```text
Base técnica
Auth
Config
CRM
Pricing
Storage
Notifications
AuditLogs
Reports
IA
Frontend base
CI/CD
Servidor
Vault
Pruebas
Pre-despliegue
```

---

## 10.2 Total con reserva mínima

```text
Total base: 2,666 h
Reserva mínima: 800 h
Total: 3,466 h
```

---

## 10.3 Total con reserva realista

```text
Total base: 2,666 h
Reserva realista: 1,200 h
Total: 3,866 h
```

---

## 10.4 Total con reserva conservadora

```text
Total base: 2,666 h
Reserva conservadora: 1,600 h
Total: 4,266 h
```

---

# 11. Duración estimada por escenario

## 11.1 Escenario A - Solo una persona

Capacidad efectiva:

```text
32 horas semanales
```

| Escenario                   | Horas | Semanas | Meses aproximados |
| --------------------------- | ----: | ------: | ----------------: |
| Base sin módulos pendientes | 2,666 |      84 |     19 a 21 meses |
| Con reserva mínima          | 3,466 |     109 |     25 a 27 meses |
| Con reserva realista        | 3,866 |     121 |     28 a 30 meses |
| Con reserva conservadora    | 4,266 |     134 |     31 a 33 meses |

---

## 11.2 Escenario B - Persona líder + persona desarrolladora

Capacidad efectiva:

```text
68 horas semanales
```

| Escenario                   | Horas | Semanas | Meses aproximados |
| --------------------------- | ----: | ------: | ----------------: |
| Base sin módulos pendientes | 2,666 |      40 |      9 a 10 meses |
| Con reserva mínima          | 3,466 |      51 |          12 meses |
| Con reserva realista        | 3,866 |      57 |     13 a 14 meses |
| Con reserva conservadora    | 4,266 |      63 |          15 meses |

---

# 12. Interpretación ejecutiva

## 12.1 Si se trabaja solo

Trabajar solo permite avanzar, pero el proyecto completo se extiende demasiado.

Para el alcance actual base, sin contar todos los departamentos pendientes, el tiempo estimado es:

```text
19 a 21 meses
```

Si se agregan los módulos pendientes con una reserva realista, el tiempo estimado sube a:

```text
28 a 30 meses
```

Esto significa que trabajar solo es viable técnicamente, pero no es recomendable si se espera cubrir todos los departamentos en un plazo razonable.

---

## 12.2 Si se contrata una persona adicional

Con una persona desarrolladora adicional, el alcance base puede completarse aproximadamente en:

```text
9 a 10 meses
```

Con la reserva realista para módulos pendientes, el tiempo estimado sería:

```text
13 a 14 meses
```

Este escenario es más sano para el proyecto, especialmente porque las bases firmes reducen el tiempo de desarrollo de módulos posteriores.

---

# 13. Por qué los módulos posteriores deberían ser más rápidos

Los primeros módulos son más costosos porque cargan con la creación de la base técnica.

CRM y Pricing no solo desarrollan funcionalidad, también obligan a construir:

```text
Auth
Permisos
Frontend base
Storage
Eventos
Outbox
Inbox
Redis Streams
CI/CD
Servidor
Pruebas
Estándares
```

Una vez que estas bases estén firmes, los módulos posteriores pueden reutilizar:

```text
Estructura base de servicio
Patrón de Minimal APIs
Patrón CQRS sin MediatR
Validación de scopes
Base de frontend
Componentes UI
Manejo de permisos
Storage
Reports
AuditLogs
Notifications
Eventos
Workers
CI/CD
Docker
Vault
```

Por eso, un nuevo módulo departamental después de CRM y Pricing debería requerir menos tiempo que los primeros módulos.

---

# 14. Estimación por tipo de módulo posterior

## 14.1 Módulo simple

Ejemplos:

```text
Catálogos
Configuraciones
Mantenimientos pequeños
Consultas simples
```

Estimación:

```text
80 a 120 horas
```

Incluye:

```text
Backend
Frontend
Base de datos
Permisos
Pruebas
```

---

## 14.2 Módulo medio

Ejemplos:

```text
Seguimientos
Tareas operativas
Estados simples
Reportes básicos
Documentos simples
```

Estimación:

```text
160 a 240 horas
```

Incluye:

```text
Backend
Frontend
Base de datos
Permisos
Eventos
Pruebas
Reportes básicos si aplica
```

---

## 14.3 Módulo complejo

Ejemplos:

```text
Facturación
Liquidación de trámites
Coordinación operativa
Pedimentación
Flujos con múltiples estados
```

Estimación:

```text
280 a 400 horas
```

Incluye:

```text
Backend
Frontend
Base de datos
Permisos
Eventos
Workers
Reportes
Auditoría
Pruebas E2E
```

---

## 14.4 Módulo con integración fuerte

Ejemplos:

```text
Integración con sistemas externos
Sincronización con plataformas externas
Procesos financieros complejos
Automatizaciones entre varios departamentos
```

Estimación:

```text
400 a 600 horas
```

Incluye:

```text
Backend
Frontend
Base de datos
Permisos
Eventos
Workers
Integraciones
Reintentos
Auditoría
Pruebas E2E
Pruebas de errores
```

---

# 15. Priorización recomendada

Para evitar que el proyecto crezca sin control, se recomienda priorizar así:

## Fase 1 - Base técnica y seguridad

```text
Auth
Config
Repositorios
Base de servicio
Permisos
Redis
CI/CD inicial
```

---

## Fase 2 - Base comercial

```text
CRM
Pricing
Storage
PDF básico
Frontend base
```

---

## Fase 3 - Servicios complementarios

```text
AuditLogs
Reports
Notifications
IA MVP
```

---

## Fase 4 - Departamentos operativos

```text
Documentación
Coordinación de Origen
Tránsito
Coordinación de Destino
Servicio al Cliente
Pedimentación
Transporte
Bodega
```

---

## Fase 5 - Procesos financieros

```text
Facturación
Liquidación de trámites
Contabilidad
Reportes financieros
Integraciones financieras
```

---

# 16. Recomendación general

La recomendación general es no estimar el proyecto completo como cerrado hasta terminar los levantamientos de los departamentos pendientes.

Sin embargo, para planificación ejecutiva se puede trabajar con tres escenarios:

```text
Escenario base:
2,666 horas
Solo servicios principales y complementarios actuales.

Escenario realista:
3,866 horas
Incluye reserva para módulos pendientes.

Escenario conservador:
4,266 horas
Incluye mayor protección ante módulos complejos, cambios e integraciones.
```

El escenario recomendado para presentar es:

```text
3,866 horas
```

Porque reconoce que faltan departamentos y evita vender una expectativa demasiado baja.

---

# 17. Recomendación de equipo

Para el alcance actual y los módulos pendientes, trabajar solo no es lo más recomendable.

## Solo una persona

```text
Duración realista con módulos pendientes:
28 a 30 meses
```

Riesgos:

```text
Alta carga operativa
Mayor riesgo de retrasos
Menos tiempo para pruebas
Menos margen para soporte y reuniones
Mayor dificultad para avanzar con varios frentes
```

---

## Persona líder + persona desarrolladora

```text
Duración realista con módulos pendientes:
13 a 14 meses
```

Ventajas:

```text
Mejor velocidad
Más capacidad de pruebas
Menos riesgo de atraso
Mejor continuidad
Mayor posibilidad de atender nuevos requerimientos
Mejor separación de trabajo
Más probabilidad de llegar a entregas parciales útiles
```

---

# 18. Entregas parciales recomendadas

Aunque el proyecto completo pueda durar más, se recomienda entregar por fases.

## Entrega 1 - Octubre

```text
CRM funcional
Pricing funcional
Auth funcional
Config funcional
Storage mínimo
Frontend funcional
IA MVP complementaria si hay segunda persona
CI/CD inicial
Servidor configurado
```

---

## Entrega 2 - Servicios complementarios

```text
Reports
Notifications
AuditLogs
Mejoras de IA
Reportes programados
PDFs mejorados
```

---

## Entrega 3 - Departamentos operativos

```text
Documentación
Coordinación de Origen
Tránsito
Coordinación de Destino
Servicio al Cliente
Pedimentación
Transporte
Bodega
```

---

## Entrega 4 - Procesos financieros

```text
Facturación
Liquidación de trámites
Contabilidad
Reportes financieros
Integraciones financieras
```

---

# 19. Riesgos generales

## 19.1 Falta de requerimientos completos

Todavía faltan módulos y requerimientos de otros departamentos.

Riesgo:

```text
Alto
```

Impacto:

```text
La estimación total puede aumentar.
```

Mitigación:

```text
Mantener reserva de alcance y estimar por módulo conforme se completen los levantamientos.
```

---

## 19.2 Crecimiento de Pricing

Pricing puede crecer más de lo esperado por tarifas, costos, márgenes, aprobaciones y documentos.

Riesgo:

```text
Alto
```

Mitigación:

```text
Separar Pricing MVP de Pricing avanzado.
```

---

## 19.3 Complejidad de procesos operativos

Departamentos como Documentación, Coordinación, Tránsito, Pedimentación y Liquidación pueden tener flujos complejos.

Riesgo:

```text
Alto
```

Mitigación:

```text
Realizar levantamientos por departamento antes de comprometer fechas cerradas.
```

---

## 19.4 IA local limitada por servidor

La IA local puede estar limitada por falta de GPU.

Riesgo:

```text
Medio-Alto
```

Mitigación:

```text
Usar IA complementaria, análisis estático y procesos asíncronos.
```

---

## 19.5 CI/CD, servidor y despliegue

La configuración on-premise, Vault, Docker, CI/CD y pruebas previas al despliegue pueden consumir tiempo considerable.

Riesgo:

```text
Alto
```

Mitigación:

```text
Iniciar DevOps desde fases tempranas.
```

---

# 20. Conclusión

El proyecto Dhole Microservices es viable, pero debe planificarse por fases.

La estimación base actual es:

```text
2,666 horas
```

Pero como faltan módulos y requerimientos de varios departamentos, la estimación recomendada para planificación general es:

```text
3,866 horas
```

Trabajando solo, esto representa aproximadamente:

```text
28 a 30 meses
```

Con una persona desarrolladora adicional, representa aproximadamente:

```text
13 a 14 meses
```

La recomendación es avanzar con entregas parciales, iniciando por CRM y Pricing, porque estas bases facilitarán el desarrollo de los demás módulos.

---

## 21. Estado del documento

```text
Estado: Borrador inicial
Pendiente: Ajustar contra las 46 HU exactas de GitHub
Pendiente: Ajustar cuando se completen los levantamientos faltantes
Pendiente: Separar estimación por departamento cuando existan requerimientos completos
Pendiente: Validar alcance final de IA
Pendiente: Validar capacidad real de persona desarrolladora adicional
```
