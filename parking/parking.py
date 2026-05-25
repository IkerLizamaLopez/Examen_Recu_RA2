from threading import Condition
import logging
import time


class Parking:
    def __init__(self, plazas, precio):
        self.plazas_disponibles = plazas
        self.plazas_totales = plazas
        self.precio = precio
        self.total_acumulado = 0
        self.condicion = Condition()
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger(__name__)

    def entrar(self, coche):
        with self.condicion:
            while self.plazas_disponibles == 0:
                self.logger.info(f"Coche [{coche}] esperando plaza...")
                self.condicion.wait()

            self.plazas_disponibles -= 1
            self.logger.info(
                f"Coche [{coche}] ENTRA al parking "
                f"(plazas libres: {self.plazas_disponibles}/{self.plazas_totales})"
            )

    def salir(self, coche, horas):
        with self.condicion:
            self.plazas_disponibles += 1
            pago = horas * self.precio
            self.total_acumulado += pago
            self.logger.info(
                f"Coche [{coche}] SALE del parking — "
                f"{horas}h × {self.precio}€ = {pago:.2f}€ "
                f"(recaudado: {self.total_acumulado:.2f}€)"
            )
            self.condicion.notify()