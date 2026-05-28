# Ejercicio 01: Contador - Race Condition

## Enunciado
Implementa un programa simple que demuestre una **race condition** (condicion de carrera).

- Crea 3 hilos
- Cada hilo debe incrementar un contador global 1000 veces
- **NO USES sincronizacion** (sin Lock)
- Ejecuta varias veces y observa que el resultado NUNCA es 3000

## Concepto
Una race condition ocurre cuando dos o mas hilos acceden simultaneamente a datos compartidos sin proteccion, causando resultados impredecibles.

La operacion `contador += 1` NO es atomica. Se compone de:
1. Leer el valor actual
2. Sumarle 1
3. Escribir el nuevo valor

Si dos hilos hacen esto a la vez, pueden sobrescribirse los cambios.

## Salida esperada (ejemplo)
```
Iniciando 3 hilos...
Hilo 1 completado
Hilo 2 completado
Hilo 3 completado
Contador final: 2847 (INCORRECTO - deberia ser 3000)
```

Ejecuta varias veces: veras valores diferentes cada ejecucion.

## Pistas
- Usa time.sleep(0.000001) para forzar cambios de contexto y hacer visible la race condition
- No uses Lock ni Condition ni Semaphore
- Imprime mensajes cuando empieza y termina cada hilo
