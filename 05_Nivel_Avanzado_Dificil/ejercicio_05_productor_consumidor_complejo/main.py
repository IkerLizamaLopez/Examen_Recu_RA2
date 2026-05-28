"""
EJERCICIO 05: Productor-Consumidor Complejo (NIVEL AVANZADO)
"""

import threading
import time
from queue import Queue

colas = [Queue() for _ in range(3)]
condition = threading.Condition()

def productor(id_prod):
    for i in range(9):
        cola_id = i % len(colas)
        dato = f"P{id_prod}-{i}"
        colas[cola_id].put(dato)
        print(f"Productor {id_prod} produce {dato} en cola {cola_id}")
        time.sleep(0.2)
    colas[0].put(None)  # Senial

def consumidor(id_cons, cola_id):
    contador = 0
    while True:
        dato = colas[cola_id].get()
        if dato is None:
            print(f"Consumidor {id_cons} completado ({contador} items)")
            break
        print(f"Consumidor {id_cons} consume {dato} de cola {cola_id}")
        contador += 1
        time.sleep(0.3)

if __name__ == "__main__":
    print("=== Productor-Consumidor Complejo (3 productores, 3 colas) ===\n")
    
    hilos = []
    
    for i in range(1, 4):
        h = threading.Thread(target=productor, args=(i,))
        hilos.append(h)
        h.start()
    
    for i in range(1, 4):
        h = threading.Thread(target=consumidor, args=(i, i-1))
        hilos.append(h)
        h.start()
    
    for h in hilos:
        h.join()
    
    print("\nCompletado")
