# Desafio 96 - Função que calcula área

"""
Faça um programa que tenha uma função chamada ÁREA(), que receba as dimensões de um terreno
retangular (largura e comprimento) e mostre a ÁREA DO TERRENO
"""


def área(a, b):   # Defini a função com o nome área, passando dois parametros -> a, b (largura e comprimento)
    vezes = a * b
    print(f'A área de um terreno {a}x{b} é de {vezes}m²')


# Programa principal
print()  # Print vazio para a string controle de terrenos ser mostrada mais abaixo no console
print(f'{"Controle de terrenos":^30}')
print('-' * 30)

largura = float(input('Largura (m): '))
comprimento = float(input('Comprimento (m): '))
área(largura, comprimento)  # Muda os parametros a, b para largura, comprimento