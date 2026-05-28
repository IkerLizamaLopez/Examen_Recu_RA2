"""
EJERCICIO 06: Fabrica Ensamblador (NIVEL AVANZADO)
"""

import threading
import time

inventario = {'ruedas': 0, 'motores': 0, 'bastidor': 0}
condition = threading.Condition()

def productor_ruedas():
    for i in range(6):
        with condition:
            inventario['ruedas'] += 1
            print(f"Productor ruedas: produce rueda ({inventario})")
            condition.notify_all()
        time.sleep(0.3)

def productor_motores():
    for i in range(3):
        with condition:
            inventario['motores'] += 1
            print(f"Productor motores: produce motor ({inventario})")
            condition.notify_all()
        time.sleep(0.5)

def productor_bastidor():
    for i in range(3):
        with condition:
            inventario['bastidor'] += 1
            print(f"Productor bastidor: produce bastidor ({inventario})")
            condition.notify_all()
        time.sleep(0.5)

def ensamblador():
    para_ensamblar = 0
    while para_ensamblar < 3:
        with condition:
            while inventario['ruedas'] < 2 or inventario['motores'] < 1 or inventario['bastidor'] < 1:
                print(f"Ensamblador espera (inventario: {inventario})")
                condition.wait()
            
            inventario['ruedas'] -= 2
            inventario['motores'] -= 1
            inventario['bastidor'] -= 1
            para_ensamblar += 1
            
            print(f"Ensamblador ensambla vehiculo {para_ensamblar} (quedan: {inventario})")
            condition.notify_all()

if __name__ == "__main__":
    print("=== Fabrica - Ensamblador ===\n")
    
    h1 = threading.Thread(target=productor_ruedas)
    h2 = threading.Thread(target=productor_motores)
    h3 = threading.Thread(target=productor_bastidor)
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
