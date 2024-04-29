""" Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a
tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de
tinta a serem compradas e o preço total.
    Autor: Caique Manochio
    Data: 29/04/2024_
"""
#pegando quantos metros quadrados a serem pintados. 
metros_quadrados = int(input("Quantos metros quadrados você deseja pintar? "))

#Calculando quantos litros de tinta var ser usado
litros_usados = metros_quadrados/3

#Calculando quantas latas de tinta vai ser usada 
latas_usadas = litros_usados/18

#Calculando qual o valor a ser pago pelas latas de tintas
preço_total = latas_usadas * 80

#pritnando na tela
print(f"Serão usadas {latas_usadas} latas de tinta e o valor a ser pago é R$:{preço_total} reais")
