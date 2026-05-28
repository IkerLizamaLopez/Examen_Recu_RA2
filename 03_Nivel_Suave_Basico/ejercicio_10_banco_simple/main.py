"""
EJERCICIO 10: Banco Simple - Lock (NIVEL SUAVE)
Retiros seguros de una cuenta bancaria
"""

import threading
import time

saldo = 1000
lock = threading.Lock()

def retirar(id_hilo, cantidad):
    global saldo
    
    print(f"Hilo {id_hilo} retirando {cantidad}...")
    
    with lock:
        # Seccion critica protegida
        saldo_antes = saldo
        print(f"  Saldo antes: {saldo_antes}")
        
        time.sleep(1)  # Simula operacion del banco
        
        saldo = saldo - cantidad
        print(f"  Saldo despues: {saldo}")

if __name__ == "__main__":
    print("=== Cajero Automatico Seguro ===")
    print(f"Saldo inicial: {saldo}")
    print("")
    
    h1 = threading.Thread(target=retirar, args=(1, 300))
    h2 = threading.Thread(target=retirar, args=(2, 200))
    
    h1.start()
    h2.start()
    
    h1.join()
    h2.join()
    
    print("")
    print(f"Saldo final: {saldo}")
