""" 
   Escreva um programa que receba três variáveis (a, b e c), com valores -4, 12 e 79,
respectivamente, e determine se:
   Autor: Caique Manochio
   Data: 01/04/2024_
"""

a = int(input("Digite um número: "))
b = int(input("Digite um segundo número: "))
c = int(input("Digite um terceito número: "))

# como reslvar o TypeError: '>' not supported between instances of 'int' and 'complex'

#a) ((a>a<b) and (not(a > b < a)) or (a>a<b) or (not(a > b < a)) or not(1==1))
alternativa_a = ((a > a < b) and (not(a > b < a)) or (a > a < b) or (not(a > b < a)) or not(1 == 1))

#b) ((a<b) and (not(a > b < a)) or (a>a<b) or (not(a > b < a)) or not(1==1)) and (not(1>a**(1/2)))
alternativa_b = ((a < b) and (not(a > b < a)) or (a > a < b) or (not(a > b < a)) or not(1 == 1)) and (not(1 > a**(1/2)))

print(f"A respostas para cada alternativa são:\n a: {alternativa_a}\n b: {alternativa_b}")
