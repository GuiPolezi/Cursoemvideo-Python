# Desafio 57 - Validação de dados

"""
Faça um programa que leia o sexo de uma pessoa.
Mas so aceite os valores 'M' ou 'F'
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""

sexo = str(input('Informe seu sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalídos, Digite seu sexo: ')).strip().upper()[0]
print(f'Sexo {sexo} registrado com sucesso!')
