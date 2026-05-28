# Ejercicio 03: Filosofos Comensales (Evitacion de Deadlocks)

### Enunciado
Resuelve el problema clasico de la cena de los 5 filosofos que piensan y comen alternadamente.
- Hay 5 filosofos sentados alrededor de una mesa redonda.
- Hay 5 tenedores en la mesa, uno entre cada par de filosofos vecinos.
- Para comer, un filosofo necesita coger ambos tenedores contiguos (el de su izquierda y el de su derecha).
- Si todos los filosofos cogieran simultaneamente su tenedor izquierdo, se produciria un interbloqueo (deadlock) esperando indefinidamente por el tenedor derecho.
- Resuelve este problema aplicando la estrategia de **jerarquia de recursos**: los filosofos deben intentar coger siempre el tenedor con el indice numerico mas bajo primero, y luego el de indice mas alto.
- Simula que los filosofos realizan este ciclo (pensar, tener hambre, coger tenedores, comer y soltar tenedores) 3 veces consecutivas cada uno.
