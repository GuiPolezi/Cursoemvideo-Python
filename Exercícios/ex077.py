# Desafio 77 - Contando vogais em tupla

"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais
"""
palavras = ('praticar', 'aprender', 'foco', 'escrever', 'entender', 'dificuldade')
vogais = 'aeiou'
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')