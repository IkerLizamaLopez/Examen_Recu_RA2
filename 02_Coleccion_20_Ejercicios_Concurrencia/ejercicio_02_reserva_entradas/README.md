# Ejercicio 02: Reserva de Entradas (Locks)

### Enunciado
Implementa un sistema de reservas de entradas de cine concurrentes.
- El cine dispone de un stock total de 20 entradas.
- Habra 10 hilos "Cliente" que intentan reservar un numero aleatorio de entradas (entre 1 y 4 entradas por reserva).
- Cada cliente verifica si quedan suficientes entradas libres. Si es asi, realiza la reserva restandolas del stock.
- Utiliza `threading.Lock` para que el stock de entradas no se vuelva negativo ni se reserven de forma duplicada entradas inexistentes.
- Imprime de forma legible cuando llega cada cliente, cuantas entradas solicita, si la reserva fue exitosa o fallida, y cuantas quedan en el stock actual.
