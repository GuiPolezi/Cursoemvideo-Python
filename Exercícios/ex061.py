# Desafio 61 - Progressão aritmética 2.0

"""
Refaça o desafio 51, lendo o primeiro termo
e a razão de uma pa, mostrando os 10 primeiros termos da progressão
usando a estrutura while
"""

print('\033[31mGerador de PA\033[0m')
print('-=' * 15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -> ', end='')
    termo += razao
    cont += 1
print('FIM')