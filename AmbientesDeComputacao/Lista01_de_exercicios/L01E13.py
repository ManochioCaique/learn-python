"""
    Escreva um programa que receba um número inteiro maior que zero e retorne se ele é par
ou ímpar.
    Autor: Caique Manochio 
    Data: 01/04/2024
"""
#Armazenando a entrada do usuario
x = int(input("Digite um numero maior que 0: "))
#Condiçaõ para verificar se par ou impar
#% modulo da o resto da divisao
if x % 2 == 0:
    print(f"O número {x} é par")
else:
    print(f"Esse número {x} é ímpar")