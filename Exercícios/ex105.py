# Desafio 105 - Analisando e gerando dicionarios

"""
Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar
um dicionário
com as seguintes informações:
- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)
- Adicione também as docstrings da função
"""


def notas(* num, sit=False):
    """
    Função notas utilizada para retornar um dicionario com informações da turma
    :param num: parametro infinito, recebe varios números ou recebe apenas 1
    :param sit: parametro opcional, se sit=True -> escreve a situação da turma
    :return: retorna o dicionario -> armazenado varias informações sobre a situação da turma
    """
    dicionario = dict()
    dicionario['total'] = len(num)
    dicionario['maior'] = max(num)
    dicionario['menor'] = min(num)
    dicionario['média'] = sum(num) / len(num)
    if sit:
        if dicionario['média'] <= 5:
            print('Situação: Recuperação')
        if 6 <= dicionario['média'] <= 8:
            print('Situação: Médiano')
        elif 9 <= dicionario['média'] <= 10:
            print('Situação: Boa')
    return dicionario


aluno1 = notas(4.5, 10, 6.5, sit=True)
aluno2 = notas(10, 5, 7, 8)
print(aluno1)
print('-' * 60)
print(aluno2)
help(notas)