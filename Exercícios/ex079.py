# Desafio 79 - Valores únicos em uma lista

"""
Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente
"""
from time import sleep
valores = list()
while True:
    n = int(input('\033[34mDigite um valor: \033[m'))
    if n not in valores:
        valores.append(n)
        print('\033[32mValor adicionado com sucesso!\033[m')
    else:
        print('\033[31mValor duplicado, não vou adicionar!\033[m')
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    sleep(0.5)
    print('-=' * 30)
    if continuar not in 'S':
        break
print(f'\033[35mLista em ordem crescente:\033[m')
valores.sort()
print(valores)