""" 
   Escreva um programa que receba dois números e mostre qual deles é o maior. Teste com os
valores 0.918259123 e 0.012412
   Autor: Caique Manochio 
   Data: 01/05/2024

"""
#Recebendo os valores dos usuarios
valor_um = float(input("Digite um valor: "))

valor_dois = float(input("Digite um outro valor: "))

resultado = valor_um > valor_dois


if resultado == True:
    print(f"O maior valor é: {valor_um}")
else: 
    print(f"O maior valor é: {valor_dois}")