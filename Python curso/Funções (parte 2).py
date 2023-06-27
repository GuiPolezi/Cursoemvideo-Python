# Curso Python # 21 - Funções parte 2

"""
Nessa aula, vamos continuar nossos estudos de funções em Python,
aprendendo mais sobre Interactive Help em Python,
o uso de docstrings para documentar nossas funções,
argumentos opcionais para dar mais dinamismo em funções Python, escopo de variáveis e retorno de resultados.
"""

#               INTERACTIVE HELP = AJUDA INTERATIVA
# Obtida atraves da função interna (metodo) help()  -> digite help no console

# ----------------------------------------------------------------------------------------------------------------------
print('-' * 40)  # DIVIDINDO NO CONSOLE


#                   DOCSTRINGS - STRING DE DOCUMENTAÇÃO
# -> Todas as funcionalidades internas do python possuem sua propria docstring
# Porém é possivel fazer sua propria docstring para definir a documentação de sua função
# Docstring entra na primeira linha abaixo da função
# Para criar e abrir a sua docstring é so abrir aspas duplas ("") tres vezes logo na linha debaixo do comando def
# Significados:
"""
:param -> parâmetro
"""


def contador(i, f, p):
    """
    -> A função faz uma contagem e mostra na tela
    :param i: Inicio da contagem
    :param f: Fim da contagem
    :param p: Passo da contagem
    :return:  Sem retorno
    Função criada por GuiPolezi - Feita para o curso em video
    """
    c = i  # contagem recebe inicio
    while c <= f:  # enquanto contagem for menor q o fim da minha contagem
        print(f'{c} ', end='')
        c += p  # Contagem recebe inicio e passo
    print('Fim')


contador(2, 10, 2)
help(contador)  # -> interactive help (help()) usado para saber a docstring da função contador criada por mim


# ----------------------------------------------------------------------------------------------------------------------
print('-' * 40)  # DIVIDINDO NO CONSOLE


#               PARÂMETROS OPCIONAIS
# Diferente de multiplos parametros!!
# Função recebe A, B, C
# C=0, significa que caso os parametros A, B recebam valores e o C não, C recebe 0, Criando assim parametro opcional
# É possivel fazer os 3 parametros receberem parametros opcionais (a=0, b=0, c=0)
# parametros opcionais = não necessariamente precisam ser passados


def somar(a=0, b=0, c=0):
    """
    -> Faz a soma de 2 até 3 valores
    :param a: Recebe o Primeiro valor, Caso não A=0 (A igual a 0)
    :param b: Recebe o Segundo valor, Caso não B=0 (B igual a 0)
    :param c: Recebe o Terceiro valor, Caso não C=0(C igual a 0)
    Função criada Por Gui Polezi
    """
    s = a + b + c
    print(f'A soma vale {s}')


help(somar)
somar(3, 5, 2)
somar(8, 4)  # terceiro valor (c) não informado recebe 0
somar(c=4, b=10)
somar()


# ----------------------------------------------------------------------------------------------------------------------
print('-' * 40)  # DIVIDINDO NO CONSOLE


#               ESCOPO DE VARIÁVEIS - ESCOPO DE DECLARAÇÕES
# escopo é o local onde uma variavel vai existir e o local onde ela não vai mais existir
# ESCOPO GLOBAL = Mesmo N sendo definido la embaixo, ele vai funcionar em toda essa área ate mesmo na função
# b possui escopo local, pois ele existe somente dentro da função teste, so vai funcionar na area da função

def teste(b):  # Função recebe parametro B
    """
    -> função teste para estudo sobre ESCOPO DE VARIAVEIS
    Escopo global: variavel dentro do "programa principal" funciona em td o programa
    Escopo local: variavel que existe somente dentro de um local (função), só funciona na mesma área
    todas as variaveis dentro de teste só existem e funcionam em teste.
    Função criada por Gui Polezi
    :param b: Parametro B -> fora da função foi passado a variavel A no lugar, resultando b+= 4 em 9, pois param b = n
    (b recebe n)
    Função criada por Gui Polezi
    """
    global n  # Faz com que não crie uma variavel nova (n) e sim use a variavel com escopo global (n fora da função)
    n = 8
    b += 4  # B (ESCOPO LOCAL) recebe B + 4, Fora da função, teste teve como parametro N, então B recebe 5 (N) + 4 = 9
    c = 2  # C é um escopo local pois so funciona e existe dentro dessa função
    print(f'N dentro vale {n}')  # agora N vale 3 por estar em um escopo local
    print(f'B dentro vale {b}')  # B vale 9
    print(f'C dentro vale {c}')  # c vale 2

# Programa principal

help(teste)
n = 5  # Variavel N -> ESCOPO GLOBAL, A varial (n) mesmo declarada fora da função ela continua funcionando dentro
teste(n)  # Transforma a função B em A (Escopo global), então B recebe 5 (N) + 4 = 9
# print(f'b fora vale {b}')  # esse codigo da erro por b ser um escopo local e esta sendo printado fora do seu local
print(f'N fora vale {n}')  # com a palavra global N passou a receber 8

# ----------------------------------------------------------------------------------------------------------------------
print('-' * 40)  # DIVIDINDO NO CONSOLE


#           Retornando os valores - return
def soma(a=0, b=0, c=0):
    """

    :param a: Parametro opcional, recebe um numero para soma
    :param b: Parametro opcional, recebe um numero para soma
    :param c: Parametro opcional, recebe um numero para soma
    :return: retorna s (resultado da soma) para fora da função em alguma coisa antes de somar(),
    por exemplo r1 = somar(3, 2, 5) = 10, o resultado (s) vai para dentro da variavel r1, entao r1 recebe 10
    assim sendo possivel colocar um print da maneira que eu quiser (flexivel) (personalização do resultado)
    """
    s = a + b + c
    return s  # retorno para s


help(soma)
r1 = soma(3, 2, 5)
r2 = soma(4, 8)
r3 = soma(10)
print(f'Meus calculos deram {r1}, {r2} e {r3}')
print(f'Não somei nenhum número apenas adicionei o número: {r3}')

# ----------------------------------------------------------------------------------------------------------------------
print('-' * 40)  # DIVIDINDO NO CONSOLE

#                       PRATICANDO
print('HORA DA PRATICA!!!!')


# CALCULO DE FATORIAL
def fatorial(num=1):  # função fatorial com parametro opcional, se não passar numero nenhum ele vai ser = 1
    f = 1  # fatorial recebe 1
    for c in range(num, 0, - 1):
        f *= c
    return f


n = int(input('Digite um número: '))
print(f'O fatorial de {n} é = {fatorial(n)}')

# ----------------------------------------------------------------------------------------------------------------------
print('-' * 40)  # DIVIDINDO NO CONSOLE


# PAR OU IMPAR
def parOuImpar(numero=0):
    if numero % 2 == 0:
        return True
    else:
        return False


print('Par ou Impar')
num = int(input('Digite um numero: '))
if parOuImpar(num):  # Se parOuImpar(num) for RETURN True = for verdadeiro dentro da função, print par
    print('É par!')
else:  # Se não, retorna false = é impar
    print('É impar!')