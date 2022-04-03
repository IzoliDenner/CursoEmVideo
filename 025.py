#Exercício Python 025:
# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

# maneira errada
'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva ? {}'.format(nome[:5] == 'Silva'))
'''

#2º Maneira utilizando o 'in' conseguimos corrigir o fato do nome silva não estar no inicio da palavra
'''
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva ? {}'.format('Silva' in nome))
'''
# 3º Maneira corrigindo as letras estarem maiusculas ou nao
nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome tem Silva ? {}'.format('silva' in nome.lower()))

