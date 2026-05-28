# Ejercicio 06: Aforo - Semaphore Basico

## Enunciado
Implementa control de aforo (capacidad maxima) usando un Semaphore.

- 5 clientes quieren entrar en un local
- El local tiene capacidad para 2 personas simultaneamente
- Usa `threading.Semaphore(2)` para controlar la entrada

## Concepto
Un `threading.Semaphore` es un contador que permite controlar el acceso a recursos limitados:

- `semaphore.acquire()` o `with semaphore:` - Decrementa el contador
- Si el contador llega a 0, bloquea hasta que se incremente
- `semaphore.release()` - Incrementa el contador automaticamente con `with`

## Salida esperada
```
Cliente 1 entrando...
Cliente 2 entrando...
Local lleno (2 personas)
Cliente 3 esperando...
Cliente 1 saliendo...
Cliente 3 entrando...
Cliente 2 saliendo...
Cliente 4 entrando...
...
```

## Pistas
- Crea Semaphore con `threading.Semaphore(2)`
- Usa `with semaphore:` para entrar (acquire) y salir (release)
- Cada cliente simula estar en el local un tiempo
- Imprime cuando entra y sale
