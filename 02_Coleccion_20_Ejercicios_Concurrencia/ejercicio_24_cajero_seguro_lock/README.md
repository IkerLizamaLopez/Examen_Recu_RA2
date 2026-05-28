# Ejercicio 24: Operaciones en Cajero Automatico Seguro (Locks)

### Enunciado
Implementa una simulación de transacciones en una cuenta bancaria compartida con operaciones concurrentes de ingresos y retiradas.
- La cuenta tiene un saldo inicial de 100 EUR.
- Habra 4 hilos "ClienteRetira" que intentan sacar 40 EUR cada uno.
- Habra 2 hilos "ClienteIngresa" que ingresan 50 EUR cada uno.
- Las operaciones sobre el saldo compartido no son atomicas y requieren exclusión mutua mediante un cerrojo (`threading.Lock`).
- Antes de permitir la retirada de dinero, se debe verificar que el saldo disponible sea igual o mayor que la cantidad solicitada. Si no es asi, se debe rechazar la transaccion para evitar saldos negativos.
- Muestra mensajes descriptivos sobre el saldo actual antes y despues de cada operacion de forma sincronizada.
- Asegurate de que no queden tildes ni emojis en ningun print.
