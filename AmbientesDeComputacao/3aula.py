'''
Título: 3ª aula
Função: Anotações da aula
Autor: Caique Manóchio
Data: 20/03/2024

'''
#comando condicionais

'''
if condição:
    comando 
'''
#declaração de variáveis
x = 1

y = 2

#estruta condicional
if  y > x:
    print("Condição atendida")

#Identação hierárquica
    
c1, c2, c3, c4, c5, = True, True, True, True, True
if  c1:
    if c2:
        if c3:
            if c4:
                if c5:
                    print("Olá mundo")


c1, c2, c3, c4, c5, = True, True, False, False, True
if  c1:
    if c2:
        if c3:
            if c4:
                print("Nada Aqui")
        if c5:
            print("Olá mundo")

x = 1

y = 2

#else
if  y > x:
    print("x maior que  y")
else:
    print("y maior que x")


x = 2

y = 2

#elif
if  y > x:
    print("x maior que  y")
elif x < y:
    print("x menor que y")
else:
    print("x igual a y")

#Lição de casa
#Descobrir se switch existe em python

#Operados lógicos
    #and
    #or
    #not

#AND
x = 7
y = 38
z = 9

if x < y and z > x:
    print("True")
else:
    print("False")

#OR
x = 7
y = 38
z = 9

if x < y or z == x:
    print("True")
else:
    print("False")

#NOT
