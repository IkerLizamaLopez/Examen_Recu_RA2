"""
EJERCICIO 18: El Comedero de Mascotas con Limite de Intentos (Condition + Timeout)
Enunciado:
Simula un plato de comida compartido con un aforo maximo de 2 animales.
Si el plato esta lleno, los animales esperan con un timeout de 1.0 segundos.
Tienen un limite de 3 intentos. Si se agotan los intentos, se rinden.
"""

import threading
import time
import random

CAPACIDAD = 2
animales_comiendo = 0

# Sincronizacion
cond_comedero = threading.Condition()
print_lock = threading.Lock()

def animal_proceso(id_animal, tipo_animal):
    global animales_comiendo
    nombre = f" [{tipo_animal}-{id_animal}]" if tipo_animal == "Gato" else f" [{tipo_animal}-{id_animal}]"
    
    intentos_maximos = 3
    comido_con_exito = False
    
    # Tiempo inicial antes de sentir hambre
    time.sleep(random.uniform(0.1, 0.8))
    
    for intento in range(1, intentos_maximos + 1):
        with cond_comedero:
            with print_lock:
                print(f" {nombre} tiene hambre. Intento {intento}/{intentos_maximos} de acercarse al comedero.")
                
            # Comprobar si hay espacio en el comedero
            if animales_comiendo < CAPACIDAD:
                animales_comiendo += 1
                comido_con_exito = True
            else:
                # Si esta lleno, esperar con un timeout de 1.0 segundos
                with print_lock:
                    print(f" {nombre} encuentra el comedero lleno. Esperando un maximo de 1.0s...")
                    
                # wait(timeout) retorna True si fue despertado por notify y False si vencio el timeout
                despertado = cond_comedero.wait(timeout=1.0)
                
                if despertado and animales_comiendo < CAPACIDAD:
                    animales_comiendo += 1
                    comido_con_exito = True
                else:
                    with print_lock:
                        print(f" {nombre}: Excedido el tiempo de espera (timeout) en el intento {intento}.")
                        
        # Si consiguio entrar a comer, realiza la accion y sale del bucle de intentos
        if comido_con_exito:
            with print_lock:
                print(f" {nombre} ENTRA a comer. (Animales comiendo: {animales_comiendo}/{CAPACIDAD})")
            
            # Simular tiempo de comida
            time.sleep(random.uniform(0.8, 1.4))
            
            with cond_comedero:
                animales_comiendo -= 1
                with print_lock:
                    print(f" {nombre} ha terminado de comer y SALE del comedero. (Quedan: {animales_comiendo})")
                cond_comedero.notify_all() # Notificar a los que esperan
                
            break # Salir del bucle for de intentos
            
        else:
            # Si fallo este intento, descansar un momento antes de volver a intentar
            time.sleep(random.uniform(0.5, 1.0))
            
    if not comido_con_exito:
        with print_lock:
            print(f" {nombre} agoto sus {intentos_maximos} intentos sin poder comer. Se va a dormir hambriento.")

if __name__ == "__main__":
    print(f"Iniciando simulacion del Comedero de Mascotas con Aforo {CAPACIDAD} y reintentos...")
    
    hilos = []
    especies = ["Gato", "Perro", "Gato", "Perro", "Gato"]
    for i, especie in enumerate(especies, 1):
        t = threading.Thread(target=animal_proceso, args=(i, especie))
        hilos.append(t)
        t.start()
        
    for t in hilos:
        t.join()
        
    print("\n La simulacion del comedero de mascotas ha concluido.")
