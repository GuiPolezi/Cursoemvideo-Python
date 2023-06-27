# Desafio 28 - Jogo da adivinhação v1.0

"""
Escreva um programa que faça o computador "pensar em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual o número escolhido pelo computador.

O programa deverá escrever na tela se o usuário venceu ou perdeu
"""

from time import sleep
from random import randint

print('-=' * 30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=' * 30)

computador = randint(0, 5)
escolha = int(input("Em que número eu pensei? "))

if escolha == computador:
    print('Processando...')
    sleep(1)
    print(computador)
    print(F'Você acertou!!!')
elif escolha > 5:
    print('Número errado: Digite um número de 0 a 5.')
else:
    print('Processando...')
    sleep(1)
    print(f'Você errou o número pensado foi: {computador}')