import time
class Escritor:
    def __init__(self, fichero, tiempo_escritura):
        self.fichero = fichero
        self.tiempo_escritura = tiempo_escritura

    def escribir(self):
        while True:
            with self.fichero.lock:
                with open(self.fichero.ruta, "w") as file:
                    self.fichero.incrementar()
                    try:
                        file.write(str(self.fichero.numero))
                        print("El escritor ha escrito", self.fichero.numero)
                    except Exception as e:
                        print(e)
            time.sleep(self.tiempo_escritura)