"""
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo
    Autor: Caique Manochio
    Data: 11/04/2024_

"""
#Pegando os numeros inteiros
num_inteiro_um = int(input("Digite um numero inteiro: "))

num_inteiro_dois = int(input("Digite um segundo numero inteiro: "))

#Pegando um numero real 
num_real = float(input("Digite o um numero real: "))

#respondendo a pergunta a. 
resposta_a = (2 * num_inteiro_um) * (num_inteiro_dois/2)

#Respondendo a pergunta b.
resposta_b = num_real + (3 * num_inteiro_um)

#Respondendo a pergunta c. 
resposta_c = num_real**3

#printando a resposta
print(f'A resposta da "a" é: {resposta_a}\n A resposta da "b" é: {resposta_b}\n A resposta da "c" é: {resposta_c}')