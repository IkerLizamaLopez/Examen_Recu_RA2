"""
EJERCICIO 11: Carrera de Recursos (NIVEL INTERMEDIO)
"""

import threading
import time

semaforo = threading.Semaphore(2)

def cliente_taxi(id_cliente):
    print(f"Cliente {id_cliente} pidiendo taxi...")
    
    with semaforo:
        print(f"Cliente {id_cliente} sube al taxi")
        time.sleep(2)
        print(f"Cliente {id_cliente} baja del taxi")

if __name__ == "__main__":
    print("=== Carrera de Taxis (2 taxis, 5 clientes) ===\n")
    
    hilos = [threading.Thread(target=cliente_taxi, args=(i,)) for i in range(1, 6)]
    
    for h in hilos:
        h.start()
    
    for h in hilos:
        h.join()
    
    print("\nCompletado")
