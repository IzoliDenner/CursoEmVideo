# padrão ANSI - escape sequence:  Padrão de normalização internacional, funciona para diversos
# ambientes, utilizar para terminar = tudo dentro do ansi comça com CONTRA / - barra invertida

# ex: \033[m

# entre o colchete e o M, colocamos o código da cor
# primeiro informamos é o codigo do comportamento ou estilo, segundo código código do texto ultimo código do
# background cor de fundo

# \033[0;33;44m

# 1º STYLE
# 0 - none sem estilo nenhum
# 1 - texto em negrito
# 4 - sublinhado
# 7 - vai inverter as configurações

# 2º TEXT
# 30 - branco
# 31 - vermelho
# 32 - verde
# 33 - amarelo
# 34 - azul
# 35 - magenta
# 36 - ciano
# 37 - cinza

# 3º BACK - mesmas cores que o anterior. Porem a numeração é de 40 a 47
# 40 - branco
# 41 - vermelho
# 42 - verde
# 43 - amarelo
# 44 - azul
# 45 - magenta
# 46 - ciano
# 47 - cinza

# print('teste')
# \033[0;30;41m
# \033[4;33;44m
# \033[1;35;43m
# \033[30;42m
# \033[m - padrão do terminal, fundo preto letras cinzas
# \033[7;30;m - 7 invertendo o fundo preto para letras pretas

# print('\033[4;30;45mOla, Mundo!!\033[m')
# print('\033[0;33;44mOla, Mundo!!\033[m')
# print('\033[7;33;44mOla, Mundo!!\033[m')

# a = 3
# b = 5
# print('Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!!'.format(a, b))

# nome = 'Denner'
# print('Olá !! Muito prazer em te conhecer, {}{}{} !!!'.format('\033[4;34m', nome, '\033[m'))

# nome = 'Denner'
# cores = {'limpa':'\033[m',
#          'azul':'\033[34m',
#          'amarelo':'\033[33m',
#          'preto':'\033[7;30m'}
#
# print('Olá !! Muito prazer em te conhecer, {}{}{} !!!'.format(cores['azul'], nome, cores, ['limpa']))
conta = 19 // 2
conta1 = 19%2
print(conta, conta1)