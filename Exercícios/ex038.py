# Desafio 38 - Comparando números

"""
Escreva um programa que leia DOIS NÚMEROS inteiros e compare-os,
mostrando na tela uma mensagem:

- o PRIMEIRO VALOR é maior
- o SEGUNDO VALOR é maior
- NAO EXISTE valor maior, os dois são iguais
"""

a = int(input('Primeiro número: '))
b = int(input('Segundo número: '))

if a > b:
    print('O primeiro valor é MAIOR!')
elif a < b:
    print('O segundo valor é MAIOR!')
else:
    print('Não existe valor maior, os dois são iguais!!!')
