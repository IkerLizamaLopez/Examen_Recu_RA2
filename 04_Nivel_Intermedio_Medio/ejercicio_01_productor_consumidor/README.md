# Ejercicio 01: Productor-Consumidor Avanzado

## Enunciado
Extiende el pattern productor-consumidor con 2 productores y 2 consumidores.

- 2 productores generan numeros (1-5, 6-10)
- 2 consumidores procesan los numeros
- Usa una cola compartida thread-safe

## Conceptos
- Queue para sincronizacion automatica
- Multiples productores y consumidores
- Patron de "sentinela" para terminar (None)

## Salida esperada
```
Productor 1: Genera 1
Productor 2: Genera 6
Consumidor 1: Recibe 1
Consumidor 2: Recibe 6
...
```
