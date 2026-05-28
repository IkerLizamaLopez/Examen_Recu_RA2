# Ejercicio 01: Contador Seguro (Locks)

### Enunciado
Implementa una simulacion en la que varios hilos acceden a un contador compartido en un servidor web para contar las visitas.
- Habra 5 hilos "lector_visitas" que simulan visitas web. Cada hilo incrementara el contador compartido 10.000 veces.
- Si no se utiliza sincronizacion, se producira una condicion de carrera (race condition) y el total final sera incorrecto.
- Resuelve el problema utilizando `threading.Lock` para garantizar la exclusion mutua de modo que el resultado final sea exactamente 50.000.
- Imprime por consola el resultado obtenido con y sin sincronizacion (o explica su efecto), mostrando mensajes claros al empezar y terminar la simulacion.
