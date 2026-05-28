# Ejercicio 22: La Lavanderia Autoservicio (Semaphoros)

### Enunciado
Implementa una simulacion de una lavanderia autoservicio con maquinas de lavar limitadas.
- La lavanderia dispone de un total de 4 maquinas de lavar.
- Habra 8 hilos "Cliente" que acuden de forma concurrente para lavar sus prendas de ropa.
- Cada cliente requiere adquirir una lavadora para poder iniciar su lavado. Si todas estan ocupadas, debe esperar haciendo cola de forma ordenada.
- Resuelve esta limitacion de recursos utilizando un semaforo (`threading.Semaphore`) configurado a 4.
- Imprime mensajes descriptivos de la llegada del cliente, el inicio del lavado (que dura entre 0.8 y 1.6 segundos), y la salida para permitir que entren otros clientes de la cola.
- Toda la simulacion debe estar escrita libre de tildes y emojis en sus prints.
