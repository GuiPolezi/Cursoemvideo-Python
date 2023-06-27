# Desafio 98 - Função de Contador

"""
Faça um programa que tenha uma função chamada CONTADOR(), que receba 3 parametros:
INICIO, FIM e PASSO e realize a contagem

Seu programa tem que realizar três contagens através da função criada:
- De 1 até 10, de 1 em 1
- de 10 até 0, de 2 em 2
- Uma contagem personalizada
"""
from time import sleep


def contador(a, b, c):
    if c < 0:  # Se o passo for negativo
        c *= -1  # transforma em positivo

    if c == 0:  # Se o passo for 0
        c = 1  # passo se transforma em 1
    print('-=' * 20)
    print(f'Contagem de {a} até {b} de {c} em {c}')
    sleep(1)
    if a < b:  # Se o inicio for menor que o fim
        cont = a  # Contador recebe a -> inicio
        while cont <= b:  # Enquanto contador for menor que o fim
            print(f'{cont}', end=' -> ')
            sleep(0.2)
            cont += c  # Contador recebe + c (Passo), assim aumentando conforme o passo escolhido e não printando 1 infinitamente
        print('Fim')
    else:
        cont = a
        while cont >= b:  # Enquanto cont for maior que o fim
            print(f'{cont}', end=' -> ')
            sleep(0.2)
            cont -= c  # Contador recebe - c ( passo), assim sendo regressivo
        print('Fim')


# Programa principal
contador(1, 10, 1)  # Contando 1 até 10, de 1 em 1
contador(10, 0, 2)  # Contagem regressiva de 10 até 0, pulando de 2 em 2
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
inicio = int(input('Inicio: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)