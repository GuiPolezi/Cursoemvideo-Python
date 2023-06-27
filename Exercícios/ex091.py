# Desafio 91 - Jogo de dados em python

"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados
em um dicionário. No final, coloque esse dicionario em ordem, sabendo que o vencedor tirou o maior número
no dado
"""

from random import randint
from time import sleep

jogos = dict()
c = 0

for cont in range(1, 5):  # 4 jogadores
    jogada = randint(1, 6)  # randomizando as jogadas
    jogos["Jogador" + str(cont)] = jogada  # adicionando a chave 'jogador' + contagem de 1 a 4, no valor jogada
print('\033[34mValores sorteados:\033[m')

for k, v in jogos.items():  # para key(chave), valor in jogos1.items() -> acessando os items(keys e valores)
    sleep(0.5)
    print(f'{k} tirou {v} no dado')  # K -> key = jogador, v -> valor = jogada
    sleep(0.5)
print('=' * 30)
print(f'{"== Ranking Jogadores ==":^30}')

# noinspection PyTypeChecker
jogos_ordenados = dict(sorted(jogos.items(), key=lambda item: item[1], reverse=True))  # Colocar em ordem decrescente
for k, v in jogos_ordenados.items():  # para key(chave), valor in jogos_ordenados(Dicionario em ordem decrescente)
    c += 1  # Contador
    print(f'{c}o. Lugar: {k} com {v}')
    sleep(0.5)