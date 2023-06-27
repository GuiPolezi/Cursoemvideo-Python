# Desafio 103 - Ficha de jogador

"""
Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador
e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a FICHA DO JOGADOR, mesmo que algum dado não tenha sido informado
corretamente
"""


def ficha(nome='<desconhecido>', ngols=0):
    print(f'O jogador {nome} fez {ngols} gol(s) no campeonato.')
    return ''

# Programa principal
print('-' * 30)
nome = str(input('Nome do Jogador: '))
gols = str(input('Número de Gols: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(ngols=gols)
else:
    ficha(nome, gols)