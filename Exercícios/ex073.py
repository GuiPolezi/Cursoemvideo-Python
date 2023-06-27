# Desafio 73 - Tuplas com times de futebol

"""
Crie uma tupla preenchida com os 20 primeiros colocados
da tabela do BRASILEIRÃO SERIE A, na ordem de colocação.
Depois mostre:

- Apenas os 5 primeiros colocados.
- os últimos 4 colocados da tabela.
- Uma lista com os times em ordém alfabética
- Em que posição na tabela está o SÃO PAULO
"""

times = ('Ámerica-MG', 'Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Corinthians', 'Coritiba', 'Cruzeiro',
         'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras',
         'Bragantino', 'Santos', 'São Paulo', 'Vasco')

print('-=' * 30)
print(f'\033[34m{"BRASILEIRÃO SERIE A 2023":^55}\033[m')
print('-=' * 30)

print('\033[31mPrimeiros 5 colocados:\033[m')
print(times[0:5])

print('\033[31mZona de rebaixamento:\033[m')
for time in times[-4:]:  # Para aparecer um abaixo do outro
    print(time)

print('\033[31mTimes em ordem alfabética:\033[m')
print(sorted(times))

print('\033[31mPosição do SÃO PAULO:\033[m')
print(f'São paulo está na {times.index("São Paulo") + 1}ª colocação')