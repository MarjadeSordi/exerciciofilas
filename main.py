from classes import *
from fila import *

torrescadastradas = []
aptocadastrados = []

def inserir_torre():
  numero = input('Digite o id da Torre: ')
  nome = input ('Digite o nome da Torre: ')
  endereco = input('Digite o endereço da Torre: ')
  inserir = Torre(numero, nome, endereco)
  torrescadastradas.append(nome)
  inserir.getimprimir()


def escolhertorre():
    for i, torres in enumerate(torrescadastradas): 
      print (i + 1, torres )
    torreescolhida = int(input('Escolha uma torre pelo índice: '))
    torre = torrescadastradas[(torreescolhida - 1)]
    return torre

def inserir_apartamento():
  id = input('Digite o id do Apartamento: ')
  numero = str(input('Digite o número do Apartamento: '))
  aptocadastrados.append(numero)
  vaga = input ('Digite o número da Vaga do apto, caso não tenha vaga, digite 0: ')
  torre = escolhertorre()
  inserir = Apartamento(id, numero, vaga, torre)
  inserir.getimprimir()

def escolherApartamento():
    for i, aptos in enumerate(aptocadastrados): 
      print (i + 1, aptos )
    aptosescolhidos = int(input('Escolha um apartamento para acrescentar na fila pelo índice: '))
    apart = aptocadastrados[(aptosescolhidos - 1)]
    return apart

def inserir_apartamento_na_fila():
  apartamento = escolherApartamento()
  inserirNafila = Fila()
  inserirNafila.push(apartamento)
  mostraroudeletar = int(input('Digite 1 para imprimir a fila e 2 para retirar da fila de espera o primeiro elemento: '))
  if mostraroudeletar == 1 :
    return inserirNafila.imprimir()
  elif mostraroudeletar == 2:
    inserirNafila.pop()
  mostrafila = int(input('Elemento deletado. Deseja imprimir a fila? Digite 1 para imprimir e 2 voltar ao menu: '))
  if mostrafila == 1:
    return inserirNafila.imprimir()
  elif mostrafila == 2:
    return menu ()
  

def menu():
    while True:
        print('''Digite: 
        1- Para inserir uma nova Torre;
        2- Para inserir um novo Apartamento;
        3- Para cadastrar ou deletar um apartamento na fila de espera para uma vaga: 
        0- para sair do programa''')
        consulta = input ('')
        if consulta == '0':break 
        elif consulta == '1': inserir_torre(); 
        elif consulta == '2': inserir_apartamento(); 
        elif consulta == '3': inserir_apartamento_na_fila();
    
menu()

