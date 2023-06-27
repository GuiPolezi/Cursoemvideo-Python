# Desafio 114 - Site esta acessivel?

"""
Crie um codigo em python que teste se o site Pudim está acessivel
pelo computador usado
"""

import urllib
import urllib.request

# noinspection PyBroadException
try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except:
    print('\033[31mO site não esta acessivel no momento\033[m')
else:
    print('\033[32mFoi possivel acessar o site Pudim\033[m')