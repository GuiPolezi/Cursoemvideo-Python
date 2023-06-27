# Desafio 25 - Procurando uma string dentro de outra

"""
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
"""

nome = str(input('Qual seu nome completo? '))
print(f'Seu nome possui SILVA? {"SILVA" in nome.upper().split()}')
