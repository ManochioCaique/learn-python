"""Escreva um programa em Python que retorne o maior elemento da lista e sua posição
    Autor: Caique Manochio
    Data: 03/04/2024
"""
numeros = [5,15,3,67,8,9,1,7,4,100,97,47,2,72]
#Variavel auxiliar
max = 0
#For para  checar cada elemento da lista
for i in numeros:
    i =int(i)
    #condição que verifica qual valor é maior 
    if i > max:
        max = i
        #verifica qual a posição da variavel max e armazena na variavel posicao 
        posicao = numeros.index(max)

print(f"O item de maior valor da lista é {max}, e esta na posição {posicao} da lista ")
