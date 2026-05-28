"""
EJERCICIO 01: Filosofos Comensales (NIVEL AVANZADO)
Problema clasico - evita deadlock con jerarquia de recursos
"""

import threading
import time

NUM_FILOSOFOS = 5

# Un lock por tenedor
tenedores = [threading.Lock() for _ in range(NUM_FILOSOFOS)]

def filosofo(id_fil):
    for i in range(2):
        # Pensar
        print(f"Filosofo {id_fil} piensa")
        time.sleep(1)
        
        # Intentar comer - adquirir tenedores en orden (jerarquia)
        tenedor_izq = id_fil
        tenedor_der = (id_fil + 1) % NUM_FILOSOFOS
        
        # Siempre adquirir el menor ID primero (jerarquia)
        if tenedor_izq < tenedor_der:
            primero, segundo = tenedor_izq, tenedor_der
        else:
            primero, segundo = tenedor_der, tenedor_izq
        
        print(f"Filosofo {id_fil} intenta comer (tenedor {primero}, {segundo})")
        
        with tenedores[primero]:
            with tenedores[segundo]:
                print(f"Filosofo {id_fil} COME")
                time.sleep(1)
                print(f"Filosofo {id_fil} termina de comer")

if __name__ == "__main__":
    print("=== Filosofos Comensales (5 filosofos) ===\n")
    
    hilos = [threading.Thread(target=filosofo, args=(i,)) for i in range(NUM_FILOSOFOS)]
    
    for h in hilos:
        h.start()
    
    for h in hilos:
        h.join()
    
    print("\nCompletado (sin deadlock)")
