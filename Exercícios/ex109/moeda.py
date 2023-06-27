# Criando módulo para o exercicio 107 - Exercitando módulos em Python
# Modulo para moeda que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade()

def dobro(n=0, r=False):
    preço = n * 2
    if r:
        return f'{moeda(preço)}'
    else:
        return n * 2


# noinspection PyTypeChecker
def metade(n=0, r=False):
    meio = float(n / 2)
    return meio if r is False else moeda(meio)


# noinspection PyTypeChecker
def aumentar(n=0, porcent=0, r=False):
    number = porcent / 100 * n
    aumentando_porcent = float(number + n)
    return aumentando_porcent if r is False else moeda(aumentando_porcent)


# noinspection PyTypeChecker
def diminuir(n=0, porcent=0, r=False):
    numero = porcent / 100 * n
    diminuindo_porcent = float(n - numero)
    return diminuindo_porcent if r is False else moeda(diminuindo_porcent)


# Fazendo o desafio 108 - Melhorar o codigo do desafio 107 e adicionar uma nova função chamada moeda()

def moeda(n=0):
    return f'R${n:>1.2f}'.replace('.', ',')
