# Curso python 12 - condições aninhadas - mundo 2

"""
if - se
elif - senao se
else - senao
"""

nome = str(input('qual é o seu nome? '))
if nome == 'Guilherme':
    print('Você é zica')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Ana':
    print('Seu nome é muito popular no brasil')
elif nome in 'Claudia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é bem normal')
print(f'Tenha um bom dia, {nome}')
