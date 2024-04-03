"""Escreva um programa em Python que retorne o menor elemento da lista e sua posição
    Autor: Caique Manochio 
    Data: 03/04/2024"""

numeros = [5,15,3,67,8,9,1,7,4,100,97,47,2,72]
#Variavel auxiliar
mim = 200
#For para verificar cada elemento da lista 
for i in numeros:
    i =int(i)
    #Condiçao que vai chegar e manter apenas o elemento de menor valor 
    if i < mim:
        mim = i
        #verifica qual a posição do valor mim e armazena na variavel posição 
        posicao = numeros.index(mim)

print(f"O item de menor valor da lista é {mim}, e esta na posição {posicao} da lista ")
