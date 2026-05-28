# Ejercicio 23: Almacen de Piezas y Ensamblado (Condition)

### Enunciado
Implementa un sistema de fabricacion de paquetes de regalo que requiere diferentes piezas para poder ser montados.
- Disponemos de dos tipos de piezas compartidas en el almacen:
  - `piezas_A` (inicialmente 0)
  - `piezas_B` (inicialmente 0)
- Habra dos operarios productores independientes:
  - **Productor A**: Anade 1 pieza A cada 0.5 segundos.
  - **Productor B**: Anade 1 pieza B cada 0.7 segundos.
- Habra un operario **Ensamblador**:
  - Para montar un "paquete de regalo", se requiere obligatoriamente **1 pieza A y 1 pieza B**.
  - Si en el almacen no hay existencias de alguna de las piezas, el ensamblador debe esperar pacientemente llamando a `.wait()` en una variable de condicion.
  - Cuando los productores anadan piezas, deben notificar al ensamblador mediante `.notify_all()`.
  - Cuando haya suficientes piezas, el ensamblador las consume, monta el paquete e incrementa su contador.
- Deten la simulación limpiamente tras ensamblar 5 paquetes completos.
- Toda la simulacion debe estar libre de acentos (tildes) y emojis.
