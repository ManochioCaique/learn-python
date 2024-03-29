'''
Título: Calculadora de fatorial
Função: Calcular o fatorial de um numero
Autor: Caique Manóchio
Data: 27/03/2024

'''
 #valor de entrata      
x = int(input("Digite um numero: "))

#variaveis
numeros = []                                           
aux = x
#comando parar criar uma lista como os numeros fatoriais 
while (aux > 0):
    pergunta = aux
    numeros.append(pergunta)
    aux -= 1

#variavel para servir de multiplicação
resultado = 1
#multiplica a lista com os numeros retornando o resultado. 
for i in numeros:
    resultado *= i

print(f"O fatorial de {x} é {resultado}")


### Outra forma de fazer, (COMO O PROFESSOR FEZ)
entrada = 5
aux1 = 1 

while entrada > 0:
    aux1 *= entrada
    entrada -= 1
print(aux1)