"""
EJERCICIO 09: Conejos y Comedero (NIVEL AVANZADO)
EXAMEN OFICIAL JOVELLANOS - Implementacion orientada a objetos
Demuestra mejor practica: uso de clases para organizar logica
"""

import threading
import time
import random


class Comedero:
    """
    Recurso compartido: Comedero con control de acceso sincronizado.
    Usa Lock para exclusion mutua y Semaphore para gestionar raciones.
    """
    
    def __init__(self, raciones_iniciales=0):
        self.raciones_disponibles = raciones_iniciales
        self.total_comidas = 0
        self.lock = threading.Lock()
        # Semaphore: representa raciones disponibles (acquire/release)
        self.semaforo_raciones = threading.Semaphore(raciones_iniciales)

    def intentar_comer(self, nombre_conejo):
        """
        Intenta conseguir una racion sin bloquear (non-blocking).
        Retorna True si logra comer, False si no hay raciones.
        """
        # acquire(blocking=False) intenta tomar recurso sin esperar
        exito = self.semaforo_raciones.acquire(blocking=False)
        
        if exito:
            # Zona critica: actualizar estado del comedero
            with self.lock:
                self.raciones_disponibles -= 1
                self.total_comidas += 1
                print(f"  [COMEDERO] {nombre_conejo} COME. Raciones restantes: {self.raciones_disponibles}")
            return True
        else:
            print(f"  [COMEDERO] {nombre_conejo} NO HAY COMIDA")
            return False

    def reponer(self, cantidad):
        """
        Anade raciones y notifica al semaphore.
        """
        with self.lock:
            self.raciones_disponibles += cantidad
            print(f"[REPONEDOR] Anade {cantidad} raciones. Total: {self.raciones_disponibles}")
            # Libera el semaphore tantas veces como raciones anadidas
            for _ in range(cantidad):
                self.semaforo_raciones.release()


class Conejo(threading.Thread):
    """
    Hilo que simula comportamiento de un conejo.
    - 5 intentos de comer
    - Muere si 3 fallos consecutivos
    - Si logra comer, reinicia contador de fallos
    """
    
    def __init__(self, nombre, comedero):
        super().__init__(name=nombre)
        self.nombre = nombre
        self.comedero = comedero
        self.comidas_realizadas = 0
        self.fallos_consecutivos = 0
        self.vivo = True

    def run(self):
        """Ejecucion del hilo conejo."""
        print(f"[CONEJO] {self.nombre} nace")
        
        # 5 intentos de comer (tiempo de simulacion)
        for intento_num in range(1, 6):
            if not self.vivo:
                break
            
            # Espera aleatoria 0.5-2 segundos
            tiempo_espera = random.uniform(0.5, 2.0)
            time.sleep(tiempo_espera)
            
            print(f"[CONEJO] {self.nombre} intento {intento_num}/5 (fallos: {self.fallos_consecutivos}/3)")
            
            # Intentar comer
            comio = self.comedero.intentar_comer(self.nombre)
            
            if comio:
                # Exito: incrementa comidas y reinicia fallos
                self.comidas_realizadas += 1
                self.fallos_consecutivos = 0
            else:
                # Fallo: incrementa fallos consecutivos
                self.fallos_consecutivos += 1
                
                # Muere si 3 fallos consecutivos
                if self.fallos_consecutivos >= 3:
                    self.vivo = False
                    print(f"[MUERTE] {self.nombre} muere tras 3 fallos consecutivos")
                    break
        
        if self.vivo:
            print(f"[CONEJO] {self.nombre} se va (comio {self.comidas_realizadas} veces)")


def reponedor_proceso(comedero):
    """
    Hilo reponedor: anade 3 raciones cada 2 segundos (5 veces).
    """
    print("[REPONEDOR] Iniciado\n")
    
    for ciclo in range(1, 6):
        time.sleep(2.0)
        print(f"[REPONEDOR] Ciclo {ciclo}/5")
        comedero.reponer(3)
        print()


if __name__ == "__main__":
    print("=" * 70)
    print("EXAMEN OFICIAL JOVELLANOS - CONEJOS Y COMEDERO")
    print("Implementacion orientada a objetos (NIVEL AVANZADO)")
    print("=" * 70)
    print("\nConfiguracion:")
    print("  - 4 conejos (hilos independientes)")
    print("  - Cada conejo: 5 intentos de comer")
    print("  - Muerte: tras 3 fallos consecutivos")
    print("  - Reponedor: 3 raciones cada 2 segundos (5 ciclos)")
    print("  - Raciones iniciales: 0 (esperan reponedor)")
    print("=" * 70 + "\n")
    
    # Crear comedero (comienza con 0 raciones)
    comedero = Comedero(0)
    
    # Crear 4 conejos
    conejos = [
        Conejo("Conejo-Blanco", comedero),
        Conejo("Conejo-Gris", comedero),
        Conejo("Conejo-Cafe", comedero),
        Conejo("Conejo-Negro", comedero),
    ]
    
    # Iniciar hilo reponedor
    hilo_reponedor = threading.Thread(target=reponedor_proceso, args=(comedero,), 
                                       name="Reponedor", daemon=True)
    hilo_reponedor.start()
    
    # Iniciar conejos
    for conejo in conejos:
        conejo.start()
    
    # Esperar a que terminen todos los conejos
    for conejo in conejos:
        conejo.join()
    
    # Estadisticas finales
    print("\n" + "=" * 70)
    print("ESTADISTICAS FINALES")
    print("=" * 70)
    
    print("\nComidas por conejo:")
    for conejo in conejos:
        print(f"  {conejo.nombre}: {conejo.comidas_realizadas} comidas")
    
    print(f"\nTotal de comidas dadas: {comedero.total_comidas}")
    print(f"Raciones sin repartir: {comedero.raciones_disponibles}")
    print("=" * 70)
