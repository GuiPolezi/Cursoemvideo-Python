# Desafio 66 - Vários números com flag

"""
Crie um programa que leia varios números inteiros pelo teclado.
O programa so vai parar quando o usuario digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag)
"""

cont = soma = 0
while True:
    n = int(input('Digite um valor (999 para parar): '))
    if n == 999:
        print('Programa encerrado!')
        break
    cont += 1
    soma += n
print('=' * 30)
print(f'Total de números digitados = \033[33m{cont}\033[m')
print(f'Soma de todos os números = \033[34m{soma}\033[m')

