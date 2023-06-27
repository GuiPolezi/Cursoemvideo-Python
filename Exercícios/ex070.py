# Desafio 70 - Estatísticas em produtos

"""
Crie um programa que leia o nome e o preço de varios produtos.
O programa deverá perguntar se o usuário vai continuar.
no final, mostre:

- Qual o total gasto na compra.
- Quantos produtos custam MAIS de R$1000
- Qual é o nome do produto mais barato
"""

print('-' * 30)
print(f'\033[31m{"Loja do crime":^30}\033[m')
print('-' * 30)

totmil = soma = menor = cont = 0
nomemenor = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    cont += 1
    soma += preço
    if preço >= 1000:
        totmil += 1
    if cont == 1:
        menor = preço
        nomemenor = nome
    else:
        if preço < menor:
            menor = preço
            nomemenor = nome
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break

print('-' * 30)
print(f'Total gasto na compra: \033[31mR${soma:.2f}\033[m')
print(f'\033[31m{totmil}\033[m Produto[s] custa[m] mais de R$1000')
print(f'Nome do menor valor: \033[31m{nomemenor}\033[3m, \033[31mR${menor:.2f}\033[m')