"""
EJERCICIO 24: Operaciones en Cajero Automatico Seguro (Locks)
Enunciado:
Simula operaciones bancarias concurrentes sobre una cuenta compartida.
Usa un Lock para garantizar exclusion mutua y evitar saldos negativos.
"""

import threading
import time
import random

class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
        self.lock = threading.Lock()

    def retirar(self, cantidad, cliente_nombre):
        print(f"[SOLICITUD] {cliente_nombre} quiere retirar {cantidad} EUR.")
        time.sleep(random.uniform(0.1, 0.4))
        
        with self.lock:
            if self.saldo >= cantidad:
                saldo_previo = self.saldo
                self.saldo -= cantidad
                print(f"[RETIRADA EXITOSA] {cliente_nombre} saco {cantidad} EUR. Saldo previo: {saldo_previo} EUR -> Saldo actual: {self.saldo} EUR.")
                return True
            else:
                print(f"[RECHAZADA] {cliente_nombre} no pudo retirar {cantidad} EUR. Saldo insuficiente: {self.saldo} EUR.")
                return False

    def ingresar(self, cantidad, cliente_nombre):
        print(f"[SOLICITUD] {cliente_nombre} quiere ingresar {cantidad} EUR.")
        time.sleep(random.uniform(0.1, 0.4))
        
        with self.lock:
            saldo_previo = self.saldo
            self.saldo += cantidad
            print(f"[INGRESO EXITOSO] {cliente_nombre} ingreso {cantidad} EUR. Saldo previo: {saldo_previo} EUR -> Saldo actual: {self.saldo} EUR.")

def cliente_retirar_proceso(cuenta, id_cliente):
    nombre = f"ClienteRetira-{id_cliente}"
    cuenta.retirar(40, nombre)

def cliente_ingresar_proceso(cuenta, id_cliente):
    nombre = f"ClienteIngresa-{id_cliente}"
    cuenta.ingresar(50, nombre)

if __name__ == "__main__":
    print("=== SIMULACION DE CAJERO AUTOMATICO SEGURO CON LOCKS ===")
    cuenta = CuentaBancaria(100) # Saldo inicial 100 EUR
    
    hilos = []
    
    # Crear 4 clientes que retiran 40 EUR (Total demandas = 160 EUR)
    for i in range(1, 5):
        t = threading.Thread(target=cliente_retirar_proceso, args=(cuenta, i))
        hilos.append(t)
        
    # Crear 2 clientes que ingresan 50 EUR (Total ingresos = 100 EUR)
    for i in range(1, 3):
        t = threading.Thread(target=cliente_ingresar_proceso, args=(cuenta, i))
        hilos.append(t)
        
    # Iniciar en orden aleatorio
    random.shuffle(hilos)
    for t in hilos:
        t.start()
        
    for t in hilos:
        t.join()
        
    print(f"\n=== Simulación terminada. Saldo final en cuenta: {cuenta.saldo} EUR (Esperado: 40 EUR) ===")
