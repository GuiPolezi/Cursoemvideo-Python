# Curso 10 - condições

"""
    if carro.esquerda():
        bloco True
    else:
        bloco False
"""

# Exemplo
"""
tempo = int(input('Quantos anos tem seu carro?'))
if tempo <=3
    print('carro novo')
else:
    print('carro velho')
print('---fim---')
"""

# Condição simplificada
"""
tempo = int(input('Quantos anos tem seu carro?'))
print('carro novo' if tempo <=3 else 'carro velho')
print('--fim--')
"""

# Praticando
""" nome = str(input('qual é seu nome? '))
if nome == 'guilherme':
    print('Que belo nome!')
else:
    print('nome porco kk')

print(f'bom dia {nome}')
"""

# Praticando: 2
n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
m = (n1 + n2) /2
print(f'A sua média é de: {m:.1f}')

if m >= 5.0:
    print('A sua nota é azul')
else:
    print('Ta de recuperação')