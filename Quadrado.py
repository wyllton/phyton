class Quadrado:
    def __init__(self, lado):
        self.lado = lado

    def novoLado(self, novolado):
        self.lado = novolado
        return self.lado**2
