# Ejercicio 04: Banco y Transferencias Concurrentes (Prevencion de Deadlocks)

### Enunciado
Implementa un sistema de transferencia de dinero entre cuentas bancarias en hilos paralelos.
- Tenemos 3 cuentas bancarias (Cuenta A, Cuenta B y Cuenta C) con saldos iniciales de 1000EUR cada una.
- Cada cuenta dispone de su propio `threading.Lock` para que sus modificaciones individuales sean atomicas y seguras.
- Se lanzaran multiples transferencias cruzadas concurrentes:
  - Hilo 1: Cuenta A transfiere 100EUR a Cuenta B.
  - Hilo 2: Cuenta B transfiere 50EUR a Cuenta A.
- Si no se toman precauciones, cuando el Hilo 1 bloquee la Cuenta A e intente bloquear la Cuenta B, al mismo tiempo el Hilo 2 podria bloquear la Cuenta B e intentar bloquear la Cuenta A, provocando un interbloqueo eterno (Deadlock).
- Resuelve este problema ordenando de manera determinista los locks (por ejemplo, por el identificador de cuenta) de forma que siempre se adquiera primero el lock de la cuenta con menor identificador al realizar cualquier transferencia.
