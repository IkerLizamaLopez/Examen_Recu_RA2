"""
EJERCICIO 13: Ping-Pong Alternado (Events)
Enunciado:
Implementa un juego de Ping-Pong alternado perfecto utilizando eventos (threading.Event).
Usa dos eventos de modo que los hilos Ping y Pong impriman de manera estrictamente alternada.
"""

import threading
import time

# Crear dos eventos
event_ping = threading.Event()
event_pong = threading.Event()

iteraciones = 5

def hilo_ping():
    for i in range(1, iteraciones + 1):
        # Esperar a que toque PING (en la primera vuelta arranca activo)
        event_ping.wait()
        
        print(f" [PONG-PONG-GAME] PING ({i}/{iteraciones})")
        time.sleep(0.3) # Simular pequeno tiempo de juego
        
        # Limpiar nuestro evento para la proxima ronda
        event_ping.clear()
        # Activar el evento del oponente (PONG)
        event_pong.set()

def hilo_pong():
    for i in range(1, iteraciones + 1):
        # Esperar a que toque PONG
        event_pong.wait()
        
        print(f" [PONG-PONG-GAME] PONG ({i}/{iteraciones})")
        time.sleep(0.3)
        
        # Limpiar nuestro evento
        event_pong.clear()
        # Activar el evento del oponente (PING)
        event_ping.set()

if __name__ == "__main__":
    print("Iniciando juego de Ping-Pong con Eventos (5 rondas)...")
    
    t_ping = threading.Thread(target=hilo_ping, name="Hilo-Ping")
    t_pong = threading.Thread(target=hilo_pong, name="Hilo-Pong")
    
    t_ping.start()
    t_pong.start()
    
    # Arrancar el juego disparando el primer evento de PING
    event_ping.set()
    
    t_ping.join()
    t_pong.join()
    
    print("\n Fin del juego. Ha sido una gran partida!")
