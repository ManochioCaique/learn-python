"""
    Escreva um programa em Python que imprima o primeiro e o último item.
    Autor: Caique Manochio
    Data: 02/04/2024
"""
#Lista para ser usadas
numeros = [5,15,3,67,8,9,1,7,4,100,97,47,2,72]


n = len(numeros)

#Primeiro item
primeiro = numeros[0]

#ultimo item  
ultimo = numeros[n - 1]


print(f"O primeiro item da lista é {primeiro} e o último item da lita é {ultimo}")