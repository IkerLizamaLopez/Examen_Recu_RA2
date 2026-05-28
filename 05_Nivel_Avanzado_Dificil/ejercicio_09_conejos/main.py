"""
EJERCICIO 09: Conejos y Comedero (NIVEL AVANZADO)
EXAMEN OFICIAL JOVELLANOS - Comedero de Conejos
"""

import threading
import time
import random

# Recurso compartido: comedero
raciones_disponibles = 10
total_comidas_global = 0

# Proteccion de zona critica
lock_comedero = threading.Lock()

# Estadisticas por conejo
comidas_por_conejo = {}

def conejo(id_conejo):
    """
    Cada conejo intenta comer durante 5 intentos.
    Si falla 3 veces seguidas, muere.
    Si logra comer, los fallos seguidos se reinician.
    """
    global raciones_disponibles, total_comidas_global
    
    comidas_por_conejo[id_conejo] = 0
    intentos_totales = 5
    fallos_seguidos = 0
    
    while intentos_totales > 0:
        # Espera aleatoria entre 0.5 y 2 segundos
        tiempo_espera = random.uniform(0.5, 2.0)
        time.sleep(tiempo_espera)
        
        print(f"Conejo {id_conejo} intenta comer (intentos restantes: {intentos_totales}, fallos seguidos: {fallos_seguidos}/3)")
        
        # ZONA CRITICA - protegida por lock
        with lock_comedero:
            if raciones_disponibles > 0:
                # Logra comer
                raciones_disponibles -= 1
                comidas_por_conejo[id_conejo] += 1
                total_comidas_global += 1
                fallos_seguidos = 0  # Reinicia fallos seguidos
                
                print(f"  EXITO: Conejo {id_conejo} COME (raciones restantes: {raciones_disponibles})")
            else:
                # Falla al comer
                fallos_seguidos += 1
                print(f"  FALLO: Conejo {id_conejo} no hay comida (fallos seguidos: {fallos_seguidos}/3)")
                
                # Muere tras 3 fallos seguidos
                if fallos_seguidos >= 3:
                    print(f"  MUERTE: Conejo {id_conejo} MUERE por hambre tras 3 fallos seguidos")
                    return
        
        intentos_totales -= 1
    
    print(f"Conejo {id_conejo} se va satisfecho (comio {comidas_por_conejo[id_conejo]} veces)")

def reponedor():
    """
    Repone el comedero con 3 raciones cada 2 segundos.
    Hace 5 reposiciones completas.
    """
    global raciones_disponibles
    
    for reposicion in range(1, 6):
        time.sleep(2)
        
        with lock_comedero:
            raciones_disponibles += 3
            print(f"[REPONEDOR] Reposicion {reposicion}: anade 3 raciones (total: {raciones_disponibles})\n")

if __name__ == "__main__":
    print("=" * 60)
    print("EXAMEN JOVELLANOS - CONEJOS Y COMEDERO")
    print("=" * 60)
    print(f"\nConfiguracion inicial:")
    print(f"- 4 conejos (hilos)")
    print(f"- Raciones iniciales: {raciones_disponibles}")
    print(f"- Cada conejo: 5 intentos maximo")
    print(f"- Muere si: 3 fallos seguidos")
    print(f"- Reponedor: 3 raciones cada 2 segundos (5 veces)")
    print("\n" + "=" * 60 + "\n")
    
    # Crear hilos de conejos
    hilos_conejos = [threading.Thread(target=conejo, args=(i,), name=f"Conejo-{i}") 
                     for i in range(1, 5)]
    
    # Crear hilo reponedor
    hilo_reponedor = threading.Thread(target=reponedor, name="Reponedor", daemon=True)
    
    # Iniciar todos los hilos
    hilo_reponedor.start()
    
    for h in hilos_conejos:
        h.start()
    
    # Esperar a que terminen todos
    for h in hilos_conejos:
        h.join()
    
    # Resultados finales
    print("\n" + "=" * 60)
    print("ESTADISTICAS FINALES")
    print("=" * 60)
    
    for id_conejo in sorted(comidas_por_conejo.keys()):
        print(f"Conejo {id_conejo}: comio {comidas_por_conejo[id_conejo]} veces")
    
    print(f"\nTotal de comidas dadas: {total_comidas_global}")
    print(f"Raciones sin repartir: {raciones_disponibles}")
    print("=" * 60)
