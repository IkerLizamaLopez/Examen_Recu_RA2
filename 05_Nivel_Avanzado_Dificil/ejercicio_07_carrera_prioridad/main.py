"""
EJERCICIO 07: Carrera con Prioridad (NIVEL AVANZADO)
Previene starvation con contador
"""

import threading
import time

contador_acceso = 0
contador_alta = 0
contador_baja = 0
lock = threading.Lock()

def tarea_alta_prioridad(id_tarea):
    global contador_acceso, contador_alta
    
    for i in range(3):
        with lock:
            contador_alta += 1
            if contador_acceso % 2 == 0:  # Prioridad
                contador_acceso += 1
                print(f"Alta {id_tarea} accede (acceso: {contador_acceso})")
                time.sleep(0.3)

def tarea_baja_prioridad(id_tarea):
    global contador_acceso, contador_baja
    
    for i in range(3):
        with lock:
            contador_baja += 1
            if contador_acceso % 2 == 1:  # Turno
                contador_acceso += 1
                print(f"Baja {id_tarea} accede (acceso: {contador_acceso})")
                time.sleep(0.3)

if __name__ == "__main__":
    print("=== Carrera con Prioridad (sin starvation) ===\n")
    
    hilos = []
    
    for i in range(1, 3):
        h = threading.Thread(target=tarea_alta_prioridad, args=(i,))
        hilos.append(h)
        h.start()
    
    for i in range(1, 3):
        h = threading.Thread(target=tarea_baja_prioridad, args=(i,))
        hilos.append(h)
        h.start()
    
    for h in hilos:
        h.join()
    
    print(f"\nCompletado")
