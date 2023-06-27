# Desafio 56 - Analisador completo

"""
Desenvolva um programa que leia:
o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:

- Média de idade do grupo.
- Nome do homem mais velho.
- Quantas mulheres tem menos de 21 anos
"""

somaidade = 0
idadehvelho = 0
nomehvelho = 0
mulhermenos = 0
for p in range(1, 5):
    print('-' * 5, f'{p}ª PESSOA', '-' * 5)
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    somaidade = somaidade + idade
    mediaidade = somaidade / 4
    if sexo == 'M' and idade > idadehvelho:
        idadehvelho = idade
        nomehvelho = nome
    if sexo == 'F' and mulhermenos < 21:
        mulhermenos += 1
print(f'A média de idades dessas pessoas é de {mediaidade:.0f} anos')
print(f'O homem mais velho chama-se: {nomehvelho}, e tem {idadehvelho} anos')
print(f'Mulheres com menos de 21 anos = {mulhermenos}')