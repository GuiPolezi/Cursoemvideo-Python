# Curso python 11 - Cores no terminal
"""
cores:

  style             text                    background
0 - none        30      black           preto           40
1 - bold        31      red             vermelho        41
4 - underline   32      green           verde           42
7 - negative    33      yellow          amarelo         43
                34      blue            azul            44
                35      Magenta         Magenta         45
                36      cyan            ciano           46
                37      grey            cinza           47
                97      white           branco          107
"""

"""
 ANSI - escape sequence -> \
 
 exemplo: 
        style back        
    \033[0;33;44m
          text
"""

# Testes:

# print('\033[1;97;40mOlá, mundo!\033[m')
"""
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b}\033[m')
"""
nome = 'Polezi'
cores = {'limpa': '\033[m',
         'azul': '\033[34m',
         'amarelo': '\033[33m',
         'pretoebranco': '\033[7:30m'}
print(f'Prazer em te conhecer {cores["amarelo"]} {nome} {cores["limpa"]}!!!')
