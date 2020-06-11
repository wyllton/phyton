class NPC:
    def __init__(self, nome,time,forca,municao):
        self.nome = nome
        self.time = time
        self.forca = forca
        self.municao = municao
        self.vivo = True
        self.energia = 100


    def info(self):
        print(f'Nome {self.nome}')
        print(f'Time: {self.time}')
        print(f'Forca: {self.forca}')
        print(f'Municao {self.municao}')
        print(f'Vivo: {self.vivo}')
        print(f'energia: {self.energia}')


class Soldado(NPC):
    def __init__(self,nome,time):
        self.forca = 200
        self.municao = 200
        super(Soldado, self).__init__(nome,time,self.forca,self.municao)

class Guarda(NPC):
    def __init__(self,nome,time):
        self.forca = 100
        self.municao = 20
        super(Guarda, self).__init__(nome,time,self.forca,self.municao)

class Elite(NPC):
    def __init__(self,nome,time):
        self.forca =400
        self.municao = 500
        super(Elite, self).__init__(nome,time,self.forca,self.municao)


