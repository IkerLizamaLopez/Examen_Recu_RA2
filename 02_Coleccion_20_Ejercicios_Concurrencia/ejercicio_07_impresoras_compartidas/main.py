"""
EJERCICIO 07: Impresoras Compartidas (Semaforos y Locks)
Enunciado:
Implementa un sistema de gestion para una oficina con 3 impresoras compartidas (A, B, C) y 8 trabajadores.
Usa un semaforo para limitar a 3 impresiones paralelas y un Lock para asignar e identificar que impresora coge cada uno.
"""

import threading
import time
import random

class CentroImpresion:
    def __init__(self):
        # 3 impresoras disponibles fisicas
        self.impresoras = ["Impresora-A", "Impresora-B", "Impresora-C"]
        # Estado de disponibilidad: True si esta libre
        self.estado_impresoras = [True, True, True]
        
        # Sincronizacion
        self.semaforo_aforo = threading.Semaphore(3) # Maximo de 3 impresiones paralelas
        self.lock_seleccion = threading.Lock() # Exclusion mutua al consultar/modificar la lista
        
    def imprimir_documento(self, empleado_nombre):
        print(f" [{empleado_nombre}] necesita imprimir un informe.")
        
        # Espera plaza en el pool de impresoras
        self.semaforo_aforo.acquire()
        
        impresora_asignada = None
        indice_asignado = -1
        
        # Seccion critica: Consultar y reservar la impresora libre
        with self.lock_seleccion:
            for idx in range(3):
                if self.estado_impresoras[idx]: # Si esta libre
                    self.estado_impresoras[idx] = False # Ocupar
                    impresora_asignada = self.impresoras[idx]
                    indice_asignado = idx
                    break
                    
        print(f"  [IMPRIMIENDO] {empleado_nombre} esta usando la [{impresora_asignada}].")
        
        # Simular tiempo de impresion
        time.sleep(random.uniform(1.0, 2.0))
        
        # Seccion critica: Liberar la impresora fisica
        with self.lock_seleccion:
            self.estado_impresoras[indice_asignado] = True # Marcar libre
            
        print(f" [COMPLETADO] {empleado_nombre} ha recogido su informe de la [{impresora_asignada}].")
        
        # Liberar plaza de semaforo
        self.semaforo_aforo.release()

def empleado_trabajo(centro, id_empleado):
    nombre = f"Empleado-{id_empleado}"
    time.sleep(random.uniform(0.1, 1.5))
    centro.imprimir_documento(nombre)

if __name__ == "__main__":
    print("Iniciando simulacion del Centro de Impresion Concurrente...")
    centro = CentroImpresion()
    
    hilos = []
    for i in range(1, 9):
        h = threading.Thread(target=empleado_trabajo, args=(centro, i))
        hilos.append(h)
        h.start()
        
    for h in hilos:
        h.join()
        
    print("\n La jornada laboral ha terminado. Todos los informes estan impresos.")
