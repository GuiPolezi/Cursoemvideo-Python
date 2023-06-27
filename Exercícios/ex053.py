# Desafio 53 - Detector de Palíndromo

"""
Crie um programa que leia uma frase qualquer
e diga se ela é um PALÍNDROMO, desconsiderando os espaços
"""

frase = str(input('Digite uma frase: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
# print(f'Você digitou a frase {junto}')
inverso = ''
for letra in range(len(junto)-1, -1, -1):
    inverso += junto[letra]
if inverso == junto:
    print(f'O inverso de {junto} é {inverso}')
    print('Temos um palíndromo!')
else:
    print('A frase digitada não é um palíndromo!')
# print(junto, inverso)
