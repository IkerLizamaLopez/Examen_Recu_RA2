"""
EJERCICIO 12: Puente Estrecho con Turno y Prioridad (Condition)
Enunciado:
Simula el puente estrecho de un unico carril entre coches de direccion NORTE y SUR.
Usa una variable Condition para que los hilos esperen si la direccion es opuesta o si se
supero el limite de 3 coches consecutivos existiendo trafico contrario.
"""

import threading
import time
import random

class PuenteEstrecho:
    def __init__(self):
        self.sentido_actual = "NORTE"
        self.coches_en_puente = 0
        self.coches_consecutivos = 0
        self.esperando_norte = 0
        self.esperando_sur = 0
        
        # Sincronizacion
        self.cond = threading.Condition()
        self.print_lock = threading.Lock()

    def entrar_puente(self, coche_nombre, sentido):
        with self.cond:
            # Incrementar contadores de espera
            if sentido == "NORTE":
                self.esperando_norte += 1
            else:
                self.esperando_sur += 1
                
            with self.print_lock:
                print(f" [{coche_nombre}] llega al puente hacia el {sentido}. (Cola N:{self.esperando_norte} | S:{self.esperando_sur})")
            
            # Condicion de espera:
            # - Si hay coches en el puente en sentido opuesto
            # - Si el sentido actual es opuesto
            # - Si ya cruzaron 3 coches seguidos de esta direccion y hay coches esperando en el otro sentido
            while True:
                opuesto = "SUR" if sentido == "NORTE" else "NORTE"
                esperando_opuesto = self.esperando_sur if sentido == "NORTE" else self.esperando_norte
                
                # Debe esperar?
                esperar = False
                if self.coches_en_puente > 0 and self.sentido_actual != sentido:
                    esperar = True
                elif self.sentido_actual != sentido and (self.coches_en_puente > 0 or esperando_opuesto > 0):
                    esperar = True
                elif self.coches_consecutivos >= 3 and esperando_opuesto > 0:
                    esperar = True
                    
                if not esperar:
                    break
                    
                self.cond.wait()
                
            # Entrar al puente
            if sentido == "NORTE":
                self.esperando_norte -= 1
            else:
                self.esperando_sur -= 1
                
            # Ajustar sentido y contador de consecutivos
            if self.sentido_actual != sentido:
                self.sentido_actual = sentido
                self.coches_consecutivos = 0
                
            self.coches_en_puente += 1
            self.coches_consecutivos += 1
            
            with self.print_lock:
                print(f" [CRUZANDO] {coche_nombre} ENTRA al puente hacia {sentido}. "
                      f"(Coches cruzando: {self.coches_en_puente} | Consecutivos: {self.coches_consecutivos})")

    def salir_puente(self, coche_nombre, sentido):
        with self.cond:
            self.coches_en_puente -= 1
            with self.print_lock:
                print(f" [SALIDA] {coche_nombre} SALE del puente. (Quedan en puente: {self.coches_en_puente})")
                
            # Si el puente queda vacio y ya hemos alcanzado el limite de coches seguidos,
            # o si ya no hay nadie esperando en este sentido, forzamos cambio de turno
            esperando_mismo_sentido = self.esperando_norte if sentido == "NORTE" else self.esperando_sur
            esperando_opuesto = self.esperando_sur if sentido == "NORTE" else self.esperando_norte
            
            if self.coches_en_puente == 0:
                if self.coches_consecutivos >= 3 and esperando_opuesto > 0:
                    self.sentido_actual = "SUR" if sentido == "NORTE" else "NORTE"
                    self.coches_consecutivos = 0
                    with self.print_lock:
                        print(f" [CAMBIO TURNO] Forzado cambio de sentido a: {self.sentido_actual}")
                elif esperando_mismo_sentido == 0 and esperando_opuesto > 0:
                    self.sentido_actual = "SUR" if sentido == "NORTE" else "NORTE"
                    self.coches_consecutivos = 0
                    with self.print_lock:
                        print(f" [CAMBIO TURNO] No hay mas coches del {sentido}. Sentido actual: {self.sentido_actual}")
                        
            # Notificar a todos para recalcular condiciones de paso
            self.cond.notify_all()

def vehiculo_proceso(puente, id_vehiculo, sentido):
    nombre = f"Coche-{sentido[:1]}-{id_vehiculo}"
    time.sleep(random.uniform(0.1, 1.0)) # Retardo de llegada
    puente.entrar_puente(nombre, sentido)
    time.sleep(random.uniform(0.5, 1.0)) # Tiempo que tarda en cruzar
    puente.salir_puente(nombre, sentido)

if __name__ == "__main__":
    print("Iniciando simulacion del Puente de carril unico con prioridad anti-hambruna...")
    puente = PuenteEstrecho()
    
    hilos = []
    # Lanzar 4 coches hacia el NORTE y 4 hacia el SUR
    for i in range(1, 5):
        t1 = threading.Thread(target=vehiculo_proceso, args=(puente, i, "NORTE"))
        t2 = threading.Thread(target=vehiculo_proceso, args=(puente, i, "SUR"))
        hilos.extend([t1, t2])
        t1.start()
        t2.start()
        
    for h in hilos:
        h.join()
        
    print("\n El puente se encuentra despejado. Simulacion completada.")
