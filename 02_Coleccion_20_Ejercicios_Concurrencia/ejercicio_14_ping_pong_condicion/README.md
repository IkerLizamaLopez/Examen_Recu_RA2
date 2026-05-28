# Ejercicio 14: Ping-Pong Alternado (Condition)

### Enunciado
Resuelve de nuevo el problema de impresion alternada de "PING" y "PONG", pero esta vez empleando una **unica variable de condicion** (`threading.Condition`) y una **variable de estado compartida** (por ejemplo, una cadena de texto `turno = "PING"`).
- Habra 2 hilos que representan a los jugadores.
- El hilo **Ping** solo podra imprimir "PING" cuando `turno == "PING"`. En caso contrario, llamara a `wait()`.
- El hilo **Pong** solo podra imprimir "PONG" cuando `turno == "PONG"`. En caso contrario, llamara a `wait()`.
- Tras realizar la impresion, el hilo actual modifica la variable `turno` para otorgarle el paso al oponente y llama a `notify_all()`.
- Realiza 5 rondas completas y deten la ejecucion limpiamente.
