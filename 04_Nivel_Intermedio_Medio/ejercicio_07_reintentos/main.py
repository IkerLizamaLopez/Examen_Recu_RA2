"""
EJERCICIO 07: Reintentos (NIVEL INTERMEDIO)
"""

import threading
import time
import random

lock = threading.Lock()

def cliente(id_cliente):
    max_intentos = 3
    intento = 0
    
    while intento < max_intentos:
        intento += 1
        print(f"Cliente {id_cliente} intenta acceder (intento {intento}/{max_intentos})")
        
        # 70% de probabilidad de fallo
        if random.random() < 0.7:
            print(f"Cliente {id_cliente} FALLO")
            time.sleep(0.5)
            continue
        
        # Exito
        with lock:
            print(f"Cliente {id_cliente} EXITO - accede al recurso")
            time.sleep(0.5)
            return
    
    print(f"Cliente {id_cliente} AGOTO REINTENTOS - se retira")

if __name__ == "__main__":
    print("=== Reintentos Limitados ===\n")
    
    hilos = [threading.Thread(target=cliente, args=(i,)) for i in range(1, 4)]
    
    for h in hilos:
        h.start()
    
    for h in hilos:
        h.join()
    
    print("\nCompletado")
