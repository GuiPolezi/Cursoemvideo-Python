from ex115.lib.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')  # 'rt' read text - abrir o arquivo em modo texto
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')  # 'wt' escreve um arquivo de texto, e esse + cria o arquivo
        a.close()
    except:
        print('Houve um erro ao criar o arquivo')
    else:
        print(f'{nome} criado com sucesso')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>5} anos')
    finally:
        a.close()


def cadastrar(arq, nome='Desconhecido', idade='desconhecida'):
    try:
        a = open(arq, 'at') # at+ -> append arquivo de texto, adiciona
    except:
        print('Houve um erro na abertuda do arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('Houve um erro na hora de escrever os dados')
        else:
            print(f'Novo registo de {nome} adicionado!')