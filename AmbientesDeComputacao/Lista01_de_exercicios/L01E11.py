"""
Escreva um programa em que calcule o diâmetro, a circunferência e a área de um círculo.
O programa deve receber como entrada uma variável com o valor do raio. Considere Pi como
3,14. Teste com o valor 10.
Autor: Caique Manochio 
Data: 01/04/2024
Considere:
r = raio
pi =  valor de Pi
circuferencia = circuferecia 
d = diametro 
area
"""
#Recebendo o valor de raio do usuário
r = float(input("Digite o valor do raio: "))

#Valor de pi
pi = 3.14

#Calcular diametro
d = 2 * r

#Calcular  o circuferencia
circuferencia =  2 * pi * r 

#Calcular a area 
area = pi * (r**2)

print(f" A área é {area}\n A circuferência é {circuferencia}\n O diâmetro é {d}")