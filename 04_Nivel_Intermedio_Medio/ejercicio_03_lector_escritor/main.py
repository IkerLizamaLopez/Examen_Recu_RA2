"""
EJERCICIO 03: Lector-Escritor (NIVEL INTERMEDIO)
"""

import threading
import time

recurso = "Dato inicial"
lock = threading.Lock()
lock_lectores = threading.Lock()
num_lectores = 0

def lector(id_lector):
    global num_lectores
    
    for i in range(3):
        with lock_lectores:
            num_lectores += 1
            if num_lectores == 1:
                lock.acquire()
        
        print(f"Lector {id_lector} leyendo: '{recurso}'")
        time.sleep(0.5)
        
        with lock_lectores:
            num_lectores -= 1
            if num_lectores == 0:
                lock.release()

def escritor(id_escr):
    global recurso
    
    for i in range(2):
        with lock:
            recurso = f"Dato escrito por E{id_escr}-{i}"
            print(f"Escritor {id_escr} escribe: '{recurso}'")
            time.sleep(0.5)

if __name__ == "__main__":
    print("=== Problema Lector-Escritor ===\n")
    
    lectores = [threading.Thread(target=lector, args=(i,)) for i in range(1, 4)]
    escritores = [threading.Thread(target=escritor, args=(i,)) for i in range(1, 3)]
    
    for h in lectores + escritores:
        h.start()
    
    for h in lectores + escritores:
        h.join()
    
    print("\nCompletado")
