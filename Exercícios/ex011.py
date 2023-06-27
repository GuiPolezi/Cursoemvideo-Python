# Desafio 11 - Pintando parede

"""
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
"""
lp = float(input('Largura da parede: '))
ap = float(input('Altura da parede: '))
area = lp * ap
tinta = area / 2
print(f'Sua parede tem a dimensão de {lp}X{ap} e sua área é de {area}²')
print(f'Para pintar essa parede, você precisará de {tinta}l de tinta')