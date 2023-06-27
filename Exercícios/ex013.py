# Desafio 13 - Reajuste Salarial

"""
Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
"""

salario = float(input("Qual é o salário do funcionário? R$"))
porcentagem = salario * 15 / 100
aumento = salario + (salario * 15/100)
print(f'O salario que antes era de R${salario}, com 15% de aumento passou a ser R${aumento:.2f}')
print(f'O aumento foi de R${porcentagem:.2f}')
