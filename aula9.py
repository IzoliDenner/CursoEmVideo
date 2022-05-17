# [] = listas
'''
frase = 'Curso em Video Python'

print(frase[9:21:2])  # vai começar do caractere de numero 9 vai até o 21 pulando de 2 em 2
print(frase[:5])  # Quando não escolho de onde começar ele começa do começo
print(frase[15:])  # Quando não indico o final, ele entende que vai até o final
print(frase[9::3])  # Começo no 9 caractere, nao indiquei onde termina logo entende que vai até o final
#pula de 3 em 3

print(frase.count('o'))  # count serve para mostrar quantas vezes a letra escolhida aparece
print(frase.count('o',0,13))  # count contagem ja com fatiamento nesse caso, vai contar quantas letras
# o aparecem do caractere 0 até o 13

print(frase.find('deo'))  # find vai mostrar em que lugar da str foi encontrado o que se pediu
#  encontrei DEO a partir do caractere 11
print(frase.find('Android'))  #  quando procuro algo que não tenho na str me retorna -1 não foi encontrado

print('Curso' in frase)  #  Existe a palavra Curso na String Frase, o operador IN retorna TRUE
'''


'''
frase = 'curso em video Python'
print(frase.replace('Python', 'Android' ))
# vai encontrar onde tem python e modificar por android
# replace : serve para modificar palavra encontrada na str ex

print(frase.upper())
# upper : vai deixar toda a string maiuscula

print(frase.lower())
# lower : vai deixar toda a string minuscula

print(frase.capitalize())
# capitalize : ele vai jogar toda a string para minusculos, e vai deixar sempre a primeira palavra Maiusculos

print(frase.title())
# tittle : parecido, porem vai deixar maiuscula a primeira letra de cada palavra
'''
'''
frase = '   Aprenda Python  '
print(frase.strip())
# strip : remove todos os espaços inuteis no começo e no fim da string

print(frase.rstrip())
# rstrip : remove somente os ultimos espaços inuteis (direita)

print(frase.lstrip())
# lstrip : remove somente os primeiros espaços inuteis (esquerda)
'''
'''
frase = 'Curso em Video Python'
print(frase.split())
# split : ele faz a divisão da string, cada palavra se torna um indice independente

print('-'.join(frase))
# join : ao contrário, ele faz uma junção das palavras para se tornar apenas um indice
'''


frase = 'Curso em Video Python'
print(frase.upper().count('O'))
# Imprima a frase toda em maisculas e me retorne quantas letras O tem na palavra

frase = '   Curso em Video Python   '
print(len(frase.strip()))
# Len conta a quantidade de palavras, e strip exclui possiveis espaços digitados

frase = 'Curso em Video Python'
print(frase.replace('Python', 'Android'))
print(frase)
# replace eu modifico a primeira palavra atribuida pela segunda palavra atribuida
# Lembrando que com este replace eu não modifiquei a string, eu atribui naquele momento uma nova palavra
frase = frase.replace('Python', 'Android')
print(frase)
# para que eu modifique a string devo fazer a atribuição como no exemplo acima

frase = 'Curso em Video Python'
print(frase.lower().find('video'))
# imprima a frase toda em minuscula e encontre 'FIND' e palavra video. find mostra em qual posição na
# string esta.

frase = 'Curso em Video Python'
dividido = (frase.split())
print(dividido)
# Split faz a divisão de cada palavra se tornar uma string separadamente
# imprimindo separadamente
print(dividido[0])
# imprimindo a string de posição 0
print(dividido[2][3])
# pega a string de posição 2 e mostre a letra 3

