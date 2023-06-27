# Desafio 36 - Aprovando emprestimo

"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
O programa vai perguntar o VALOR DA CASA, o SALÁRIO do comprador e em QUANTOS ANOS ele vai pagar.

Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
ou então o empréstimo sera negado.
"""

valorcasa = float(input('Valor da casa: R$'))
salariocomprador = float(input('Salário Comprador: R$'))
anosfin = int(input('Quantos anos de financiamento? '))
prestmensal = valorcasa / (anosfin * 12)
print(f'Para pagar uma casa de R${valorcasa:.2f}, em {anosfin} anos.')
print(f'A prestação sera de R${prestmensal:.2f}')
if prestmensal >= salariocomprador * 30 / 100:
    print('Empréstimo negado!')
else:
    print('Empréstimo concedido!')