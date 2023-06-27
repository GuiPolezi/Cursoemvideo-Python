# Desafio 31 - Custo da viagem

"""
Desenvolva um programa que pergunte a distância de uma viagem em KM.
Calcule o preço da passagem, cobrando R$0,50 por KM para viagens de ATÉ 200 Km
E R$0,45 para viagens mais longas.
"""

viagem = int(input('Qual a distância da sua viagem? -> '))
if viagem <= 200:
    passagem = viagem * 0.50
    print(f'Você está prestes a começar uma viagem de {viagem}Km.')
    print(f'E o preço da sua passagem será de R${passagem:.2f}')
else:
    passagem = viagem * 0.45
    print(f'Você está prestes a começar uma viagem de {viagem}Km.')
    print(f'E o preço da sua passagem será de R${passagem:.2f}')


# Outra forma de fazer o codigo:

# passagem = viagem * 0.50 if viagem <= 200 else viagem * 0.45