# Desafio 37 - Conversor de bases númericas

"""
Escreva um programa que leia um número inteiro qualquer
e peça para o usuário escolher qual será a BASE DE CONVERSÃO

- 1 para BINÁRIO
- 2 para OCTAL
- 3 para HEXADECIMAL
"""
from time import sleep

n = int(input('Digite um número: '))
print('Escolha para qual opção você quer converter:')
print('Digite 1 para BÍNARIO')
print('Digite 2 para OCTAL')
print('Digite 3 para HEXADECIMAL')
escolha = int(input('Faça sua escolha: '))
if escolha == 1:
    binario = bin(n).replace("0b", "")
    print(f'Convertendo {n} para BINÁRIO')
    print('...')
    sleep(1)
    print(f'O resultado é: {binario}')
elif escolha == 2:
    octal = oct(n).replace("0o", "")
    print(f'Convertendo {n} para OCTAL')
    print('...')
    sleep(1)
    print(f'O resultado é: {octal}')
elif escolha == 3:
    hexa = hex(n).replace("0x", "")
    print(f'Convertendo {n} para HEXADECIMAL')
    print('...')
    sleep(1)
    print(f'O resultado é: {hexa}')
else:
    print('Opção não encontrada!')
