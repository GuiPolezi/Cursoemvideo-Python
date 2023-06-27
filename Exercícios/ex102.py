# Desafio 102 - Função para fatorial

"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro que indique o número a calcular
o segundo chamado show, que será um valor lógico (opcional) indicando se será
ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(a, show=False):
    """
    -> Calcula o fatorial de um número
    :param a: Número a ser calculado
    :param show: parametro opcional, se quiser utilize escrevendo show=True, para mostrar o calculo da fatorial
    :return: retorna o valor do fatorial de um número a
    """
    f = 1  # fatorial recebe 1
    for c in range(a, 0, -1):  # para c na distancia de a=numero escolhido, até 0, passo - 1
        if show:
            print(c, end='')
            if c > 1:  # Se c for maior q 1, ou seja c é o fatorial até chegar em 1
                print(f'! x ', end='')  # antes de chegar em 1 vai multiplicando. ou recebendo a string X
            else:  # Se chegou em um, recebe a string =, pois dps de 1 é o resultado do fatorial
                print('! = ', end='')
        f *= c  # fatorial recebe fatorial vezes c
    return f


# Programa principal

print(f'O resultado do fatorial de 10 é = {fatorial(10)}')
print(f'{fatorial(5, show=True)} > calculo do fatorial de 5')
help(fatorial)