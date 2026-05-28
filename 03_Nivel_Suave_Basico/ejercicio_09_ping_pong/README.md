# Ejercicio 09: Ping-Pong Basico - Event

## Enunciado
Implementa alternancia perfecta entre dos hilos ("Ping" y "Pong").

- Hilo Ping: Imprime "PING", espera a que Pong haga su turno
- Hilo Pong: Espera a que Ping imprima, imprime "PONG", espera a Ping
- Repite 5 veces

## Concepto
Usa dos Events para sincronizar:
- `event_ping` - Se activa cuando es turno de Ping
- `event_pong` - Se activa cuando es turno de Pong

## Salida esperada
```
PING
PONG
PING
PONG
PING
PONG
PING
PONG
PING
PONG
```

## Pistas
- Crea dos Events: `event_ping` y `event_pong`
- Inicia con `event_ping` activado
- Cada hilo: espera su evento, hace su trabajo, activa el otro evento
- Usa `event.clear()` para desactivar, `set()` para activar
