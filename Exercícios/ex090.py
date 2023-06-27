# Desafio 90 - Dicionário em Python

"""
Faça um programa que leia o nome e média de um aluno,
Guardando também a situação em um dicionario. No final, mostre o conteúdo da estrutura na tela
"""
from time import sleep

aluno = {'Nome': str(input('Nome: '))}
aluno['Média'] = float(input(f'Média de {aluno["Nome"]}: '))
print(f'Média é = {aluno["Média"]}')
if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
elif 5 <= aluno['Média'] < 7:
    aluno['Situação'] = 'Recuperação'
else:
    aluno['Situação'] = 'Reprovado'
print('-' * 30)
print('Analisando...')
sleep(0.5)
for key, value in aluno.items():
    print(f'{key}: {value}')