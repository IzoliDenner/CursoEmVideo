'''Metodo

replace : serve para modificar palavra encontrada na str exm

frase = 'Curso em video Python
frase.replace('Python', Android)

vai encontrar onde tem python e modificar por android

upper : vai deixar toda a string maiuscula
lower : vai deixar toda a string minuscula
capitalize : ele vai jogar toda a string para minusculos, e vai deixar sempre a primeira palavra Maiusculos
tittle : parecido, porem vai deixar maiuscula a primeira letra de cada palavra
strip : remove todos os espaços inuteis no começo e no fim da string
rstrip : remove somente os ultimos espaços inuteis (direita)
lstrip : remove somente os primeiros espaços inuteis (esquerda)
split : ele faz a divisão da string, cada palavra se torna um indice independente
join : ao contrário, ele faz uma junção das palavras para se tornar apenas um indice
'''

'''frase = 'Curso em Video Python'
print(frase.upper().count('O'))'''

'''frase = '   Curso em Video Python   '
print(len(frase.strip()))'''

'''frase = 'Curso em Video Python'
print(frase.replace('Python', 'Android'))'''

'''frase = 'Curso em Video Python'
print(frase.lower().find('video'))'''

frase = 'Curso em Video Python'
dividido = (frase.split())
print(dividido[2][3])