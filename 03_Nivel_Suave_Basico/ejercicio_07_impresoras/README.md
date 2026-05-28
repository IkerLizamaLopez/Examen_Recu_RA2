# Ejercicio 07: Impresoras Simples - Lock + Semaphore

## Enunciado
Implementa una oficina con 2 impresoras compartidas entre 4 trabajadores.

- 4 trabajadores quieren imprimir
- Solo 2 impresoras disponibles (aforo con Semaphore)
- Cada trabajador usa una impresora aleatoria (Lock para saber cual)

## Concepto
Combina dos primitivas:
- `Semaphore(2)` - Para controlar que maximo 2 impresoras estan en uso
- `Lock` - Para proteger la eleccion de cual impresora usar

## Salida esperada
```
Trabajador 1 intentando imprimir...
Trabajador 1 usando impresora 1
Trabajador 2 intentando imprimir...
Trabajador 2 usando impresora 2
Trabajador 3 esperando impresora...
Trabajador 1 termino, liberando impresora 1
Trabajador 3 usando impresora 1
```

## Pistas
- Crea `Semaphore(2)` para limitar a 2 impresoras
- Crea `Lock()` para proteger array de impresoras
- Array indica cual esta libre: [True, True] = ambas libres
- Primero hace acquire del semaforo, luego busca impresora libre con lock
