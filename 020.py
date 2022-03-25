# 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos
# dos alunos. Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle
aluno1 = str(input('Digite o Nome do Primeiro Aluno: '))
aluno2 = str(input('Digite o Nome do Segundo Aluno: '))
aluno3 = str(input('Digite o Nome do Terceiro Aluno: '))
aluno4 = str(input('Digite o Nome do Quarto Aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
shuffle(lista)
print('A ordem de apresentadação será: {}.'.format(lista))