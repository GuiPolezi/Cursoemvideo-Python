# Desafio 67 - Tabuada v3.0

"""
Faça um programa que mostre a tabuada de vários números, um de cada vez,
pra cada valor digitado pelo usuário. O programa será interrompido
quando o número solicitado for negativo.
"""
from time import sleep

while True:
    print('\033[31mPara encerrar o programa digite um número negativo!!!\033[m')
    tabuada = int(input('Quer ver a tabuada de qual valor? -> '))
    sleep(0.5)
    print('\033[34m-\033[m' * 20)
    if tabuada < 0:
        break
    for c in range(1, 11):
        print(f'{tabuada} X {c:2} = {tabuada * c}')
    print('\033[34m-\033[m' * 20)
    sleep(1)
print('\033[30mTabuada v3.0 -> Encerrada!!!\033[m')