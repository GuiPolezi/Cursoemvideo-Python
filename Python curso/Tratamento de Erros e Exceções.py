# Curso python 23 - Tratamento de Erros e Exceções

"""
Erros acontecem.
Python é repleto de exceções
exceção não é um erro sintatico mas ele está acontecendo
"""

# Tratando exceções com python
"""
Clausulas para tratar exceções: 
- try (tente) - tentar
    operação (os comandos que normalmente dariam problemas)

# Em um mesmo try é possivel se ter varios excepts

- except (exceção) -> se der problema
    falha (se eu tentar a coisa de cima e falhar, o que ira acontecer?)
    
Clausulas opcionais:
- else (se não der problema) - se meu try deu certo
    deu certo
- finally (finalmente) - acontece independente se deu certo ou falha
    certo/falha
"""

# Exemplos com try e except
try:  # tenta ler e tentar dividir
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except Exception as erro:  # Exception é o pai das exceções, para informar o tipo de erro escreve Exception as erro
    print(f'Problema encontrado foi {erro.__cause__}')  # erro.__cause__ vai mostrar a causa do erro

# Outro tipo de except
except (ValueError, TypeError):
    print(f'Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print(f'Não é possivel dividir por 0')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
else:
    print(f'O resultado é {r}')
finally:
    print('Fim do programa')

# primt(x) - apenas um erro de sintaxe
# print(x) - exceção -> x não existe -> aparece uma exceção no console dizendo nameError = erro de nome

# Exemplo de exceção:
"""
n = int(input('Número: '))
print(f'Você digitou o número {n}')
Se o codigo acima for digitado com valor sem ser int, ou seja não digitar um número e sim uma palavra
Acontece o que chamamos de exceção -> no console aparece ValueError = erro de valor
"""

# Outro exemplo de exceção:
"""
a = int(input('Numerador: '))
b = int(input('Denominador: '))
r = a / b
print(f'o resultado é {r}')
Se tentar dividir por 0 acontece outra exceção com o valor de ZeroDivisionError, já que divisão por 0 n é possivel fzr
"""
