# Desafio 42 - Analisando triângulos v2.0

"""
Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:

- EQUILATERO: todos os lados iguais
- ISOSCELES: dois lados iguais
- ESCALENO: todos os lados diferentes
"""

print('=-' * 30)
print('Analisador de Triângulos V2.0')
print('=-' * 30)

a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if a < b + c and b < a + c and c < a + b:
    print('Os segmentos acima PODEM formar um triângulo', end=' ')
    if a == b == c:
        print('EQUILATERO!')
    elif a != b != c != a:
        print('ESCALENO!')
    else:
        print('ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM formar um triângulo')
