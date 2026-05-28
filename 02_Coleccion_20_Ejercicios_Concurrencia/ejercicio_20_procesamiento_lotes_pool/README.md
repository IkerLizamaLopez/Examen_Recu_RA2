# Ejercicio 20: Descarga en Paralelo de Lotes con Pool de Hilos (ThreadPoolExecutor)

### Enunciado
Implementa un procesador de tareas por lotes concurrente utilizando un pool de hilos (`concurrent.futures.ThreadPoolExecutor`).
- El sistema debe simular la descarga de datos desde 10 servidores web distintos de forma paralela.
- Define una funcion `descargar_servidor(servidor_id)` que:
  - Recibe el identificador del servidor.
  - Simula la descarga tardando un tiempo aleatorio entre 0.5 y 1.5 segundos.
  - Devuelve una cadena con el resultado: `"Exito desde Servidor-{servidor_id}"` o lanza una excepcion simulada si el id del servidor es multiplo de 5, para simular fallos de red.
- Configura el `ThreadPoolExecutor` con un **limite de 3 hilos de trabajo paralelos**.
- Utiliza el metodo `.submit()` para enviar las 10 tareas de descarga de forma no bloqueante.
- Almacena los objetos `Future` devueltos y, al finalizar, itera sobre ellos en el hilo principal utilizando `.result()` o `concurrent.futures.as_completed()` para capturar y mostrar los resultados exitosos y capturar/gestionar adecuadamente las excepciones producidas por los servidores caidos.
