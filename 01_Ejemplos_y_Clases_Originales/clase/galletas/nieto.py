import time

class Nieto:
    num_nietos = 1
    def __init__(self, tiempo_galleta, limite_hambre, tiempo_descanso, mesa):
        self.id_nieto = Nieto.num_nietos
        Nieto.num_nietos += 1
        self.tiempo_galleta = tiempo_galleta
        self.limite_hambre = limite_hambre
        self.tiempo_descanso = tiempo_descanso
        self.mesa = mesa
        self.contador_galletas = 0

    def comer_galletas(self):
        while True:
            print(f"El nieto [{self}] quiere comer galletas")
            with self.mesa.condicion:
                while self.mesa.galletas <= 0:
                    self.mesa.condicion.wait()
                self.mesa.coger_galleta() # la tiene
                self.contador_galletas += 1
                print(f"El nieto [{self}] está comiendo una galleta, lleva {self.contador_galletas}, en la mesa quedan {self.mesa.galletas}")
                self.mesa.condicion.notify_all()
            
            time.sleep(self.tiempo_galleta)
            if self.contador_galletas >= self.limite_hambre:
                print(f"El nieto [{self}] está bastante lleno, se espera antes de volver a coger")
                time.sleep(self.tiempo_descanso)
            

    def __str__(self):
        return f"NIETO_{self.id_nieto}"

    