# Desafio 97 - Um print especial

"""
Faça um programa que tenha uma função chamada ESCREVA(),
que receba um texto qualquer como PARÂMETRO e mostre uma mensagem com tamanho adaptavel.

EXEMPLO:
escreva('Olá, mundo!')

Saída:
~~~~~~~~~~
Olá,Mundo!
~~~~~~~~~~
"""


def escreva(txt):  # Função escreva, recebe um parametro que vai ser um texto/mensagem
    text = len(txt) + 4  # variavel text(texto) recebe len(comprimento) de txt(parametro), + 4 para centralizar a msg
    print('~' * text)  # printa '~' vezes o comprimento de txt(parametro)
    print(f'{txt:^{text}}')  # Printa o parametro -> depois passa um argumento, centraliza a mensagem
    print('~' * text)


# Programa principal
escreva('Python')   # Argumento - Informação passada para a função, no lugar do parametro
escreva('Desafio 97')
escreva('Olá, Mundo!')
escreva('Escrevendo uma enorme frase para testar se a função está funcionando')