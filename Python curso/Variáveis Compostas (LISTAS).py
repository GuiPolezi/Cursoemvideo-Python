# Curso Python 17
"""
As listas são variáveis compostas
que permitem armazenar vários valores em uma mesma estrutura, acessíveis por chaves individuais.
"""

# lISTA [
"""
Utiliza-se colchetes
"""

# Modificando lista
"""
Listas podem ser modificadas, diferente das tuplas que são imutaveis.
Para adicionar elementos novos na lista USA O METODO APPEND() no final da lista

Para adicionar elemento em outras posições, entre os elementos, depois ou antes. - 
Usamos o insert()

EXEMPLOS:
lanche.append('Coockie')
lanche.insert(0,'Cachorro-quente')
"""

# Apagar elementos
"""
Comando mais basico -> del lanche[3] -> PELO INDICE
ou lanche.pop(3) -> se for utilizado isoladamente ele elimina o último elemento
lanche.remove(valor) -> lanche.remove('Pizza') -> elimina o elemento e reposiciona os indices

Para saber se um elemento está na lista e você quer remove-lo
usa o metodo if e in: exemplo

if 'pizza' in lanche:
    lanche.remove('pizza)

"""

# Listas criadas por ranges
"""
valores = list(range(4, 11)) -> vai criar uma lista chamada valores contando de 4 a 10.
"""

# Funções da lista
"""
Organizar a lista em ordem decrescente ou crescente:
    ordem crescente:
    valores.sort() -> organiza os números na lista valores

    ordem decrescente ou reversa:
    valores.sort(reverse=True) -> organiza os números do maior para menor

Saber o tamanho da lista -> len(valores)> mostra os elementos
"""

# Modificando a lista
"""
lanche = ['Hamburguer', 'pizza', 'refri', 'púdim']
lanche[3] = 'picolé'
lanche.append('Suco de laranja')
lanche.insert(1, 'Pastel')
print(lanche)
print(f'essa lista tem {len(lanche)} elementos')
"""

"""
valores = list()
for cont in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'na posição {c} encontrei o valor {v}')
print('Cheguei ao final da lista')
"""
# Aprendendo
valores = list()  # LISTA VAZIA -> valores = [] TAMBÉM FUNCIONA
for cont in range(0, 5): # LER UM VALOR E ADICIONAR NA LISTA
    valores.append(int(input('Digite um valor: ')))
for c, v in enumerate(valores):
    print(f'Na posição {c} temos o número {v}!')
print(f'Na lista temos {len(valores)} elementos')
print('Chegamos ao fim da lista')

# Copia de lista
a = [2, 3, 4, 5, 7]
b = a[:]  # -> Se não fizer isso a lista vai se conectar com a outra e então o que fizer em uma muda na outra.
b[2] = 8
print(f'A lista A: {a}')
print(f'A lista b: {b}')
