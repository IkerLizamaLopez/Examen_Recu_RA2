# Ejercicio 01: Filosofos Comensales (Clasico)

## Enunciado
El problema clasico de los 5 filosofos comensales.

- 5 filosofos comparten una mesa redonda
- 5 tenedores (uno entre cada par)
- Cada filosofo alterna entre pensar y comer
- Para comer necesita AMBOS tenedores adyacentes
- Evitar deadlock usando jerarquia de recursos

## Concepto
Deadlock classico. Solucion: ordenar adquisicion de recursos (tenedor bajo ID primero).

## Salida esperada
```
Filosofo 1 piensa
Filosofo 2 piensa
Filosofo 1 intenta comer (tenedor 0, tenedor 1)
Filosofo 1 come
Filosofo 1 termina de comer
Filosofo 2 intenta comer (tenedor 1, tenedor 2)
...
```
