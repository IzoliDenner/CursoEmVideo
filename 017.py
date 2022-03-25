# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triangulo
# retangulo, calcule e mostre o comprimento da hipotenusa

# 1º solução
'''
co = float(input('Comprimento do cateto Oposto: '))
ca = float(input('Comprimento do cateto Adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A Hipotenusa vai medir: {:.2f}'.format(hi))'''

# 2º Solução

from math import hypot
co = float(input('Comprimento do cateto Oposto: '))
ca = float(input('Comprimento do cateto Adjacente: '))
hi = hypot(co, ca)
print('A Hipotenusa vai medir: {:.2f}'.format(hi))
