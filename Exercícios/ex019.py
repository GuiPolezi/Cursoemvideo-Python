# Desafio 19 - Sorteando item na lista

"""
Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido
"""

import random

p1 = str(input('Primeiro aluno: '))
p2 = str(input('Segundo aluno: '))
p3 = str(input('Terceiro aluno: '))
p4 = str(input('Quarto aluno: '))
lista = [p1, p2, p3 ,p4]
escolhido = random.choice(lista)
print(f'O aluno escolhido para apagar a lousa foi: {escolhido}')