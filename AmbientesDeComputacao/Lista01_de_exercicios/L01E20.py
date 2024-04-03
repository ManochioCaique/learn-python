"""Escreva um programa que extraia do texto apenas a palavra Python
    Autor: Caique Manochio
    Data: 03/04/2024
"""

#Varialvel usada 
mensagem = "Eu amo Python"

#Criando uma lista com da string 
mensagem_lista = mensagem.split()
#Vendo o tamnho da lista 
n = len(mensagem_lista)
#Extraindo a palavra Python
texto_extraido = mensagem_lista[n-1]
print(f'Aqui esta a palavra pedida:\n {texto_extraido}')