# 010 Crie um programa que leia quando dinheiro uma pessoa tem na carteira e mostre quando dolares ela pode comprar.

din = float(input('Digite quando tem de dinheiro em sua Carteira:'))
dol = din / 3.27

print('Com R$ {} Reais, voce conseguirar comprar U$ {:.2f} Dólares.'.format(din, dol))

