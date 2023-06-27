# Desafio 74 - Maior e Menor valores em tupla

"""
Crie um programa que vai gerar 5 números aleatorios e colocar em uma tupla
Depois disso, mostre a listagem de números gerados e também indique o Menor e o Maior
valor que está na tupla
"""
from random import randint
numeros = (randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100))
print('\033[34mOs números sorteados são:\033[m')
for n in numeros:
    print(f'\033[31m{n}\033[m', end=' → ')
print('Fim')
print(f'O maior número é \033[33m{max(numeros)}\033[m')
print(f'O menor número é \033[33m{min(numeros)}\033[m')
