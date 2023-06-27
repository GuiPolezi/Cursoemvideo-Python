# Desafio 23 - Separando digitos de um número

"""
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
"""
num = int(input("Informe um número: "))
un = num // 1 % 10
dez = num // 10 % 10
cen = num // 100 % 10
mil = num // 1000 % 10
print(f'Unidade: {un}')
print(f'Dezena: {dez}')
print(f'Centena: {cen}')
print(f'Milhar: {mil}')