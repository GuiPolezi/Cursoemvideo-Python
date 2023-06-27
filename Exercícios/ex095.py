# Desafio 95 - Aprimorando os dicionarios

"""
Aprimore o DESAFIO 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de DETALHES DO APROVEITAMENTO de cada jogador.
"""

from emoji import emojize

print('=' * 30)
print(f'\033[32m{"== TRANSFERMARKET 2.0 ==":^30}\033[m')
print('=' * 30)

jogador = dict()  # dicionario
partidas = []  # lista
time = list()  # lista

while True:  # laço infinito
    jogador.clear()  # Limpa o dicionario
    jogador['Nome'] = str(input(f'Nome do jogador {emojize(":trophy:")}: '))
    tot = int(input(f'Quantas partidas {jogador["Nome"]} jogou?: '))
    partidas.clear()  # lista limpada
    for c in range(0, tot):  # para contador in range 0 ate total de jogos
        partidas.append(int((input(f'-> Quantos gols{emojize(":soccer_ball:")} na {c + 1}ª partida? '))))
        # adiciona na lista partidas
    jogador['Gols'] = partidas[:]  # cria key gols com copia da lista partidas
    jogador['Total'] = sum(partidas)  # key total, soma de partidas
    time.append(jogador.copy())  # lista time adiciona copia do dicionario
    continuar = str(input('\033[34mQuer continuar [S/N]? \033[m')).upper().strip()[0]
    while continuar not in 'SN':
        continuar = str(input('\033[31mResposta invalida! Quer continuar [S/N]? \033[m')).upper().strip()[0]
    print('-' * 30)
    if continuar == 'N':
        break

print('No. ', end='')  # cabeçalho
for i in jogador.keys():  # indice na chave do dicionario
    print(f'{i:<15}', end='')
print()  # quebra linha
print('-=' * 30)
for k, v in enumerate(time):  # k = key, v = value, numerando a lista time
    print(f'{k:<5}', end='')
    for d in v.values():  # d = dado, valores da lista enumarada
        print(f'{str(d):<15}', end='')
    print()
print('-=' * 30)
while True:  # laço infinito
    busca = int(input('Buscar dados de qual jogador? (999 interrompe) '))  # variavel busca
    if busca == 999:
        break
    if busca >= len(time):  # se a variavel for maior que lenght(comprimento) da lista time
        print(f'ERRO! Não existe jogador com codigo {busca}!')
    else:
        print(f' -- Levantamento do jogador {time[busca]["Nome"]}')
        for i, g in enumerate(time[busca]['Gols']):   # i = indice, g = gols, enumerado lista times -> variavel -> gols
            print(f' No jogo {i + 1} fez {g} {"gol" if g == 1 else "gols"}')
    print('-' * 40)
print('<<< VOLTE SEMPRE >>>')