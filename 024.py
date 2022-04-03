#Exercício Python 024:
# Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
#1 º maneira
'''cid = str(input('Onde voce nasceu: '))
print(cid[:5] == 'Santo')'''

cid = str(input('Onde voce nasceu: ')).strip()
print(cid[:5].upper() == 'SANTO')

# desta maneira, utilizando o strip tiramos os possivies espaços que o usuario poderia colocar
# e o upper faz com que deixa tudo maiusculo, fazendo assim confirmar o nome Santo independente da menira
# que foi digitado pelo usuario