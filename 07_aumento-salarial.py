"""
#Titulo: aumento salarial.
# autor: waldson korylo
# data: 24/09/2024

descrição: Faça um programa que receba o salário de um funcionário, calcule e mostre o novo
         salário, sabendo-se que:
Salário< R$ 1000,00 aumento de 25%.
Salário >= R$ 1000,00 e < R$ 2000,00 aumento de 15%.
Salário >= R$ 2000,00 aumento de 10%.
"""
#entrada de dados
salario = float(input ('Digite  o salário:'))

#procedimentos de dados
if salario < 1000:
    salario_reajuste = salario *1.25

if salario >= 1000 and salario <2000:
    ajuste = salario *0.15

    salario_reajuste = salario + ajuste

if salario < 2000:
   salarioa_ajuste = salario *1.1 

#saida de dados
print("Seu novo salario:", salario_reajuste)