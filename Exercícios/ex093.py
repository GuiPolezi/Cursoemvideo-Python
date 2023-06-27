# Desafio 93 - Cadastro de jogador de futebol

"""
Crie um programa que gerencie o aproveitamento de um JOGADOR DE FUTEBOL.
O programa vai ler o NOME DO JOGADOR e QUANTAS PARTIDAS ele jogou.
Depois vai ler a QUANTIDADE DE GOLS feito em CADA PARTIDA. No final, tudo isso será guardado em um dicionário,
incluindo o TOTAL DE GOLS feitos durante o campeonato.
"""

print('=' * 30)
print(f'\033[32m{"== TRANSFERMARKET ==":^30}\033[m')
print('=' * 30)

jogador = dict()  # dicionario
gols = []   # lista
total = 0  # total

jogador['Nome'] = str(input('Nome do Jogador: '))
partidas_jogadas = int(input(f'Quantas partidas {jogador["Nome"]} jogou? '))

for p in range(partidas_jogadas):  # p = partida
    jogador["Gols"] = int(input(f'   Quantos gols na partida {p + 1}? '))   # adicionado chave(key) -> gols
    total = total + jogador["Gols"]  # Total de gols
    gols.append(jogador["Gols"])  # Adicionando na lista o dicionario com a chave Gols
jogador['Gols'] = gols  # Chave(key) gols passa a receber a lista
jogador['Total'] = total  # chave(key) total

print('=' * 60)
print(jogador)
print('=' * 60)

for k, v in jogador.items():   # k = key, v = valor
    print(f'O campo {k} tem o valor: {v}.')
print('=' * 60)

print(f'O jogador {jogador["Nome"]} jogou {partidas_jogadas} partidas.')

for i, v in enumerate(jogador["Gols"]):   # i = indice, v = valor
    print(f'  => Na partida {i + 1}, fez {v} gols')
print(f'Foi um total de {total} gols.')