"""
    Exercicios sobre listas
    Autor: Caique Manochio
    Data: 03/04/2023
"""

lista = [3, 7, 4, 12, 15, 5, 1]
contador = 0
for i in lista:
    contador += 1

lista_tamanho = contador
print(f"o tamanho da lista é: {lista_tamanho}")

maior = float("-inf")  
for i in lista:
    i = int(i)
    if i > maior:
        maior = i
        posicao = lista.index(maior)

print(f"O maior item da lista é: {maior}\n e a sua posição é: {posicao}")

menor = float("inf")


#For para verificar cada elemento da lista 
for i in lista:
    i =int(i)
    #Condiçao que vai chegar e manter apenas o elemento de menor valor 
    if i < menor:
        menor = i
        #verifica qual a posição do valor mim e armazena na variavel posição 
        posicao = lista.index(menor)

print(f"O menor item da lista é: {menor}\n e a sua posição é: {posicao}")