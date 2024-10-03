"""
#Titulo: Calcular média
# autor: waldson korylo
# data: 19/09/2024

# descrição: faça um algaritmo que um valor na moeda real (R$),
# a cotação da conversão REAL para DOLAR, e apresente 
# a quantidade desse valor em dólar ($)

# Exemplo de execução
# insira o valor em real: 5000
# Insira cotação do dia: 5
# 5000,00 equivalem $1000,00

"""
#comentario em linha 

#entrada de dados
moeda_real_string = input ('inserir o valor em R$:')
cotacao_dia_string = input ('insirir o valor da cotação:')

#processamento de dados
moeda_real = int (moeda_real_string)
cotacao_dia =int (cotacao_dia_string)
moeda_dolar = moeda_real/ cotacao_dia

#saida de dados
print(f'R$ {moeda_real} equivalem $ {moeda_dolar}') #format
print('R$ ' + str(moeda_real) + 'equivalem $ ' + str(moeda_dolar))