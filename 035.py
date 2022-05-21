# Exercício Python 35:
# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário
# se elas podem ou não formar um triângulo.

# cada um deles tem que ser menor que a soma do comprimento dos outros dois
print('-*=-' * 20)
print('Analisador de triangulos')
print('-*=-' * 20)

r1 = float(input('Digite o primeiro segmento: '))
r2 = float(input('Digite o segundo segmento: '))
r3 = float(input('Digite o terceiro segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR Triangulos')
else:
    print('Os segmentos acima NÂO PODEM Triangulos')