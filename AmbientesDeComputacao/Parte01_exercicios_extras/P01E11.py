"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal,
usando a seguinte fórmula: (72.7*altura) - 58
    Autor: Caique Manochio
    Data: 11/04/2024_

"""
#Pegando a altura
altura = float(input('Digite sua altura: '))

#Calculando o peso ideal segundo a formula dada
peso_ideal = (72.7 * altura) - 58

#Printando  o peso ideal
print(f"O peso ideal para sua altura é {peso_ideal} kg")