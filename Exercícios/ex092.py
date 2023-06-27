# Desafio 92 - Cadastro de Trabalhador em Python

"""
Crie um programa que leia NOME, ANO DE NASCIMENTO e CARTEIRA DE TRABALHO e cadastre-os
(com idade) em um dicionário, se por acaso a CTPS(carteira trab) for diferente de ZERO,
o dicionário recebera também o ANO DE CONTRATAÇÃO e o SALÁRIO.
Calcule e acrescente, além da IDADE, com quantos anos a pessoa vaise APOSENTAR.
"""

from datetime import datetime
print('=' * 30)
print(f'\033[31m{"== Cadastro do Trabalhador ==":^30}\033[m')
print('=' * 30)

dados = dict()
dados['Nome'] = str(input('nome: '))  # Adicionando a key Nome e lendo um valor
nascimento = int(input('Ano de nascimento: '))  # Lendo o ano de nascimento
dados['Idade'] = datetime.today().year - nascimento   # Adicionando a key Idade e recebe o ano atual - nascimento
dados['CTPS'] = int(input('Carteira de trabalho (0 não tem): '))
if dados['CTPS'] != 0:
    dados['Ano_contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = int(input('Salário: R$ '))
    dados['Aposentadoria'] = (dados['Ano_contratação'] - nascimento) + 35

print('=' * 30)
print('\033[30mDados cadastrados:\033[m')
for k, v in dados.items():
    print(f'  - {k}: {v}')