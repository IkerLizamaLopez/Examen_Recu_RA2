# Ejercicio 13: Ping-Pong Alternado (Events)

### Enunciado
Implementa un juego de Ping-Pong alternado perfecto utilizando eventos (`threading.Event`).
- Crea dos hilos:
  - Hilo **Ping**: Imprime "PING" en la consola.
  - Hilo **Pong**: Imprime "PONG" en la consola.
- Utiliza exactamente dos objetos `threading.Event` (por ejemplo, `event_ping` y `event_pong`) para coordinar los hilos de manera que escriban de forma alternada de manera estrictamente exacta: PING, PONG, PING, PONG...
- Haz que cada hilo repita su impresion 5 veces consecutivas y luego se detenga ordenadamente.
- El hilo "Ping" comenzara el juego.
