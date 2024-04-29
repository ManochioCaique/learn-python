"""
Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal,
utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) - 58
b. Para mulheres: (62.1*h) - 44.7
    Autor: Caique Manochio
    Data: 11/04/2024_

"""
#Pegando sexo da pessoa
#sexo =  input("Digite seu genero: ")

#Pegando a altura
altura = float(input("Qual sua altura: "))

"""
#Verificando se mulher ou homem  e calculando o peso ideal 
if sexo.lower == "feminino" or "mulher":
    peso_ideal_mulheres = (62.1 * altura) - 44.7
    print(f"Seu peso ideal mulher é {peso_ideal_mulheres}")
else:
    peso_ideal_homem = (72.7 * altura) - 58 
    print(f"Seu peso ideal é {peso_ideal_homem}")
"""
#Calculando para homem (pergunta a )
peso_ideal_homem = (72.7 * altura) - 58 


#Calculando para mulher
peso_ideal_mulheres = (62.1 * altura) - 44.7


print(f"Se você for mulher o seu peso ideal é {peso_ideal_mulheres}\nSe você for homem seu peso ideal é {peso_ideal_homem}")