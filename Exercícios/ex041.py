# Desafio 41 - Classificando atletas

"""
A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta
e mostre sua categoria, de acordo com a idade:

- até 9 anos: MIRIM
- até 14 anos: INFANTIL
- até 19 anos: JUNIOR
- até 20 anos: SENIOR
- acima: MASTER
"""
from datetime import date

anonasc = int(input('Diga o seu ano de nascimento: '))
atual = date.today().year
idade = atual - anonasc

if idade <= 9:
    print('Categoria MIRIM')
    print(f'Você tem {idade} anos')
elif 10 <= idade <= 14:
    print('Categoria INFANTIL')
    print(f'você tem {idade} anos')
elif 15 <= idade <= 19:
    print('Categoria JUNIOR')
    print(f'Você tem {idade} anos')
elif 20 <= idade <= 25:
    print('Categoria Sênior')
    print(f'Você tem {idade} anos')
else:
    print('Você está na maior categoria: MASTER!')
    print(f'Você tem {idade} anos')