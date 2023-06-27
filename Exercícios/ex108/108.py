# Desafio 108 - Formatando Moedas em Python
"""
Adapte o código do Desafio 107, criando uma função adicional chamada moeda()
que consiga mostrar os valores como um valor monetário formatado
"""

from ex108 import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {p} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando o preço em 10%, temos {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'Reduzindo o preço em 13%, temos {moeda.moeda(moeda.diminuir(p, 13))}')
