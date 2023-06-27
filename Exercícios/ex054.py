# Desafio 54 - Grupo de maioridade

"""
Crie um programa que leia o ano de nascimento de 7 pessoas,
no final mostre quantas pessoas ainda não atingiram a maioridade
e quantas ja são maiores
"""
from datetime import date
ano = date.today().year
cmenor = 0
cmaior = 0

for c in range(1, 8):
    nasc = int(input(f'Em que ano a {c}ª pessoa nasceu? '))
    idade = ano - nasc
    if idade >= 18:
        cmaior += 1
    else:
        cmenor += 1
print(f'Ao todo tivemos {cmenor} pessoas menores de idade')
print(f'E também tivemos {cmaior} pessoas maiores de idade')