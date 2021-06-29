from fila import *



class Torre():
    def __init__(self,id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def getimprimir(self):
        print('Id da Torre:  ' + str(self.id) + ' Nome da Torre: ' + str(self.nome) + ' Endereço'+ str(self.endereco))

    
class Apartamento(): 
    def __init__(self, id, numero, vaga, torre):
        self.id = id
        self.numero = numero
        self.vaga = vaga
        self.torre = torre
    
    def getimprimir(self):
        print('Id da Torre:  ' + str(self.id) + ' Numero do Apartamento: ' + str(self.numero) + ' Vaga'+ str(self.vaga) + ' Torre: ' + str(self.torre))

