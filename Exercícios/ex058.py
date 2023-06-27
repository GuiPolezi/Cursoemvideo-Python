# Desafio 58 - Jogo da adivinhação

"""
Melhore o jogo do DESAFIO 028, onde o computador vai "pensar" em um número
entre 0 a 10. Só que agora o jogador vai tentar adivinhar ate ele acertar,
mostrando no final quantos palpites foram necessários para vencer.
"""

from random import randint

print('=' * 30)
print('\033[31mJOGO DA ADIVINHAÇÃO')
print('\033[m=' * 30)

print('Computador: Vou pensar em um número entre 0 e 10, tente acertar!')
c = 0
pc = randint(0, 10)
acertou = False
while not acertou:
    jogador = int(input('Digite um número: '))
    c += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente mais uma vez')
        else:
            print('Menos... Tente mais uma vez')
print('\033[33mConseguiu!')
print(f'Você acertou com {c} tentativa[s]')