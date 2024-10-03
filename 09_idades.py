"""
#Titulo:idade.
# autor: waldson korylo
# data: 01/10/2024

#descrição:Escreva um programa que leia a idade de um indivíduo e escreva a faixa etária a que
pertence, de acordo com a tabela abaixo;.
faixa_etária      classificação
<12                 criança
13~17               Adolecente
18^59                Adulto
>60                  Especilista
"""


#entrada de dados
idade = int(input ('digite a idade do usuario'))

# precessamentos de dados 

if idade <=12:
     faixa_etária ='criança'
elif idade >=13 and idade <=17:
     faixa_etária ='adolecente'
elif idade >=18 and idade <= 58:
     faixa_etária ='adulto'
elif idade >=60:
     faixa_etária ='especialista'

#saida de dados 
print(faixa_etária)
    