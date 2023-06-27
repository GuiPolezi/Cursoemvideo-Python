# Desafio 71 - Simulador de caixa eletrônico

"""
Crie um programa que simule o funcionamento de um caixa eletrônico. No inicio, pergunte ao usuario
qual sera o valor a ser sacado (numero inteiro) e o programa vai informar quantas cédulas de cada
valor serão entregues

obs: Considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1
"""

from time import sleep
print('\033[31m=' * 30)
print(f'{"BANCO":^30}')
print('=' * 30, '\033[m')
valor = int(input('Qual valor você quer sacar? R$'))
sleep(0.5)
print('\033[34mSacando...\033[m')
sleep(1)
total = valor
céd = 100
totcéd = 0
while True:
    if total >= céd:
        total -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} de {"cédula" if totcéd == 1 else "cédulas"} de R${céd}')
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 5
        elif céd == 5:
            céd = 1
        totcéd = 0
        if total == 0:
            break
print('=' * 30)
print('\033[34mValor sacado!\033[m')