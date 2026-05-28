"""
EJERCICIO 25: Paso Alterno sobre Puente Estrecho Simple (Lock + Condition)
Enunciado:
Simula de forma simplificada el paso de coches sobre un puente de un solo carril.
Usa Lock y Condition para alternar de forma segura entre sentidos Norte y Sur.
"""

import threading
import time
import random

class PuenteEstrechoSimple:
    def __init__(self):
        self.sentido_actual = None
        self.coches_cruzando = 0
        self.lock = threading.Lock()
        self.cond = threading.Condition(self.lock)

    def entrar_puente(self, coche_nombre, sentido):
        with self.cond:
            # Esperar mientras el puente este ocupado por coches del sentido contrario
            while self.coches_cruzando > 0 and self.sentido_actual != sentido:
                print(f"[ESPERANDO] {coche_nombre} ({sentido}) espera para entrar al puente.")
                self.cond.wait()
                
            # Establecer sentido si el puente estaba vacio
            if self.coches_cruzando == 0:
                self.sentido_actual = sentido
                
            self.coches_cruzando += 1
            print(f"[ENTRADA] {coche_nombre} ({sentido}) entra al puente. Coches cruzando: {self.coches_cruzando}")

    def salir_puente(self, coche_nombre, sentido):
        with self.cond:
            self.coches_cruzando -= 1
            print(f"[SALIDA] {coche_nombre} ({sentido}) sale del puente. Coches restantes: {self.coches_cruzando}")
            
            # Si el puente queda totalmente vacio, reseteamos el sentido y avisamos a todos
            if self.coches_cruzando == 0:
                self.sentido_actual = None
                self.cond.notify_all()

def coche_proceso(puente, id_coche, sentido):
    nombre = f"Coche-{sentido[:1]}-{id_coche}"
    
    # Tiempo de aproximacion aleatorio
    time.sleep(random.uniform(0.1, 1.0))
    
    puente.entrar_puente(nombre, sentido)
    
    # Tiempo cruzando el puente
    time.sleep(random.uniform(0.6, 1.2))
    
    puente.salir_puente(nombre, sentido)

if __name__ == "__main__":
    print("=== SIMULACION DE PUENTE ESTRECHO SIMPLIFICADO ===")
    puente = PuenteEstrechoSimple()
    
    hilos = []
    
    # Crear 3 coches hacia el Norte
    for i in range(1, 4):
        t = threading.Thread(target=coche_proceso, args=(puente, i, "NORTE"))
        hilos.append(t)
        
    # Crear 3 coches hacia el Sur
    for i in range(1, 4):
        t = threading.Thread(target=coche_proceso, args=(puente, i, "SUR"))
        hilos.append(t)
        
    random.shuffle(hilos)
    for t in hilos:
        t.start()
        
    for t in hilos:
        t.join()
        
    print("\n=== Simulacion del puente finalizada con éxito. ===")
