# Desafio 89 - Boletim com listas compostas

"""
Crie um programa que leia nome e duas notas de varios alunos e guarde tudo em uma lista composta
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas
de cada aluno individualmente.
"""
from time import sleep

ficha = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    ficha.append([nome, [nota1, nota2], media])
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while resposta not in 'SN':
        resposta = str(input('ERRO! Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta in 'N':
        break
print('-=' * 30)
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>6}')
print('-' * 26)
for i, a in enumerate(ficha):  # i = índice, a = aluno
    print(f'{i:<4}{a[0]:<10}{a[2]:>6.1f}')
while True:
    print('-' * 35)
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if opcao == 999:
        print('Finalizando...')
        sleep(0.5)
        break
    if opcao <= len(ficha) - 1:
        print(f'Notas de {ficha[opcao][0]} = {ficha[opcao][1]}')
print('<<<<< Volte sempre >>>>>')