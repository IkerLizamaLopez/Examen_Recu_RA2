"""
EJERCICIO 09: Recursos Multiples Ordenados (NIVEL INTERMEDIO)
"""

import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def hilo_1():
    for i in range(3):
        print(f"Hilo 1 paso {i}: adquiriendo lock1")
        with lock1:
            print(f"Hilo 1 paso {i}: adquiriendo lock2")
            with lock2:
                print(f"Hilo 1 paso {i}: TIENE AMBOS LOCKS")
                time.sleep(0.5)
            print(f"Hilo 1 paso {i}: libera lock2")
        print(f"Hilo 1 paso {i}: libera lock1\n")

def hilo_2():
    for i in range(3):
        print(f"Hilo 2 paso {i}: adquiriendo lock1")
        with lock1:
            print(f"Hilo 2 paso {i}: adquiriendo lock2")
            with lock2:
                print(f"Hilo 2 paso {i}: TIENE AMBOS LOCKS")
                time.sleep(0.5)
            print(f"Hilo 2 paso {i}: libera lock2")
        print(f"Hilo 2 paso {i}: libera lock1\n")

if __name__ == "__main__":
    print("=== Jerarquia de Recursos (sin deadlock) ===\n")
    
    h1 = threading.Thread(target=hilo_1)
    h2 = threading.Thread(target=hilo_2)
    
    h1.start()
    h2.start()
    
    h1.join()
    h2.join()
    
    print("Completado (sin deadlock)")
