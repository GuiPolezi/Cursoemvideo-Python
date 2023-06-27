# Desafio 111 - Transformando módulos em Pacotes

"""
Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados
dados e moeda.

Transfira todos as funções utilizadas nos desafios 107, 108, 109 e 110
para o primeiro pacote e mantenha tudo funcionando
"""

from ex111.utilidadesCeV import moeda

p = float(input('Digite o preço: R$'))
moeda.resumo(p, 80, 20)