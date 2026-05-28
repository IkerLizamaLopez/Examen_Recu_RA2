"""
EJERCICIO 05: Cola Simple - Queue (NIVEL SUAVE)
Productor-consumidor basico con queue.Queue
"""

import threading
import time
from queue import Queue

cola = Queue(maxsize=2)  # Cola con tamanio maximo 2

def productor():
    print("Productor: iniciando")
    for i in range(1, 6):
        print(f"Productor: generando {i}")
        cola.put(i)  # Pone el numero en la cola
        time.sleep(0.5)
    print("Productor: terminado")

def consumidor():
    print("Consumidor: iniciando")
    for i in range(1, 6):
        numero = cola.get()  # Extrae de la cola (espera si esta vacia)
        print(f"Consumidor: recibio {numero}")
        time.sleep(0.3)
    print("Consumidor: terminado")

if __name__ == "__main__":
    print("=== Productor-Consumidor Simple ===")
    print("")
    
    h1 = threading.Thread(target=productor)
    h2 = threading.Thread(target=consumidor)
    
    h1.start()
    h2.start()
    
    h1.join()
    h2.join()
    
    print("")
    print("Completado")
