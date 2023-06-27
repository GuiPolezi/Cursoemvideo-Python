# Desafio 104 - Validando entrada de dados em Python

"""
Crie um programa que tenha a função leiaint(), que vai funcionar de forma semelhante à função ja existente
input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
exemplo:
n = leiaint('Digite um n')
"""


def leiaint(msg):  # Função leiainteiro - parametro vai ser uma mensagem
    ok = False  # Ok recebe falso
    valor = 0  # valor recebe 0
    while True:  # Loop infinito, enquanto verdadeiro
        n = str(input(msg))  # n recebe input de string do parametro -> mensagem
        if n.isnumeric():  # se n é numero
            valor = int(n)  # valor recebe n transformado em inteiro
            ok = True  # ok vai ser verdadeiro
        else: # se não mensagem de erro
            print(f'\033[31mERRO! Digite um número inteiro valido!\033[m')
        if ok:  # se OK estiver como verdadeiro break
            break
    return valor  # retorna o valor = n


# Programa principal
print('-' * 30)
n = leiaint('Digite um número: ')   # escopo global - n, retornou o valor -> valor armazenado no N
print(f'Você acabou de digitar o número {n}')
