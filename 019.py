# 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''
import random
aluno1 = str(input('Digite o Nome do Primeiro Aluno: '))
aluno2 = str(input('Digite o Nome do Segundo Aluno: '))
aluno3 = str(input('Digite o Nome do Terceiro Aluno: '))
aluno4 = str(input('Digite o Nome do Quarto Aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = random.choice(lista)
print('O aluno Escolhido foi: {}.'.format(escolhido))
'''
from random import choice
aluno1 = str(input('Digite o Nome do Primeiro Aluno: '))
aluno2 = str(input('Digite o Nome do Segundo Aluno: '))
aluno3 = str(input('Digite o Nome do Terceiro Aluno: '))
aluno4 = str(input('Digite o Nome do Quarto Aluno: '))
lista = [aluno1, aluno2, aluno3, aluno4]
escolhido = choice(lista)
print('O aluno Escolhido foi: {}.'.format(escolhido))