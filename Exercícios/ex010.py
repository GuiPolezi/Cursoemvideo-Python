# Desafio 10 - Conversor de moedas

"""
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dolares ela pode comprar.
"""

carteira = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = carteira / 5.11
print(f'Com R${carteira} você consegue comprar US${dolar:.2f}')