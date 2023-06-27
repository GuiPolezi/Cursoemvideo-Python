# Desafio 18 - Seno, Cosseno e Tangente

"""
Faça um programa que leia um ângulo qualquer e mostre na tela:
seu Seno, Cosseno e Tangente desse ângulo
"""

import math

ang = math.radians(int(input('Digite o ângulo: ')))
sen = math.sin(ang)
cos = math.cos(ang)
tan = math.tan(ang)
print(f'O angulo é de {ang}º')
print(f'O seno é {sen:.2f}')
print(f'O cosseno é {cos:.2f}')
print(f'A tangente é {tan:.2f}')