# Ejercicio 04: Turnos - Condition Variable Basica

## Enunciado
Implementa un sistema de turnos donde los hilos se alternan.

- Hilo 1: Ejecuta, cede el turno
- Hilo 2: Ejecuta, cede el turno
- Se repite 3 veces

## Concepto
Una `threading.Condition` permite que hilos esperen y se despierten bajo ciertas condiciones:

- `condition.wait()` - Espera (bloquea) hasta ser despertado
- `condition.notify()` - Despierta a UN hilo en espera
- `condition.notify_all()` - Despierta a TODOS los hilos en espera

## Salida esperada
```
Turno de Hilo 1 (ronda 1)
Turno de Hilo 2 (ronda 1)
Turno de Hilo 1 (ronda 2)
Turno de Hilo 2 (ronda 2)
Turno de Hilo 1 (ronda 3)
Turno de Hilo 2 (ronda 3)
```

## Pistas
- Crea una Condition con `threading.Condition()`
- Mantén una variable para saber de quien es el turno
- Usa `condition.wait()` si NO es tu turno
- Usa `condition.notify()` para despertar al otro hilo
- Usa `with condition:` para proteger el acceso
