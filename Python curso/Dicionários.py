# Curso Python 19 - Dicionários

# Mais uma estrutura de dados composta!

"""
------------------------------------------------------------------------------------------------------------------------
Dicionários são identificados por {}

É possivel declarar das seguintes formas:
dados = dict()
dados = {}
------------------------------------------------------------------------------------------------------------------------

Para colocar os dados dentro da estrutura e dizendo o índice, pode fazer assim:
dados = dict()
dados = { 'nome':'Pedro', 'idade':25 } -> Nome, idade = identificador do elemento, Pedro, 25 = valor
print(dados['nome']) = Pedro
print(dados[idade]) = 25

Para adicionar elementos no dicionario: -> append não funciona
dados['sexo'] = 'M' -> Cria o elemento Sexo e coloca o valor M

Para remover elementos:
del dados[idade] -> elimina o elemento e o valor

------------------------------------------------------------------------------------------------------------------------

Outro exemplo:
Guardar nomes de filme

filme = {'Titulo':'star wars',        -> Estrutura de dados FILME com 3 elementos: titulo, ano, diretor
        'ano':1977,
        'diretor':'George lucas'}

------------------------------------------------------------------------------------------------------------------------

No dicionário podemos acessar a qualquer momento: Itens, keys(chaves) ou os valores:
print(filme.values()) - Retorna todos os valores do dicionario = Star wars, 1977, george lucas
print(filme.keys()) - Retorna as chaves = Titulo, ano, diretor
print(filme.items()) - Retorna todos os valores = Values e keys.

------------------------------------------------------------------------------------------------------------------------

É possivel usar esses conceitos (values, keys, items) nos laços (for, while) , parecido ao enumerate:
Exemplo:
K = key, v = value
"""

filme = {'Titulo': 'star wars', 'ano': 1977, 'diretor': 'George lucas'}

for k, v in filme.items():  # Ficando desse jeito:
    print(f'O {k} é {v}')   # O titulo é star wars
                            # O ano é 1977
                            # O diretor é george lucas
"""
------------------------------------------------------------------------------------------------------------------------

É possivel criar uma lista e com append adicionar os dicionarios:
Exemplo:
Criar uma lista chamada locadora e adicionar o dicionario
Sendo possivel criar uma lista onde cada elemento tem um dicionario

------------------------------------------------------------------------------------------------------------------------
"""

# PRATICA:
print('-' * 30)  # Separando no console!

pessoas = {'Nome': 'Guilherme', 'Sexo': 'Masculino', 'Idade': 17}  # Dicionario
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} anos')  # Para referenciar elementos usa-se [] Colchetes
# Outro exemplo com print:
print('-' * 30)  # Separando no console!

print(pessoas.keys())  # Mostra = Nome, sexo, idade
print(pessoas.values())  # Mostra = Guilherme, Masculino, 17
print(pessoas.items())  # Mostra os dois como uma composição de elementos -> ([('Nome', 'Guilherme'),
# ('Sexo', 'Masculino') -> Os items são uma lista composta de 3 tuplas!!!

print('-' * 30)  # Separando no console!

# ----------------------------------------------------------------------------------------------------------------------
""" 
Acessar as keys, valores e items por laços (for, while)

for k in pessoas.keys():  # Para cada uma das chaves
    print(k)

->  Nome
    Sexo
    Idade
------------------------------------------------------------------------------------------------------------------------
for k in pessoas.values(): # para cada um dos valores
    print(k)

-> Guilherme
   Masculino
   17 

------------------------------------------------------------------------------------------------------------------------
"""
# Para utilizar o pessoas.items() -> tem q ter a chave e o valor:
pessoas['Nome'] = 'Leo'
pessoas['Peso'] = 67  # Adicionando elemento
for k, v in pessoas.items():
    print(f'{k} = {v}')

print('-' * 30)  # Separando no console!

# ----------------------------------------------------------------------------------------------------------------------

"Criando um dicionario dentro de uma lista:"
brasil = list()
estado1 = {'Cidade': 'Rio de janeiro', 'Sigla': 'RJ'}
estado2 = {'Cidade': 'São paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil)

print('-' * 30)  # Separando no console!

# ----------------------------------------------------------------------------------------------------------------------
Estado = dict()
Brasil = list()
for c in range(0, 3):  # Ler 3 estados
    Estado['Cidade'] = str(input('Cidade: '))   # Adiciona a chave CIDADE e o elemento respondido
    Estado['Sigla'] = str(input('Sigla do estado: '))  # Adiciona a key sigla e o elemento respondido
    Brasil.append(Estado.copy())
    # Com dicionario só é possivel copiar usando .copy, a copia é necessaria para fzr o fatiamento dos dados
    # Sem a copia o que vai ser printado(print(Brasil)) vai ser tudo a mesma resposta
for e in Brasil:  # for da lista
    for v in e.values():  # For do dicionario - value
        print(f'{v}', end=' ')
    print()  # Pular linha
