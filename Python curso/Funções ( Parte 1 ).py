# Curso python 20 - Funções (parte 1)

"""
Funções são trechos de código que podem ser executados em momentos diferentes de nossos códigos em Python.
"""


# Def = definição de função


def mensagem(msg):  # Definindo a função -> mensagem, passando um parametro -> msg
    print('-' * 30)
    print(f'{msg:^30}')
    print('-' * 30)


mensagem('Aprendendo Funções')  # -> muda o parametro msg para essa mensagem
mensagem('Curso em video')  # msg = curso em video
mensagem('Python')  # msg = python


# Praticando

def soma(a, b):  # Definindo a funçao soma, recebendo dois parametros = a, b
    s = a + b  # variavel s = soma, somando os dois parametros
    print(s)  # quando chamar a função vai sempre printar a soma de a + b


# Programa principal
soma(a=4, b=5)  # os dois parametros se transformam nesses números, assim fazendo a função de somar
soma(5, 15)
soma(6, 4)


def contador(*núm):  # * -> Desempacotar, quer dizer que não sabe quantos parametros vão ser passados, assim jgnd tudo dentro de num
    tamanho = len(núm)
    print(f'Recebi os valores {núm}, e são ao todo {tamanho} números')


contador(1, 2, 3, 4)
contador(5, 6)
contador(9, 9, 8, 7)


def dobra(list):
    pos = 0  # Posição 0
    while pos < len(list):  # enquanto a posição for menor que o tamanho da lista
        list[pos] *= 2  # parametro lista, na posição 0 vezes 2
        pos += 1


lista = [1, 2, 3, 4, 5]  # função com lista, dobrar os valores dentro da lista
dobra(lista)
print(lista)

# DESEMPACOTANDO -> FUNÇÃO SOMA COM MAIS DE 2 VALORES


def soma2(* valores):  # Recebe varios valores
    s = 0  # soma = 0
    for num in valores:  # para cada número em valores (valores é o parametro)
        s = s + num
    print(f'Somando os valores {valores} temos {s}')


soma2(2, 5, 9)
soma2(1, 3)
soma2(5, 5, 5, 5)