"""
EJERCICIO 03: Puente Estrecho (NIVEL AVANZADO)
"""

import threading
import time

coches_norte = 0
coches_sur = 0
condition = threading.Condition()
sentido = 'norte'  # norte o sur

def coche_norte(id_coche):
    global coches_norte, sentido
    
    with condition:
        while sentido != 'norte' or coches_sur > 0:
            condition.wait()
        
        coches_norte += 1
        sentido = 'norte'
        print(f"Coche N{id_coche} ENTRA (norte: {coches_norte}, sur: {coches_sur})")
    
    time.sleep(1)  # Cruza
    
    with condition:
        coches_norte -= 1
        print(f"Coche N{id_coche} SALE (norte: {coches_norte}, sur: {coches_sur})")
        
        if coches_norte == 0:
            sentido = 'sur'
        
        condition.notify_all()

def coche_sur(id_coche):
    global coches_sur, sentido
    
    with condition:
        while sentido != 'sur' or coches_norte > 0:
            condition.wait()
        
        coches_sur += 1
        sentido = 'sur'
        print(f"Coche S{id_coche} ENTRA (norte: {coches_norte}, sur: {coches_sur})")
    
    time.sleep(1)  # Cruza
    
    with condition:
        coches_sur -= 1
        print(f"Coche S{id_coche} SALE (norte: {coches_norte}, sur: {coches_sur})")
        
        if coches_sur == 0:
            sentido = 'norte'
        
        condition.notify_all()

if __name__ == "__main__":
    print("=== Puente Estrecho (N-S) ===\n")
    
    hilos = []
    
    for i in range(1, 4):
        h = threading.Thread(target=coche_norte, args=(i,))
        hilos.append(h)
        h.start()
    
    for i in range(1, 4):
        h = threading.Thread(target=coche_sur, args=(i,))
        hilos.append(h)
        h.start()
    
    for h in hilos:
        h.join()
    
    print("\nCompletado")
