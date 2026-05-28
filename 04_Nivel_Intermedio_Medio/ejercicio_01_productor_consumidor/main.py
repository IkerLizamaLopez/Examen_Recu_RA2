"""
EJERCICIO 01: Productor-Consumidor Avanzado (NIVEL INTERMEDIO)
"""

import threading
import time
from queue import Queue

cola = Queue()

def productor(id_prod, rango_inicio, rango_fin):
    for i in range(rango_inicio, rango_fin + 1):
        print(f"Productor {id_prod}: Genera {i}")
        cola.put(i)
        time.sleep(0.2)
    cola.put(None)  # Senial de fin

def consumidor(id_cons):
    while True:
        valor = cola.get()
        if valor is None:
            cola.put(None)  # Pasar la senial a otro consumidor
            break
        print(f"Consumidor {id_cons}: Recibe {valor}")
        time.sleep(0.3)

if __name__ == "__main__":
    print("=== Productor-Consumidor Multiples ===\n")
    
    h1 = threading.Thread(target=productor, args=(1, 1, 5))
    h2 = threading.Thread(target=productor, args=(2, 6, 10))
    h3 = threading.Thread(target=consumidor, args=(1,))
    h4 = threading.Thread(target=consumidor, args=(2,))
    
    h1.start()
    h2.start()
    h3.start()
    h4.start()
    
    h1.join()
    h2.join()
    h3.join()
    h4.join()
    
    print("\nCompletado")
