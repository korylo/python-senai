"""
#Titulo:idade.
# autor: waldson korylo
# data: 01/10/2024

  #descrição: Faça um programa para exibir a ocupação de um funcionário a partir de seu código de
profissão, de acordo com a tabela abaixo;

Código de Profissão              Ocupação
1                              Matemático
2                            Analista de Sistemas
3                                 Físico
4                                Arquiteto
5                             Piloto de Aeronaves
"""

#entrada de dados
codigo = int(input ('insira o codigo de  profissão'))

#processamento de dados
if codigo == 1:
    codigo = 'Matemático'
elif codigo == 2:  
    cogigo = 'Analista de Sistema' 
elif codigo == 3:
    codigo = 'fisico'   
elif codigo == 4:
    codigo = 'arquiteto'
elif codigo == 5:
    codigo = 'piloto de aeronave'    




#saida de dados
print(codigo)