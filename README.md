# Repositorio de Preparacion: Programacion Concurrente y Multihilo (RA2)

Este repositorio ha sido organizado y ampliado para servir como una guia de estudio exhaustiva y practica para el bloque de Programacion Concurrente en Python (Resultado de Aprendizaje 2).

Toda la coleccion de ejercicios ha sido depurada para eliminar emojis, acentos (tildes) y caracteres especiales complejos, garantizando una ejecucion 100% segura y sin fallos de codificacion en consolas clasicas de Windows o Linux.

---

## Estructura del Repositorio

El repositorio se divide en dos bloques principales para facilitar el aprendizaje:

1. **`01_Ejemplos_y_Clases_Originales/`**
   * Contiene todos los scripts, explicaciones y proyectos practicos que se desarrollaron originalmente en clase (como el puente estrecho original, el comedor de galletas, simulaciones del banco, ping-pong, etc.).
   * Preserva el 100% de tu codigo previo de forma intacta.

2. **`02_Coleccion_20_Ejercicios_Concurrencia/`**
   * Una coleccion organizada de **25 ejercicios resueltos** paso a paso, abarcando desde los fundamentos mas sencillos de exclusión mutua hasta patrones de concurrencia avanzados y examenes oficiales.
   * Cada ejercicio esta en su propia carpeta e incluye:
     * **`README.md`**: El enunciado detallado y explicaciones teoricas en castellano puro sin tildes ni emojis.
     * **`main.py`**: El codigo de la solucion completo, altamente modular, autodocumentado y listo para ser ejecutado directamente.

---

## Catalogo de los 25 Ejercicios Creados (Indice General)

### Bloque 1: Locks y Exclusion Mutua (Basico)
* **`ejercicio_01_contador_seguro`**: Simula el acceso seguro a una seccion critica con `threading.Lock` para contar visitas web concurrentes de forma exacta.
* **`ejercicio_02_reserva_entradas`**: Simula reservas de entradas de cine concurrentes con control de stock sin permitir duplicaciones ni inventario negativo.
* **`ejercicio_03_filosofos_comensales`**: El problema clasico de los 5 filosofos comensales. Resuelto mediante la tecnica de jerarquia de recursos para evitar interbloqueos (deadlocks).
* **`ejercicio_04_banco_transferencias`**: Transferencias concurrentes cruzadas entre cuentas bancarias. Resuelve deadlocks ordenando los IDs de cuentas antes de adquirir los locks.

### Bloque 2: Semaforos y Control de Aforo
* **`ejercicio_05_cafeteria_aforo`**: Simulación de aforo limitado en un local mediante `threading.Semaphore`.
* **`ejercicio_06_peaje_autopista`**: Control del uso de cabinas de pago activas en paralelo mediante `threading.BoundedSemaphore` para una mayor seguridad.
* **`ejercicio_07_impresoras_compartidas`**: Una oficina con 3 impresoras distintas compartidas. Combina un `Semaphore(3)` para el aforo general y un `Lock` para saber y reservar la impresora exacta elegida.

### Bloque 3: Variables de Condicion y Productor-Consumidor
* **`ejercicio_08_productor_consumidor_cola`**: Patrón Productor-Consumidor clasico mediante `queue.Queue` limitada. Utiliza senales de parada centinela (`None`) para un apagado limpio de hilos.
* **`ejercicio_09_ensamblador_fabrica`**: Montaje de patinetes que requieren piezas de 3 productores independientes. Utiliza `threading.Condition` para esperar eficientemente la disponibilidad de todas las piezas requeridas (2 ruedas, 1 manillar, 1 motor).
* **`ejercicio_10_buffer_limitado_manual`**: Recrea un bufer circular de tamaño fijo manualmente mediante una `list` estandar y una variable `threading.Condition`, sin utilizar la libreria `queue`.
* **`ejercicio_11_barbero_durmiente`**: Implementa la coordinacion del barbero durmiente con 3 sillas de espera mediante `threading.Condition`.
* **`ejercicio_12_puente_estrecho_prioridad`**: Simulación avanzada de puente de carril unico con prioridades y limites consecutivos para evitar hambruna (starvation) de un carril.

### Bloque 4: Coordinacion con Eventos y Barreras
* **`ejercicio_13_ping_pong_eventos`**: Alternancia perfecta de dos hilos ("Ping" y "Pong") mediante dos objetos `threading.Event`.
* **`ejercicio_14_ping_pong_condicion`**: Alternancia perfecta de hilos de juego usando una unica variable `threading.Condition` y una variable de turno compartido.
* **`ejercicio_15_cruce_peatones`**: Regulacion de coches que circulan hasta que un peaton pulsa el boton, coordinados por un `threading.Event` que actua como semaforo interactivo.
* **`ejercicio_16_lobby_multijugador`**: Inicio simultaneo de una partida online unicamente cuando se registran 4 jugadores usando `threading.Barrier`.

### Bloque 5: Casos Avanzados de Examen e Hilos Coordinados
* **`ejercicio_17_parking_mixto_vip`**: Aparcamiento con plazas Estandar y VIP, donde los vehiculos VIP tienen prioridad de plaza VIP y capacidad de usar Estandar, sincronizados mediante `Condition`.
* **`ejercicio_18_comedero_mascotas_intentos`**: Mascotas que comen de un comedero compartido de capacidad 2. Si esta lleno, esperan llamando a `wait(timeout=1.0)` y se retiran tras agotar 3 intentos fallidos.
* **`ejercicio_19_urgencias_hospital_prioridad`**: Simulación de triaje en urgencias medicas donde los pacientes se atienden prioritariamente segun su gravedad mediante `queue.PriorityQueue`.
* **`ejercicio_20_procesamiento_lotes_pool`**: Consulta asincrona paralela a 10 servidores mediante un pool de hilos `concurrent.futures.ThreadPoolExecutor`, gestionando respuestas exitosas y excepciones mediante `Future`.

### Bloque 6: Casos de Examen Jovellanos y Ampliacion (Nuevos)
* **`ejercicio_21_comedero_conejos`**: El examen oficial de Jovellanos (Conejos y Comedero). Conejos que son hilos con 5 intentos totales, muerte tras 3 fallos seguidos, Lock de exclusion mutua y Semaphore para representar porciones disponibles.
* **`ejercicio_22_lavanderia_sem`**: Simulación de aforo en una lavanderia con 4 maquinas y 8 clientes concurrentes mediante `threading.Semaphore`.
* **`ejercicio_23_almacen_piezas_cond`**: Almacen donde operarios depositan piezas A y B de forma concurrente, y un ensamblador espera con `Condition` a tener al menos 1 de cada una para crear un paquete.
* **`ejercicio_24_cajero_seguro_lock`**: Cajero automatico seguro con multiples clientes de ingresos y retiradas usando `Lock` para proteger el saldo compartido contra valores negativos y condiciones de carrera.
* **`ejercicio_25_puente_estrecho_simple`**: Simulación simplificada y basica del paso alterno Norte-Sur sobre un puente estrecho de un unico carril usando un `Lock` principal y una `Condition` para el cambio de sentido.

---

## Como ejecutar los ejercicios

1. **Requisito**: Tener instalado Python 3 en tu sistema.
2. **Ejecutar**: Navega a la carpeta de cualquier ejercicio y ejecuta su archivo `main.py`.
   Por ejemplo, para el Ejercicio 21 (el examen de conejos):
   ```bash
   python 02_Coleccion_20_Ejercicios_Concurrencia/ejercicio_21_comedero_conejos/main.py
   ```
3. **Observar**: Mira con atencion la salida en consola. Cada ejercicio incluye impresiones descriptivas muy detalladas en texto ASCII plano que muestran el comportamiento exacto de los hilos.
