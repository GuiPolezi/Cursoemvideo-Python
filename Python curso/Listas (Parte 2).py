# Curso python 17 - parte 2

"""
dados = list()
dados.append('Pedro')  # Será adicionado no índice 0 da lista
dados.append(25)  # será adicionado no índice 1 da lista
print(dados[0])  # vai mostrar o índice 0 -> 'Pedro'
print(dados[1])  # mostra o índice 1 -> 25
"""

# É POSSIVEL ADICIONAR UMA LISTA DENTRO DA OUTRA
# pessoas = list()
# pessoas.append(dados[:])  # Copia da lista/estrutura dados, dentro da lista pessoas
# Agora o íncide 0 da lista pessoas, passa a receber todos os valores da lista dados
# print(pessoas)

# Maneira de declarar a estrutura de uma vez
# pessoas = [['Gui', 17], ['Pedro', 19], ['João', 32]]  # -> 3 Listas dentro da estrutura pessoas
# print(pessoas[0][0])  # -> dentro do índice 0 de pessoas = Gui, 17/ vai pegar o item 0 -> Gui
# print(pessoas[1][1])  # -> índice 1 de pessoas = PEDRO, 19/ pega o ítem 1 -> 19
# print(pessoas[2][0])  # -> [2] = joão, 32/ vai mostrar só o 0 -> 'João'
# print(pessoas[1])

# Praticando
"""
teste = list()
teste.append('Gui')
teste.append(17)
galera = list()
galera.append(teste[:])
teste[0] = 'Leo'
teste[1] = 24
galera.append(teste[:])
print(galera)
"""

"""
galera = [['Gui', 17], ['João', 20], ['Pedro', 12], ['Julia', 19]]
# print(galera[2][1])
# print(galera[1:])
for pessoa in galera:
    #  print(pessoa[0])  # Mostra só os nomes
    # print(pessoa[1])  # mostra só as idades
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade')
"""
galera = list()
dado = list()  # Estrutura auxiliar
totmaior = totmen = 0
for c in range(0, 3):  # Bloco para ler os dados e jogar dentro de galera
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])  # Sempre á copia da lista
    dado.clear()

for p in galera:  # para saber pessoas com mais de 21 anos
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmaior} maiores e {totmen} menores de idade')
