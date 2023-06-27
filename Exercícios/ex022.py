# Desafio 22 - Analisador de texto

"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo ( sem considerar espaços)
- Quantas letras tem o primeiro nome.
"""
from time import sleep

nome = str(input("Digite seu nome completo: "))
sleep(1)
print('Analisando seu nome...')
print(f'Seu nome em maiúsculas é: {nome.upper()}')
print(f'Seu nome em minúsculas é: {nome.lower()}')
print(f'Seu nome ao todo tem {len(nome)} letras')
print(f'Seu primeiro nome tem {nome.find(" ")} letras')