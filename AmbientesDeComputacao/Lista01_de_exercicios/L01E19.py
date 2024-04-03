"""Escreva um programa que transforme o texto apresentado em uma lista de palavras.
    Autor: Caique Manochio 
    Data: 03/04/2024"""

#Varialvel usada 
mensagem = "Eu amo Python"


#criando lista com cada palavra
mensagem_lista = mensagem.split()

print(f"O texto apresentado transformado em lista fica:\n {mensagem_lista}")
#Criando um lista com as letras

#Tirando os espaços entre as palavras
mensagem_sem_espacos = mensagem.replace(" ", "")
#criando um lista vazia para armazenas os elementos
lista_por_letra = []

for i in mensagem_sem_espacos:
    letra = i
    lista_por_letra.append(letra)

print(f"E uma lista com letras aqui:\n{lista_por_letra}")