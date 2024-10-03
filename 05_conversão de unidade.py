"""
#Titulo: convensão da unidade.
# autor: waldson korylo
# data: 24/09/2024

# descrição: faça um programa que recebe um numero em pés,faça conversões 
a seguir mostra os resultados.

- polegadas;
-jardas;
-milhas;
sabe-se que:

1 pé = 12 polegadas;
1 jarda = 3 pés;
1 milha = 1.760 jada;

"""
#comentario em linha 

#entrada de dados
pes = int(input ('inserir o valor em pés:'))

#processamento de dados
polegadas = pes*12
jardas = pes /3
milhas = jardas /1760




#saida de dados
print('polegadas:', polegadas)
print('jardas:', jardas)
print('milha',milhas)