# Ejercicio 06: Peaje de Autopista (Semaforo Acotado)

### Enunciado
Implementa un simulador de peaje de autopista.
- El peaje dispone de exactamente 2 cabinas de pago activas.
- Habra 8 vehiculos (hilos) circulando que deben cruzar el peaje obligatoriamente.
- Cada vehiculo que llega intenta ocupar una cabina libre. Si ambas estan ocupadas, espera haciendo cola.
- El proceso de pago en la cabina tarda entre 0.5 y 1.5 segundos.
- Utiliza `threading.Semaphore` (o un `threading.BoundedSemaphore` para evitar que llamadas extranas a `.release()` desborden el limite inicial) configurado con un limite de 2 cabinas.
- Imprime eventos detallados sobre que vehiculo esta esperando, cual esta pagando en que momento y cuando deja la cabina libre.
