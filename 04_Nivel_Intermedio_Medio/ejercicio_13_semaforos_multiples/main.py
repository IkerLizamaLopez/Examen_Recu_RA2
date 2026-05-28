"""
EJERCICIO 13: Semaforos Multiples (NIVEL INTERMEDIO)
"""

import threading
import time
import random

semaforos = {
    'impresora1': threading.Semaphore(1),
    'impresora2': threading.Semaphore(1),
    'impresora3': threading.Semaphore(1),
}

def trabajador(id_trab):
    impresoras = list(semaforos.keys())
    
    for i in range(2):
        imp = random.choice(impresoras)
        print(f"Trabajador {id_trab} intenta usar {imp}")
        
        with semaforos[imp]:
            print(f"Trabajador {id_trab} usando {imp}")
            time.sleep(1)
            print(f"Trabajador {id_trab} termina {imp}")

if __name__ == "__main__":
    print("=== Semaforos Multiples (3 impresoras) ===\n")
    
    hilos = [threading.Thread(target=trabajador, args=(i,)) for i in range(1, 5)]
    
    for h in hilos:
        h.start()
    
    for h in hilos:
        h.join()
    
    print("\nCompletado")
