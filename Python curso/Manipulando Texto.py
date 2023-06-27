# Curso 09 - Manipulando texto

"""
- Fatiamento

    frase:
    C-u-r-s-o-  e-m-  V- i- d- e- o-   P- y- t- h- o- n
    0-1-2-3-4-5 6-7-8-9-10-11-12-13-14-15-16-17-18-19-20

    ex:
     print frase[9] - VAI PEGAR A LETRA V - 9
     print frase[9:13] - PEGA AS LETRAS - Vide
"""

"""
- Análise
    
    frase:
    C-u-r-s-o-  e-m-  V- i- d- e- o-   P- y- t- h- o- n
    0-1-2-3-4-5 6-7-8-9-10-11-12-13-14-15-16-17-18-19-20
    
    ex:
    len(frase) - length - 21
    frase.count('o') - contar quantas vezes aparece o mínusculo
    frase.find('deo') - retorna 11 começo da palavra deo
    frase.find('android') - retorna -1 -nao foi encontrado
"""

"""
- Transformação
    
    frase:
    C-u-r-s-o-  e-m-  V- i- d- e- o-   P- y- t- h- o- n
    0-1-2-3-4-5 6-7-8-9-10-11-12-13-14-15-16-17-18-19-20
    
    ex:
    frase.replace('python', 'android') - troca a palavra python por android
    frase.upper() - Letras maiusculas
    frase.lower() - Letras minusculas 
    frase.capítalize()
    frase.title()
    frase.strip() - remover espaços inuteis no  inicio e no final da string
"""

"""
- Divisão

    frase:
    C-u-r-s-o-  e-m-  V- i- d- e- o-   P- y- t- h- o- n
    0-1-2-3-4-5 6-7-8-9-10-11-12-13-14-15-16-17-18-19-20
    
    ex:
    frase.split() - divisão dentro da string considerando os espaços
    
"""

"""
- Junçao

    frase:
    C-u-r-s-o-  e-m-  V- i- d- e- o-   P- y- t- h- o- n
    0-1-2-3-4-5 6-7-8-9-10-11-12-13-14-15-16-17-18-19-20
    
    ex:
    -.join(frase) - traço no lugar de espaço
"""

# Testes
frase = 'Curso em video python'
print(frase.replace('python', 'iphone'))