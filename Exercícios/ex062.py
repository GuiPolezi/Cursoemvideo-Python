# Desafio 62 - Super progressão aritmética 3.0

"""
Melhore o desafio 61, perguntando para o usuário se ele quer mostrar mais alguns termos
O programa encerra quando ele disser que quer mostrar 0 termos.
"""

print('\033[35mGerador de PA\033[0m')
print('=-' * 15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo}', end=' -> ')
        termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print(f'Progressão finalizada com {total} termos ')