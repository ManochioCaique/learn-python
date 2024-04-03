"""
    Escreva um programa em Python que retorne a primeira e a última letra da variável “mensagem”
    Autor: Caique Manochio
    Data: 03/04/2024
"""
#Varialvel usada 
mensagem = "Eu amo Python"

#Primeira letra da variavel
primeira = mensagem[0]

#ultima letra
n = len(mensagem)

ultima = mensagem[n-1]

print(f'A primeira letra da variavel mensagem é "{primeira}" e ultima letra é "{ultima}"')