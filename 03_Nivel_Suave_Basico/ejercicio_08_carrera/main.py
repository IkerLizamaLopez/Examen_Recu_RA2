"""
EJERCICIO 08: Carrera - Barrier (NIVEL SUAVE)
Sincroniza 4 atletas para salida simultanea
"""

import threading
import time

barrera = threading.Barrier(4)

def atleta(id_atleta):
    print(f"Atleta {id_atleta} preparando...")
    time.sleep(1)
    
    print(f"Atleta {id_atleta} listo en linea de salida")
    barrera.wait()  # Espera a que todos lleguen
    
    print(f"SALIDA! Atleta {id_atleta} corriendo")
    time.sleep(1)
    print(f"Atleta {id_atleta} cruzo la meta")

if __name__ == "__main__":
    print("=== Carrera con Barrier ===")
    print("4 atletas")
    print("")
    
    hilos = []
    for i in range(1, 5):
        h = threading.Thread(target=atleta, args=(i,))
        hilos.append(h)
        h.start()
    
    for h in hilos:
        h.join()
    
    print("")
    print("Carrera completada")
