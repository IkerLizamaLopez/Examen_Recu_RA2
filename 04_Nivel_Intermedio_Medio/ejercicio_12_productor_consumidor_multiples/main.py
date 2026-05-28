"""
EJERCICIO 12: Productor-Consumidor Multiples Avanzado (NIVEL INTERMEDIO)
"""

import threading
import time
from queue import Queue

colas = {
    'A': Queue(),
    'B': Queue(),
}

def productor(id_prod, tipo):
    for i in range(3):
        dato = f"P{id_prod}-{tipo}-{i}"
        colas[tipo].put(dato)
        print(f"Productor {id_prod} genera {dato} en cola {tipo}")
        time.sleep(0.3)

def consumidor(id_cons, tipo):
    for i in range(3):
        dato = colas[tipo].get()
        print(f"Consumidor {id_cons} consume {dato} de cola {tipo}")
        time.sleep(0.4)

if __name__ == "__main__":
    print("=== Multiples Colas - Productor/Consumidor ===\n")
    
    h1 = threading.Thread(target=productor, args=(1, 'A'))
    h2 = threading.Thread(target=productor, args=(2, 'B'))
    h3 = threading.Thread(target=consumidor, args=(1, 'A'))
    h4 = threading.Thread(target=consumidor, args=(2, 'B'))
    
    h1.start()
    h2.start()
    h3.start()
    h4.start()
    
    h1.join()
    h2.join()
    h3.join()
    h4.join()
    
    print("\nCompletado")
