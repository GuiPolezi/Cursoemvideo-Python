# Desafio 6 - Dobro, Triplo e Raiz quadrada

"""
Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada
"""

n = int(input('Digite um número: '))
d = n * 2
t = n * 3
r = n ** (1/2)
print(f'O dobro de {n} é {d}')
print(f'O triplo de {n} é {t}')
print(f'A raiz quadrada de {n} é {r:.2f}')