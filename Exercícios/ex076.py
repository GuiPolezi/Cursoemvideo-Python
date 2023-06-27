# Desafio 76 - Lista de preços com tupla

"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência
No final, mostre uma listagem de preços organizando os dados em forma tabular.
"""

lista = ('Pão', 1,
         'Maionese', 2.50,
         'Leite', 3,
         'Frango', 10.50,
         'Arroz', 20.99)
print('\033[31m-=' * 30)
print(f'{"LISTAGEM DE PREÇOS":^60}')
print('-=' * 30, '\033[m')

for c in lista:
    if type(c) is str:
        print(f'{c:.<32}', end=' ')
    else:
        print(f'R${c:.2f}')
print('-' * 40)