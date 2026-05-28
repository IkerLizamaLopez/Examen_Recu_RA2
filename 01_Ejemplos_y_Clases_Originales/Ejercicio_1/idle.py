from threading import Thread,Lock
import time
import os

oro = 0
nivel = 1

lock = Lock()

def generar_oro():
    global oro
    while True: #Hacemos un bucle infinito para que siga produciendose oro siempre
        with lock:#Bloqueamos para poder modificar la variable oro y evitar problemas de concurrencia
            producir = nivel * 2
            oro += producir #Actualizamos la variable
        time.sleep(0.2)

def principal():
    global oro,nivel
    while True:
        print(f"Tiene {oro}de oro y su nivel del pico es {nivel}")
        opcion = input("(Enter).Volver a mostrar \n (m).Mejorar pico \n (q).Salir \n").strip().lower()
        if opcion == "":
            continue #Si presionamos el enter salimos del if y volvemos a mostrar el oro y el nivel
        elif opcion == "m":
            with lock:
                if oro >= 100:#Si el oro es mayor le quitamos los 100 de oro por la mejora del pico y le subimos un nivel
                    oro -= 100
                    nivel += 1
                else:
                    print("No tienes suficiente oro")
        elif opcion == "q":
            os._exit(0)#Salimos 
        else:
            print("Valor introducido no valido")

hilo_generar = Thread(target=generar_oro).start()
hilo_principal = Thread(target=principal).start()
