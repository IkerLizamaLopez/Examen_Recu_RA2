# Ejercicio 19: Triaje de Urgencias Medicas (PriorityQueue)

### Enunciado
Implementa un sistema de gestion de la sala de espera de urgencias en un hospital utilizando una cola de prioridad thread-safe (`queue.PriorityQueue`).
- Los pacientes llegan al hospital con diferentes niveles de gravedad:
  - Gravedad 1: **Critico / Alta Prioridad** (ej. dolor toracico severo).
  - Gravedad 2: **Moderado / Media Prioridad** (ej. fractura de extremidad).
  - Gravedad 3: **Leve / Baja Prioridad** (ej. resfriado comun).
- Recuerda que `PriorityQueue` ordena los elementos de menor a mayor. Por tanto, el numero de gravedad mas bajo (1) se procesara primero de forma automatica.
- Varios hilos **Paciente** (productores) llegan al hospital en tiempos aleatorios y registran su nombre y nivel de prioridad en la cola compartida.
- Un hilo **Medico** (consumidor) atiende a los pacientes de uno en uno:
  - Extrae el paciente mas grave de la cola mediante `get()`.
  - Simula el tiempo de consulta medica segun la gravedad (por ejemplo, atender un caso critico lleva mas tiempo que una consulta leve).
  - Muestra claramente en la consola que paciente esta atendiendo y como la prioridad determina el orden, independientemente del orden de llegada.
- Envia una senal de parada especial al medico cuando todos los pacientes hayan sido atendidos.
