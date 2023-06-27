# Desafio 100 - Funções para sortear e somar

"""
Faça um programa que tenha uma LISTA chamada NÚMEROS e duas FUNÇÕES chamadas
SORTEIA() e SOMAPAR().
A primeira função vai sortear 5 números e vai coloca-los dentro da lista
A segunda função vai mostrar a SOMA entre todos os valores PARES sorteados da função anterior
"""
from random import randint


def sorteia(lista):  # Função sorteia recebendo parametro lista
    print('Sorteando 5 valores da lista: ', end='')
    for cont in range(0, 5):  # Para contagem em range de 0 a 5
        n = randint(1, 10)  # numero recebe randint(gerador de números aleatorios de 1 a 10)
        lista.append(n)  # Lista (parametro) adiciona número (5 números gerados )
        print(f'{n} ', end='')  # print numeros
    print('SORTEADO!')


def somapar(lista):  # função somapar recebe parametro lista
    soma = 0  # soma recebe 0
    for valor in lista:  # para valor no parametro lista
        if valor % 2 == 0:  # se valor dividido por 2 igual a 0
            soma += valor  # soma recebe soma(0) + valor(números gerados dentro da lista)
    print(f'Somando os valores pares de {lista} temos {soma}')


numeros = list()   # numeros é a lista
sorteia(numeros)  # sorteia recebe numeros(lista) que vai no lugar do parametro lista
somapar(numeros)  # somapar recebe a lista(numeros) que vai no lugar do parametro lista