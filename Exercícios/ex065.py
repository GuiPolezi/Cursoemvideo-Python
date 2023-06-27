# Desafio 65 - Maior e Menor valores

"""
Crie um programa que leia varios números inteiros pelo teclado
no final da execução mostre a média entre todos os valores e qual foi o maior e o menor
valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
"""
from time import sleep

cont = 0
soma = 0
maior = 0
menor = 0

print('\033[31mLENDO NÚMEROS\033[m')
print('=-' * 20)
while True:
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    media = soma / cont
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    pergunta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if pergunta == 'N':
        print("Encerrando o programa...")
        break
    elif pergunta.isalpha():
        print('\033[32mContinuando...\033[m')
    else:
        print('\033[34mResposta inválida.\033[m')
        break
sleep(2)
print('-' * 30)
print(f'\033[32m{cont}\033[m Número[s] lido[s]')
print(f'A soma é = \033[32m{soma}\033[m')
print(f'Média do[s] número[s] = \033[32m{media:.2f}\033[m')
print(f'O maior valor é \033[32m{maior}\033[m')
print(f'O menor valor é \033[32m{menor}\033[m')