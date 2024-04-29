""" Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o
Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
a. salário bruto.
b. quanto pagou ao INSS.
c. quanto pagou ao sindicato.
d. o salário líquido.
e. calcule os descontos e o salário líquido, conforme a tabela abaixo:
    Autor: Caique Manochio
    Data: 24/04/2024_
"""
#Perguntando quantas horas trabalhadas e valor da hora por mes
valor_hora = int(input("Qual o valor da hora trabalhada? "))
horas_trabalhadas = int(input("Quantas horas vc trabalhou no mês? "))

#Salario bruto
salario_bruto =  valor_hora * horas_trabalhadas

#Quando pagou a INSS
valor_INSS = (salario_bruto * 8)/100

#Quando pagou ao sindicato 
valor_sindicato = (salario_bruto * 5 )/100

#Quando pagou de imposto de renda
valor_imposto_renda = (salario_bruto * 11)/100

#Quanto de saláario liquido
salario_liquido = salario_bruto - (valor_imposto_renda + valor_sindicato + valor_INSS) 

print(f"Salário bruto: R${salario_bruto}\nIR (11%): R${valor_imposto_renda}\n INSS (8%): R$:{valor_INSS}\nSindicato (5%): R$:{valor_sindicato}\nSalário lquído: R${salario_liquido}")