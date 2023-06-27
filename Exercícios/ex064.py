# Desafio 64 - Tratando varios valores v1.0

"""
Crie um programa que leia varios números inteiros pelo teclado.
O programa só vai parar quando o usuario digitar o valor 999, que é a condição de parada
No final mostre quantos números foram digitados e qual foi a soma entre eles ( desconsiderando o flag)
"""


print('\033[33mTratando varios valores\033[m')
print('O programa so vai parar se o usuário digitar \033[31m999\033[m')
print('-' * 20)
n = 0
cont = 0
soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    cont += 1
    soma += n
print(f'O programa foi encerrado com {cont} números digitados!')
print(f'= {soma}')