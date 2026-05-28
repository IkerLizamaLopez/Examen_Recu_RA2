"""
EJERCICIO 06: Aforo - Semaphore (NIVEL SUAVE)
Usa Semaphore para controlar capacidad maxima
"""

import threading
import time

semaforo = threading.Semaphore(2)  # Capacidad para 2 personas

def cliente(id_cliente):
    print(f"Cliente {id_cliente} esperando entrada...")
    
    with semaforo:
        print(f"Cliente {id_cliente} DENTRO del local")
        time.sleep(2)  # Simula estar dentro
        print(f"Cliente {id_cliente} SALIENDO del local")

if __name__ == "__main__":
    print("=== Control de Aforo con Semaphore ===")
    print("Capacidad maxima: 2 personas")
    print("")
    
    hilos = []
    for i in range(1, 6):
        h = threading.Thread(target=cliente, args=(i,))
        hilos.append(h)
        h.start()
    
    for h in hilos:
        h.join()
    
    print("")
    print("Todos los clientes procesados")
