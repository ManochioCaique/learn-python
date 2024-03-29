'''
Título: Verificar pares, impar, multiplos de 7 
Função: Printar na tela os numeros pares, impar e mutiplos de 7 de 0 a 100
data: 25/03/2024
Autor: Caique Manóchio
'''
listas = range(101)

for i in listas:
    print(i)

for i in listas:
    if i % 2 == 0:
        print(i, end=',')

print("\nFIM")
 
for i in listas:
    if i % 2 == 1:
        print(i, end=',')

print("\n FIM")

for i in listas:
    if i%7 == 0 and i > 0:
        print(i, end=',')



