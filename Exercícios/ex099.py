# Desafio 99 - Função que descobre o maior

"""
Faça um programa que tenha uma função chamada MAIOR(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o mnaior
"""
from time import sleep


def maior(* num):  # Funçao maior - recebe varios parametros ( * )
    cont = 0
    maiorv = 0  # maior valor
    print('-=' * 30)
    print('Analisando os valores passados...')
    for valor in num:  # Para valor em num
        print(valor, end=' ')
        sleep(0.3)
        if cont == 0:  # Se o contador for igual a 0
            maiorv = valor  # maior recebe valor (0)
        else:  # Se não
            if valor > maiorv:  # Se o valor for maior que o maior número (0)
                maiorv = valor  # Maior recebe valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maiorv}.')


maior(1, 2, 3)
maior(1, 4, 5, 6, 7)
maior(6)
maior()
maior(100, 101, 235)