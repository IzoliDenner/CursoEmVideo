# Exercício Python 31:
# Desenvolva um programa que pergunte a distância de uma viagem em Km.
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
# e R$0,45 parta viagens mais longas.

#  1º maneira
'''
km = float(input('Digite a disância da viajem a ser percorrida: '))
if km <= 200:
    preco = 0.50 * km
    print('Voce percorrerá {:.2f}km e sua passagem custará R${:.2f}.'.format(km, preco))
else:
    preco = 0.45 * km
    print('Voce percorrerá {:.2f}km e sua passagem custará R${:.2f}.'.format(km, preco))
'''

# condição simplificada
distancia = float(input('Qual é a distancia da sua viagem ? '))
print('Voce esta prestes a começar uma viagem de {}km .'.format(distancia))
preço = distancia * 0.50 if distancia <= 200 else distancia * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))