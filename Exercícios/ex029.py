# Desafio 29 - Radar eletrônico

"""
Escreva um programa que leia a velocidade de um carro.

Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
a multa vai CUSTAR R$7,00 por cada Km acima do limite.
"""

vel = int(input('Qual a velocidade do carro? '))
if vel > 80:
    print(f'Você ultrapassou o limite de 80Km/h, sua velôcidade é de: {vel}Km/h')
    multa = (vel - 80) * 7
    print(f'MULTADO!!! você terá q pagar uma multa de: R${multa}')
else:
    print('Você está na velocidade permitida!!')
    print(f'{vel}Km/h')