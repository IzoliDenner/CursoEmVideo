# 06 Crie um algoritmo que leia um numero e mostro o seu dobro, triplo e raiz quadrada
# primeira maneira
n = int(input('Digite um numero'))
d = n * 2
t = n * 3
r = n ** (1/2)

print('O numero digitado é {}, o dobro dele é {}, o triplo dele é {} e a raiz quadrada é {}.'.format(n, d, t, r))

n = int(input('Digite um numero'))
print('O dobro de {} vale {}.'.format(n, (n*2)))
print('O triplo de {} vale {}. A raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, (n**(1/2))))


