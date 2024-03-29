'''
Título: 4ª aula
Função: Anotações da aula
Autor: Caique Manóchio
Data: 25/03/2024

'''
#Estruturas de repetição.
"""
           Organizar os script em github, ou diretorios.
           Descri das aulas. 
           Sempre colcoar  nome do autor, data e outras coisa.
"""
#WHILE
#Repetir um bloco de codigos enquanto for verdadeira.

i = 0 
while i <5:
    print(i)
    i +=1

#Forma reduzida (+=, -=, *= e /=)
#FOR
#Usado para percorrer lista.
 
for i in [1, 2, 3]:
    print(i)

for i in range(8):
    print(i)

#range 
#função retorna valores entre as condições pedidas, como se fosse uma lista.

um = range(3)  #Vai criar um objeto que retorna um 0, 1, 2
dois = range(1,3) #Dois numeros o primeiro onde o começa os numeros retornos e o segundo o final onde nao inclui o numero final
tres = range(0, 10, 2) #O terceiro numero é o intervalo que vai charmar 

for i in um:
    print(i, end=',')
print("\n")
#Usando dois argumentos na função  range
for i in dois:
     print(i, end=',')
print("\n")
#Usando tres argumentos no range 
for i in tres:
     print(i, end=',')

print("\n")
#Usando float na função range
for i in range(0, 10, 2):
   i /= 10 #conversão em float 
   print(i, end=',')
print("\n")

#Combinando a função range com outras funçõs no caso len
coisas = [
    "abacate",
    "bola",
    "cachorro"
]
#função len retorna o tamanho de uma variavel

for i in range(len(coisas)):
    print(i, coisas[i])

print("\n")
#Fazendo com que  lista começe com valor 1
cont = 0 
for i in range(len(coisas)):
    cont = i + 1
    print(cont, coisas[i])
print("\n")
#Clausulas break e continue
#continue salta a execuçã atual
#break vai interronpender a execusão do bloco
    
lista = range(10)
for i in lista:
    print(i, end=',')
    break

print("\nFIM")

lista = range(10)
for i in lista:
    continue
    print(i, end=',')
    

print("\nFIM")

lista = range(10)
for i in lista:
    if i % 2 == 1:
        continue
    elif i > 5:
        break
    else:
        print(i, end=',')
print("\nFIM")