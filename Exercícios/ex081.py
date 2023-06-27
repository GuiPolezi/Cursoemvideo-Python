# Desafio 81 - Extraindo dados de uma lista

"""
Crie um programa que vai ler vários números e colocar em uma lista
Depois disso, mostre:

- Quanto números foram digitados.
- A lista de valores ordenada de forma decrescente.
- Se o valor 5 foi digitado e está na lista.
"""

valores = list()
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('Resposta invalida! Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar not in 'S':
        break

print('=' * 30)
print(f'\033[34mVocê digitou {len(valores)} elementos.\033[m')
print('\033[31mLista em ordem decrescente:\033[m')
valores.sort(reverse=True)
print(valores)
if 5 not in valores:
    print('O número 5 não está na lista!')
else:
    print('O valor 5 faz parte da lista!')