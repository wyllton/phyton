class Carro:
    def __init__(self, velMax, cor: object = "", ligado: object = False) -> object:
        self.velMax = velMax
        self.cor = cor
        self.ligado = ligado


    def mostrar(self):
        print(self.velMax)
        print(self.cor)
        print(self.ligado)


    def ligar(self):
        self.ligado = True


    def desligar(self):
        self.ligado = False


    def andar(self):
        if self.ligado:
            print("Andando")
        else:
            print("Carro Desligado")