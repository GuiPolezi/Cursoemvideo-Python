# Desafio 14 - Conversor de Temperatura

"""
Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.
"""

tempC = float(input('Informe a temperatura em ºC: '))
tempF = tempC * 1.8 + 32
# tempF2 = (tempC * 9/5) + 32 => outra formúla de fazer a conversão
print(f'A temperatura de {tempC}ºC corresponde a {tempF}ºF!')