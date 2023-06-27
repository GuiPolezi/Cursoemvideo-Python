# Desafio 24 - Verificando a primeira letra de um texto

"""
Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome santo
"""

cidade = str(input('Digite o nome da sua cidade: ')).strip()
print(f'{cidade[5] == "SANTO".upper()}')