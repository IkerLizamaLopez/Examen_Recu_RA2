# Ejercicio 03: Bandera - Event Basico

## Enunciado
Implementa una comunicacion simple entre dos hilos usando un Event.

- Hilo 1: Espera a que se establezca una "bandera" (event)
- Hilo 2: Realiza trabajo y luego activa la bandera
- Hilo 1: Cuando se activa la bandera, continua e imprime un mensaje

## Concepto
Un `threading.Event` es un mecanismo de sincronizacion simple que permite a un hilo esperar a que algo suceda (un evento).

- `event.set()` - Activa el evento
- `event.wait()` - Espera (bloquea) hasta que el evento se active
- `event.clear()` - Desactiva el evento

## Salida esperada
```
Hilo 1 esperando...
Hilo 2 trabajando...
[Hilo 2 termina]
Hilo 1 continua (evento activado)
```

## Pistas
- Crea un Event con `threading.Event()`
- Usa `event.wait()` en el hilo que espera
- Usa `event.set()` para activar el evento
- Imprime mensajes para ver el flujo de sincronizacion
