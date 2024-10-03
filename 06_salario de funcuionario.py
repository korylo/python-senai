"""
#Titulo: salario de funcionario.
# autor: waldson korylo
# data: 24/09/2024

 descrição: Faça um programa que receba o salario de um funcionario, calcule e mostre o novo
salario,sabendo-se que este sofre um aumento de 25%.
"""
#entrada de dados
salario_atual = float(input ('Inserir o salário atual:'))

#processamento de dados
novo_salario = salario_atual *1.25


#saida de dados
print(f'seu novo salário sera de {novo_salario}')