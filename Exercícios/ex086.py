# Desafio 86 - Matriz em python

"""
Crie um programa que crie uma matriz de dimensão 3x3 e preencha com valores lido pelo teclado
No final, mostre a matriz na tela, com a formatação correta
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range(0, 3):  # LINHA
    for c in range(0, 3):  # COLUNA
        matriz[linha][c] = int(input(f'Digite um valor para [{linha}, {c}]: '))
print('-=' * 30)
for linha in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[linha][c]:^5}]', end='')
    print()
