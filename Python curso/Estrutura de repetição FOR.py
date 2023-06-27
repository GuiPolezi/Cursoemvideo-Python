# Curso python 13 - FOR

"""
exemplo:
for C in range(1, 10):      RANGE = INTERVALO
    passo
pega

outro exemplo:

for C in range(0, 3):
    if moeda:
        pega
    passo
    pula
passo
pega
"""

# Exercícios da aula:

"""
for c in range(1, 6):
    print('Oi')
print('Fim')
"""

""" 
n = int(input('Digite um número: '))
for c in range(0, n+1):
    print(c)
print('fim')
"""

""" 
i = int(input('Início: ')) # Inicio da contagem
f = int(input('Fim: ')) # Fim
p = int(input('Passo: ')) # Pulando quantos números - Passos
for c in range(i, f+1, p):
    print(c)
print('Fim')
"""

s = 0
for c in range(0, 4):
    n = int(input('Digite um valor: '))
    s += n
print(f'O somatorio de todos os valores foi {s}')