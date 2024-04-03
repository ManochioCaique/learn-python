"""
   Escreva um programa que receba três variáveis (a, b e c), com valores 10, 14 e 7,
respectivamente, e determine se:
   Autor: Caique Manochio
   Data: 01/04/2024_
"""
a = int(input("Digite um número: "))
b = int(input("Digite um segundo número: "))
c = int(input("Digite um terceito número: "))

#a) a > b and a*2 < c

alternativa_a = a > b and (a*2) < c 

#b) a*5 < c**2 or a ==b

alternativa_b = (a*5) < (c**2) or a == b 


#c) not(b >= c*2 and a <= c+3)

alternativa_c = not (b >= (c*2) and a <= (c+3))

#d) (a**2 < c **(1/2) and (a>b+c))
alternativa_d = (a**2 < c**(1/2) and (a > b + c))

print(f"A respostas para cada alternativa são:\n a: {alternativa_a}\n b: {alternativa_b}\n c: {alternativa_c}\n d: {alternativa_d} ")