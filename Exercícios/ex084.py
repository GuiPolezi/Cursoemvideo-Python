# Desafio 84 - Lista composta e análise de dados

"""
Faça um programa que leia o nome e peso de várias pessoas, guardando tudo em uma lista.
No final, mostre:

- Quantas pessoas foram cadastradas.
- Uma listagem com as pessoas mais pesadas.
- Uma listagem com as pessoas mais leves.
"""

pessoas = list()
dado = list()  # Estrutura auxiliar
cont = 0
menor = maior = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Peso: KG ')))
    if len(pessoas) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    pessoas.append(dado[:])
    print('=' * 30)
    continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    print('=' * 30)
    while continuar not in 'SN':
        continuar = str(input('Resposta invalida! Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
    dado.clear()
print(f'Os dados foram: {pessoas}')
print(f'Ao todo, você cadastrou {len(pessoas)} {"pessoa" if cont == 1 else "pessoas"}')
print(f'O maior peso foi: {maior}KG. Peso de ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'O menor peso foi: {menor}KG. Peso de: ', end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
print()