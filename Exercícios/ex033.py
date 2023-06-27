# Desafio 33 - Maior e menor valores

"""
Faça um programa que leia três números e mostre qual é O MAIOR
e qual é o MENOR
"""

p1 = float(input('Primeiro valor: '))
p2 = float(input('Segundo valor: '))
p3 = float(input('Terceiro valor: '))
menor = p1
maior = p3
# VERIFICANDO O MENOR
if p2 < p1 and p2 < p3:
    menor = p2
if p3 < p1 and p3 < p2:
    menor = p3
# VERIFICANDO O MAIOR
if p2 > p1 and p2 > p3:
    maior = p2
if p1 > p2 and p1 > p3:
    maior = p1
print(f'O maior valor digitado foi: {maior}')
print(f'O menor valor digitado foi: {menor}')
