"""
EJERCICIO 03: Bandera - Event (NIVEL SUAVE)
Usa Event para comunicar entre hilos
"""

import threading
import time

evento = threading.Event()

def hilo_esperador():
    print("Hilo 1 esperando la bandera...")
    evento.wait()  # Espera hasta que se active el evento
    print("Hilo 1 continua (evento activado)")

def hilo_productor():
    print("Hilo 2 trabajando...")
    time.sleep(2)  # Simula trabajo
    print("Hilo 2 termina - activando evento")
    evento.set()  # Activa el evento

if __name__ == "__main__":
    print("=== Comunicacion con Event ===")
    print("")
    
    h1 = threading.Thread(target=hilo_esperador)
    h2 = threading.Thread(target=hilo_productor)
    
    h1.start()
    h2.start()
    
    h1.join()
    h2.join()
    
    print("")
    print("Ambos hilos completados")
