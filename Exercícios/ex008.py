# Desafio 8 - Conversor de medidas
"""
Escreva um progranma que leia um valor em metros e o exiba convertido em centimetros e milimetros
"""

metros = int(input('Uma distância em metros: '))
centimetros = metros * 100
milimetros = metros * 1000
print(f'{metros}m para centímetros é {centimetros}cm')
print(f'{metros}m para milímetros é {milimetros}mm')