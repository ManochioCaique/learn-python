"""Escreva um programa que transforme o texto apresentado em uma lista de palavras.
    Autor: Caique Manochio 
    Data: 03/04/2024"""

#Varialvel usada 
mensagem = "Eu amo Python"

mensagem_sem_espacos = mensagem.strip()

mensagem_lista = mensagem_sem_espacos.split()

print(f"O texto apresentado transformado em lista fica:\n {mensagem_lista}")