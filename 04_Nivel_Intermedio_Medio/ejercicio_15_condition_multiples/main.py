"""
EJERCICIO 15: Condition Variables Multiples (NIVEL INTERMEDIO)
"""

import threading
import time

# Orden de ejecucion
orden = 1
condition = threading.Condition()

def tarea(id_tarea, numero_esperado):
    global orden
    
    with condition:
        while orden != numero_esperado:
            print(f"Tarea {id_tarea} esperando (orden actual={orden})")
            condition.wait()
        
        print(f"Tarea {id_tarea} ejecutando")
        time.sleep(0.5)
        orden += 1
        print(f"Tarea {id_tarea} termina (avanza orden a {orden})")
        condition.notify_all()

if __name__ == "__main__":
    print("=== Condition - Orden de Ejecucion ===\n")
    
    h1 = threading.Thread(target=tarea, args=(1, 1))
    h2 = threading.Thread(target=tarea, args=(2, 2))
    h3 = threading.Thread(target=tarea, args=(3, 3))
    
    # Iniciar en orden aleatorio
    h2.start()
    h3.start()
    h1.start()
    
    h1.join()
    h2.join()
    h3.join()
    
    print("\nCompletado")
