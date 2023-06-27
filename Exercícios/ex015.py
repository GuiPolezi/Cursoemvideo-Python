# Desafio 15 - Aluguel de Carros

"""
Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que
o carro CUSTA R$ 60 por dia e R$ 0.15 por Km rodado.
"""

Qdia = int(input('Quantos dias alugado? '))
Qkm = float(input('Quantos km foram percorridos? '))
total = Qdia * 60 + (Qkm * 0.15)

print(f'O carro foi alugado por {Qdia} dias, e rodou por {Qkm} Km')
print(f'O total a pagar é de R${total:.2f}')

