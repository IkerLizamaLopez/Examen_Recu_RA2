"""
EJERCICIO 14: Eventos de Coordinacion (NIVEL INTERMEDIO)
"""

import threading
import time

evento_inicio = threading.Event()
evento_fin = threading.Event()

def trabajador(id_trab):
    print(f"Trabajador {id_trab} esperando inicio...")
    evento_inicio.wait()
    
    print(f"Trabajador {id_trab} trabajando...")
    time.sleep(1)
    
    print(f"Trabajador {id_trab} espera confirmacion de fin")
    evento_fin.wait()
    
    print(f"Trabajador {id_trab} completado")

def coordinador():
    print("Coordinador esperando 2 segundos...")
    time.sleep(2)
    
    print("\nCordinador: INICIO!")
    evento_inicio.set()
    
    print("Coordinador esperando 3 segundos...")
    time.sleep(3)
    
    print("Coordinador: FIN!")
    evento_fin.set()

if __name__ == "__main__":
    print("=== Eventos de Coordinacion ===\n")
    
    h1 = threading.Thread(target=coordinador)
    h2 = threading.Thread(target=trabajador, args=(1,))
    h3 = threading.Thread(target=trabajador, args=(2,))
    
    h1.start()
    h2.start()
    h3.start()
    
    h1.join()
    h2.join()
    h3.join()
    
    print("\nCompletado")
