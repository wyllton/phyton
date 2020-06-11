class Bola:
    def __init__(self,cor,circunferencia,material):
        self.cor = cor
        self.circinferencia = circunferencia
        self.material = material

    def trocaCor(self,novacor):
        self.cor = novacor

    def mostraCor(self):
        return self.cor
