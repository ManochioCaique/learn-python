"""
   Agora, escreva um programa que receba três variáveis (a, b e c), com valores 18, 4 e 3,
respectivamente, e determine se:
   Autor: Caique Manochio
   Data: 01/04/2024_
"""
a = int(input("Digite um número: "))
b = int(input("Digite um segundo número: "))
c = int(input("Digite um terceito número: "))

#a) (a+b+c < a*c*b) or (1==1)
alternativa_a = (a + b + c < a * b * c) or (1 == 1)

#b) (a+b+c < a*c*b) and (1==1)
alternativa_b = (a + b + c < a * b * c)  and (1 == 1)

#c) (a>a<b) and (not(a > b < a))
alternativa_c = (a > a < b) and (not(a > b < a))

#d) (a>a<b) or (not(a > b < a))
alternativa_d = (a > a < b) or (not (a > b < a))

print(f"A respostas para cada alternativa são:\n a: {alternativa_a}\n b: {alternativa_b}\n c: {alternativa_c}\n d: {alternativa_d} ")
