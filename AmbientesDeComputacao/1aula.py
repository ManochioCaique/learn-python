'''
Título: 1ª aula
Função: Anotações da aula
Autor: Caique Manóchio
Data: 13/03/2024

'''
print("Hello World!")
#Funções em python sempre tem os parentes  ()


#operações matemáticas
print(2+2)

print(2-5)

print(4**2)

#Raiz quadrada usando exponenciação

print(4**(1/2))

#Importando modulos para fazer raiza quadrada.  
import math

#from math import sqrt
print(math.sqrt(4))

#VARIÁVEIS  E TIPOS DE DADOS
#Nomear váriavel, não pode começar com número, não poder ter espaço ou hífen, são case sensitive
#operador de atribuição (=)
#Numeros interios 47
#Numerico flutuante 12.855
#Textual "Olá mundo!"
#Booleano True or False
mensagem =  "Olá mundo"
print(mensagem)

#Tipagem forte - não se pode fazer operações com variáveis diferentes.
print(type(mensagem))
v1 = 2
v2="3"
v2 = int(v2)
soma = v1 + v2
print(soma)


####
a = int(input("Digite o valor o valor de a:"))

b = int(input("Digite o valor  de b: "))

soma = a + b 

print("A soam de", a, "com", b, "é", soma)
