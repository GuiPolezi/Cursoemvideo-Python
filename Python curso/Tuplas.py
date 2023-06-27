# Curso python 16 - VARIAVEIS COMPOSTAS

# TUPLAS

"""
AS TUPLAS SÃO IMUTAVEIS
TUPLA É ENTRE PARENTESES
"""

lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(len(lanche))

# PARA VER A POSIÇÃO PODE SE USAR ESSE METODO
for cont in range(len(lanche)):
    print(f'Eu vou comer {lanche[cont]}, na posição {cont}')

print('-' * 30)
# Metodo padrao
for c in lanche:
    print(f'eu vou comer {c}')
print('To cheio!')

print('-' * 30)

# outro metodo
for pos, comida in enumerate(lanche):
    print(f'Eu vou comer {comida} na posição {pos}')

print('-' * 30)

"""
É possível utilizar uma Tupla com mais de uma Saída de dado.
Como por exemplo: 
"""

pessoa: tuple[int, str, int, int] = (2, 'Polezi', 0, 3)
print(pessoa)

print('-' * 30)

a = (2, 5, 4)
b = (5, 9, 1, 3)
c = b + a   # QUANDO USA + EM TUPLA ELA JUNTA
print(len(c))  # COMPRIMENTO
print(c)
print(c.count(5))  # QUANTAS VEZES APARECE O NUMERO - 5
print(c.index(9))  # EM QUE POSIÇÃO ESTA O NUMERO - 9

print('-' * 30)

# OUTRO EXEMPLO

pessoa2 = ('Guilherme', 17, 'Masculino', 64)
# del(pessoa2)  # APAGA A VARIAVEL/TUPLA
print(pessoa2)