# Ejercicio 05: La Cafeteria (Semaforos)

### Enunciado
Simula una cafeteria con un aforo limitado a 3 clientes simultaneos.
- Habra 10 clientes (hilos) que llegan a la cafeteria a intervalos aleatorios.
- Al llegar, si hay hueco libre en la cafeteria, entran de inmediato. De lo contrario, deben esperar pacientemente en la puerta.
- Cada cliente permanece consumiendo dentro de la cafeteria un tiempo aleatorio de entre 1 y 2 segundos.
- Al salir, el cliente avisa para que pueda entrar el siguiente en la cola.
- Resuelve este control de aforo mediante `threading.Semaphore` configurado con una capacidad de 3.
- Muestra el estado del aforo en tiempo real con prints claros (por ejemplo, cuantas plazas libres quedan).
