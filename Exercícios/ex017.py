# Desafio 17 - Catetos e Hipotenusas

"""
Faça um programa que leia o comprimento do cateto oposto e do
cateto adjacente de um triângulo retângulo, calcule e mostre o comprimento da
hipotenusa
"""

from math import hypot
co = float(input("Digite o comprimento do cateto oposto: "))
ca = float(input("Digite o comprimento do cateto adjacente: "))
hip = hypot(co, ca)
print('(H² = c² + c²) -> Formula de pitágoras')
print(f'A hipotenusa vai medir {hip:.2f}')
