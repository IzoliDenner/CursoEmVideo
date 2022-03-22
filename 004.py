#exercicio4

a = input ('Digite algo:')
print('O tipo primitivo desse valor é', type(a))
print('Só tem espaços?', a.isspace())
print('É um número?', a.isnumeric())
print('É alfabético?', a.isalpha())
print('É alfanemérico?', a.isalnum())
print('Esta em maiusculas?', a.isupper())
print('Esta em minusculas?', a.islower())
print('Esta capitalizada?', a.istitle())'''

'''nome = input('Qual éo seu nome?:')
print('Prazer em te conhecer {:=^20}!'.format (nome))'''
'''
n1 = int(input('Um valor:'))
n2 = int(input('Outro Valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2


print('A soma é {}, \no produto é {} e a divisão é {:.3f}'.format(s, m, d), end=' ')
print('Divisão Inteira {} e potencialização {}' .format(di, e))

