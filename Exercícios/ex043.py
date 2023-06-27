# Desafio 43 - Índice de massa corporal (IMC)

"""
Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu IMC
e mostre seu status, de acordo com a tabela abaixo:

- abaixo de 18.5: abaixo do peso
- entre 18.5 e 25: peso ideal
- 25 ate 30: sobrepeso
- 30 até 40: obesidade
- acima de 40: obesidade morbida
"""

peso = float(input('Digite seu peso: (KG) '))
altura = float(input('Digite sua altura: (M) '))
imc = peso / (altura ** 2)
# Informações sobre você
print('Suas informações:')
print(f'{peso}KG')
print(f'{altura:.2f}m de altura')
if imc <= 18.5:
    print(f'Seu IMC é {imc:.1f}: ABAIXO DO PESO!')
elif imc <= 25:
    print(f'Seu IMC é {imc:.1f}: PESO IDEAL!')
elif imc <= 30:
    print(f'Seu IMC é {imc:.1f}: SOBREPESO!')
elif imc <= 40:
    print(f'Seu IMC é {imc:.1f}: OBESIDADE!')
else:
    print(f'Seu IMC é {imc:.1f}: OBESIDADE MORBIDA!!')