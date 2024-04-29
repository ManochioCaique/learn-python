"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o
usuário.
    Autor: Caique Manochio
    Data: 11/04/2024_

"""
#Pegando a medida de uma lado do quadrado
lado = int(input("Digite o quadrado em centimetro: "))

#Calculando a area do quadrado em cm²
area = lado**2

#calculando o dobro da area 
dobro = area * 2

#printando a valor na tela
print(f"O dobro da area é {dobro}")