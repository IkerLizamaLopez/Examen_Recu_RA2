"""
EJERCICIO 04: Productores Multiples Coordinados (NIVEL INTERMEDIO)
"""

import threading
import time

storage = {'A': 0, 'B': 0, 'C': 0}
condition = threading.Condition()

def productor(tipo):
    for i in range(3):
        with condition:
            storage[tipo] += 1
            print(f"Productor {tipo}: Genera {tipo} (stock: {storage})")
            condition.notify_all()
        time.sleep(0.3)

def ensamblador():
    for i in range(3):
        with condition:
            while storage['A'] < 1 or storage['B'] < 1 or storage['C'] < 1:
                print(f"Ensamblador espera (stock: {storage})")
                condition.wait()
            
            storage['A'] -= 1
            storage['B'] -= 1
            storage['C'] -= 1
            print(f"Ensamblador ensambla paquete {i+1} (quedan: {storage})")
            condition.notify_all()

if __name__ == "__main__":
    print("=== Productores Coordinados - Ensamblador ===\n")
    
    h1 = threading.Thread(target=productor, args=('A',))
    h2 = threading.Thread(target=productor, args=('B',))
    h3 = threading.Thread(target=productor, args=('C',))
    h4 = threading.Thread(target=ensamblador)
    
    h1.start()
    h2.start()
    h3.start()
    h4.start()
    
    h1.join()
    h2.join()
    h3.join()
    h4.join()
    
    print("\nCompletado")
