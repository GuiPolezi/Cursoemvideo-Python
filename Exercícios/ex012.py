# Desafio 12 - Calculando desconto

"""
 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
"""
produto = float(input('Qual é o preço do produto? R$'))
desconto = produto * 5 / 100
total = produto - desconto
print(f'O produto que custava R${produto}, passou a custar R${total:.2f}')
print(f'Seu desconto foi de R${desconto}, 5% de {produto}')