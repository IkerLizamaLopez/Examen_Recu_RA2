"""
EJERCICIO 20: Descarga en Paralelo de Lotes con Pool de Hilos (ThreadPoolExecutor)
Enunciado:
Simula la descarga de datos desde 10 servidores paralelos utilizando un ThreadPoolExecutor de tamano 3.
Captura los resultados exitosos y gestiona las excepciones mediante objetos Future.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed
import threading
import time
import random

# Lock para sincronizar impresiones
print_lock = threading.Lock()

def descargar_servidor(servidor_id):
    nombre_hilo = threading.current_thread().name
    
    with print_lock:
        print(f" [{nombre_hilo}] Iniciando descarga del Servidor-{servidor_id}...")
        
    # Simular tiempo de descarga
    tiempo_descarga = random.uniform(0.5, 1.5)
    time.sleep(tiempo_descarga)
    
    # Simular fallos aleatorios (los servidores multiples de 5 fallan)
    if servidor_id % 5 == 0:
        raise ConnectionError(f"Fallo de conexion critico en el Servidor-{servidor_id} (Timeout).")
        
    return f"Exito: Descargados {random.randint(100, 500)} KB desde Servidor-{servidor_id} (t={tiempo_descarga:.2f}s)"

if __name__ == "__main__":
    print("Iniciando descargas en lote mediante ThreadPoolExecutor (Limite: 3 hilos paralelos)...")
    
    start_time = time.time()
    
    # Crear un pool con un maximo de 3 hilos concurrentes
    # El uso de 'with' garantiza que al salir se cierren todos los hilos del pool (equivale a shutdown)
    with ThreadPoolExecutor(max_workers=3) as executor:
        # Enviar las tareas al executor de manera asincrona
        #submit() retorna un objeto Future que representa la ejecucion pendiente
        tareas_futuras = {}
        for i in range(1, 11):
            future = executor.submit(descargar_servidor, i)
            tareas_futuras[future] = i
            
        print(" Todas las 10 peticiones han sido enviadas al pool de hilos de forma no bloqueante.\n")
        
        # Procesar los resultados a medida que se completen las descargas
        # as_completed() va cediendo los futures completados en tiempo real
        for future in as_completed(tareas_futuras):
            id_servidor = tareas_futuras[future]
            try:
                # Obtener el retorno del metodo o propagar la excepcion ocurrida
                resultado = future.result()
                with print_lock:
                    print(f" [EXITO-FUTURE] Servidor-{id_servidor}: {resultado}")
            except ConnectionError as ce:
                with print_lock:
                    print(f" [FALLO-FUTURE] Servidor-{id_servidor}: Ocurrio un error. Detalle: {ce}")
            except Exception as e:
                with print_lock:
                    print(f" [ERROR GENERAL] Servidor-{id_servidor}: {e}")
                    
    total_time = time.time() - start_time
    print(f"\n Todas las descargas en lote han terminado. Tiempo de ejecucion total: {total_time:.2f} segundos.")
    print("Nota: Con 3 hilos trabajando en paralelo y 10 descargas de ~1s, el tiempo total ronda los ~3.5s, en lugar de 10s secuenciales.")
