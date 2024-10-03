"""
#Titulo: mês por extenso.
# autor: waldson korylo
# data: 24/09/2024

#descrição: Faça um programa que receba o mês em número e apresente-o por extenso.
"""
#entrada de dados
# receo valor pelo usuario e converto para inteiro
mes =int(input('inseriro  numero do  mês:'))

#processamento de dados
if mes == 1:
    mes_extenso = "janeiro"
elif mes == 2:
    mes_extenso = "fevereiro"
elif mes == 3:
    mes_extenso = "março" 
elif mes == 4:
    mes_extenso = "abril"
elif mes == 5:
    mes_extenso = "maio"
elif mes == 6:
    mes_extenso = "junho"
elif mes == 7:
    mes_extenso = "julho"
elif mes == 8:
    mes_extenso = "agosto"
elif mes == 9:
    mes_extenso = "setembro"
elif mes == 10:
    mes_extenso = "outubro"
elif mes == 11:
    mes_extenso = "novembro"
elif mes == 12:
    mes_extenso = "dezembro"
else: 
    mes_extenso = 'mes não existe'  

#saida de dados
print(mes_extenso)

# No Python, o comando else é executado quando nenhuma das condições anteriores (if ou elif) for verdadeira. 
# A estrutura if-else é uma estrutura condicional que permite que um programa tome decisões com base em condições específicas. A gramática geral é:
# if(condição){ faça isso } else {faça aquilo} 