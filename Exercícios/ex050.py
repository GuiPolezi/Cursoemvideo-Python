# Desafio 50 - Soma dos pares

"""
Desenvolva um programa que leia SEIS NUMEROS INTEIROS
e mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o
"""

cont = 0
contpar = 0
s = 0
for c in range(0, 6):
    n = int(input('Digite um valor: '))
    cont += 1
    if n % 2 == 0:
        s += n
        contpar += 1
print('Apenas números pares foram considerados!')
print(f'Você digitou {cont} números')
print(f'E apenas {contpar} desses números são pares.')
print(f'A soma dos valores é {s}')