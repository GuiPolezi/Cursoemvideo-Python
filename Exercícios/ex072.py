# Desafio 72 - Número por extenso

"""
Crie um programa que tenha uma TUPLA totalmente preenchida com uma contagem por extenso,
de zero até vinte.
Seu programa vai ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
"""
from time import sleep
numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze', 'treze', 'catorze', 'quinze', 'dezesseis', 'dezessete',
           'dezoito', 'dezenove', 'vinte')
cont = 0
while True:
    pergunta = int(input('\033[31mDigite um número de 0 a 20:\033[m '))
    cont += 1
    while int(pergunta) > len(numeros) - 1:
        pergunta = int(input('Tente novamente. Digite um número de 0 a 20: '))
    else:
        print(f'Você digitou o número \033[34m{numeros[pergunta]}\033[m')
        sleep(0.5)
    continuar = str(input('\033[31mVocê quer continuar?\033[m [S/N] ')).upper().strip()[0]
    print('-' * 30)
    sleep(0.5)
    if continuar in 'N':
        break
print(f'Você digitou {cont} {"números" if cont != 1 else "número"}')