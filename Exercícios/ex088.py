# Desafio 88 - Palpites para Mega Sena

"""
Faça um programa que ajude o jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
"""
import emoji
from time import sleep
import random

print('-' * 30)
print(f'{emoji.emojize(":heavy_dollar_sign:")}\033[31m{"MEGA SENA":^27}\033[m{emoji.emojize(":heavy_dollar_sign:")}')
print('-' * 30)

jogos = []
pergunta = int(input('Quantos jogos você quer que eu sorteie? '))
print('\033[34m-=' * 5, f'SORTEANDO {pergunta} {"JOGO" if pergunta == 1 else "JOGOS"}', '-=' * 5, '\033[m')
for j in range(pergunta):
    jogos[:].append([])
    jogos.append(random.sample(range(1, 60), 6))  # Adiciona 6 números em cada jogo
    sleep(0.5)
for c in range(pergunta):
    print(f'Jogo {c + 1} = {sorted(jogos[c])}')
    sleep(0.5)
print('\033[34m-=' * 5, f'< BOA SORTE {emoji.emojize(":joker:")} >', '-=' * 5, '\033[m')
