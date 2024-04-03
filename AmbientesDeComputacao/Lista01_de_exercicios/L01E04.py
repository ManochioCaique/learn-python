'''
Escreva um programa que receba duas variáveis (a e b), com valores 10 e 7, respectivamente,
e determine se: 
Autor: Caique Manochio
Data: 01/04/2024_
'''
x = int(input("Digite um número: "))
y = int(input("Digite um segundo número: "))
#Considere x como a e y como b

#a. a > b
A = x > y

#b. (a * a) > b²
B = (x*x) > (y**2)

#c. (b * a) <= a²
C = (y*x) <= (x**2)

#d. 2+5(a * a)-10 > a*b²
D = ((2 + 5)*(x * x) -10) > (x * (y**2))

print(f"O resultado para cada uma é: \nA: {A} \nB: {B} \nC: {C}\nD: {D}")





