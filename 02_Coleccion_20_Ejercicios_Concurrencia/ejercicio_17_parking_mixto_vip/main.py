"""
EJERCICIO 17: Parking con Plazas Estandar y VIP (Condition)
Enunciado:
Simula un parking con 2 plazas Estandar y 1 plaza VIP.
Los coches estandar solo pueden usar plazas estandar. Los VIP pueden usar cualquiera de las dos,
priorizando las VIP. Usa Condition para bloquear y liberar segun disponibilidad de plazas.
"""

import threading
import time
import random

class ParkingMixto:
    def __init__(self):
        # Numero de plazas libres de cada tipo
        self.plazas_estandar_libres = 2
        self.plaza_vip_libre = 1
        
        # Sincronizacion
        self.cond = threading.Condition()
        self.print_lock = threading.Lock()

    def entrar_parking(self, coche_nombre, es_vip):
        with self.cond:
            if es_vip:
                # Coche VIP espera si TODO el parking esta ocupado
                while self.plaza_vip_libre == 0 and self.plazas_estandar_libres == 0:
                    with self.print_lock:
                        print(f" [ESPERANDO] Coche VIP [{coche_nombre}] espera plaza libre...")
                    self.cond.wait()
                
                # Asignar plaza priorizando VIP
                if self.plaza_vip_libre > 0:
                    self.plaza_vip_libre -= 1
                    plaza_usada = "PLAZA VIP"
                else:
                    self.plazas_estandar_libres -= 1
                    plaza_usada = "PLAZA ESTANDAR"
            else:
                # Coche Normal espera si las plazas estandar estan llenas
                while self.plazas_estandar_libres == 0:
                    with self.print_lock:
                        print(f" [ESPERANDO] Coche Normal [{coche_nombre}] espera plaza estandar libre...")
                    self.cond.wait()
                    
                self.plazas_estandar_libres -= 1
                plaza_usada = "PLAZA ESTANDAR"
                
            with self.print_lock:
                print(f" [APARCADO] {coche_nombre} ha aparcado en la [{plaza_usada}]. "
                      f"Disponibles: Estandar:{self.plazas_estandar_libres} | VIP:{self.plaza_vip_libre}")
            
            return plaza_usada

    def salir_parking(self, coche_nombre, plaza_usada):
        with self.cond:
            if plaza_usada == "PLAZA VIP":
                self.plaza_vip_libre += 1
            else:
                self.plazas_estandar_libres += 1
                
            with self.print_lock:
                print(f" [SALIDA] {coche_nombre} abandona su [{plaza_usada}]. "
                      f"Disponibles: Estandar:{self.plazas_estandar_libres} | VIP:{self.plaza_vip_libre}")
                
            # Notificar para que los coches despierten y reevaluen las plazas libres
            self.cond.notify_all()

def coche_proceso(parking, id_coche, es_vip):
    tipo = "VIP " if es_vip else "Normal "
    nombre = f"Coche-{tipo}-{id_coche}"
    
    # Tiempo de llegada aleatorio
    time.sleep(random.uniform(0.1, 1.0))
    
    # Intentar aparcar
    plaza = parking.entrar_parking(nombre, es_vip)
    
    # Permanecer aparcado
    time.sleep(random.uniform(1.0, 2.0))
    
    # Salir del parking
    parking.salir_parking(nombre, plaza)

if __name__ == "__main__":
    print("Iniciando simulacion del Parking Mixto (2 Estandar, 1 VIP)...")
    parking = ParkingMixto()
    
    hilos = []
    
    # Lanzar 4 coches normales
    for i in range(1, 5):
        t = threading.Thread(target=coche_proceso, args=(parking, i, False))
        hilos.append(t)
        t.start()
        
    # Lanzar 2 coches VIP
    for i in range(1, 3):
        t = threading.Thread(target=coche_proceso, args=(parking, i, True))
        hilos.append(t)
        t.start()
        
    for t in hilos:
        t.join()
        
    print("\n Simulacion del parking finalizada. Todos los vehiculos han salido.")
