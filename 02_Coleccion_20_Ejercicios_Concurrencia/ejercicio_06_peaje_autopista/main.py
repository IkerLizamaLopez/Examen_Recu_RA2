"""
EJERCICIO 06: Peaje de Autopista (Semaforo Acotado)
Enunciado:
Implementa un simulador de peaje de autopista con exactamente 2 cabinas de pago activas.
Utiliza BoundedSemaphore para limitar el aforo de cabinas ocupadas de manera estricta.
"""

import threading
import time
import random

# Definimos 2 cabinas de pago en el peaje
CABINAS_LIMIT = 2
peaje_sem = threading.BoundedSemaphore(CABINAS_LIMIT)
print_lock = threading.Lock()

def vehiculo(id_vehiculo):
    nombre = f" Vehiculo-{id_vehiculo}"
    
    # Tiempo de viaje hasta el peaje
    time.sleep(random.uniform(0.1, 1.2))
    
    with print_lock:
        print(f" {nombre} se aproxima y hace cola en el peaje.")
        
    # Adquirir una cabina de pago
    peaje_sem.acquire()
    
    with print_lock:
        print(f" {nombre} entra a una cabina y empieza a pagar.")
        
    # Simular tiempo de transaccion
    time.sleep(random.uniform(0.5, 1.5))
    
    with print_lock:
        print(f" {nombre} ha pagado y abandona el peaje.")
        
    # Liberar la cabina para el proximo coche
    peaje_sem.release()

if __name__ == "__main__":
    print(f"Simulando Peaje de Autopista con {CABINAS_LIMIT} cabinas activas para 8 vehiculos...")
    
    hilos = []
    for i in range(1, 9):
        h = threading.Thread(target=vehiculo, args=(i,))
        hilos.append(h)
        h.start()
        
    for h in hilos:
        h.join()
        
    print("\n Todos los vehiculos han cruzado el peaje satisfactoriamente.")
