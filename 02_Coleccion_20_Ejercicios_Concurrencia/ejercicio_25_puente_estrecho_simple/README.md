# Ejercicio 25: Paso Alterno sobre Puente Estrecho Simple (Lock + Condition)

### Enunciado
Implementa una simulación basica y sencilla de un puente de un carril compartido por coches que circulan en direcciones opuestas (Sentido Norte y Sentido Sur).
- Al ser de carril unico, no pueden cruzar coches en sentidos distintos al mismo tiempo.
- Resuelve este escenario utilizando exclusión mutua mediante un `Lock` y una variable de condición `Condition`.
- Si un coche de Sentido Norte quiere cruzar y hay coches del Sentido Sur cruzando, debe esperar llamando a `.wait()`.
- Cuando un coche termina de cruzar y el puente queda vacio, notifica a los demas mediante `.notify_all()`.
- Simula 3 coches del Norte y 3 coches del Sur cruzando el puente secuencialmente para observar el paso coordinado.
- Toda la simulacion debe estar escrita sin tildes ni emojis en sus prints.
