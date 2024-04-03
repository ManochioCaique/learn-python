"""Escreva um programa em Python que retorne o menor elemento da lista e sua posição
    Autor: Caique Manochio 
    Data: 03/04/2024"""

numeros = [5,15,3,67,8,9,1,7,4,100,97,47,2,72]

mim = 200

for i in numeros:
    i =int(i)
    if i < mim:
        mim = i
        posicao = numeros.index(mim)

print(f"O item de menor valor da lista é {mim}, e esta na posição {posicao} da lista ")
