# Desafio 109 - Formatando Moedas em Python pt 2
"""
Modifique as funções que foram criadas no desafio 107 para que elas aceitem um parâmetro a mais,
informando se o valor retornado que elas vai ser ou não formatado pela função moeda().
Desenvolvida no exercício 108
"""

import moeda

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {p} é {moeda.dobro(p, True)}')
print(f'Aumentando o preço em 10%, temos {moeda.aumentar(p, 10, True)}')
print(f'Reduzindo o preço em 13%, temos {moeda.diminuir(p, 13, True)}')
