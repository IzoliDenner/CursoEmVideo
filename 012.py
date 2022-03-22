#012 Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preço = float(input('Digite o preço atual para calcularmos o desconto: R$ '))
desconto = (preço * 5) / 100

print('O valor do desconto de 5% é de: R$ {} e o novo valor do produto é R$ {}'.format(desconto, preço - desconto))


