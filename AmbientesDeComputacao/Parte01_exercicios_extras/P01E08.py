"""
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em
graus Celsius.
o C = 5 * ((F-32) / 9).
    Autor: Caique Manochio
    Data: 11/04/2024_

"""
#Pegando o temperatura em Fahrenheit
F = int(input("Dgite o valor da temperatura Fahrenheit: "))

#Calculando a temperatura em Celsius
C = 5 * ((F -32) / 9 )

#Printando a temperatura em Celsius
print(f"A temperatur é {C} graus celsius")