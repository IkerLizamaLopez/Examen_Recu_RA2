"""
EJERCICIO 05: Cola con Prioridad (NIVEL INTERMEDIO)
"""

import threading
import time
from queue import PriorityQueue

cola = PriorityQueue()

def pacientes():
    pacientes_list = [
        (3, "Juan - Leve"),
        (1, "Maria - Critico"),
        (2, "Pedro - Moderado"),
        (1, "Sofia - Critico"),
        (3, "Luis - Leve"),
    ]
    
    for prioridad, nombre in pacientes_list:
        cola.put((prioridad, nombre))
        print(f"Llega: {nombre}")
        time.sleep(0.5)

def medico():
    print("\nMedico atendiendo:\n")
    for _ in range(5):
        prioridad, nombre = cola.get()
        print(f"Atiende: {nombre}")
        time.sleep(1)

if __name__ == "__main__":
    print("=== Triaje Hospital - PriorityQueue ===\n")
    
    h1 = threading.Thread(target=pacientes)
    h2 = threading.Thread(target=medico)
    
    h1.start()
    h2.start()
    
    h1.join()
    h2.join()
    
    print("\nCompletado")
