"""
EJERCICIO 04: Parking VIP (NIVEL AVANZADO)
"""

import threading
import time

plazas_estandar = 2
plazas_vip = 1
condition = threading.Condition()

def coche_vip(id_coche):
    global plazas_vip, plazas_estandar
    
    print(f"VIP {id_coche} busca plaza...")
    
    with condition:
        while plazas_vip == 0:
            print(f"VIP {id_coche} espera plaza VIP...")
            condition.wait()
        
        plazas_vip -= 1
        print(f"VIP {id_coche} ESTACIONADO en VIP (VIP: {plazas_vip}, Est: {plazas_estandar})")
    
    time.sleep(2)
    
    with condition:
        plazas_vip += 1
        print(f"VIP {id_coche} SE VA de VIP (VIP: {plazas_vip}, Est: {plazas_estandar})")
        condition.notify_all()

def coche_normal(id_coche):
    global plazas_estandar, plazas_vip
    
    print(f"Normal {id_coche} busca plaza...")
    
    with condition:
        while plazas_estandar == 0 and plazas_vip == 0:
            print(f"Normal {id_coche} espera plaza...")
            condition.wait()
        
        if plazas_estandar > 0:
            plazas_estandar -= 1
            tipo = "Estandar"
        else:
            plazas_vip -= 1
            tipo = "VIP"
        
        print(f"Normal {id_coche} ESTACIONADO en {tipo} (VIP: {plazas_vip}, Est: {plazas_estandar})")
    
    time.sleep(2)
    
    with condition:
        if tipo == "Estandar":
            plazas_estandar += 1
        else:
            plazas_vip += 1
        
        print(f"Normal {id_coche} SE VA de {tipo} (VIP: {plazas_vip}, Est: {plazas_estandar})")
        condition.notify_all()

if __name__ == "__main__":
    print("=== Parking VIP (1VIP, 2Estandar) ===\n")
    
    hilos = []
    
    for i in range(1, 3):
        h = threading.Thread(target=coche_vip, args=(i,))
        hilos.append(h)
        h.start()
    
    for i in range(1, 4):
        h = threading.Thread(target=coche_normal, args=(i,))
        hilos.append(h)
        h.start()
    
    for h in hilos:
        h.join()
    
    print("\nCompletado")
