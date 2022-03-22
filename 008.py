#008 Escrava um programa que leia um valor em metros e o exiba convertido em centimetros e milimetros.

m = float(input('Digite a medida em metros: '))
c =  m * 100
mi = m * 1000

print('{} metros, é igual a {} centimetros e o mesmo que {} milimetros.'.format(m, c, mi))

