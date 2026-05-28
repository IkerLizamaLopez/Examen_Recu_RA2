"""
EJERCICIO 03: Filosofos Comensales (Evitacion de Deadlocks)
Enunciado:
Resuelve el problema clasico de la cena de los 5 filosofos que piensan y comen alternadamente.
Utiliza la estrategia de jerarquia de recursos (coger el tenedor con el ID menor primero) para evitar el interbloqueo.
"""

import threading
import time
import random

class Filosofo(threading.Thread):
    def __init__(self, id_filosofo, tenedor_izq, tenedor_der):
        super().__init__()
        self.id_filosofo = id_filosofo
        # Tenedores asignados
        self.tenedor_izq = tenedor_izq
        self.tenedor_der = tenedor_der
        self.nombre = f"Filosofo-{id_filosofo}"
        
        # Estrategia de evitacion de Deadlock: Ordenar por ID de tenedor
        # El tenedor con menor identificador se coge PRIMERO
        if tenedor_izq.id < tenedor_der.id:
            self.primer_tenedor = tenedor_izq
            self.segundo_tenedor = tenedor_der
        else:
            self.primer_tenedor = tenedor_der
            self.segundo_tenedor = tenedor_izq
            
    def pensar(self):
        print(f" {self.nombre} esta pensando...")
        time.sleep(random.uniform(0.5, 1.5))
        
    def comer(self):
        print(f" {self.nombre} esta comiendo con alegria...")
        time.sleep(random.uniform(0.5, 1.0))
        print(f" {self.nombre} ha terminado de comer y empieza a digerir.")

    def run(self):
        for ciclo in range(1, 4):
            self.pensar()
            
            print(f" {self.nombre} tiene hambre (Ciclo {ciclo}/3). Intenta conseguir tenedores.")
            
            # Adquirir primer tenedor (el de ID menor)
            with self.primer_tenedor.lock:
                print(f" {self.nombre} cogio su PRIMER tenedor (Tenedor-{self.primer_tenedor.id})")
                time.sleep(0.1) # Pausa dramatica para acentuar posibilidad de deadlock si no hubiese ordenamiento
                
                # Adquirir segundo tenedor (el de ID mayor)
                with self.segundo_tenedor.lock:
                    print(f" {self.nombre} cogio su SEGUNDO tenedor (Tenedor-{self.segundo_tenedor.id})")
                    self.comer()
                    print(f" {self.nombre} suelta el SEGUNDO tenedor (Tenedor-{self.segundo_tenedor.id})")
                
                print(f" {self.nombre} suelta el PRIMER tenedor (Tenedor-{self.primer_tenedor.id})")

class Tenedor:
    def __init__(self, id_tenedor):
        self.id = id_tenedor
        self.lock = threading.Lock()

if __name__ == "__main__":
    print("Iniciando la mesa de los filosofos comensales (Ciclos: 3 por filosofo)...")
    
    # Crear 5 tenedores
    tenedores = [Tenedor(i) for i in range(5)]
    
    # Crear 5 filosofos asignandoles sus respectivos tenedores contiguos
    filosofos = []
    for i in range(5):
        # El filosofo i comparte tenedor izquierdo (i) y derecho ((i+1)%5)
        f = Filosofo(i, tenedores[i], tenedores[(i + 1) % 5])
        filosofos.append(f)
        
    # Iniciar simulacion
    for f in filosofos:
        f.start()
        
    for f in filosofos:
        f.join()
        
    print("\n La cena ha terminado con exito y sin interbloqueos.")
