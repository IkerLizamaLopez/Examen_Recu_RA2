"""
EJERCICIO 02: Barbero Durmiente (NIVEL AVANZADO)
"""

import threading
import time

NUM_SILLAS = 3
sillas_libres = NUM_SILLAS
condition = threading.Condition()
barbero_ocupado = False

def barbero():
    global barbero_ocupado
    while True:
        with condition:
            while sillas_libres == NUM_SILLAS and not barbero_ocupado:
                print(f"Barbero durmiendo (sillas: {NUM_SILLAS - sillas_libres}/{NUM_SILLAS})")
                condition.wait()
            
            if barbero_ocupado:
                print("Barbero cortando...")
                time.sleep(1)
                barbero_ocupado = False
            
            condition.notify_all()

def cliente(id_cliente):
    global sillas_libres, barbero_ocupado
    
    with condition:
        if sillas_libres > 0:
            sillas_libres -= 1
            print(f"Cliente {id_cliente} entra (sillas: {NUM_SILLAS - sillas_libres}/{NUM_SILLAS})")
            barbero_ocupado = True
            condition.notify_all()
            
            # Espera a ser atendido
            while barbero_ocupado:
                condition.wait()
            
            sillas_libres += 1
            print(f"Cliente {id_cliente} se va (sillas: {NUM_SILLAS - sillas_libres}/{NUM_SILLAS})")
        else:
            print(f"Cliente {id_cliente} ve sillas llenas y se va")

if __name__ == "__main__":
    print("=== Barbero Durmiente (3 sillas) ===\n")
    
    h_barbero = threading.Thread(target=barbero, daemon=True)
    h_barbero.start()
    
    # Clientes llegan
    time.sleep(0.5)
    for i in range(1, 8):
        h = threading.Thread(target=cliente, args=(i,))
        h.start()
        time.sleep(0.3)
    
    # Espera a que terminen clientes
    time.sleep(5)
    print("\nCompletado")
