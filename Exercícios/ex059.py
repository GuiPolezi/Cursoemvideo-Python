# Desafio 59 - Criando um menu de opçôes

"""
Crie um programa que leia 2 valores
e mostre um menu na tela:

1 - Somar
2 - Multiplicar
3 - Maior
4 - Novos números
5 - sair do programa

seu programa devera realizar a operação solicitada em cada caso.
"""
from time import sleep


a = float(input('Primeiro valor: '))
b = float(input('Segundo valor: '))
option = 0
print('\033[34mMENU:')
while option != 5:
    print('-' * 20)
    print('\033[mEscolha uma opção')
    print(' [1] - Somar')
    print(' [2] - Multiplicar')
    print(' [3] - Maior')
    print(' [4] - Novos números')
    print(' [5] - Sair do programa')
    option = int(input('Escolha uma opção:  '))
    if option == 1:
        soma = a + b
        print('\033[32mSOMA:\033[0m')
        print(f'{a} + {b} = {soma}')
        sleep(2)
    elif option == 2:
        multiplicar = a * b
        print('\033[32mMULTIPLICAÇÃO:\033[0m')
        print(f'{a} X {b} = {multiplicar}')
        sleep(2)
    elif option == 3:
        print('\033[32mMAIOR:\033[0m')
        if a > b:
            print(f'Entre {a} e {b} o maior é \033[31m{a}\033[0m')
        elif a < b:
            print(f'Entre {a} e {b} o maior é \033[31m{b}\033[0m')
        else:
            print(f'Os dois números são iguais, \033[31m{a} = {b}\033[0m')
        sleep(2)
    elif option == 4:
        print('\033[32mNOVOS NÚMEROS:\033[0m')
        print('Escolha novos números.')
        sleep(2)
        a = float(input('Primeiro valor: '))
        b = float(input('Segundo valor: '))
    elif option > 5:
        print('\033[31mNumero inválido!\033[0m')
        sleep(2)
print('\033[31mPrograma encerrado.\033[0m')
