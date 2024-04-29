""" Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da
área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a
tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
o Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3
situações:
o comprar apenas latas de 18 litros;
o comprar apenas galões de 3,6 litros;
o misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e
sempre arredonde os valores para cima, isto é, considere latas cheias.
    Autor: Caique Manochio
    Data: 29/04/2024_
"""

#pegando quantos metros quadrados a serem pintados. 
metros_quadrados = int(input("Quantos metros quadrados você deseja pintar? "))

#Calculando quantos litros de tinta var ser usado
litros_usados = metros_quadrados/6

#Calculando quantas latas de tinta vai ser usada 
latas_usadas = litros_usados/18

#Calculando qual o valor a ser pago pelas latas de tintas
preco_total = latas_usadas * 80

#Calculando quantos galões serão necessário 
galoes_usados = litros_usados/3.6

#Calcular o valor toltal pago em galoes
preco_total_g =  galoes_usados *25

#Calculando os 10% a mais 
dez_porcento = (litros_usados*10)/100

#Calculando valor sem desperticio 
#Litros usados com mais 10%
litros_total = litros_usados + dez_porcento

#Calculando quantas latas de tindas vou precisar
latas_usadas_total = litros_total // 18

#Calculando quanto de tinta sobrou das latas 
litros_sobrando_das_latas = litros_total - (latas_usadas_total * 18)

#Calculando quantos galoes vamos usar 
galoes_usados_total = litros_sobrando_das_latas/3.6
galoes_usados_total = round(galoes_usados_total, 0)

#Calculando os preços que vamos pagar pelas tintas e galoes e os dois juntos 
preco_latas_juntos = latas_usadas_total * 80
preco_galoes_juntos = galoes_usados_total * 25
preco_total_juntos =  preco_galoes_juntos + preco_latas_juntos

#pritnando na tela
print(f"Serão usadas {latas_usadas} latas de tinta e o valor a ser pago é R$:{preco_total} reais\nSerão usadas {galoes_usados} galões de tinta e o valor a ser pago é R$:{preco_total_g} reais\nSerão usadas {latas_usadas_total} latas de tintas e {galoes_usados_total} galões de tinta e e o valor a ser pago é R$:{preco_total_juntos} reais ")

