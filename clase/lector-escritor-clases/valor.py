class Valor:
    def __init__(self, inicial=0):
        self.numero = inicial
    
    def incrementar(self):
        self.numero += 1

    def set_valor(self,num):
        self.numero = num
