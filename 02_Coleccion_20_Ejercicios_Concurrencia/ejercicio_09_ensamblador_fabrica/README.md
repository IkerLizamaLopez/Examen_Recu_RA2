# Ejercicio 09: Ensamblador de Fabrica (Condition con Multiples Recursos)

### Enunciado
Implementa un sistema de ensamblaje en una fabrica de patinetes electricos que requiere multiples piezas para fabricar un producto terminado.
- Hay un stock compartido de piezas:
  - `ruedas` (inicialmente 0)
  - `manillares` (inicialmente 0)
  - `motores` (inicialmente 0)
- Hay tres tipos de hilos productores:
  - **Productor de Ruedas**: Anade 1 rueda al stock cada 0.4 segundos.
  - **Productor de Manillares**: Anade 1 manillar al stock cada 0.8 segundos.
  - **Productor de Motores**: Anade 1 motor al stock cada 1.2 segundos.
- Hay un hilo **Ensamblador**:
  - Para montar un patinete, requiere obligatoriamente **2 ruedas, 1 manillar y 1 motor**.
  - Si no hay suficientes piezas de alguna de ellas, debe esperar eficientemente mediante `threading.Condition` llamando a `wait()`.
  - Cuando se produce cualquier pieza, se debe notificar mediante `notify_all()`.
  - Al montar un patinete, consume las piezas correspondientes, incrementa el contador de patinetes fabricados y repite la tarea.
- Deten la simulacion limpiamente cuando se hayan fabricado 5 patinetes completos.
