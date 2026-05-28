"""
EJERCICIO 15: Cruce de Peatones Inteligente (Events)
Enunciado:
Simula un semaforo interactivo con pulsador para peatones.
Usa threading.Event para controlar cuando fluyen los coches (evento set) y cuando se detienen (clear)
para que cruce un peaton.
"""

import threading
import time
import random

# Evento: Si esta activo (set), el semaforo esta VERDE y los coches pasan.
# Si esta inactivo (clear), esta ROJO y los coches deben pararse.
semaforo_verde = threading.Event()
print_lock = threading.Lock()
simulacion_activa = True

def coche_proceso(id_coche):
    nombre = f" Coche-{id_coche}"
    
    while simulacion_activa:
        time.sleep(random.uniform(0.3, 0.8)) # Conducir un tramo
        
        with print_lock:
            print(f"  {nombre} se acerca al paso de peatones...")
            
        # Comprobar estado del semaforo. Si esta rojo (clear), se bloquea esperando aqui.
        if not semaforo_verde.is_set():
            with print_lock:
                print(f" {nombre} detecta SEMAFORO EN ROJO. Deteniendo vehiculo y esperando...")
                
        semaforo_verde.wait() # Espera a que el evento pase a estar 'set'
        
        with print_lock:
            print(f" {nombre} cruza el paso de peatones de forma fluida.")

def peaton_proceso():
    global simulacion_activa
    time.sleep(1.5) # El peaton camina por la acera antes de llegar al cruce
    
    with print_lock:
        print("\n [PEATON] Llega al paso y PULSA EL BOTON de solicitud de cruce.")
        
    # Poner semaforo en rojo para coches
    semaforo_verde.clear()
    
    with print_lock:
        print(" [SEMAFORO] Cambio a ROJO! Deteniendo vehiculos...")
        print(" [PEATON] Cruzando la calzada de forma segura...")
        
    time.sleep(2.0) # Tiempo que tarda en cruzar
    
    with print_lock:
        print(" [PEATON] Ha llegado al otro lado de la acera con exito.")
        print(" [SEMAFORO] Cambio a VERDE! Reanudando circulacion...")
        
    # Poner semaforo en verde para coches
    semaforo_verde.set()
    
    # Dejar rodar un poco mas la circulacion antes de terminar la simulacion
    time.sleep(1.0)
    simulacion_activa = False

if __name__ == "__main__":
    print("Iniciando simulacion del Semaforo Inteligente Peatonal...")
    
    # El semaforo empieza en VERDE
    semaforo_verde.set()
    
    # Hilos de coches
    hilos_coches = []
    for i in range(1, 5):
        t = threading.Thread(target=coche_proceso, args=(i,))
        hilos_coches.append(t)
        t.start()
        
    # Hilo de peaton
    h_peaton = threading.Thread(target=peaton_proceso)
    h_peaton.start()
    
    h_peaton.join()
    
    # Despertar y terminar coches si estuvieran bloqueados por seguridad
    semaforo_verde.set()
    for t in hilos_coches:
        t.join()
        
    print("\n Simulacion vial finalizada.")
