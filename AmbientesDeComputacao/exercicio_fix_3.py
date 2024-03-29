'''
Título: Comparando sentença 
Função: Verifica quais das expressões são verdadeira ou falsa

'''
x = int(input("Digite um número: "))
y = int(input("Digite um segundo número: "))

A = x > y

B = x < y 

C = x >= y

D = x != y

E = (x*x) > (y**2)

F = (y*x) <= (x**2)

G = ((2 + 5)*(x * x) -10) > (x * (y**2))

print(f"O resultado para cada uma é: \nA {A},\nB {B},\nC {C}\nD {D}\nE {E}\nF {F}\nG {G}")