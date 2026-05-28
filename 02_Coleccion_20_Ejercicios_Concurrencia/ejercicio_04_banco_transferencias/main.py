"""
EJERCICIO 04: Banco y Transferencias Concurrentes (Prevencion de Deadlocks)
Enunciado:
Implementa un sistema de transferencia de dinero entre cuentas bancarias concurrentemente.
Evita el interbloqueo ordenando siempre las cuentas por su ID antes de adquirir los Locks.
"""

import threading
import time
import random

class CuentaBancaria:
    def __init__(self, id_cuenta, saldo_inicial):
        self.id = id_cuenta
        self.saldo = saldo_inicial
        self.lock = threading.Lock()

def transferir(origen, destino, cantidad):
    # Estrategia de prevencion de Deadlocks por adquisicion ordenada:
    # Siempre adquirimos el Lock de la cuenta con ID mas bajo primero.
    cuenta_primera = origen if origen.id < destino.id else destino
    cuenta_segunda = destino if origen.id < destino.id else origen
    
    print(f" [SOLICITUD] Transferencia de {cantidad}EUR desde {origen.id} hacia {destino.id}.")
    
    # Bloquear la primera cuenta ordenada
    with cuenta_primera.lock:
        print(f" [BLOQUEADA-1] Cuenta {cuenta_primera.id}")
        time.sleep(0.1) # Breve retardo para forzar condiciones de carrera/deadlock si no estuvieran ordenadas
        
        # Bloquear la segunda cuenta ordenada
        with cuenta_segunda.lock:
            print(f" [BLOQUEADA-2] Cuenta {cuenta_segunda.id}")
            
            # Ejecutar transferencia real
            if origen.saldo >= cantidad:
                origen.saldo -= cantidad
                destino.saldo += cantidad
                print(f" [EXITO] Transferidos {cantidad}EUR de {origen.id} a {destino.id}.")
            else:
                print(f" [FALLO] Fondos insuficientes en {origen.id} (Saldo: {origen.saldo}EUR).")
                
    print(f" [LIBERADAS] Cuentas {cuenta_primera.id} y {cuenta_segunda.id}")

if __name__ == "__main__":
    print("Iniciando simulacion de transferencias concurrentes...")
    
    # Crear tres cuentas
    cuenta_A = CuentaBancaria("Cuenta-A", 1000)
    cuenta_B = CuentaBancaria("Cuenta-B", 1000)
    cuenta_C = CuentaBancaria("Cuenta-C", 1000)
    
    hilos = []
    
    # Hilos que realizan transferencias concurrentes cruzadas (potencial Deadlock sin ordenacion)
    # A -> B y B -> A simultaneamente
    t1 = threading.Thread(target=transferir, args=(cuenta_A, cuenta_B, 100), name="Transf-1")
    t2 = threading.Thread(target=transferir, args=(cuenta_B, cuenta_A, 50), name="Transf-2")
    
    # B -> C y C -> B simultaneamente
    t3 = threading.Thread(target=transferir, args=(cuenta_B, cuenta_C, 200), name="Transf-3")
    t4 = threading.Thread(target=transferir, args=(cuenta_C, cuenta_B, 150), name="Transf-4")
    
    # A -> C y C -> A simultaneamente
    t5 = threading.Thread(target=transferir, args=(cuenta_A, cuenta_C, 300), name="Transf-5")
    t6 = threading.Thread(target=transferir, args=(cuenta_C, cuenta_A, 100), name="Transf-6")
    
    hilos.extend([t1, t2, t3, t4, t5, t6])
    
    for h in hilos:
        h.start()
        
    for h in hilos:
        h.join()
        
    print("\n Saldos Finales:")
    print(f"Saldo {cuenta_A.id}: {cuenta_A.saldo}EUR")
    print(f"Saldo {cuenta_B.id}: {cuenta_B.saldo}EUR")
    print(f"Saldo {cuenta_C.id}: {cuenta_C.saldo}EUR")
    print(f"Suma total del dinero en el banco: {cuenta_A.saldo + cuenta_B.saldo + cuenta_C.saldo}EUR (Esperado: 3000EUR)")
