"""
EJERCICIO 11: El Barbero Durmiente (Sincronizacion Clasica)
Enunciado:
Simula el problema clasico del barbero durmiente con 3 sillas de espera.
Usa una variable Condition para coordinar el sueno del barbero y los estados de espera.
"""

import threading
import time
import random

# Parametros del sistema
SILLAS_ESPERA = 3
sillas_ocupadas = 0
barbero_libre = True
simulacion_activa = True

# Sincronizacion
cond_barberia = threading.Condition()
print_lock = threading.Lock()

def barbero():
    global sillas_ocupadas, barbero_libre, simulacion_activa
    
    while simulacion_activa or sillas_ocupadas > 0:
        with cond_barberia:
            # Si no hay clientes esperando, el barbero duerme
            while sillas_ocupadas == 0 and simulacion_activa:
                with print_lock:
                    print(" [BARBERO] No hay clientes. El barbero se queda dormido...")
                cond_barberia.wait()
                
            if not simulacion_activa and sillas_ocupadas == 0:
                break
                
            # Coger al cliente de la sala de espera
            sillas_ocupadas -= 1
            barbero_libre = False
            
            with print_lock:
                print(f" [BARBERO] Despierta o llama al siguiente cliente. Sillas de espera ocupadas: {sillas_ocupadas}/{SILLAS_ESPERA}")
                
        # Realizar el corte de pelo (fuera de la condicion critica para permitir concurrencia)
        corte_duracion = random.uniform(0.8, 1.5)
        time.sleep(corte_duracion)
        
        with cond_barberia:
            barbero_libre = True
            with print_lock:
                print("  [BARBERO] Ha terminado de cortar el pelo al cliente actual.")
            # Notificar al cliente que su corte ha terminado o a los que estan esperando
            cond_barberia.notify_all()

def cliente(id_cliente):
    global sillas_ocupadas, barbero_libre
    nombre = f"Cliente-{id_cliente}"
    
    # Tiempo de llegada aleatorio
    time.sleep(random.uniform(0.1, 2.0))
    
    with cond_barberia:
        with print_lock:
            print(f" {nombre} entra a la barberia.")
            
        # Caso 1: El barbero esta durmiendo (libre)
        if barbero_libre and sillas_ocupadas == 0:
            with print_lock:
                print(f" {nombre} despierta al barbero y se sienta en la silla de afeitar.")
            sillas_ocupadas += 1 # Ocupa silla temporalmente para despertar
            cond_barberia.notify_all() # Despierta al barbero
            
            # Esperar a que el barbero termine el corte
            while not barbero_libre:
                cond_barberia.wait()
                
        # Caso 2: El barbero esta ocupado, pero hay sillas libres
        elif sillas_ocupadas < SILLAS_ESPERA:
            sillas_ocupadas += 1
            with print_lock:
                print(f" {nombre} se sienta a esperar en la sala. Sillas ocupadas: {sillas_ocupadas}/{SILLAS_ESPERA}")
                
            cond_barberia.notify_all() # Notifica que hay alguien esperando
            
            # Esperar a ser atendido y que termine su corte
            # En una simulacion real, esperaremos hasta que el barbero termine de atendernos
            # pero para simplificar, el cliente espera a que el barbero le atienda
            # Esperamos en la condicion de que el barbero este libre
            # (se simplifica a esperar a que cambie el estado)
            # Para esta simulacion didactica, el wait simula la espera de turno y salida
            cond_barberia.wait()
            with print_lock:
                print(f" {nombre} sale feliz de la barberia con su corte terminado.")
                
        # Caso 3: La barberia esta llena de clientes
        else:
            with print_lock:
                print(f" {nombre}: Sala llena. Se marcha enfadado sin cortarse el pelo.")

if __name__ == "__main__":
    print(f"Iniciando simulacion del Barbero Durmiente. Sala de espera: {SILLAS_ESPERA} sillas.")
    
    h_barbero = threading.Thread(target=barbero, name="Barbero")
    h_barbero.start()
    
    hilos_clientes = []
    for i in range(1, 9):
        h = threading.Thread(target=cliente, args=(i,))
        hilos_clientes.append(h)
        h.start()
        
    for h in hilos_clientes:
        h.join()
        
    # Detener al barbero de forma limpia indicando el fin de la simulacion
    with cond_barberia:
        simulacion_activa = False
        cond_barberia.notify_all()
        
    h_barbero.join()
    print("\n La barberia ha cerrado sus puertas por hoy.")
