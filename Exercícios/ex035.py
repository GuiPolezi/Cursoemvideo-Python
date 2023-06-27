# Desafio 35 - Analisando Triângulo v1.0

"""
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuario se elas podem ou não formar um triângulo
"""
print('=-' * 30)
print('Analisador de Triângulos')
print('=-' * 30)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))
if a < b + c and b < a + c and c < a + b:
    resposta = 'Podem'
else:
    resposta = 'Não podem'

print(f'os segmentos {a}, {b}, {c}. {resposta} formar um triângulo')