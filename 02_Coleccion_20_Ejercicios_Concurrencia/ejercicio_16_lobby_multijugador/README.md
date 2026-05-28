# Ejercicio 16: Lobby de Partida Multijugador (Barriers)

### Enunciado
Implementa un lobby de emparejamiento para una partida multijugador online.
- Una partida requiere exactamente **4 jugadores** conectados para comenzar.
- Habra 4 hilos **Jugador** que se conectan al servidor tras realizar la carga de recursos de su cliente a intervalos aleatorios (simulados con sleep).
- Al conectarse al lobby, el jugador indica que esta listo, pero debe esperar obligatoriamente a que los otros 3 jugadores tambien esten listos.
- Utiliza `threading.Barrier` configurada para 4 hilos para sincronizar el inicio del juego.
- Cuando se conecte el cuarto jugador, la barrera se rompera, se llamara a una funcion de accion colectiva ("Comenzando partida...") y todos los hilos continuaran su ejecucion en paralelo dentro de la partida.
