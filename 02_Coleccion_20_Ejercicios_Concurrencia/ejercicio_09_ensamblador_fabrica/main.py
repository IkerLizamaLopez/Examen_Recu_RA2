"""
EJERCICIO 09: Ensamblador de Fabrica (Condition con Multiples Recursos)
Enunciado:
Simula el montaje en una fabrica de patinetes.
Se necesitan 2 ruedas, 1 manillar y 1 motor para ensamblar un patinete.
Los productores anaden piezas al almacen y el ensamblador espera (wait) mediante una unica variable Condition.
"""

import threading
import time
import random

# Variables compartidas (Almacen)
ruedas = 0
manillares = 0
motores = 0
patinetes_creados = 0
limite_patinetes = 5

# Sincronizacion
cond_almacen = threading.Condition()
simulacion_activa = True

def productor_ruedas():
    global ruedas, simulacion_activa
    while simulacion_activa:
        time.sleep(0.4)
        with cond_almacen:
            if not simulacion_activa:
                break
            ruedas += 1
            print(f" [PRODUCCION] Se anadio 1 Rueda. Stock: (Ruedas: {ruedas}, Manillares: {manillares}, Motores: {motores})")
            cond_almacen.notify_all()

def productor_manillares():
    global manillares, simulacion_activa
    while simulacion_activa:
        time.sleep(0.8)
        with cond_almacen:
            if not simulacion_activa:
                break
            manillares += 1
            print(f" [PRODUCCION] Se anadio 1 Manillar. Stock: (Ruedas: {ruedas}, Manillares: {manillares}, Motores: {motores})")
            cond_almacen.notify_all()

def productor_motores():
    global motores, simulacion_activa
    while simulacion_activa:
        time.sleep(1.2)
        with cond_almacen:
            if not simulacion_activa:
                break
            motores += 1
            print(f" [PRODUCCION] Se anadio 1 Motor. Stock: (Ruedas: {ruedas}, Manillares: {manillares}, Motores: {motores})")
            cond_almacen.notify_all()

def ensamblador():
    global ruedas, manillares, motores, patinetes_creados, simulacion_activa
    while patinetes_creados < limite_patinetes:
        with cond_almacen:
            # Esperar mientras falten piezas para armar 1 patinete (2 ruedas, 1 manillar, 1 motor)
            while (ruedas < 2 or manillares < 1 or motores < 1) and simulacion_activa:
                print(f" [ENSAMBLADOR] Esperando piezas necesarias... Stock: (R:{ruedas}, M:{manillares}, Mot:{motores})")
                cond_almacen.wait()
                
            if not simulacion_activa:
                break
                
            # Consumir piezas del almacen
            ruedas -= 2
            manillares -= 1
            motores -= 1
            patinetes_creados += 1
            
            print(f"  [ENSAMBLADO] Patinete #{patinetes_creados} montado con exito! Piezas restantes: (R:{ruedas}, M:{manillares}, Mot:{motores})")
            
            if patinetes_creados >= limite_patinetes:
                print(f" Se ha alcanzado el limite de {limite_patinetes} patinetes!")
                simulacion_activa = False
                cond_almacen.notify_all()
                break

if __name__ == "__main__":
    print("Iniciando la linea de produccion de la fabrica de patinetes...")
    
    # Crear e iniciar hilos
    h_ruedas = threading.Thread(target=productor_ruedas, name="ProdRuedas")
    h_manillares = threading.Thread(target=productor_manillares, name="ProdManillares")
    h_motores = threading.Thread(target=productor_motores, name="ProdMotores")
    h_ensamblador = threading.Thread(target=ensamblador, name="Ensamblador")
    
    h_ruedas.start()
    h_manillares.start()
    h_motores.start()
    h_ensamblador.start()
    
    # Esperar solo al ensamblador, que es el que detiene la simulacion
    h_ensamblador.join()
    
    # Asegurar que los hilos productores se enteren y finalicen
    with cond_almacen:
        simulacion_activa = False
        cond_almacen.notify_all()
        
    h_ruedas.join()
    h_manillares.join()
    h_motores.join()
    
    print("\n Fabrica cerrada. Todo el lote de patinetes ha sido completado.")
