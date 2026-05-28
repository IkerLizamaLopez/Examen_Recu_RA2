"""
EJERCICIO 01: Contador - Race Condition (NIVEL SUAVE)
Demuestra una race condition sin sincronizacion
"""

import threading
import time

contador = 0

def incrementar(hilo_id):
    global contador
    print(f"Hilo {hilo_id} iniciado")
    for _ in range(1000):
        # Operacion NO ATOMICA
        temp = contador
        time.sleep(0.000001)  # Forzar cambio de contexto
        contador = temp + 1
    print(f"Hilo {hilo_id} completado")

if __name__ == "__main__":
    print("=== Demostracion de Race Condition ===")
    print("Iniciando 3 hilos (cada uno incrementa 1000 veces)...")
    print("Resultado esperado: 3000")
    print("")
    
    hilos = []
    for i in range(1, 4):
        h = threading.Thread(target=incrementar, args=(i,))
        hilos.append(h)
        h.start()
    
    for h in hilos:
        h.join()
    
    print("")
    print(f"Contador final: {contador}")
    if contador == 3000:
        print("CORRECTO (pero poco probable sin sincronizacion)")
    else:
        print(f"INCORRECTO - Faltaron {3000 - contador} incrementos (race condition)")
