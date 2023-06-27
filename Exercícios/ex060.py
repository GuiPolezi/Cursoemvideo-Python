# Desafio 60 - Cálculo do fatorial

"""
Faça um programa que leia um número qualquer
e mostre seu fatorial

exemplo:
5! = 5x4x3x2x1 = 120
"""

print('\033[32mCalculo de fatorial!\033[0m')
n = int(input('Digite um número: '))
c = n
f = 1
print(f'\033[33mCalculando {n}\033[0m!', end=' ')
while c > 0:
    print(f'{c}', end=' ')
    print(f'x ' if c > 1 else '=', end='')
    f = f * c
    c -= 1
print(f' {f}')