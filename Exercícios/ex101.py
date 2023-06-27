# Desafio 101 - Funções para votação

"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa,
retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATORIO nas eleições
"""


def voto(ano):
    """

    :param ano: Ano de nascimento.
    :return: votação que recebe tres valores diferentes dependendo da idade
    feito por Gui Polezi
    """
    from datetime import datetime  # Importando modulo como escopo local, ja que so vai ser necessaria na função
    ano_atual = datetime.today().year
    idade = ano_atual - ano
    votação = 'VOTO OBRIGATORIO'
    if idade >= 18:
        return f'Com {idade} anos: {votação}'
    if 18 > idade >= 16 or idade > 65:
        votação = 'VOTO OPCIONAL'
        return f'Com {idade} anos: {votação}'
    else:
        votação = 'VOTO NEGADO'
        return f'Com {idade} anos: {votação}'


# Programa principal
print('-' * 30)
nasc = int(input('Ano de nascimento: '))
print(voto(nasc))  # Parametro recebe nasc = você digita o ano