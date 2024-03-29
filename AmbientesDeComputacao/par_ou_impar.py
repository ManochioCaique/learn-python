'''
Título: par ou ímpar
Função: criando um programa que vai dizer se o numero é par ou impar
'''

x = int(input("Digite um numero: "))

if x % 2 == 0:
    print(f"O número {x} é par")
else:
    print(f"Esse número {x} é ímpar")
