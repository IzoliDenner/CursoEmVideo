#013 faça um algoritmo que leia o salario de um funcionario e mostre seu novo salario com 15% aumento.

salario = float(input('Digite seu Salario atual para Calculo do aumento disponivel: '))
aumento = salario + (salario * 15 /100)
print('Voce ganhava R$ {} tera um aumento de 15%, seu novo salario é de R$ {}.'.format(salario, aumento))


