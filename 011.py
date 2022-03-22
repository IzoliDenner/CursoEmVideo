# 011 Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta
# necessária para pinta-lo, sabendo que cada litro de tinta pinta uma area de 2m2

largura = float(input('Digita a Largura da parede:'))
altura = float(input('Digita a Altura da parede:'))
area = largura * altura
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m2'.format(largura, altura, area))

tinta = area / 2
print('Para pintar essa parede, voce precisara de: {} lts de tinta'.format(tinta))

