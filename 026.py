# Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
# em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite a frase desejada: ... ')).upper().strip()

# Upper deixa o texto todo em maiusculo corrigindo a possibilidade de o
# usuario digitar o texto. Strip tira todos os possiveis espaços digitados pelo usuario

print('A letra A aparece {} vezes na frase'.format(frase.count('A')))
print('A primeira letra A apareceu na posição {} '.format(frase.find('A')+1))
print('A ultima Letra A aparecei na posição {}'.format(frase.rfind('A')+1))