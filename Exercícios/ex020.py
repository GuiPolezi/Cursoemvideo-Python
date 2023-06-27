# Desafio 20 - Sorteando uma ordem na lista

"""
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
"""

from random import shuffle

p1 = str(input('Primeiro aluno: '))
p2 = str(input('Segundo aluno: '))
p3 = str(input('Terceiro aluno: '))
p4 = str(input('Quarto aluno: '))
lista = [p1, p2, p3, p4]
shuffle(lista)
print(f'A ordem de apresentação será:')
print(lista)