# Exercício Python 33:
# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

# 1º maneira - correta mais complicada
'''
num1 = int(input('Primeiro valor:'))
num2 = int(input('Segundo valor:'))
num3 = int(input('Terceiro valor:'))
if num1 >= num2 and num1 >= num3:
    print('O número {} é maior que o número {} e o número {}.'.format(num1, num2, num3))
'''
# 2º maneira simplificada
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
num3 = int(input('Terceiro valor: '))

# verificando que é o menor
menor = num1
if num2 < num1 and num2 < num3:
    menor = num2
if num3 < num1 and num3 < num2:
    menor = num3
print('O menor valor digitado foi: {}'.format(menor))

# verificando quem é o maior
maior = num1
if num2 > num1 and num2 > num3:
    maior = num2
if num3 > num1 and num3 > num2:
    maior = num3
print('O maior valor digitado foi: {}'.format(maior))
