# Criando módulo para o exercicio 107 - Exercitando módulos em Python
# Modulo para moeda que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade()

def dobro(n=0):
    return n * 2


def metade(n=0):
    return n / 2


def aumentar(n=0, porcent=0):
    number = porcent / 100 * n
    aumentando_porcent = number + n
    return aumentando_porcent


def diminuir(n=0, porcent=0):
    numero = porcent / 100 * n
    diminuindo_porcent = n - numero
    return diminuindo_porcent


# Fazendo o desafio 108 - Melhorar o codigo do desafio 107 e adicionar uma nova função chamada moeda()

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:>8.2f}'.replace('.', ',')