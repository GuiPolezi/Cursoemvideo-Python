# Desafio 49 - Tabuada v2.0

"""
Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher,
só que agora utilizando um laço for.
"""

n = int(input('Digite o valor para ver sua tabuada: '))
for c in range(1, 11):
    print(f'{n} x {c:2} = {n * c}')

