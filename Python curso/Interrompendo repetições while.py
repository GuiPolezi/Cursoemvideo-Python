# Curso 15 - interrompendo repetições while

"""
laços de repetição parte 3
"""


"""
Comando BREAK, interrompe o laço while - jogar pra fora de uma estrutura de repetição
"""

# EXEMPLOS
"""
cont = 1
while cont <= 10:
    print(cont,' ', end='')
    cont += 1
print('Acabou')
"""

soma = 0 
while True:
    numero = int(input('Digite um número: '))
    if numero == 999:
        break
    soma += numero
print(f'A soma vale {soma}')
