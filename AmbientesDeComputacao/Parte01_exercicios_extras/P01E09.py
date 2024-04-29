"""
Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
    Autor: Caique Manochio
    Data: 11/04/2024_

"""
#Pegando o valor da temperatura em celsius
C = int(input("Digite a temperatura em graus celsius: "))

#Conventendo a temperatura em celsius em fahrenheint
F = (C * 1.8) + 32

#Printando o resultado  na tela 
print(f'A temperatura em é {F} graus fahrenheit')