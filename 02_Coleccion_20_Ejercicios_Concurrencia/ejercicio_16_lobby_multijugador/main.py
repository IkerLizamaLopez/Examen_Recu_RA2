"""
EJERCICIO 16: Lobby de Partida Multijugador (Barriers)
Enunciado:
Simula un sistema de inicio de partida multijugador que requiere exactamente 4 jugadores.
Usa threading.Barrier para sincronizar a los hilos de modo que no comience el juego hasta estar todos listos.
"""

import threading
import time
import random

# Accion colectiva a ejecutar cuando se rompa la barrera (cuando se junten los 4 hilos)
def notificar_inicio_partida():
    print("\n [SERVIDOR] Lobby Completo! Emparejando jugadores y comenzando la partida en 3, 2, 1... \n")

# Crear una barrera de sincronizacion para 4 hilos
barrera_lobby = threading.Barrier(parties=4, action=notificar_inicio_partida)
print_lock = threading.Lock()

def jugador_proceso(id_jugador):
    nombre = f" Jugador-{id_jugador}"
    
    # Simular tiempo de carga del juego
    tiempo_carga = random.uniform(0.5, 2.0)
    time.sleep(tiempo_carga)
    
    with print_lock:
        print(f" {nombre} se ha cargado (t={tiempo_carga:.2f}s). Entrando al lobby de espera...")
        
    try:
        # Esperar en la barrera
        # wait() devuelve un indice unico de 0 a 3 a cada hilo que llega
        indice_llegada = barrera_lobby.wait()
        
        with print_lock:
            print(f"  {nombre} esta dentro de la partida! (Llego en posicion {indice_llegada})")
            
        # Simular juego activo por un breve instante
        time.sleep(1.0)
        
        with print_lock:
            print(f" {nombre} ha salido de la partida de forma segura.")
            
    except threading.BrokenBarrierError:
        print(f" Error: La barrera del lobby se rompio antes de completarse.")

if __name__ == "__main__":
    print("Iniciando Lobby de Matchmaking de 4 jugadores con Barreras...")
    
    hilos = []
    for i in range(1, 5):
        t = threading.Thread(target=jugador_proceso, args=(i,))
        hilos.append(t)
        t.start()
        
    for t in hilos:
        t.join()
        
    print("\n Servidor cerrado. Simulacion multijugador exitosa.")
