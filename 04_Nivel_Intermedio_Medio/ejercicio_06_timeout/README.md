# Ejercicio 06: Timeout - Espera con Limite

## Enunciado
Usa esperas con timeout (limite de tiempo).

- Consumidor espera 2 segundos por datos
- Si no llega en 2 seg, continua sin datos

## Concepto
queue.get(timeout=2.0) lanza exception si no recibe antes del timeout.
