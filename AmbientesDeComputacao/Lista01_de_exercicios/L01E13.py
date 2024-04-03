"""
    Escreva um programa que receba um número inteiro maior que zero e retorne se ele é par
ou ímpar.
    Autor: Caique Manochio 
    Data: 01/04/2024
"""
x = int(input("Digite um numero maior que 0: "))

if x % 2 == 0:
    print(f"O número {x} é par")
else:
    print(f"Esse número {x} é ímpar")