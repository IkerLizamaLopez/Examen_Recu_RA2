# Ejercicio 10: Bufer Limitado Manual (List + Condition)

### Enunciado
Implementa el clasico patron Productor-Consumidor recreando un bufer circular de tamano fijo *manualmente*, es decir, **sin utilizar `queue.Queue`**.
- Utiliza una lista estandar de Python (`list`) y una variable compartida de capacidad maxima $K = 3$.
- Sincroniza el acceso de los hilos mediante una unica variable de condicion (`threading.Condition`).
- Un hilo **Productor** anade numeros secuenciales al bufer cada 0.3 segundos:
  - Si el bufer esta lleno (longitud igual a $K$), el productor debe esperar llamando a `wait()`.
  - Al anadir un numero, notifica a los hilos en espera mediante `notify_all()`.
- Un hilo **Consumidor** extrae numeros del bufer (del inicio de la lista, simulando una cola FIFO) cada 1.0 segundos:
  - Si el bufer esta vacio (longitud igual a 0), el consumidor debe esperar llamando a `wait()`.
  - Al extraer un numero, notifica a los hilos en espera mediante `notify_all()`.
- Imprime de forma vistosa los contenidos del bufer tras cada insercion y extraccion.
