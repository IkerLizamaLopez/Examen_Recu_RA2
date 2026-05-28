"""
EJERCICIO 01: Contador Seguro (Locks)
Enunciado:
Implementa una simulacion en la que varios hilos acceden a un contador compartido en un servidor web para contar las visitas.
Habra 5 hilos que simulan visitas web. Cada hilo incrementara el contador compartido 10.000 veces.
Resuelve el problema utilizando threading.Lock para garantizar la exclusion mutua de modo que el resultado final sea exactamente 50.000.
"""

import threading
import time

# Recurso compartido
contador = 0
iteraciones = 10000
hilos_cantidad = 5

# Lock para la sincronizacion
lock_contador = threading.Lock()

def incrementar_sin_sincronizacion():
    global contador
    for _ in range(iteraciones):
        # Operacion no atomica
        contador_actual = contador
        time.sleep(0.000001) # Forzar el cambio de contexto para provocar condicion de carrera
        contador = contador_actual + 1

def incrementar_con_sincronizacion():
    global contador
    for _ in range(iteraciones):
        with lock_contador:
            # Seccion critica protegida por Lock
            contador_actual = contador
            contador = contador_actual + 1

def simular(modo):
    global contador
    contador = 0
    hilos = []
    
    print(f"\n--- Iniciando simulacion {modo} ---")
    
    funcion_objetivo = incrementar_con_sincronizacion if modo == "CON_SINCRONIZACION" else incrementar_sin_sincronizacion
    
    for i in range(hilos_cantidad):
        h = threading.Thread(target=funcion_objetivo, name=f"HiloVisitas-{i+1}")
        hilos.append(h)
        h.start()
        
    for h in hilos:
        h.join()
        
    print(f"Resultado final del contador {modo}: {contador}")
    print(f"Resultado esperado: {hilos_cantidad * iteraciones}")

if __name__ == "__main__":
    # La simulacion sin sincronizacion tarda un poco por los sleeps artificiales pero ilustra perfectamente el fallo
    # Hacemos una version rapida de la simulacion
    print("Demostracion de exclusion mutua con Locks:")
    
    # 1. Simulacion Sincronizada (Lock garantizado)
    start_time = time.time()
    simular("CON_SINCRONIZACION")
    print(f"Tiempo transcurrido: {time.time() - start_time:.4f} segundos")
    
    # 2. Simulacion Insegura (Seccion critica desprotegida)
    # Nota: Usamos menos iteraciones o sleeps muy breves para no eternizar la ejecucion del ejemplo
    iteraciones = 200 # Reducimos temporalmente solo para ver la condicion de carrera rapido
    simular("SIN_SINCRONIZACION")
