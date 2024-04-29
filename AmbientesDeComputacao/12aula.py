'''
Título: 12ª aula
Função: Anotações da aula
Autor: Caique Manóchio
Data: 24/04/2024

'''
#beecroed PA 
#Topicos avançados em dados seuqencias
""" Compreensão de lista é um recurso da linguegem que permiyte  manipulçaõ de lista.  com redução de lista
Lista =[VARIAVEL LAÇO CONDIÇÃO]
"""
lista = []
for i in range(10):
    lista.append(i**2)

print(lista)
#de forma melhor
lista2 = [i**2 for i in range(10)]

lista_impar = []
for i in range(100):
    if i%2 == 1:
        lista_impar.append(i)

print(lista_impar)
#Variavel laço condicional 
lista_impar = [i for i in range(100) if i % 2 == 1]

#converta a lista de strng  em interros
lista_string = ["1", "2", "3"]
print(lista_string)
lista_int = []
for i in lista_string:
    a = int(i)
    lista_int.append(a)

#de outra maneira mais  rapida
lista_int = [int(i) for i  in lista_string]
print(lista_int)

#Exercicios somar duas lista 
a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]

soma = []
try:
    for i in range(len(a)):
        soma.append(a[i] + b[i])
    print(soma)

except:
    print("Erro: lista de tamanhos diferentes")


#if len(a) == len(b): 
soma = [a[i] + b[i] for i in range(len(a)) if len(a) == len(b)]

if soma: print(soma)
else: print("listas de tamanhos diferentes")
#usando o zip
soma = [i + j for i,j in zip(a, b)]


#Enumeração  
#enumerate forma de navegar pela lista e atribuir um indici para
lista = ["bola", "casa", "abacate"] 
for i, nome in enumerate(lista):
    print(i, ":", nome, sep = "")

#Retorna uma tupla  


#Função de compactação zip pega duas listas de mesmo tamanho e juntas as duas juntos, 
#sendo que o output vai se tuplas   
lista = ["bola", "casa", "abacate"]
indice = ["A", "B", "C"]
unidos = zip(indice, lista)
for i in unidos:
    print(i)

a = [1, 2 ,3]
b = [5, 6, 6]
c = [9, 7, 6]
for i, j, k in zip(a, b, c):
    print(i, j, k)

#Função filter() recebe um lista e filtra com base em outra função.
def pares(i):
    if i % 2 == 0:
        return i 
    
lista = [1, 2, 2, 3, 4, 8, 9, 8, 7, 10, 11, 16]
    
lista_somente_pares = filter(pares, lista)
print(list(lista_somente_pares))

#função map(), mapear para cada um dos elementos de ua deterinada lista a esta função 
def dobro (x):
    return x*2 
    
lista = [1, 2, 2, 3, 4, 8, 9, 8, 7, 10, 11, 16]
    
valores_dobrados = map(dobro, lista)
print(list(valores_dobrados))

#Função reduce recebe uma lista de valores e retorna apenas um valor
from functools import reduce

def soma(x, y):
    return x + y 
    
lista = [1, 2, 2, 3, 4, 8, 9, 8, 7, 10, 11, 16]
    
resultado = reduce(soma, lista)
print(resultado)

print(resultado/len(lista))


