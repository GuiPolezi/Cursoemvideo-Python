# Desafio 107 - Exercitando módulos em Python

"""
Crie um módulo chamado moeda.py que tenha as funções incorporadas
aumentar(), diminuir(), dobro() e metade()

Faça também um programa que importe esse móludo e use alguma dessas
funções
"""

from ex107 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando o preço em 10%, temos {moeda.aumentar(p, 10)}')
print(f'Reduzindo o preço em 13%, temos {moeda.diminuir(p, 13)}')
