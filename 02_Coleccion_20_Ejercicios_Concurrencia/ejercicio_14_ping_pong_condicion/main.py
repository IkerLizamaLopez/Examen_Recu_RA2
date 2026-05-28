"""
EJERCICIO 14: Ping-Pong Alternado (Condition)
Enunciado:
Implementa el juego alternado Ping-Pong utilizando una sola variable Condition.
Coordinar la alternancia mediante una variable de estado de turno compartida.
"""

import threading
import time

# Variable de estado compartida
turno = "PING"
iteraciones = 5

# Sincronizacion
condicion_juego = threading.Condition()

def jugador_ping():
    global turno
    for i in range(1, iteraciones + 1):
        with condicion_juego:
            # Esperar a que sea el turno de PING
            while turno != "PING":
                condicion_juego.wait()
                
            print(f" [PONG-COND-GAME] PING ({i}/{iteraciones})")
            time.sleep(0.3)
            
            # Cambiar turno al rival y notificar
            turno = "PONG"
            condicion_juego.notify_all()

def jugador_pong():
    global turno
    for i in range(1, iteraciones + 1):
        with condicion_juego:
            # Esperar a que sea el turno de PONG
            while turno != "PONG":
                condicion_juego.wait()
                
            print(f" [PONG-COND-GAME] PONG ({i}/{iteraciones})")
            time.sleep(0.3)
            
            # Cambiar turno al rival y notificar
            turno = "PING"
            condicion_juego.notify_all()

if __name__ == "__main__":
    print("Iniciando juego de Ping-Pong con Variable de Condicion...")
    
    t_ping = threading.Thread(target=jugador_ping, name="Jugador-Ping")
    t_pong = threading.Thread(target=jugador_pong, name="Jugador-Pong")
    
    t_ping.start()
    t_pong.start()
    
    t_ping.join()
    t_pong.join()
    
    print("\n Partido terminado. Excelente coordinacion!")
