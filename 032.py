# Exercício Python 32:
# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# 1º maneira fórmula imcompleta
'''
ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {}  não é BISSEXTO.'.format(ano))
'''

# 2º maneira fórmula completa
'''
ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} não é BISSEXTO.'.format(ano))
'''

from datetime import date
# 3º mais uma condição para analisar o ano atual que esta na nossa maquina
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO.'.format(ano))
else:
    print('O ano {} não é BISSEXTO.'.format(ano))