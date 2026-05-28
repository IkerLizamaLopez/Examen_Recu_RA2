from threading import Lock

class Fichero:
    def __init__(self, ruta, valor=0):
        self.ruta = ruta
        self.lock = Lock()
        self.numero = valor

    def incrementar(self):
        self.numero += 1

    def set_valor(self, num):
        self.numero = num
