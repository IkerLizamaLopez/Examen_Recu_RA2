# Ejercicio 07: Impresoras Compartidas (Semaforos y Locks)

### Enunciado
Implementa un sistema de gestion para una oficina con 3 impresoras compartidas (Impresora A, Impresora B, Impresora C) que son utilizadas por 8 trabajadores concurrentemente.
- Se debe usar un semaforo (`threading.Semaphore`) inicializado a 3 para controlar que no impriman mas de 3 trabajadores a la vez.
- Para saber exactamente **que impresora fisica** coge cada empleado (ya que son distintas), implementa una estructura de datos compartida protegida por un Lock (por ejemplo, una lista de booleanos `[True, True, True]` que represente si la impresora `[A, B, C]` esta libre o no).
- Cuando un empleado adquiere el semaforo de aforo, debe examinar la lista bajo exclusion mutua (`Lock`), marcar la impresora que va a usar como ocupada (`False`) e imprimir.
- Tras terminar la impresion (que dura de 1 a 2 segundos), liberara la impresora concreta (marcando `True` de nuevo) y liberara el semaforo.
- Muestra mensajes divertidos e informativos indicando que empleado imprime en que impresora.
