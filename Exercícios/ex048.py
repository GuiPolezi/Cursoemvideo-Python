# Desafio 48 - Soma ímpares múltiplos de três

"""
Faça um programa que calcule os números ímpares que
são múltiplos de três e que se encontram no intervalo de 1 até 500
"""

cont = 0
soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma += c
        cont += 1
print(f'A soma de todos os {cont} valores solicitados é {soma}')