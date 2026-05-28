"""
EJERCICIO 06: Timeout - Espera con Limite (NIVEL INTERMEDIO)
"""

import threading
import time
from queue import Queue, Empty

cola = Queue()

def productor():
    for i in range(3):
        print(f"Productor: genera {i}")
        cola.put(i)
        time.sleep(1)

def consumidor():
    for i in range(5):
        try:
            valor = cola.get(timeout=2.0)
            print(f"Consumidor: recibe {valor}")
        except Empty:
            print(f"Consumidor: TIMEOUT - no hay datos")
        time.sleep(0.5)

if __name__ == "__main__":
    print("=== Timeout - Cola.get() ===\n")
    
    h1 = threading.Thread(target=productor)
    h2 = threading.Thread(target=consumidor)
    
    h1.start()
    h2.start()
    
    h1.join()
    h2.join()
    
    print("\nCompletado")
