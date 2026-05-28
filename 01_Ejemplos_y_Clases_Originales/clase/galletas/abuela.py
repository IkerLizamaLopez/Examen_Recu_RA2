import time
class Abuela:
    def __init__(self, galletas_bandeja, tiempo_cocinado, mesa):
        self.galletas_bandeja = galletas_bandeja
        self.tiempo_cocinado = tiempo_cocinado
        self.mesa = mesa

    def hacer_galletas(self):
        while True:
            with self.mesa.condicion:
                while (self.mesa.galletas + self.galletas_bandeja) > self.mesa.huecos_max:
                    self.mesa.condicion.wait()
                self.mesa.condicion.notify_all()
            print(f"Abuela se dispone a preparar una tanda de galletas")
            time.sleep(self.tiempo_cocinado)
            with self.mesa.condicion:
                self.mesa.annadir_bandeja(self.galletas_bandeja)
                print(f"Abuela deja la bandeja en la mesa, hay {self.mesa.galletas} en total")
        
        