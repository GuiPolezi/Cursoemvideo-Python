# Desafio 115a - Criando um menu em Python
"""
Crie um pequeno sistema modulazriado
que permita cadastrar pessoas pelo seu nome e idade em um arquivo de texto simples.

O sistema so vai ter 2 opções: cadastrar uma nova pessoa e listar todas as pessoas cadastradas
"""

# Desafio 115b - Arquivos em Python


from ex115.lib.interface import *
from ex115.lib.arquivos import *
from time import sleep

arq = 'arquivo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar nova pessoa', 'Lista de pessoas cadastradas', 'Sair do Sistema'])
    if resposta == 1:
        # Opção cadastrar pessoas
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = int(input('Idade: '))
        cadastrar(arq, nome, idade)
    elif resposta == 2:
        # Opção de listar pessoas
        lerArquivo(arq)
    elif resposta == 3:
        cabeçalho('Encerrando o Sistema...')
        break
    else:
        print('\033[31mERRO: dados invalidos\033[m')
    sleep(2)