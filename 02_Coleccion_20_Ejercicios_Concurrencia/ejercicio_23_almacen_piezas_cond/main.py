"""
EJERCICIO 23: Almacen de Piezas y Ensamblado (Condition)
Enunciado:
Simula un almacen de piezas con dos productores (A y B) y un ensamblador.
Se requiere 1 pieza A y 1 pieza B para crear un producto.
Usa Condition para esperar y notificar de forma eficiente.
"""

import threading
import time
import random

# Almacen compartido
piezas_A = 0
piezas_B = 0
paquetes_creados = 0
limite_paquetes = 5
simulacion_activa = True

# Sincronizacion
cond_almacen = threading.Condition()
print_lock = threading.Lock()

def productor_A():
    global piezas_A, simulacion_activa
    while simulacion_activa:
        time.sleep(0.5)
        with cond_almacen:
            if not simulacion_activa:
                break
            piezas_A += 1
            with print_lock:
                print(f"[PRODUCTOR A] Anade pieza A. Almacen: (A: {piezas_A} | B: {piezas_B})")
            cond_almacen.notify_all()

def productor_B():
    global piezas_B, simulacion_activa
    while simulacion_activa:
        time.sleep(0.7)
        with cond_almacen:
            if not simulacion_activa:
                break
            piezas_B += 1
            with print_lock:
                print(f"[PRODUCTOR B] Anade pieza B. Almacen: (A: {piezas_A} | B: {piezas_B})")
            cond_almacen.notify_all()

def ensamblador():
    global piezas_A, piezas_B, paquetes_creados, simulacion_activa
    while paquetes_creados < limite_paquetes:
        with cond_almacen:
            # Esperar mientras no haya al menos 1 pieza A y 1 pieza B
            while (piezas_A < 1 or piezas_B < 1) and simulacion_activa:
                with print_lock:
                    print(f"[ENSAMBLADOR] Esperando piezas... Almacen: (A: {piezas_A} | B: {piezas_B})")
                cond_almacen.wait()
                
            if not simulacion_activa:
                break
                
            # Consumir piezas
            piezas_A -= 1
            piezas_B -= 1
            paquetes_creados += 1
            
            with print_lock:
                print(f"[ENSAMBLADO] Paquete #{paquetes_creados} creado con exito! Almacen restante: (A: {piezas_A} | B: {piezas_B})")
                
            if paquetes_creados >= limite_paquetes:
                print(f"[SISTEMA] Se ha alcanzado el limite de {limite_paquetes} paquetes. Finalizando...")
                simulacion_activa = False
                cond_almacen.notify_all()
                break

if __name__ == "__main__":
    print("=== INICIANDO LINEA DE ENSAMBLADO CON VARIABLES DE CONDICION ===")
    
    h_A = threading.Thread(target=productor_A, name="ProdA")
    h_B = threading.Thread(target=productor_B, name="ProdB")
    h_ens = threading.Thread(target=ensamblador, name="Ensamblador")
    
    h_A.start()
    h_B.start()
    h_ens.start()
    
    h_ens.join()
    
    # Asegurar apagado de productores
    with cond_almacen:
        simulacion_activa = False
        cond_almacen.notify_all()
        
    h_A.join()
    h_B.join()
    
    print("\n=== Simulación finalizada con éxito. ===")
