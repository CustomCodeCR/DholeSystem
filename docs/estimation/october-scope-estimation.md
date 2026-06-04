# Estimación de Alcance hasta Octubre - Dhole Microservices

## 1. Objetivo

Este documento define una estimación realista del alcance que se puede lograr para octubre en el desarrollo de Dhole Microservices.

Se comparan dos escenarios:

1. Desarrollo realizado solo por una persona.
2. Desarrollo realizado por una persona líder más una persona desarrolladora a cargo.

El objetivo es determinar si es viable tener listos los módulos de CRM y Pricing para octubre, y si con una segunda persona es posible incluir una primera implementación de IA.

---

## 2. Supuestos generales

La estimación considera los siguientes supuestos:

```text
- Jornada ideal: 8 horas diarias.
- Se trabaja de lunes a viernes.
- Se reserva tiempo semanal para reunión con el gerente general.
- Se reserva tiempo para levantamientos adicionales o reuniones con departamentos.
- La estimación es realista, no agresiva.
- El alcance incluye backend, frontend, base de datos, pruebas, permisos e integración.
- La documentación base se realiza antes del desarrollo y no se carga a cada HU.
- Se incluye 5% de revisión/refactor.
- Se incluye 10% de colchón general.
- Se incluye tiempo para servidor, CI/CD, Docker, Vault, pruebas previas al despliegue e IA.
```

---

## 3. Fecha objetivo

Para esta estimación se consideran dos cortes posibles:

```text
Corte 1: inicio de octubre
Corte 2: cierre de octubre
```

Desde junio hasta octubre, el rango realista disponible es:

```text
Inicio de octubre: 16 a 18 semanas efectivas
Cierre de octubre: 20 a 21 semanas efectivas
```

Para evitar una estimación demasiado optimista, se usa el rango conservador.

---

## 4. Capacidad semanal estimada

Aunque la jornada ideal sea de 40 horas semanales, no todo ese tiempo será desarrollo puro para la persona líder.

Se debe reservar tiempo para:

- Reunión semanal con el gerente general.
- Revisión de avances.
- Ajustes de alcance.
- Levantamientos adicionales.
- Reuniones con departamentos.
- Pruebas funcionales.
- Correcciones no planificadas.
- Coordinación técnica.
- Revisión de trabajo de la persona desarrolladora.

---

# 5. Escenario A - Solo una persona

## 5.1 Capacidad

```text
Capacidad nominal semanal: 40 horas
Tiempo reservado para reuniones, gestión y ajustes: 8 horas
Capacidad efectiva semanal: 32 horas
```

La capacidad efectiva baja porque una sola persona debe encargarse de:

- Desarrollo backend.
- Desarrollo frontend.
- Base de datos.
- Pruebas.
- Reuniones.
- Levantamientos adicionales.
- Decisiones técnicas.
- CI/CD.
- Configuración de servidor.
- Revisión funcional.
- Corrección de errores.
- Despliegue.

---

## 5.2 Capacidad hasta octubre

```text
Hasta inicio de octubre:
32 h x 17 semanas = 544 horas aproximadas

Hasta cierre de octubre:
32 h x 21 semanas = 672 horas aproximadas
```

---

## 5.3 Conclusión del escenario

Con una sola persona, no es realista entregar CRM + Pricing completos, con frontend, Auth, Storage, pruebas, CI/CD, servidor e IA para octubre.

Sí es posible entregar un MVP recortado de CRM + Pricing, siempre que se reduzca el alcance y se deje IA fuera o únicamente documentada/preparada para una fase posterior.

---

# 6. Escenario B - Persona líder + una persona desarrolladora

## 6.1 Capacidad

La persona líder mantiene responsabilidades adicionales además del desarrollo, como:

- Reunión semanal con el gerente general.
- Revisión técnica.
- Decisiones de arquitectura.
- Control de calidad.
- Apoyo a la persona desarrolladora.
- Integración entre servicios.
- Validación funcional.
- Revisión de entregables.
- Coordinación del roadmap.
- Resolución de bloqueos técnicos.

Por esta razón, su capacidad efectiva de desarrollo se estima en:

```text
28 horas efectivas semanales
```

La persona desarrolladora estará dedicada principalmente a implementación, sin participar en reuniones con gerencia ni levantamientos funcionales.

Su tiempo se enfocará en:

- Implementación backend.
- Implementación frontend.
- Pruebas.
- Corrección de bugs.
- Ajustes técnicos.
- Tareas asignadas por la persona líder.
- Apoyo en Docker, CI/CD o integraciones cuando se le asignen tareas específicas.

Por esta razón, su capacidad efectiva se estima en:

```text
40 horas efectivas semanales
```

Capacidad efectiva total:

```text
68 horas semanales
```

---

## 6.2 Capacidad hasta octubre

```text
Hasta inicio de octubre:
68 h x 17 semanas = 1,156 horas aproximadas

Hasta cierre de octubre:
68 h x 21 semanas = 1,428 horas aproximadas
```

---

## 6.3 Conclusión del escenario

Con una persona desarrolladora dedicada, sí es realista llegar a cierre de octubre con un alcance mucho más sólido.

El escenario con dos personas permite entregar:

```text
- Base técnica firme.
- Auth funcional.
- Config funcional.
- CRM funcional.
- Pricing funcional.
- Storage mínimo funcional.
- Frontend base.
- CI/CD inicial.
- Servidor configurado.
- Vault configurado.
- Pruebas base.
- IA MVP complementaria.
```

La IA puede incluirse si se maneja como MVP complementario, no como módulo central ni crítico.

---

# 7. Alcance posible estando solo hasta octubre

## 7.1 Alcance realista

```text
Objetivo:
MVP operativo de CRM + Pricing
```

---

## 7.2 Incluye

```text
- Base técnica mínima por servicio.
- Auth mínimo funcional.
- Config mínimo funcional.
- CRM básico.
- Pricing básico.
- Storage mínimo para documentos de Pricing.
- Frontend básico para CRM y Pricing.
- Permisos por scopes.
- Pruebas mínimas.
- Deploy inicial controlado.
```

---

## 7.3 No incluye

```text
- IA implementada.
- Reports avanzado.
- Notifications avanzado.
- AuditLogs avanzado.
- Automatizaciones completas.
- Reportes programados.
- PDF avanzado.
- Monitoreo completo.
- CI/CD avanzado.
- Kubernetes.
```

---

## 7.4 Estimación de horas

| Bloque                  | Horas estimadas |
| ----------------------- | --------------: |
| Base técnica mínima     |              40 |
| Auth mínimo             |              80 |
| Config mínimo           |              16 |
| CRM backend             |              60 |
| CRM frontend básico     |              50 |
| Pricing backend         |             100 |
| Pricing frontend básico |              70 |
| Storage mínimo          |              32 |
| PDF básico de oferta    |              24 |
| Deploy básico           |              40 |
| Pruebas y ajustes       |              48 |
| **Total**               |       **560 h** |

---

## 7.5 Comparación contra capacidad

```text
Horas disponibles hasta inicio de octubre: 544 h
Horas disponibles hasta cierre de octubre: 672 h
Horas requeridas para MVP recortado: 560 h
```

---

## 7.6 Conclusión

Estando solo, el MVP recortado puede llegar para octubre, pero queda muy ajustado.

El alcance debe protegerse fuertemente. Cualquier cambio grande, reunión extra, ajuste funcional o problema técnico puede mover la entrega.

La entrega sería funcional, pero no completa.

---

# 8. Alcance posible con una persona adicional hasta octubre

## 8.1 Alcance realista

```text
Objetivo:
CRM + Pricing funcionales con base técnica firme e IA MVP complementaria
```

---

## 8.2 Incluye

```text
- Base técnica sólida por servicio.
- Auth funcional.
- Config funcional.
- Outbox e Inbox base.
- Redis Streams base.
- CRM funcional.
- Pricing funcional.
- Storage funcional mínimo.
- PDF básico o intermedio para ofertas.
- Frontend funcional para Auth, CRM y Pricing.
- Permisos por scopes en backend y frontend.
- AuditLogs básico.
- Reports básico para exportaciones iniciales.
- IA MVP complementaria.
- CI/CD inicial.
- Servidor on-premise configurado.
- Docker Compose.
- Vault configurado.
- Pruebas mínimas por servicio.
- Pruebas end-to-end de los flujos principales.
```

---

## 8.3 IA incluida en este escenario

La IA puede incluirse como un MVP complementario.

No debe plantearse como una IA que automatice todo el sistema.

El enfoque recomendado es híbrido:

```text
1. Análisis estático primero.
2. IA local cuando el servidor lo permita.
3. Validación humana cuando el caso sea complejo.
```

La IA puede iniciar con funciones como:

```text
- Analizar cotizaciones.
- Detectar posibles inconsistencias.
- Sugerir mejoras o advertencias.
- Resumir información de CRM o Pricing.
- Analizar reportes generados.
- Apoyar al usuario con recomendaciones simples.
```

No debe incluir en esta primera etapa:

```text
- Automatización total de decisiones.
- Modelos pesados.
- Procesamiento masivo.
- Dependencia obligatoria para operar CRM o Pricing.
- Entrenamiento complejo de modelos.
```

---

# 9. Estimación con una persona adicional

| Bloque                              | Horas estimadas |
| ----------------------------------- | --------------: |
| Base técnica sólida                 |              80 |
| Auth funcional                      |             130 |
| Config funcional                    |              32 |
| Outbox / Inbox / Redis Streams base |             100 |
| CRM backend completo inicial        |              90 |
| CRM frontend funcional              |              80 |
| Pricing backend completo inicial    |             150 |
| Pricing frontend funcional          |             110 |
| Storage funcional mínimo            |              70 |
| PDF de oferta básico/intermedio     |              40 |
| AuditLogs básico                    |              40 |
| Reports básico                      |              60 |
| IA MVP complementaria               |             120 |
| CI/CD inicial                       |              50 |
| Servidor on-premise, Docker y Vault |              70 |
| Pruebas end-to-end y hardening      |              90 |
| **Total**                           |     **1,312 h** |

---

# 10. Comparación contra capacidad

## 10.1 Hasta inicio de octubre

```text
Capacidad con dos personas:
1,156 h aproximadas

Alcance estimado con CRM + Pricing funcionales e IA MVP:
1,312 h
```

Conclusión:

```text
No alcanza para tener todo el alcance con IA MVP listo al inicio de octubre.
```

Para inicio de octubre habría que recortar:

```text
- Reports básico.
- AuditLogs avanzado.
- Parte de IA.
- PDF intermedio.
- Hardening completo.
```

---

## 10.2 Hasta cierre de octubre

```text
Capacidad con dos personas:
1,428 h aproximadas

Alcance estimado con CRM + Pricing funcionales e IA MVP:
1,312 h

Margen estimado:
116 h
```

Conclusión:

```text
Con una persona desarrolladora dedicada, sí es realista llegar a cierre de octubre con CRM, Pricing, base técnica firme e IA MVP complementaria.
```

El margen no debe interpretarse como tiempo libre, sino como protección ante:

- Bugs.
- Ajustes funcionales.
- Cambios menores.
- Problemas de integración.
- Pruebas adicionales.
- Configuración del servidor.
- Ajustes de CI/CD.
- Validaciones con usuarios.
- Ajustes solicitados por gerencia.

---

# 11. Versión recomendada para octubre con dos personas

Para que sea realista, el alcance recomendado hasta octubre con dos personas debería ser:

| Bloque         | Estado para octubre                |
| -------------- | ---------------------------------- |
| Base técnica   | Firme                              |
| Auth           | Funcional                          |
| Config         | Funcional                          |
| CRM            | Funcional                          |
| Pricing        | Funcional                          |
| Storage        | Funcional mínimo                   |
| PDF oferta     | Básico/intermedio                  |
| Frontend       | Funcional para Auth, CRM y Pricing |
| Permisos       | Aplicados en backend y frontend    |
| Outbox / Inbox | Base funcional                     |
| Redis Streams  | Base funcional                     |
| AuditLogs      | Básico                             |
| Reports        | Básico                             |
| IA             | MVP complementario                 |
| CI/CD          | Básico funcional                   |
| Servidor       | Configurado                        |
| Vault          | Configurado                        |
| Pruebas        | Mínimas y E2E principales          |

---

# 12. Alcance recomendado de IA para octubre

## 12.1 Objetivo

Implementar una IA complementaria que ayude en CRM y Pricing, sin convertirse en dependencia crítica del sistema.

---

## 12.2 Funciones posibles

```text
- Analizar una cotización y detectar datos faltantes.
- Sugerir revisión de márgenes bajos.
- Resumir información de cliente.
- Resumir historial comercial.
- Analizar reportes básicos.
- Generar recomendaciones simples.
- Crear explicaciones o alertas para el usuario.
```

---

## 12.3 Arquitectura de IA recomendada

```text
DholeAiService
  - AiTasks
  - AiTaskMessages
  - AiTaskResults
  - AiProviders
  - Worker de procesamiento
```

---

## 12.4 Enfoque técnico

```text
- Procesamiento asíncrono.
- IA local.
- Análisis estático cuando sea suficiente.
- Resultados guardados.
- No bloquear operaciones principales.
- No depender de GPU.
```

---

## 12.5 Limitaciones aceptadas

```text
- No se garantiza respuesta inmediata.
- No se procesan volúmenes grandes al inicio.
- No se automatizan decisiones críticas.
- El usuario humano mantiene la decisión final.
```

---

# 13. Por qué las bases firmes reducen el tiempo de los siguientes módulos

Una vez que estén listas las bases principales, los nuevos módulos o departamentos serán más rápidos de construir.

Esto aplica porque ya existirán:

```text
- Auth listo.
- Permisos por scopes listos.
- Base de Minimal APIs lista.
- Estructura de repositorios definida.
- Outbox e Inbox definidos.
- Redis Streams configurado.
- Storage funcionando.
- Reports básico funcionando.
- AuditLogs básico funcionando.
- Frontend base con rutas y permisos.
- CI/CD inicial.
- Servidor configurado.
```

Con esas bases, un nuevo módulo no empieza desde cero.

Solo debe implementar:

```text
- Entidades propias.
- Casos de uso propios.
- Endpoints propios.
- Pantallas propias.
- Eventos propios.
- Pruebas propias.
```

Por eso CRM y Pricing son más costosos al inicio: cargan con la creación de la base técnica.

Los módulos posteriores deberían ser más sencillos y rápidos si se respetan los estándares.

---

# 14. Comparación final

| Escenario        | Capacidad hasta cierre de octubre | Alcance posible                                               |
| ---------------- | --------------------------------: | ------------------------------------------------------------- |
| Solo una persona |                             672 h | MVP recortado CRM + Pricing, sin IA real                      |
| Dos personas     |                           1,428 h | CRM + Pricing funcionales, base firme e IA MVP complementaria |

---

# 15. Conclusión

## 15.1 Si se trabaja solo

Es posible llegar a octubre con un MVP recortado de CRM y Pricing.

Pero no es realista incluir IA funcional, CI/CD sólido, servidor bien probado, pruebas completas y servicios complementarios bien integrados.

El alcance debe limitarse a:

```text
CRM + Pricing MVP
Auth mínimo
Config mínimo
Storage mínimo
Frontend básico
Deploy básico
```

---

## 15.2 Si se contrata una persona adicional

Sí es posible apuntar a un alcance mucho más fuerte para octubre.

El alcance realista sería:

```text
CRM funcional
Pricing funcional
Auth funcional
Config funcional
Storage mínimo funcional
Frontend funcional
Outbox / Inbox base
Redis Streams base
AuditLogs básico
Reports básico
IA MVP complementaria
CI/CD básico
Servidor configurado
Vault configurado
Pruebas end-to-end principales
```

La IA puede entrar si se mantiene como complemento y no como dependencia central.

---

# 16. Recomendación

La recomendación para cumplir octubre con una base sólida es contratar una persona adicional.

El desarrollo con dos personas permite:

```text
- Llegar con CRM y Pricing más completos.
- Incluir IA MVP.
- Configurar servidor y CI/CD con menos presión.
- Probar mejor antes del despliegue.
- Reducir riesgo de retraso.
- Crear una base reutilizable para los siguientes módulos.
```

La estrategia recomendada sería:

```text
Junio:
Base técnica, Auth, Config, repositorios y servidor inicial.

Julio:
CRM backend/frontend, Storage mínimo y permisos.

Agosto:
Pricing backend/frontend, PDF, Outbox/Inbox y Redis Streams.

Septiembre:
AuditLogs básico, Reports básico, IA MVP y CI/CD.

Octubre:
Pruebas end-to-end, hardening, ajustes, despliegue controlado y validación con usuarios.
```

---

# 17. Riesgos

## 17.1 Riesgo: cambios de alcance

Si CRM o Pricing cambian de forma importante durante el desarrollo, la fecha de octubre puede verse afectada.

Mitigación:

```text
Cerrar alcance MVP antes de iniciar desarrollo fuerte.
```

---

## 17.2 Riesgo: Auth se atrasa

Auth es base para todo el ecosistema.

Mitigación:

```text
Desarrollar Auth temprano y no iniciar módulos protegidos hasta tener permisos mínimos funcionando.
```

---

## 17.3 Riesgo: Pricing crece más de lo esperado

Pricing puede crecer por reglas de negocio, márgenes, tarifas, documentos y aprobaciones.

Mitigación:

```text
Separar Pricing MVP de Pricing avanzado.
```

---

## 17.4 Riesgo: PDF consume más tiempo

Los documentos PDF pueden requerir ajustes de formato, diseño y validación.

Mitigación:

```text
Usar plantilla simple para octubre y dejar mejoras visuales para después.
```

---

## 17.5 Riesgo: IA local tiene limitaciones

El servidor no cuenta con GPU dedicada.

Mitigación:

```text
Usar IA como complemento, apoyarse en análisis estático y no bloquear procesos principales.
```

---

## 17.6 Riesgo: CI/CD y servidor toman más tiempo

Configurar servidor, Docker, Vault, pipelines y despliegue puede consumir más tiempo del esperado.

Mitigación:

```text
Empezar configuración de servidor y CI/CD desde fases tempranas.
```

---

# 18. Estado del documento

```text
Estado: Borrador inicial
Pendiente: Ajustar contra las 46 HU exactas de GitHub
Pendiente: Validar fecha objetivo exacta de octubre
Pendiente: Revisar estimación cuando se defina el alcance final de IA
Pendiente: Ajustar según disponibilidad real de la persona adicional
```
