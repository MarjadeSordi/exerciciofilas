from fila import *

class Torre():
    def __init__(self,id, nome, endereco):
        self.id = id
        self.nome = nome
        self.endereco = endereco
       
class Apartamento(): 
    def __init__(self, id, numero, vaga, torre):
        self.id = id
        self.numero = numero
        self.vaga = vaga
        self.torre = torre
    
    def addvaga(self, vaga):
        fila = Fila()
        fila.push(vaga) 
        return fila.imprimir()
      
    def deletevaga(self):
        vaganagaragem = Fila()
        vaganagaragem.pop()

    def imprimiraFila(self):
        vaganag = Fila()
        vaganag.imprimir()