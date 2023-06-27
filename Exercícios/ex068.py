# Desafio 68 - Jogo do Par ou ìmpar

"""
Faça um programa que jogue PAR OU IMPAR com o computador.
O jogo só será interrompido quando o JOGADOR PERDER,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo
"""

from random import randint
from time import sleep

print('-=' * 20)
print('\033[34mPAR OU ÍMPAR\033[m')
print('-=' * 20)
soma = 0
c = 0

while True:
    computador = randint(0, 10)
    jogador = int(input('Diga um valor: '))
    escolha = str(input('Par ou ímpar? [P/I] -> ')).upper().strip()[0]
    print('-' * 30)
    sleep(1)
    soma = jogador + computador
    if escolha not in "PpIi":
        sleep(1)
        print('-' * 20)
        print('\033[31mDados invalidos')
        print('Reinicie o programa!\033[m')
        print('-' * 20)
        break
    if soma % 2 == 0:
        print(f'Você jogou \033[35m{jogador}\033[m e o computador \033[35m{computador}\033[m, '
              f'total de \033[35m{soma}\033[m DEU PAR')
        print('-' * 30)
        sleep(1)
        if escolha in 'Pp':
            c += 1
            print('\033[32mVocê venceu!')
            print('Vamos jogar novamente...\033[m')
            print('=-' * 30)
            sleep(1)
        if escolha in 'Ii':
            print('\033[31mVocê perdeu!\033[m')
            print('=' * 30)
            break
    if soma % 2 == 1:
        print(f'Você jogou \033[35m{jogador}\033[m e o computador \033[35m{computador}\033[m, '
              f'total de \033[35m{soma}\033[m DEU ÍMPAR')
        print('-' * 30)
        sleep(1)
        if escolha in 'Ii':
            print('\033[32mVocê vênceu!')
            print('Vamos jogar novamente...\033[m')
            print('=-' * 30)
            sleep(1)
            c += 1
        if escolha in 'Pp':
            print('\033[31mVocê perdeu!\033[m')
            print('=' * 30)
            break
sleep(1)
print('Fim do PAR OU ÍMPAR!')
print(f'Você ganhou {c} {"vez" if c == 1 else "vezes"}')