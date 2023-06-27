# Desafio 34 - Aumentos múltiplos

"""
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento
Para salários superiores a R$1.250.00, calcule um aumento de 10%
Para os inferiores ou iguais, o aumento é de 15%
"""

salario = float(input('Qual é o salário do funcionário? R$'))
dez = salario * 10 / 100
quize = salario * 15 / 100
if salario <= 1250.00:
    print(f'Quem ganhava R${salario} Passa a ganhar R${salario + quize} agora.')
    print('Aumento de 15%')
else:
    print(f'Quem ganhava R${salario} passa a ganhar R${salario + dez} agora.')
    print('Aumento de 10%')
