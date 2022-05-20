'''tempo = int(input('Quantos anos tem seu carro ?'))
if tempo <= 3:
    print('Seu carro é praticamente um semi-novo.')
else:
    print('Seu carro esta começando a ficar velho.')
print('--FIM--')'''

# IF simplificado
'''
tempo = int(input('Quantos anos tem seu carro ?'))
print('carro novo' if tempo >= 3 else 'carro velho')
print('--FIM--')'''
# Utilizando a estrutura de condições simples, somente com o IF
# Se utilizar o Else torna-se uma estrutura de condição composta
'''
nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo voce tem!')
print('Bom dia, {}!'.format(nome))'''  # Estutura simples

'''
# Estrutura composta
nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome lindo voce tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))
'''
'''
# Condições simples.
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format((m)))
print('PARABENS' if m >= 6 else 'ESTUDE MAIS !')
'''

'''
# Condições compostas
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format((m)))
if m >= 6:
    print('PARABENS, voce obteve uma excelente média')
else:
    print('Sua média foi ruim, estude mais!')
'''

# Condições compostas

'''    
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2)/2
print('A sua média foi {:.1f}'.format((m)))
if m >= 7:
    print('Parabens voce obteve uma excelente média')
elif m == 5 and m < 7:
    print('Voce pode fazer melhor!!')
else:
    print('Corre, se não vai repetir de ano!!')
'''