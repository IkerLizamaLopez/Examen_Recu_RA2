"""
EJERCICIO 02: Buffer Limitado Manual (NIVEL INTERMEDIO)
"""

import threading
import time

buffer = []
tamanio_maximo = 3
condition = threading.Condition()

def productor(id_prod):
    for i in range(10):
        with condition:
            while len(buffer) >= tamanio_maximo:
                print(f"Productor {id_prod} espera (buffer lleno)")
                condition.wait()
            
            elemento = f"P{id_prod}-{i}"
            buffer.append(elemento)
            print(f"Productor {id_prod} produce: {elemento} (buffer: {len(buffer)})")
            condition.notify_all()
        
        time.sleep(0.2)

def consumidor(id_cons):
    for i in range(5):
        with condition:
            while len(buffer) == 0:
                print(f"Consumidor {id_cons} espera (buffer vacio)")
                condition.wait()
            
            elemento = buffer.pop(0)
            print(f"Consumidor {id_cons} consume: {elemento} (buffer: {len(buffer)})")
            condition.notify_all()
        
        time.sleep(0.3)

if __name__ == "__main__":
    print("=== Buffer Limitado Manual (tamanio=3) ===\n")
    
    h1 = threading.Thread(target=productor, args=(1,))
    h2 = threading.Thread(target=consumidor, args=(1,))
    h3 = threading.Thread(target=consumidor, args=(2,))
    
    h1.start()
    h2.start()
    h3.start()
    
    h1.join()
    h2.join()
    h3.join()
    
    print("\nCompletado")
