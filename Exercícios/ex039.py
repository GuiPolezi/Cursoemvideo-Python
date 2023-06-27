# Desafio 39 - Alistamento militar

"""
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:

- Se ele ainda vai se alistar ao serviço militar.
- Se é a hora de se alistar
- Se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou passou do prazo
"""
from datetime import date

atual = date.today().year
ano = int(input('Ano em que nasceu: '))
idade = atual - ano

if idade < 18:
    saldo = 18 - idade
    print(f'Você ainda vai se alistar no serviço militar!!')
    print(f'voce tem {idade} anos')
    print(f'Faltam {saldo} anos para se alistar')
elif idade == 18:
    print(f'Chegou a hora de se alistar no serviço militar!')
else:
    saldo = idade - 18
    print(f'Passou do tempo de se alistar')
    print(f'Velho demais, você tem {idade} anos')
    print(f'Passaram-se {saldo} anos')
print(f'Estamos em {atual}')