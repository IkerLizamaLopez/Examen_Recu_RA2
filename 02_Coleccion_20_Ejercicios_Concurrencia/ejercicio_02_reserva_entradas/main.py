"""
EJERCICIO 02: Reserva de Entradas (Locks)
Enunciado:
Implementa un sistema de reservas de entradas de cine concurrentes.
El cine dispone de un stock total de 20 entradas.
Habra 10 hilos "Cliente" que intentan reservar un numero aleatorio de entradas (entre 1 y 4).
Utiliza threading.Lock para que el stock de entradas no se vuelva negativo.
"""

import threading
import time
import random

class Cine:
    def __init__(self, entradas_iniciales):
        self.entradas_disponibles = entradas_iniciales
        self.lock = threading.Lock()
        
    def reservar(self, cantidad, cliente_nombre):
        print(f" [SOLICITUD] {cliente_nombre} quiere comprar {cantidad} entradas.")
        
        # Simular pequeno retardo de procesamiento antes de adquirir el lock (simulacion de latencia)
        time.sleep(random.uniform(0.1, 0.3))
        
        with self.lock:
            if self.entradas_disponibles >= cantidad:
                print(f" [APROBADO] {cliente_nombre}: Hay suficientes entradas. Procesando...")
                time.sleep(random.uniform(0.1, 0.2)) # Tiempo de cobro
                self.entradas_disponibles -= cantidad
                print(f" [COMPRA EXITOSA] {cliente_nombre} compro {cantidad} entradas. Stock restante: {self.entradas_disponibles}")
                return True
            else:
                print(f" [DENEGADO] {cliente_nombre}: No se pueden comprar {cantidad} entradas. Stock actual: {self.entradas_disponibles}")
                return False

def cliente_proceso(cine, id_cliente):
    nombre = f"Cliente-{id_cliente}"
    cantidad_a_reservar = random.randint(1, 4)
    cine.reservar(cantidad_a_reservar, nombre)

if __name__ == "__main__":
    print("Iniciando sistema de reservas concurrente con 20 entradas...")
    cine = Cine(20)
    
    hilos = []
    for i in range(1, 11):
        h = threading.Thread(target=cliente_proceso, args=(cine, i))
        hilos.append(h)
        h.start()
        
    for h in hilos:
        h.join()
        
    print(f"\nProceso terminado. Entradas sobrantes en taquilla: {cine.entradas_disponibles}")
