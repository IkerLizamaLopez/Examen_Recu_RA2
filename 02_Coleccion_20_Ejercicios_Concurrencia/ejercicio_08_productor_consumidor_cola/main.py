"""
EJERCICIO 08: Productor-Consumidor con Cola (Queue)
Enunciado:
Implementa el patron Productor-Consumidor usando queue.Queue.
Varios clientes anaden pedidos (put) a una cola con capacidad de 5, y varios operarios los extraen (get).
Finaliza de forma ordenada mediante el uso de centinelas None.
"""

import threading
import queue
import time
import random

# Cola de pedidos con tamano limitado
cola_pedidos = queue.Queue(maxsize=5)
print_lock = threading.Lock()

def productor_cliente(id_cliente):
    nombre = f"Cliente-{id_cliente}"
    for i in range(1, 4): # Cada cliente realiza 3 pedidos
        time.sleep(random.uniform(0.1, 0.6)) # Retardo simulado entre compras
        pedido = f"Pedido #{i} de {nombre}"
        
        with print_lock:
            print(f"[CLIENTE] {nombre} intentando enviar {pedido} a la cola... (Elementos en cola: {cola_pedidos.qsize()})")
            
        # put() se bloquea si la cola esta llena (maxsize=5)
        cola_pedidos.put(pedido)
        
        with print_lock:
            print(f"[CLIENTE] {nombre} ENVIO exitosamente {pedido}.")

def consumidor_operario(id_operario):
    nombre = f"OperarioAlmacen-{id_operario}"
    while True:
        with print_lock:
            print(f"[OPERARIO] {nombre} esperando pedidos...")
            
        # get() se bloquea si la cola esta vacia
        pedido = cola_pedidos.get()
        
        # Comprobar senal de parada (centinela)
        if pedido is None:
            with print_lock:
                print(f"[OPERARIO] {nombre} recibe senal de parada. Finalizando turno.")
            cola_pedidos.task_done()
            break
            
        with print_lock:
            print(f"[OPERARIO] {nombre} PROCESANDO y empaquetando: '{pedido}'")
            
        # Simular empaquetado del paquete
        time.sleep(random.uniform(0.6, 1.2))
        
        with print_lock:
            print(f"[OPERARIO] {nombre} COMPLETO: '{pedido}'")
            
        cola_pedidos.task_done()

if __name__ == "__main__":
    print("Iniciando sistema de procesamiento de pedidos con Cola Limitada (Max: 5)...")
    
    # 4 Hilos Clientes (Productores) -> Total de pedidos = 4 * 3 = 12 pedidos
    clientes = []
    for i in range(1, 5):
        t = threading.Thread(target=productor_cliente, args=(i,))
        clientes.append(t)
        t.start()
        
    # 2 Hilos Operarios (Consumidores)
    operarios = []
    for i in range(1, 3):
        t = threading.Thread(target=consumidor_operario, args=(i,))  # CORRECTO: consumidor_operario
        operarios.append(t)
        t.start()
        
    # Esperar a que los clientes realicen todos sus pedidos
    for t in clientes:
        t.join()
        
    print("\n[SISTEMA] Todos los clientes terminaron de comprar. Enviando senales de parada a los operarios...")
    
    # Enviar un "None" por cada operario para indicarles que terminen de forma limpia
    for _ in range(2):
        cola_pedidos.put(None)
        
    # Esperar a que terminen los operarios
    for t in operarios:
        t.join()
        
    print("\n[SISTEMA] Proceso de almacen terminado. Todos los pedidos han sido enviados.")
