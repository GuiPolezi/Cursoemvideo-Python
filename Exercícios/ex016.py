# Desafio 16 - Quebrando um número

"""
Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela
a sua porção inteira.

exemplo:
Digite um número: 6.127
o número 6.127 tem a parte inteira 6.
"""

from math import trunc

n = float(input("Digite um número: "))
pi = trunc(n)
print(f'O valor digitado foi {n} e sua porção inteira é {pi} ')