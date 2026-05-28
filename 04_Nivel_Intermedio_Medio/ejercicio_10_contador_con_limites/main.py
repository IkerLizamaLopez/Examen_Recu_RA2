"""
EJERCICIO 10: Contador con Limites (NIVEL INTERMEDIO)
"""

import threading
import time

contador = 50
condition = threading.Condition()

def incrementar(id_hilo):
    global contador
    for i in range(5):
        with condition:
            while contador >= 100:
                print(f"Hilo {id_hilo} espera (contador=100)")
                condition.wait()
            contador += 10
            print(f"Hilo {id_hilo} incrementa a {contador}")
            condition.notify_all()
        time.sleep(0.2)

def decrementar(id_hilo):
    global contador
    for i in range(5):
        with condition:
            while contador <= 0:
                print(f"Hilo {id_hilo} espera (contador=0)")
                condition.wait()
            contador -= 10
            print(f"Hilo {id_hilo} decrementa a {contador}")
            condition.notify_all()
        time.sleep(0.2)

if __name__ == "__main__":
    print("=== Contador Limitado [0-100] ===\n")
    
    h1 = threading.Thread(target=incrementar, args=(1,))
    h2 = threading.Thread(target=decrementar, args=(1,))
    h3 = threading.Thread(target=incrementar, args=(2,))
    
    h1.start()
    h2.start()
    h3.start()
    
    h1.join()
    h2.join()
    h3.join()
    
    print(f"\nContador final: {contador}")
