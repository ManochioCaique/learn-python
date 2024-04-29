"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês.
    Autor: Caique Manochio
    Data: 11/04/2024_

"""

#Pegando a valor da hora trabalhada
valor__hora_trabalhada = int(input("Qual valor da hora trabalhada? "))

#Pegando a quantidade de horas trabahada
horas_trabalhadas = int(input("Quantas horas você trabalhou no mês? "))

#Calculando a valor total do salario do mes 
salario_do_mes = valor__hora_trabalhada * horas_trabalhadas

#printando o salaro 
print(f"O seu salário trabalhado é {salario_do_mes}")