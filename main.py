from classes import *
from fila import *



teste = Torre(1, 'bloco A', 'tamandare')

apto = Apartamento(1,'202','vaga', teste)
print (apto.torre.nome)




testando = Fila()
testando.push('2')
testando.push('3')
testando.push('4')
testando.push('5')
testando.imprimir()
testando.pop()
testando.imprimir()