# Desafio 27 - Primeiro e último nome de uma pessoa

"""
Faça um programa que leia o nome completo de uma pessoa,
mostrando em seguida o primeiro e último nome separadamente

ex: Ana Maria de Souza
primeiro = Ana
último = Souza
"""

nome = str(input('Digite seu nome completo: ')).strip().split()
print(nome)
print(f'Seu primeiro nome é: {nome[0]}')
print(f'Seu último nome é: {nome[len(nome)-1]}')