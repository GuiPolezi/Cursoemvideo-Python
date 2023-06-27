# Desafio 51 - Progressão aritmética

"""
Desenvolva um programa que leia o PRIMEIRO TERMO e a RAZÃO
de uma PA. No final, mostre os 10 primeiros termos dessa progressão.
"""

print('=' * 30)
print('   ', '10 TERMOS DE UMA PA')
print('=' * 30)

termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
decimo = termo + (11 - 1) * razão # ATÉ O DECIMO TERMO
for c in range(termo, decimo, razão):
    print(c, end=' → ')
print('ACABOU!')