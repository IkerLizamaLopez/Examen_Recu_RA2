# Ejercicio 17: Parking con Plazas Estandar y VIP (Condition)

### Enunciado
Implementa un aparcamiento de plazas limitadas diferenciadas para coches normales y VIP.
- El parking dispone de:
  - 2 plazas de aparcamiento de tipo **Estandar**.
  - 1 plaza de aparcamiento de tipo **VIP**.
- Reglas de aparcamiento:
  - Un **Coche Normal** solo puede aparcar en una plaza Estandar libre. Si estan llenas, debe esperar llamando a `.wait()`.
  - Un **Coche VIP** puede aparcar tanto en la plaza VIP como en cualquier plaza Estandar libre. Daremos prioridad a que ocupen la plaza VIP si esta libre; si esta ocupada, buscaran una Estandar libre. Si todo el parking esta lleno, el Coche VIP debe esperar llamando a `.wait()`.
- Utiliza `threading.Condition` para sincronizar a los vehiculos concurrentes y coordinar de forma limpia las plazas asignadas.
- Simula 4 coches normales y 2 coches VIP llegando consecutivamente a aparcar. Cada coche permanece aparcado entre 1 y 2 segundos antes de liberar su plaza y avisar a los demas.
