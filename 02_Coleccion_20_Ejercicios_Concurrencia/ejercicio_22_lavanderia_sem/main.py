"""
EJERCICIO 22: La Lavanderia Autoservicio (Semaphoros)
Enunciado:
Simula una lavanderia con 4 lavadoras y 8 clientes.
Usa Semaphore para controlar el aforo y la asignacion de lavadoras libres de manera ordenada.
"""

import threading
import time
import random

# Aforo maximo (numero de lavadoras)
LAVADORAS_TOTALES = 4
semaforo_lavadoras = threading.Semaphore(LAVADORAS_TOTALES)
print_lock = threading.Lock()

def cliente_proceso(id_cliente):
    nombre = f"Cliente-{id_cliente}"
    
    # Tiempo de llegada aleatorio
    time.sleep(random.uniform(0.1, 1.0))
    
    with print_lock:
        print(f"[LLEGADA] {nombre} llega a la lavanderia con ropa sucia.")
        
    # Adquirir una lavadora (se bloquea si todas estan ocupadas)
    semaforo_lavadoras.acquire()
    
    with print_lock:
        # Mostramos las maquinas libres restantes en el semaforo
        print(f"[LAVADO] {nombre} ha ocupado una lavadora. (Lavadoras libres restantes: {semaforo_lavadoras._value})")
        
    # Simular tiempo de lavado
    time.sleep(random.uniform(0.8, 1.6))
    
    with print_lock:
        print(f"[SALIDA] {nombre} termina su lavado, retira la ropa y libera la lavadora.")
        
    # Liberar el recurso
    semaforo_lavadoras.release()

if __name__ == "__main__":
    print(f"=== SIMULACION DE LA LAVANDERIA AUTOSERVICIO (Max: {LAVADORAS_TOTALES} maquinas) ===")
    
    hilos = []
    for i in range(1, 9):
        t = threading.Thread(target=cliente_proceso, args=(i,))
        hilos.append(t)
        t.start()
        
    for t in hilos:
        t.join()
        
    print("\n=== Todos los clientes han lavado su ropa. Lavanderia cerrada. ===")
