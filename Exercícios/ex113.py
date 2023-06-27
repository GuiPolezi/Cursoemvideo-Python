# Desafio 113 - Funções aprofundadas em python

"""
Reescreva a funçao leitaInt() que fizemos no desafio 104, incluindo agora a possibilidade
da digitação de um número de tipo inválido. Aproveite e crie também uma função leitaFloat() com a mesma funcionalidade
"""


def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except KeyboardInterrupt:
            print('')
            print('\033[34mUsuário preferiu não digitar esse número\033[m')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número inteiro válido!\033[m')
            continue
        else:
            return inteiro


def leiaFloat(n):
    while True:
        try:
            real = float(input(n))
        except KeyboardInterrupt:
            print('\033[34m\nUsuário preferiu não digitar esse número\033[m')
            return 0
        except (TypeError, ValueError):
            print('\033[32mERRO: por favor digite um número real válido!\033[m')
            continue
        else:
            return real


ninteiro = leiaInt('Digite um Inteiro: ')
nreal = leiaFloat('Digite um Real: ')
print(f'O valor inteiro digitado foi {ninteiro} e o real foi {nreal:.2f}')