# Desafio 94 - Unindo dicionários e listas

"""
Crie um programa que leia NOME, SEXO e IDADE de várias pessoas,
guardando os dados de cada pessoa em um DICIONÁRIO e todos os dicionários em uma lista.
No final, mostre:
- Quantas pessoas foram cadastradas
- a MÉDIA de idade do grupo
- uma lista com todas as MULHERES.
- uma lista com todas as pessoas com IDADE acima da MÉDIA
"""

from time import sleep

lista = list()   # Lista vazia
mulheres = []  # Lista para armazenar as mulheres
cont = soma = 0   # Contador, Soma = 0

while True:
    dados = dict()     # Dicionario vazio
    dados['Nome'] = str(input('Nome: '))  # Chave(key) nome
    dados['Sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]   # chave(key) Sexo
    while dados['Sexo'] not in 'MF':  # Laço que roda enquanto não digitar a letra M ou F
        dados['Sexo'] = str(input('Erro ao registar! [M/F]: ')).strip().upper()[0]  # Laço rodando enqt n digita MF
    dados['Idade'] = int(input('Idade: '))  # Chave(key) idade, perguntando o valor
    cont += 1  # Contador dentro do laço while para saber quantas pessoas tem
    soma = soma + dados['Idade']
    media = soma / cont  # Soma dividido pela quantidade de pessoas (contador)
    lista.append(dados.copy())  # Adicionando o dicionario em uma lista, copiando o dicionario
    continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Erro! Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar in 'N':
        sleep(0.5)
        print('Finalizando...')
        break


print('\033[31m=-' * 30)
print(lista)

print('=-' * 30, '\033[m')
print(f' - O grupo tem {cont} {"pessoa" if cont == 0 else "pessoas"}.')
print(f' - A média de idade é de {media:.2f} anos')
for p in lista:  # P = pessoa, para cada pessoa na lista
    if p['Sexo'] == 'F':  # Verifica se pessoa[sexo] = Feminino
        mulheres.append(p['Nome'])  # Adiciona na lista mulheres, pessoa['Nome']
if mulheres:  # Se lista - mulheres
    print(f' - {"A mulher cadastrada foi:" if mulheres == 1 else "As mulheres cadastradas foram:"} '
          f'{", ".join(mulheres)}')  # join = permite unire lementos de uma lista em string separados por virgula
else:
    print(' - Nenhuma mulher foi cadastrada')
print(' - Lista das pessoas que estão acima da média: ')

for p in lista:  # P = pessoa, para cada pessoa na lista
    if p['Idade'] >= media:  # se pessoa[idade] maior que media
        print('\033[30m   ↓' * 11, '\033[m')
        for k, v in p.items():
            print(f' - {k} = {v};', end=' ')
        print()
print('\033[34m<<< Encerrado >>>\033[m')