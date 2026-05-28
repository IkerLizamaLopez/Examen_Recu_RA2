# Ejercicio 02: Buffer Limitado Manual

## Enunciado
Implementa manualmente un buffer circular de tamanio 3 usando Condition.

- Productor: Genera elementos y los pone en el buffer
- Consumidor: Extrae elementos del buffer
- Buffer nunca excede 3 elementos
- Productor espera si buffer lleno
- Consumidor espera si buffer vacio

## Concepto
Condition para coordinacion de productor-consumidor sin Queue.
