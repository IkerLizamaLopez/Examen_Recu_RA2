"""
EJERCICIO 02: Contador Seguro - Lock (NIVEL SUAVE)
Usa Lock para sincronizar el acceso al contador
"""

import threading

contador = 0
lock = threading.Lock()

def incrementar(hilo_id):
    global contador
    print(f"Hilo {hilo_id} iniciado")
    for _ in range(1000):
        with lock:
            # Seccion critica protegida
            contador += 1
    print(f"Hilo {hilo_id} completado")

if __name__ == "__main__":
    print("=== Contador Seguro con Lock ===")
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
        print("CORRECTO - Lock garantizo exclusion mutua")
    else:
        print(f"INCORRECTO - Resultado: {contador}")
