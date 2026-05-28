# Ejercicio 10: Banco Simple - Lock Basico

## Enunciado
Implementa un cajero automatico seguro con Lock.

- Cuenta bancaria con saldo inicial de 1000
- 2 hilos hacen retiros simultaneos (Lock protege)
- Imprime el saldo antes y despues de cada retiro

## Concepto
Protege operaciones sobre datos compartidos (saldo) con Lock para evitar race conditions.

## Salida esperada
```
Saldo inicial: 1000

Hilo 1 retirando 300...
Saldo antes: 1000
Saldo despues: 700

Hilo 2 retirando 200...
Saldo antes: 700
Saldo despues: 500

Saldo final: 500
```

## Pistas
- Crea `Lock()` para proteger el saldo
- Dentro del lock: lee saldo, resta cantidad, escribe nuevo saldo
- Usa `time.sleep()` para simular operacion lenta del banco
- Cada retiro debe imprimir saldo antes y despues
