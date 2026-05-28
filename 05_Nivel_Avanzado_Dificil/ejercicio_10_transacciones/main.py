"""
EJERCICIO 10: Transacciones Bancarias (NIVEL AVANZADO)
"""

import threading
import time
import random

cuentas = [1000, 1000, 1000]  # 3 cuentas
locks = [threading.Lock() for _ in range(3)]

def transferencia(id_cliente, desde, hacia, cantidad):
    print(f"Cliente {id_cliente} intenta transferir {cantidad} de cuenta {desde} a {hacia}")
    
    # Ordenar locks para evitar deadlock (siempre de menor a mayor)
    if desde < hacia:
        lock1, lock2 = locks[desde], locks[hacia]
        c1, c2 = desde, hacia
    else:
        lock1, lock2 = locks[hacia], locks[desde]
        c1, c2 = hacia, desde
    
    with lock1:
        with lock2:
            if cuentas[desde] >= cantidad:
                cuentas[desde] -= cantidad
                cuentas[hacia] += cantidad
                print(f"Cliente {id_cliente} EXITO: {cantidad} transferidos (cuentas: {cuentas})")
            else:
                print(f"Cliente {id_cliente} FALLO: saldo insuficiente")
    
    time.sleep(0.2)

def cliente(id_cliente):
    for i in range(3):
        desde = random.randint(0, 2)
        hacia = random.randint(0, 2)
        
        if desde == hacia:
            hacia = (hacia + 1) % 3
        
        cantidad = random.randint(50, 200)
        transferencia(id_cliente, desde, hacia, cantidad)

if __name__ == "__main__":
    print("=== Transacciones Bancarias Concurrentes ===\n")
    print(f"Saldos iniciales: {cuentas}\n")
    
    hilos = [threading.Thread(target=cliente, args=(i,)) for i in range(1, 6)]
    
    for h in hilos:
        h.start()
    
    for h in hilos:
        h.join()
    
    print(f"\nSaldos finales: {cuentas}")
    print(f"Total: {sum(cuentas)} (debe ser 3000)")
