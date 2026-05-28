"""
EJERCICIO 05: La Cafeteria (Semaforos)
Enunciado:
Simula una cafeteria con un aforo limitado a 3 clientes simultaneos.
Resuelve este control de aforo mediante un Semaforo (threading.Semaphore) con capacidad de 3.
"""

import threading
import time
import random

# Aforo maximo
AFORO_MAX = 3
# Semaforo para controlar el acceso
semaforo_aforo = threading.Semaphore(AFORO_MAX)
# Lock para proteger las salidas por consola y el recuento exacto de ocupacion
print_lock = threading.Lock()
ocupacion_actual = 0

def cliente(id_cliente):
    global ocupacion_actual
    nombre = f"Cliente-{id_cliente}"
    
    # Tiempo de llegada aleatorio
    time.sleep(random.uniform(0.1, 1.0))
    
    with print_lock:
        print(f" {nombre} ha llegado a la puerta de la cafeteria.")
        
    # Adquirir plaza en el semaforo (espera si el aforo esta completo)
    semaforo_aforo.acquire()
    
    with print_lock:
        ocupacion_actual += 1
        # Nota: semaforo_aforo._value nos da el valor interno actual (plazas disponibles restantes)
        # En entornos academicos se usa a menudo para mostrar depuracion
        print(f" {nombre} ENTRA a la cafeteria. (Ocupacion: {ocupacion_actual}/{AFORO_MAX} | Plazas libres: {semaforo_aforo._value})")
        
    # Simular tiempo de consumo de cafe
    time.sleep(random.uniform(1.0, 2.0))
    
    with print_lock:
        ocupacion_actual -= 1
        print(f" {nombre} ha terminado y SALE de la cafeteria.")
        
    # Liberar plaza en el semaforo para permitir entrar al siguiente
    semaforo_aforo.release()

if __name__ == "__main__":
    print(f"Iniciando simulacion de la Cafeteria. Aforo maximo: {AFORO_MAX} personas.")
    
    hilos = []
    for i in range(1, 11):
        h = threading.Thread(target=cliente, args=(i,))
        hilos.append(h)
        h.start()
        
    for h in hilos:
        h.join()
        
    print("\n La cafeteria ha cerrado. Todos los clientes han sido atendidos.")
