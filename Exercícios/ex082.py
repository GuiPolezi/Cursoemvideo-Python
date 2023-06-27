# Desafio 82 - Dividindo valores em várias listas

"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas valores PARES
e os valores ÍMPARES digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
"""

a = list()
par = list()
impar = list()
while True:
    n = (int(input('Digite um número: ')))
    a.append(n)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Resposta invalida! Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar in 'N':
        break
for v in a:
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('=' * 30)
print(f'\033[31mLista inteira: {a}\033[m')
print(f'\033[34mLista dos pares: {par}\033[m')
print(f'\033[33mLista dos ímpare: {impar}\033[m')
