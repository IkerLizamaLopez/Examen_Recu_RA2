import time
import random
import logging


class Coche:
    contador = 0

    def __init__(self, parking):
        Coche.contador += 1
        self.id = Coche.contador
        self.parking = parking
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def __str__(self):
        return f"Coche-{self.id}"

    def aparcar(self):
        self.parking.entrar(self)

        horas = random.randint(1, 8)
        self.logger.info(f"Coche [{self}] aparcado durante {horas}h")
        time.sleep(horas * 0.1)  # simulación: 0.1s por hora

        self.parking.salir(self, horas)
        self.logger.info(f"Coche [{self}] ha terminado")