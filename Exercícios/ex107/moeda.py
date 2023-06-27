# Criando módulo para o exercicio 107 - Exercitando módulos em Python
# Modulo para moeda que tenha as funções incorporadas
# aumentar(), diminuir(), dobro() e metade()

def dobro(n):
    return n * 2


def metade(n):
    return n / 2


def aumentar(n, porcent=0):
    number = porcent / 100 * n
    aumentando_porcent = number + n
    return aumentando_porcent


def diminuir(n, porcent=0):
    numero = porcent / 100 * n
    diminuindo_porcent = n - numero
    return diminuindo_porcent
