"""
EJERCICIO 09: Ping-Pong - Events (NIVEL SUAVE)
Alterna perfectamente entre dos hilos
"""

import threading

event_ping = threading.Event()
event_pong = threading.Event()

# Empieza Ping
event_ping.set()

def ping():
    for i in range(5):
        event_ping.wait()
        print("PING")
        event_ping.clear()
        event_pong.set()

def pong():
    for i in range(5):
        event_pong.wait()
        print("PONG")
        event_pong.clear()
        event_ping.set()

if __name__ == "__main__":
    print("=== Ping-Pong con Events ===")
    print("")
    
    h1 = threading.Thread(target=ping)
    h2 = threading.Thread(target=pong)
    
    h1.start()
    h2.start()
    
    h1.join()
    h2.join()
    
    print("")
    print("Completado")
