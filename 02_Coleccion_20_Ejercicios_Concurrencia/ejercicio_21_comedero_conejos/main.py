"""
EJERCICIO 21: El Comedero de Conejos (Examen Oficial)
Enunciado:
Simula un ecosistema de conejos que intentan comer de un comedero comun.
Usa Lock para exclusion mutua y Semaphore para representar las raciones disponibles.
Cada conejo hace 5 intentos. Si falla 3 veces seguidas, muere. Si come, se reinicia.
El reponedor añade 3 raciones cada 2 segundos (5 veces).
"""

import threading
import time
import random

class Comedero:
    def __init__(self, raciones_iniciales=0):
        self.raciones_disponibles = raciones_iniciales
        self.total_comidas = 0
        self.lock = threading.Lock()
        # El semaforo representa y gestiona las raciones disponibles
        self.semaforo_raciones = threading.Semaphore(raciones_iniciales)

    def intentar_comer(self, conejo_nombre):
        # Intentar adquirir una racion sin bloquear indefinidamente
        # blocking=False intenta coger el recurso de inmediato y retorna True/False
        exito = self.semaforo_raciones.acquire(blocking=False)
        
        if exito:
            # Zona critica protegida por Lock
            with self.lock:
                self.raciones_disponibles -= 1
                self.total_comidas += 1
                print(f"[COMEDERO] {conejo_nombre} esta comiendo. Raciones restantes: {self.raciones_disponibles}")
            return True
        else:
            return False

    def reponer(self, cantidad):
        # Zona critica protegida por Lock
        with self.lock:
            self.raciones_disponibles += cantidad
            print(f"[COMEDERO] Reponedor ha anadido {cantidad} raciones. Total: {self.raciones_disponibles}")
            # Liberamos el semaforo tantas veces como raciones anadidas para actualizar su valor
            for _ in range(cantidad):
                self.semaforo_raciones.release()

class Conejo(threading.Thread):
    def __init__(self, nombre, comedero):
        super().__init__()
        self.nombre = nombre
        self.comedero = comedero
        self.comidas_realizadas = 0
        self.intentos_consecutivos_restantes = 3
        self.vivo = True

    def run(self):
        # Cada conejo realiza exactamente 5 intentos de comida (tiempo de simulacion)
        for intento in range(1, 6):
            if not self.vivo:
                break
                
            # Espera aleatoria de 0.5 a 2 segundos antes de intentar comer
            time.sleep(random.uniform(0.5, 2.0))
            
            print(f"[CONEJO] {self.nombre} realiza intento {intento}/5...")
            
            # Intentar comer
            comido = self.comedero.intentar_comer(self.nombre)
            
            if comido:
                self.comidas_realizadas += 1
                # Reiniciar contador de intentos consecutivos a 3
                self.intentos_consecutivos_restantes = 3
                print(f"[CONEJO] {self.nombre} consiguio comer. Comidas totales: {self.comidas_realizadas}")
            else:
                self.intentos_consecutivos_restantes -= 1
                print(f"[CONEJO] {self.nombre} no pudo comer. Intentos seguidos restantes: {self.intentos_consecutivos_restantes}")
                
                # Si llega a 0 intentos fallidos seguidos, el conejo muere
                if self.intentos_consecutivos_restantes == 0:
                    self.vivo = False
                    print(f"[MUERTE] {self.nombre} ha muerto de hambre tras 3 intentos seguidos fallidos.")
                    break

def reponedor_proceso(comedero):
    # Añade 3 raciones cada 2 segundos (5 veces en total)
    for i in range(1, 6):
        time.sleep(2.0)
        print(f"[REPONEDOR] Reposicion {i}/5 en camino...")
        comedero.reponer(3)

if __name__ == "__main__":
    print("=== SIMULACION ECOSESTEMA DE CONEJOS (EXAMEN OFICIAL RA2) ===")
    
    # Comedero empieza con 2 raciones iniciales para dar oportunidad
    comedero = Comedero(2)
    
    # Crear 4 conejos (hilos)
    conejos = [
        Conejo("Conejo-Blanco", comedero),
        Conejo("Conejo-Gris", comedero),
        Conejo("Conejo-Negro", comedero),
        Conejo("Conejo-Orejas", comedero)
    ]
    
    # Crear hilo reponedor
    hilo_reponedor = threading.Thread(target=reponedor_proceso, args=(comedero,), name="Reponedor")
    
    # Iniciar hilos
    hilo_reponedor.start()
    for c in conejos:
        c.start()
        
    # Esperar a que todos terminen
    for c in conejos:
        c.join()
    hilo_reponedor.join()
    
    # Mostrar estadisticas finales requeridas
    print("\n=== ESTADISTICAS FINALES ===")
    print("1. Veces que comio cada conejo:")
    for c in conejos:
        estado = "VIVO" if c.vivo else "MUERTO"
        print(f"   - {c.nombre} ({estado}): comio {c.comidas_realizadas} veces.")
        
    print(f"2. Total de comidas dadas en global: {comedero.total_comidas}")
    print(f"3. Raciones que se han quedado sin repartir: {comedero.raciones_disponibles}")
    print("=============================")
