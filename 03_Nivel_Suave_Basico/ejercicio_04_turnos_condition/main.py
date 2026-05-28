"""
EJERCICIO 04: Turnos - Condition Variable (NIVEL SUAVE)
Alterna entre dos hilos usando Condition
"""

import threading

condition = threading.Condition()
turno_actual = 1  # 1 = Hilo 1, 2 = Hilo 2
rondas = 3

def hilo_1():
    global turno_actual
    for ronda in range(1, rondas + 1):
        with condition:
            # Esperar hasta que sea mi turno
            while turno_actual != 1:
                condition.wait()
            
            print(f"Turno de Hilo 1 (ronda {ronda})")
            
            # Ceder turno
            turno_actual = 2
            condition.notify()

def hilo_2():
    global turno_actual
    for ronda in range(1, rondas + 1):
        with condition:
            # Esperar hasta que sea mi turno
            while turno_actual != 2:
                condition.wait()
            
            print(f"Turno de Hilo 2 (ronda {ronda})")
            
            # Ceder turno
            turno_actual = 1
            condition.notify()

if __name__ == "__main__":
    print("=== Sistema de Turnos con Condition ===")
    print("")
    
    h1 = threading.Thread(target=hilo_1)
    h2 = threading.Thread(target=hilo_2)
    
    h1.start()
    h2.start()
    
    h1.join()
    h2.join()
    
    print("")
    print("Terminado")
