# Para adicionar módulos ou bibliotecas, basta fazer como o exemplo abaixo
'''
import math

ceil = arredonda para cima
floor = arredonda para baixo
trunc = vai eliminar da virgula pra frente
pow = power potencia
sqrt = calcular raiz quadrada
factorial = calcula factorial de um numero

para chamar somente uma funcionalidade espeficica de uma biblioteca:

exemplo

from match import sqrt
'''
#1º forma de importar bibliotecas, importando ela completa
'''
import math
num = int(input('Digite um numero: '))
raiz = math.sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num, (raiz))
'''
#2º forma de importar bibliotecas, importando somente a funcionalidade desejada
'''
from math import sqrt, floor
num = int(input('Digite um numero: '))
raiz = sqrt(num)

print('A raiz de {} é igual a {:.2f}'.format(num, floor(raiz)))'''

'''import random # funcionalidade RANDOM, escolhe um numero aleatório
num = random.randint(1,10)
print(num)'''

import emoji
print(emoji.emojize("Ola Mundo!! :earth_americas:", use_aliases=True))