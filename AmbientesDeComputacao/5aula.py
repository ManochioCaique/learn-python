'''
Título: 5ª aula
Função: Anotações da aula
Autor: Caique Manóchio
Data: 27/03/2024

'''
#String é um tipo de dado que armazena uma coleção de caracteres (texto)

#concatenação
v1 = "Olá"
v2 = "Mundo!"
concatenacao = v1 + v2
print(concatenacao, "\n")

#len(seq) vai contar a quantidade de caracteres na seq
#sorted() ordenar uma lista 
#lista.sort()
# Pegar alguma valor de uma string nome[0]
#para conseguir exibir o valor por final nome[-1]
#Para extrair uma parte seq[1:4]


# Desaio dos coelhos 
'''
Cada par de coelhos tinhas  1 par  de flhos por dia 
filhos levaram 1 dia para se tornar reprodutivos 
Crie um programa  que calcule  quanto tempo nós sobrevivemos 
cada vai 1 + reproduzir
'''
CO = 1 #Coelhos Ontem
CH = 1 #Coelhos Hoje
CA = 2 #Coelhos Amanha 
dia = 2

while CH < 15:
    CA = CH + CO
    dia = dia + 1 
    CO = CH
    CH = CA 
    print("Dia: ", dia, "Coelhos Zumbis: ", CH)
print("Morremos no dia ", dia)


