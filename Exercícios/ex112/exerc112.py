# Desafio 112 - Entrada de dados monetários

"""
Dentro do pacote utilidadesCeV que criamos no desafio 111, temos o módulo dado.
Crie uma função chamada leiaDinheiro() que seja capaz de funcionar
como a função input(), mas com validação de dados para aceitar apenas valores que sejam monetários
"""

from ex112.utilidadesCeV import moeda, dado

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p, 80, 20)