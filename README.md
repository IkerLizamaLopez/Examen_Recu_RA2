# Repositorio de Preparacion: Programacion Concurrente y Multihilo (RA2)

Este repositorio ha sido organizado y ampliado para servir como una guia de estudio exhaustiva y practica para el bloque de Programacion Concurrente en Python (Resultado de Aprendizaje 2).

Toda la coleccion de ejercicios ha sido depurada para eliminar emojis, acentos (tildes) y caracteres especiales complejos, garantizando una ejecucion 100% segura y sin fallos de codificacion en consolas clasicas de Windows o Linux.

---

## Estructura del Repositorio

El repositorio se divide en **5 bloques** principales para facilitar el aprendizaje progresivo:

1. **`01_Ejemplos_y_Clases_Originales/`**
   * Contiene todos los scripts, explicaciones y proyectos practicos que se desarrollaron originalmente en clase (como el puente estrecho original, el comedor de galletas, simulaciones del banco, ping-pong, etc.).
   * Preserva el 100% de tu codigo previo de forma intacta.

2. **`02_Coleccion_20_Ejercicios_Concurrencia/`** (ORIGINAL)
   * Una coleccion organizada de **25 ejercicios resueltos** paso a paso, abarcando desde los fundamentos mas sencillos de exclusión mutua hasta patrones de concurrencia avanzados y examenes oficiales.
   * Cada ejercicio esta en su propia carpeta e incluye README.md y main.py.

3. **`03_Nivel_Suave_Basico/`** (NUEVO - 10 EJERCICIOS BASICOS)
   * Introducción suave a los conceptos de concurrencia
   * Enfocado en estudiantes sin experiencia previa
   * Contiene: race conditions, locks simples, events, turnos, colas, semaphores, etc.

4. **`04_Nivel_Intermedio_Medio/`** (NUEVO - 15 EJERCICIOS INTERMEDIOS)
   * Combinaciones de primitivas de sincronizacion
   * Patrones mas complejos: productor-consumidor multiples, lector-escritor, timeouts, reintentos
   * Pool de hilos, jerarquia de recursos, coordinacion avanzada

5. **`05_Nivel_Avanzado_Dificil/`** (NUEVO - 10 EJERCICIOS AVANZADOS)
   * Problemas clasicos de concurrencia: filosofos, barbero, puente estrecho
   * Casos de examen: conejos, transacciones, parking VIP, fabrica
   * Prevencion de deadlock, starvation, recovery
   * Coordinacion multi-recurso compleja

---

## Catalogo Completo: 35+ Ejercicios Organizados por Dificultad

### NIVEL 1: BASICO - 10 Ejercicios (Fundamentos)
Perfect para empezar desde cero. Cubre un concepto por ejercicio.

1. **Contador - Race Condition**: Demuestra condicion de carrera sin sincronizacion
2. **Contador Seguro - Lock**: Resuelve race condition con Lock
3. **Bandera - Event Basico**: Comunicacion simple entre hilos con Event
4. **Turnos - Condition Variable**: Alterna entre dos hilos
5. **Cola Simple - Queue**: Productor-consumidor basico
6. **Aforo - Semaphore**: Limita acceso simultaneo (capacidad)
7. **Impresoras Simples**: Combina Semaphore + Lock
8. **Carrera - Barrier**: Sincroniza multiples hilos en punto
9. **Ping-Pong Basico**: Alternancia perfecta con Events
10. **Banco Simple**: Retiros seguros con Lock

### NIVEL 2: INTERMEDIO - 15 Ejercicios (Patrones Complejos)
Combina multiples primitivas. Requiere entender conceptos basicos.

1. **Productor-Consumidor Avanzado**: Multiples productores y consumidores
2. **Buffer Limitado Manual**: Implementa manualmente sin Queue
3. **Lector-Escritor**: Problema clasico de concurrencia
4. **Productores Multiples Coordinados**: 3 tipos esperan a ensamblador
5. **Cola con Prioridad**: PriorityQueue para triaje
6. **Timeout - Espera con Limite**: queue.get(timeout=X)
7. **Reintentos Limitados**: Manejo de fallos con reintentos
8. **Pool de Hilos**: ThreadPoolExecutor para paralelismo
9. **Recursos Multiples Ordenados**: Jerarquia para evitar deadlock
10. **Contador con Limites**: Invariantes con Condition
11. **Carrera de Recursos**: Semaphore con competencia
12. **Productor-Consumidor Multiples Avanzado**: Colas multiples
13. **Semaforos Multiples**: Varios recursos independientes
14. **Eventos de Coordinacion**: Fases de ejecucion
15. **Condition Variables Multiples**: Orden de ejecucion

### NIVEL 3: AVANZADO - 10 Ejercicios (Problemas Clasicos + Examen)
Problemas reales y de examen. Para dominar concurrencia.

1. **Filosofos Comensales**: Problema clasico de deadlock
2. **Barbero Durmiente**: Coordinacion consumidor con 3 sillas
3. **Puente Estrecho**: Cambio de sentido alternado N-S
4. **Parking VIP**: Recursos con prioridades
5. **Productor-Consumidor Complejo**: N productores, M colas, dinamica
6. **Fabrica Ensamblador**: 3 productores, 1 ensamblador
7. **Carrera con Prioridad**: Starvation prevention
8. **Deadlock Recovery**: Timeouts para recuperacion
9. **Conejos y Comedero**: EXAMEN OFICIAL JOVELLANOS
10. **Transacciones Bancarias**: Multiples cuentas concurrentes


