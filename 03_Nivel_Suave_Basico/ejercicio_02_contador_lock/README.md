# Ejercicio 02: Contador Seguro - Lock

## Enunciado
Resuelve el problema anterior usando `threading.Lock` para sincronizar el acceso.

- Crea 3 hilos
- Cada hilo debe incrementar un contador global 1000 veces
- **USA threading.Lock** para proteger la seccion critica
- El resultado SIEMPRE debe ser exactamente 3000

## Concepto
Un Lock (cerradura) es un mecanismo de exclusion mutua que garantiza que solo un hilo a la vez puede ejecutar una seccion critica.

```python
with lock:
    # Solo un hilo ejecuta esto a la vez
    contador += 1
```

## Salida esperada
```
Iniciando 3 hilos (cada uno incrementa 1000 veces)...
Resultado esperado: 3000

Hilo 1 iniciado
Hilo 2 iniciado
Hilo 3 iniciado
Hilo 1 completado
Hilo 2 completado
Hilo 3 completado

Contador final: 3000
CORRECTO - Lock garantizo exclusion mutua
```

Ejecuta varias veces: siempre sera 3000.

## Pistas
- Crea un Lock con `threading.Lock()`
- Rodea la operacion critica con `with lock:`
- Compara el resultado con el ejercicio anterior
