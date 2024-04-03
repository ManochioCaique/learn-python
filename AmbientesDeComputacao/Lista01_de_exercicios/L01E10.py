""" 
   Desenvolva um script que calcule o fatorial de um número. Teste com o número 5
   Autor: Caque Manochio
   Data: 01/04/2024
"""
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