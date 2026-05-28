"""
EJERCICIO 08: Pool de Hilos (NIVEL INTERMEDIO)
"""

import time
from concurrent.futures import ThreadPoolExecutor

def descargar(id_tarea):
    print(f"Tarea {id_tarea} comenzando descarga")
    time.sleep(2)
    print(f"Tarea {id_tarea} completada")
    return f"Resultado-{id_tarea}"

if __name__ == "__main__":
    print("=== Pool de Hilos - ThreadPoolExecutor ===\n")
    
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Ejecuta 10 tareas con max 3 hilos en paralelo
        futures = [executor.submit(descargar, i) for i in range(1, 11)]
        
        for i, future in enumerate(futures):
            resultado = future.result()
            print(f"Resultado {i}: {resultado}")
    
    print("\nCompletado")
