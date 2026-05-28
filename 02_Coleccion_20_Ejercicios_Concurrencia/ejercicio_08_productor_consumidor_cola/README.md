# Ejercicio 08: Productor-Consumidor con Cola (Queue)

### Enunciado
Implementa un sistema clasico de Productor-Consumidor utilizando la estructura thread-safe `queue.Queue`.
- Varios hilos "Cliente" (productores) generan pedidos concurrentemente en una tienda online. Cada cliente genera 3 pedidos y los introduce en la cola de pedidos.
- Varios hilos "Operario" (consumidores) en el almacen extraen los pedidos de la cola y los empaquetan.
- Configura la cola para tener una capacidad limitada de 5 elementos (`maxsize=5`) para ilustrar el bloqueo cuando esta llena.
- Los productores deben poner pedidos en la cola mediante `put()`, y los consumidores deben extraerlos mediante `get()`, indicando cuando se extraen y procesan.
- Envia una "senal de parada" especial (un valor centinela como `None` por cada operario) para finalizar los hilos de manera limpia cuando ya no queden mas pedidos por procesar.
