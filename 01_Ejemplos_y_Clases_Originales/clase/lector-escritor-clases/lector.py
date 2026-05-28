import time

class Lector:
    def __init__(self, fichero, tiempo_lectura):
        self.fichero = fichero
        self.tiempo_lectura = tiempo_lectura
    
    def leer(self):
        while True:
            with self.fichero.lock:
                with open(self.fichero.ruta, "r") as file:
                    try:
                        numero = int(file.read())
                        self.fichero.set_valor(numero)
                        print("El lector ha leído",self.fichero.numero)
                    except Exception as e:
                        print(e)
            time.sleep(self.tiempo_lectura)