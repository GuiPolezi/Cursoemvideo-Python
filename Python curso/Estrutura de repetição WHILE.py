# Curso python - 014

"""
while not -
    passo
pega
"""

"""
(AULA)
while not apple:
    if chão:
        passo
    if buraco:
        pula
    if moeda:
        pega
pega
"""

# Praticando

'''
for c in range(1,10):
    print(c)
print('FIM')
'''

'''
c = 1
while c < 10:
    print(c)
    c = c + 1
print('FIM')
'''

'''
n = 1
while n != 0:
    n = int(input('Digite um valor: '))
print('FIM')
'''

'''
n = 1
r = 'S'
while r == 'S':
    n = int(input('Digite um valor: '))
    r = str(input('Quer continuar? [S/N] ')).upper()
print('Fim')
'''

n = 1
par = impar = 0
while n != 0:
    n = int(input('Digite um valor: '))
    if n != 0:
        if n % 2 == 0:
            par = par + 1
        else:
            impar = impar + 1
print(f'Você digitou {par} números pares e {impar} números impares')