# Desafio 85 - Lista com pares e impares

"""
Crie um programa onde o usuário possa digitar sete valores numérisoc e cadastre-os em uma lista única
que mantenha separados os valores pares e ímpares. No final, motre os valores pares e ímpares em ordem
crescente.
"""

lista = [[], []]
valor = 0
for c in range(1, 8):
    valor = int(input(f'Digite o {c}o. valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print('=-' * 30)
print(f'Todos os valores {lista}')
print(f'valores impares {lista[1]}')
print(f'Valores pares {lista[0]}')
