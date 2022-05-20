# Escreva um programa que faça o computador "pensar" em um numero inteiro entre 0a5
# e peça para o usuário tentar descobri qual foi o numero escolhido pelo computador
# o programa devera escrever na tela se o usuario ganhou ou perdeu

from random import randint
from time import sleep

computador = randint(0, 5)
print('-*-' * 20)
print('Vou pensar em um número de 0 a 5. Tente descobrir !!!')
print('-*-' * 20)
jogador = int(input('Em que número eu pensei? '))  # o Jogador tenta advinhar.
print('PROCESSANDO...')
sleep(2)
if jogador == computador:
    print('Parabens !! Voce acertou')
else:
    print('Ganhei, pensei no número {} e não no número {} como voce informou. '.format(computador, jogador))
