# Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.
'''1º Maneira
nome = str(input('Digite aqui o seu nome: '))
maiusculo = nome.upper()
minusculo = nome.lower()
quantidade = len(nome)
#dividido = nome.split().len()

print('Seu nome em maiusculas é {}.'.format(maiusculo))
print('Seu nome em minusculas é {}.'.format(minusculo))
print('Seu nome tem ao todo {}.'.format(quantidade))
print('Seu nome em maiusculas é {}.'.format(maiusculo))'''

nome = str(input('Digite aqui o seu nome: ')).strip()
print('Analisando seu nome: ....')
print('Seu nome em maisculas é {}.'.format(nome.upper()))
print('Seu nome em Minuscula é {}.'.format(nome.lower()))
print('Seu tem ao todo {} letras.'.format(len(nome) - nome.count(' ')))
#print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))


