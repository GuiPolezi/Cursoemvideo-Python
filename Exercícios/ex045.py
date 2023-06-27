# Desafio 45 - Game: PEDRA, PAPEL OU TESOURA

"""
Crie um programa que faça o computador jogar jokenpô com você;
"""
from random import randint
from time import sleep

escolhas = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)

print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')

jogada = int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
sleep(1)
print('-=' * 11)
print(f'Computador jogou {escolhas[computador]}')
print('X')
print(f'Jogador jogou {escolhas[jogada]}')
print('-=' * 11)

if computador == 0:
    if jogada == 2:
        print('Computador ganhou!')
    elif jogada == 1:
        print('Jogador ganhou!')
    elif jogada == computador:
        print('EMPATOU!!')
elif computador == 1:
    if jogada == 0:
        print('Computador ganhou!')
    elif jogada == 2:
        print('Jogador ganhou!')
    elif jogada == computador:
        print('EMPATOU!!')
elif computador == 2:
    if jogada == 1:
        print('O computador ganhou!')
    elif jogada == 0:
        print('Jogador ganhou!')
    elif jogada == computador:
        print('EMPATOU!!')
