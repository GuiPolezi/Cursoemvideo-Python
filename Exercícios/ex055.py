# Desafio 55 - Maior e Menor da sequência

"""
Faça um programa que leia o peso de CINCO PESSOAS.
No final, mostre qual foi o maior e o menor peso lido
"""

maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso da {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'O maior peso é {maior}KG')
print(f'O menor peso é {menor}KG')