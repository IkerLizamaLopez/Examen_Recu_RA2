"""
EJERCICIO 19: Triaje de Urgencias Medicas (PriorityQueue)
Enunciado:
Simula una sala de urgencias de un hospital.
Los pacientes tienen 3 niveles de gravedad (1=Critico, 2=Moderado, 3=Leve).
Usa queue.PriorityQueue para ordenar y atender automaticamente a los de mayor prioridad (ID numerico menor).
"""

import threading
import queue
import time
import random

# Cola de prioridad compartida
# Almacena tuplas de la forma: (prioridad, timestamp, datos_paciente)
# El timestamp se usa para desempatar si dos pacientes tienen la misma prioridad
cola_urgencias = queue.PriorityQueue()
print_lock = threading.Lock()

def paciente_llegada(id_paciente, nombre, gravedad):
    # Simular tiempo de viaje/llegada al hospital
    time.sleep(random.uniform(0.1, 1.2))
    
    timestamp = time.time()
    paciente_datos = {
        "id": id_coche := id_paciente,
        "nombre": nombre,
        "gravedad": gravedad
    }
    
    prioridad_etiqueta = "CRITICO " if gravedad == 1 else ("MODERADO " if gravedad == 2 else "LEVE ")
    
    with print_lock:
        print(f" [LLEGADA] Paciente '{nombre}' entra a triaje. Gravedad: {prioridad_etiqueta}")
        
    # Meter en la cola de prioridad.
    # El primer elemento de la tupla es la prioridad de ordenamiento (1 es menor y por tanto primero)
    # El segundo es el tiempo para desempatar por orden de llegada si tienen la misma gravedad
    cola_urgencias.put((gravedad, timestamp, paciente_datos))

def medico_atencion():
    nombre_medico = " Dr. Concurrente"
    while True:
        with print_lock:
            print(f" {nombre_medico} esperando llamadas de emergencia...")
            
        # Extraer el paciente de mayor prioridad (numero mas bajo)
        # Se bloquea si la cola esta vacia
        prioridad, _, paciente = cola_urgencias.get()
        
        # Comprobar senal de parada
        if paciente is None:
            with print_lock:
                print(f" {nombre_medico} finaliza su guardia. No quedan mas pacientes.")
            cola_urgencias.task_done()
            break
            
        nombre_paciente = paciente["nombre"]
        gravedad_paciente = paciente["gravedad"]
        
        prioridad_etiqueta = "CRITICO " if gravedad_paciente == 1 else ("MODERADO " if gravedad_paciente == 2 else "LEVE ")
        
        with print_lock:
            print(f" {nombre_medico} comieza a atender a: '{nombre_paciente}' ({prioridad_etiqueta})")
            
        # Simular tiempo de consulta medica segun la gravedad del caso
        # Los casos criticos conllevan mas tiempo de estabilizacion
        tiempo_consulta = 1.5 if gravedad_paciente == 1 else (0.8 if gravedad_paciente == 2 else 0.4)
        time.sleep(tiempo_consulta)
        
        with print_lock:
            print(f" {nombre_medico} termino la atencion de '{nombre_paciente}'.")
            
        cola_urgencias.task_done()

if __name__ == "__main__":
    print("Iniciando simulacion del Servicio de Urgencias del Hospital...")
    
    # Hilo del medico
    h_medico = threading.Thread(target=medico_atencion)
    h_medico.start()
    
    # Hilos de pacientes
    pacientes_datos = [
        ("Juan", 3),   # Leve
        ("Maria", 1),  # Critico
        ("Pedro", 2),  # Moderado
        ("Ana", 1),    # Critico (llega un poco mas tarde)
        ("Luis", 3),   # Leve
        ("Laura", 2)   # Moderado
    ]
    
    hilos_pacientes = []
    for i, (nombre, gravedad) in enumerate(pacientes_datos, 1):
        t = threading.Thread(target=paciente_llegada, args=(i, nombre, gravedad))
        hilos_pacientes.append(t)
        t.start()
        
    # Esperar a que todos los pacientes lleguen a urgencias
    for t in hilos_pacientes:
        t.join()
        
    # Esperar a que la cola se procese completamente
    cola_urgencias.join()
    
    # Enviar senal de parada al medico
    # Ponemos una tupla centinela donde los datos son None
    cola_urgencias.put((99, time.time(), None))
    
    h_medico.join()
    print("\n Guardia del hospital finalizada con total exito.")
