# Ejercicio 02: Barbero Durmiente (Clasico)

## Enunciado
Barbero durmiente con N sillas de espera.

- 1 barbero (cuando no hay clientes, duerme)
- Sillas de espera limitadas
- Clientes llegan y esperan
- Si sillas llenas, cliente se va

## Concepto
Coordinacion entre productor (clientes) y consumidor (barbero).

## Salida esperada
```
Barbero durmiendo (sillas: 0/3)
Cliente 1 entra (sillas: 1/3)
Cliente 2 entra (sillas: 2/3)
Barbero se despierta - cortando Cliente 1
Cliente 1 termina (sillas: 1/3)
Cliente 3 entra (sillas: 2/3)
```
