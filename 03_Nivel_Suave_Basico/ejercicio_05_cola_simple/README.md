# Ejercicio 05: Cola Simple - Queue

## Enunciado
Implementa un productor y un consumidor usando una cola thread-safe.

- Productor: Genera 5 numeros y los pone en la cola
- Consumidor: Lee 5 numeros de la cola e imprime

## Concepto
`queue.Queue` es una estructura thread-safe (lista segura para multihilo) que:
- Protege automaticamente el acceso
- Los `put()` ponen elementos
- Los `get()` sacan elementos
- Si esta vacia, `get()` espera automaticamente hasta que haya algo

## Salida esperada
```
Productor: Generando 1
Consumidor: Recibio 1
Productor: Generando 2
Consumidor: Recibio 2
Productor: Generando 3
Consumidor: Recibio 3
Productor: Generando 4
Consumidor: Recibio 4
Productor: Generando 5
Consumidor: Recibio 5
```

## Pistas
- Importa `from queue import Queue`
- Crea cola con `queue = Queue(maxsize=2)`
- Usa `queue.put(item)` para producir
- Usa `queue.get()` para consumir
- Es thread-safe automaticamente
