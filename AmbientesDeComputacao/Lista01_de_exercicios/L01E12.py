"""_
    Escreva um programa que calcule o resultado de uma equação de segundo grau. Realize
controle de exceções para verificar se delta é menor que zero.
    Autor: Caique Manóchio 
    Data: 01/04/2024
    """

#Recebendo os valores da equação
a = int(input('Digite o termo a da equação: '))
b = int(input('Digite o termo b da equação: '))
c = int(input('Digite o termo c da equação: '))

#Calculando o delta
delta = (b**2) - 4 *(a * c)

#Estrutura condicional para calcular a raiz de delta
if delta > 0:
    x1 = ((-b) - (delta**(1/2)))/(2 * a)
    x2 = ((-b) + (delta**(1/2)))/(2 * a)
    print(f"O valor de delta é: {delta}. possui duas raizes reias\n o valor de x1 é: {x1}\n o valor de x2 é: {x2}\n ")
elif delta == 0:
    print(f"O valor de delta é zero, logo possui apenas uma raiz real")
else:
    print(f"O valor de delta é negatvo, logo não possui raiz real. Valor de delta: {delta}")