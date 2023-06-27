# Desafio 75 - Análise de dados em uma tupla

"""
Desenvolva um programa que leia quatro valores teclado e guarde-os em uma tupla.
No final, mostre:

- Quantas vezes apareceu o valor 9.
- Em que posição foi digitado o primeiro valor 3.
- Quais foram os números pares
"""
numeros = (int(input('Digite um número: ')), int(input('Digite outro número: ')),
           int(input('Digite mais um número: ')), int(input('Digite o último número: ')))
cont = 0
par = 0
print('-' * 30)
print(f'Você digitou os valores: \033[35m{numeros}\033[m')
print(f'O valor 9 {"não apareceu" if numeros.count(9) == 0 else f"apareceu {numeros.count(9)} veze[s]"} ')
if 3 not in numeros:
    print('O valor 3 não foi digitado em nenhuma posição')
else:
    print(f'O valor 3 apareceu na {numeros.index(3) + 1}ª posição')
print('Os números pares são = ', end='')
for c in numeros:
    if c % 2 == 0:
        print(c, end=' ')
    else:
        print('Não teve número par!')
        break