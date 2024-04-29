"""
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
    Autor: Caique Manochio
    Data: 11/04/2024_

"""
#Pegando o numero do raio 
raio = int(input("Digite o valor do raio em centimetros: "))
#Valor da constante pi 
PI = 3.14
#Formula que calcula a area de um circulo 
area = (PI * (raio**2))
#Mostra o resultado na tela 
print(f"A area do circulo é {area} cm²")
