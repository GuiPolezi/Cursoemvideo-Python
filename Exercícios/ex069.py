# Desafio 69 - Análise de dados de grupo

"""
Crie um programa que leia a idade e o sexo de varias pessoas.
A cada pessoa cadastrada, o programa devera perguntar se o usuário quer continuar ou não,
no final, mostre:

- Quantas pessoas tem mais de 18 anos
- Quantos homens foram cadastrados.
- Quantas mulheres tem menos de 20 anos.
"""

import datetime
ano = datetime.date.today().year

cont = 0
maior = 0
menormulheres = 0
while True:
    print('-' * 30)
    idade = int(input('\033[31mIdade\033[m: '))
#   anonasc = ano - idade
    sexo = ' '
    if idade >= 18:
        maior += 1
    while sexo not in 'MF':
        sexo = str(input('\033[32mSexo [M/F]\033[m: ')).upper().strip()[0]
    if sexo in 'M':
        cont += 1
        homens = cont
    elif sexo in 'F' and idade <= 20:
        menormulheres += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\033[33mQuer continuar? [S/N]\033[m: ')).upper().strip()[0]
    if continuar == 'N':
        break
print('=' * 30)
print('Fim da análise')
print(f'\033[34m{homens}\033[3m Homem[ns] registrado[s]!')
print(f'\033[34m{maior}\033[3m pessoa[s] maior[es] de idade!')
print(f'\033[34m{menormulheres}\033[3m Mulher[es] com menos de 20 anos!')