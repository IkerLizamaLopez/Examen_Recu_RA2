"""
EJERCICIO 07: Impresoras Simples (NIVEL SUAVE)
Usa Semaphore para limitar impresoras + Lock para elegir cual
"""

import threading
import time

semaforo = threading.Semaphore(2)  # Max 2 impresoras
lock = threading.Lock()
impresoras = [False, False]  # False = disponible, True = en uso

def trabajador(id_trabajador):
    global impresoras
    
    print(f"Trabajador {id_trabajador} intentando imprimir...")
    
    with semaforo:  # Espera a que haya impresora disponible
        with lock:  # Busca cual impresora libre
            for i in range(2):
                if not impresoras[i]:
                    impresoras[i] = True
                    id_impresora = i + 1
                    break
        
        print(f"Trabajador {id_trabajador} usando impresora {id_impresora}")
        time.sleep(2)  # Simula imprimir
        
        with lock:
            impresoras[id_impresora - 1] = False  # Libera impresora
        
        print(f"Trabajador {id_trabajador} termino impresora {id_impresora}")

if __name__ == "__main__":
    print("=== Oficina con Impresoras Compartidas ===")
    print("Impresoras: 2")
    print("Trabajadores: 4")
    print("")
    
    hilos = []
    for i in range(1, 5):
        h = threading.Thread(target=trabajador, args=(i,))
        hilos.append(h)
        h.start()
    
    for h in hilos:
        h.join()
    
    print("")
    print("Todos los trabajadores completados")
