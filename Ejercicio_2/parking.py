from threading import Condition
import time


class Parking:

    def __init__(self,plazas,precio):
        self.plazas_disponible = plazas
        self.plazas_totales = plazas
        self.precio = precio
        self.total_acumulado = 0
        self.cond = Condition()

    def entrar(self):#Bloqueamos los demas metodos , luego miramos si tenemos plazas disponibles
        with self.cond:
            while self.plazas_disponible == 0:#Si no hay plazas
                print("EL coche esta esperando")
                self.cond.wait() #Esperamos a que exista alguna libre , esperamos al notify
            self.plazas_disponible -= 1 #Le restamos 1 a la plaza disponble
            time.sleep(0.07)
            
                
                
    def salir(self,horas):
        with self.cond: #Bloqueamos a los demas metodos , y al salir sumamos una plaza 
            self.plazas_disponible += 1 
            pago = horas * self.precio
            self.total_acumulado += pago #Hacemos el pago y cambiamos el total acumulado
            print(f"El coche ha pagado {pago} por estar {horas} horas")
            self.cond.notify()#notificamos para que pueda entrar algun coche