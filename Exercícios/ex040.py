# Desafio 40 - Aquele clássico da Média

"""
Crie um programa que leia duas notas e calcule sua média, mostrando uma mensagem no final,
de acordo com a média atingida:

- média abaixo de 5.0: Reprovado
- Média entre 5.0 e 6.9: Recuperação
- média 7.0 ou superior: Aprovado
"""

a = float(input('Primeira nota: '))
b = float(input('Segunda nota: '))
media = (a + b) / 2
if media < 5.0:
    print(f'Sua nota é: {media:.1f}, então está REPROVADO!!!')
elif 5.0 <= media <= 6.9:
    print(f'Sua nota é: {media:.1f}, ficou de RECUPERAÇÃO!!!')
else:
    print(f'Você tirou {media:.1f}, foi APROVADO!!!')
    print('Parabéns')
