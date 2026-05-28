"""
EJERCICIO 10: Bufer Limitado Manual (List + Condition)
Enunciado:
Implementa el patron Productor-Consumidor con bufer circular de tamano fijo manualmente.
Usa una lista estandar y una variable Condition para sincronizar las condiciones de lleno y vacio.
"""

import threading
import time
import random

CAPACIDAD = 3
bufer = []
conteo_produccion = 15 # Total de elementos a producir
elementos_producidos = 0
elementos_consumidos = 0

# Sincronizacion
cond_bufer = threading.Condition()

def productor():
    global bufer, elementos_producidos
    while elementos_producidos < conteo_produccion:
        time.sleep(random.uniform(0.1, 0.4))
        
        with cond_bufer:
            # Esperar mientras el bufer este lleno
            while len(bufer) >= CAPACIDAD:
                print("  [PRODUCTOR] Bufer LLENO. Esperando espacio libre...")
                cond_bufer.wait()
                
            # Producir elemento
            valor = elementos_producidos + 1
            bufer.append(valor)
            elementos_producidos += 1
            
            print(f" [PRODUCTOR] Producido: {valor} | Bufer actual: {bufer} (Tamano: {len(bufer)}/{CAPACIDAD})")
            
            # Notificar que hay un elemento nuevo para consumir
            cond_bufer.notify_all()

def consumidor():
    global bufer, elementos_consumidos
    while elementos_consumidos < conteo_produccion:
        time.sleep(random.uniform(0.6, 1.2)) # El consumidor es mas lento deliberadamente
        
        with cond_bufer:
            # Esperar mientras el bufer este vacio
            while len(bufer) == 0:
                print("  [CONSUMIDOR] Bufer VACIO. Esperando a que haya datos...")
                cond_bufer.wait()
                
            # Consumir el primer elemento (FIFO)
            valor = bufer.pop(0)
            elementos_consumidos += 1
            
            print(f" [CONSUMIDOR] Consumido: {valor} | Bufer restante: {bufer} (Tamano: {len(bufer)}/{CAPACIDAD})")
            
            # Notificar que hay un hueco libre en el bufer
            cond_bufer.notify_all()

if __name__ == "__main__":
    print(f"Iniciando simulacion del Bufer Limitado Manual (Capacidad: {CAPACIDAD})...")
    
    h_productor = threading.Thread(target=productor, name="Productor")
    h_consumidor = threading.Thread(target=consumidor, name="Consumidor")
    
    h_productor.start()
    h_consumidor.start()
    
    h_productor.join()
    h_consumidor.join()
    
    print("\n La simulacion manual de bufer limitado ha concluido exitosamente.")
