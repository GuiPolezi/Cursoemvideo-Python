def leiaInt(msg):
    while True:
        try:
            inteiro = int(input(msg))
        except KeyboardInterrupt:
            print(f'\033[31mUsuário preferiu não digitar esse número.')
            return 0
        except (ValueError, TypeError):
            print('\033[31mERRO: por favor digite um número inteiro válido!\033[m')
            continue
        else:
            return inteiro


def linha(tam=42):
    print('-' * tam)


def cabeçalho(txt):
    linha(40)
    print(f'{txt:^40}')
    linha(40)


# noinspection PyBroadException
def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    cont = 1
    for item in lista:
        print(f'\033[36m{cont}\033[m -\033[30m {item}\033[m')
        cont += 1
    linha(40)
    opc = leiaInt('\033[32mSua opção: \033[m')
    return opc

