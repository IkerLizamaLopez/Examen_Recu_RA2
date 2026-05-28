"""
EJERCICIO 08: Deadlock Recovery (NIVEL AVANZADO)
"""

import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()

def hilo_1():
    for intento in range(3):
        print(f"Hilo 1 intento {intento + 1}")
        
        if not lock1.acquire(timeout=1.0):
            print("Hilo 1 TIMEOUT en lock1, reintenta...")
            continue
        
        try:
            print("Hilo 1 tiene lock1")
            time.sleep(0.3)
            
            if not lock2.acquire(timeout=1.0):
                print("Hilo 1 TIMEOUT en lock2, libera lock1")
                continue
            
            try:
                print("Hilo 1 tiene AMBOS locks")
                time.sleep(0.5)
            finally:
                lock2.release()
        finally:
            lock1.release()

def hilo_2():
    for intento in range(3):
        print(f"Hilo 2 intento {intento + 1}")
        
        if not lock2.acquire(timeout=1.0):
            print("Hilo 2 TIMEOUT en lock2, reintenta...")
            continue
        
        try:
            print("Hilo 2 tiene lock2")
            time.sleep(0.3)
            
            if not lock1.acquire(timeout=1.0):
                print("Hilo 2 TIMEOUT en lock1, libera lock2")
                continue
            
            try:
                print("Hilo 2 tiene AMBOS locks")
                time.sleep(0.5)
            finally:
                lock1.release()
        finally:
            lock2.release()

if __name__ == "__main__":
    print("=== Deadlock Recovery con Timeout ===\n")
    
    h1 = threading.Thread(target=hilo_1)
    h2 = threading.Thread(target=hilo_2)
    
    h1.start()
    h2.start()
    
    h1.join()
    h2.join()
    
    print("\nCompletado (sin deadlock)")
