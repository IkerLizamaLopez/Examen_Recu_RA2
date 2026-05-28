from threading import Condition
class Mesa:
    def __init__(self, huecos):
        self.galletas = 0
        self.huecos_max = huecos
        self.condicion = Condition()
    
    def annadir_bandeja(self, galletas):
        self.galletas = self.galletas + galletas

    def coger_galleta(self):
        self.galletas -= 1