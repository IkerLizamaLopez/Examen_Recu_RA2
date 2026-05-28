# Ejercicio 15: Cruce de Peatones Inteligente (Events)

### Enunciado
Implementa un simulador de trafico inteligente regulado por un paso de peatones con pulsador de solicitud de cruce.
- Habra 4 hilos **Coche** que circulan constantemente en bucle por una via.
- Habra un hilo **ControladorSemaforo** que regula si los coches pueden circular o no mediante un evento `semaforo_verde = threading.Event()`.
  - Cuando `semaforo_verde` esta activo (`set`), los coches circulan normalmente con impresiones de paso.
  - Cuando `semaforo_verde` esta inactivo (`clear`), el semaforo esta en rojo y los coches que lleguen deben detenerse y esperar llamando a `.wait()`.
- Habra 1 hilo **Peaton** que, despues de 1.5 segundos de simulacion, pulsa el boton de solicitud:
  - Al pulsar, el controlador pone el semaforo en rojo (`clear`) durante 2.0 segundos para que el peaton cruce con seguridad.
  - Los coches se detienen.
  - Transcurridos los 2.0 segundos de cruce, el controlador vuelve a poner el semaforo en verde (`set`) para restaurar la circulacion de vehiculos.
- Utiliza `threading.Event` para esta coordinacion.
