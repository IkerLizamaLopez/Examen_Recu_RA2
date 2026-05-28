from threading import Thread, Lock
import time
import random

class Coche(Thread):
    id_contador = 0
    lock_id = Lock()
    def __init__(self,parking):
            with Coche.lock_id:
               self.id = Coche.id_contador#Hacemos que la id sea unica y la autoincrementamos
               Coche.id_contador += 1
            self.parking = parking

    def iniciar_parking (self):
        self.parking.entrar() #Iniciamos el metodo de la clase parking
        horas_aparcadas = random.randint(1, 8) 
        time.sleep(horas_aparcadas) #Esperamos las horas que esta en el parking y el tiempo que tarda en salir 
        time.sleep(0.07)
        self.parking.salir(horas_aparcadas) #Sale algun coche