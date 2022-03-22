#014  Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

gc = float(input('Digite a temperatura em Graus Celsius: '))
gf = gc * 1.8 + 32

print('A temperatude de {}ºC corresponde a {}ºF !'.format(gc, gf))

