# Desafio 78 - Maior e menor valores na lista

"""
Faça um programa que leia 5 valores e guarde-os em uma lista.
No final, mostre qual foi o maior e menor valor digitado e as suas respectivas posições
na lista.
"""

lista = list()
for cont in range(0, 5):
    lista.append(int(input('Digite um valor: ')))
print(f'Você digitou os seguintes números: {lista}')
maior = max(lista)
menor = min(lista)
print(f'O maior valor digitado foi: {maior}, na posição {lista.index(maior)}')
print(f'O menor valor digitado foi: {menor}, na posição {lista.index(menor)}')