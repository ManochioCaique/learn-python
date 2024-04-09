#Estruturas de condições e repetições 
"""Intentação (espaço) é os espaços antes de começar a escrever.
No python é obrigatório, sendo ele o que determina a fechamento de um bloco
Geralmente é usado 4 espaços em branco
"""
#Exemplo

def sacar (valor):
    saldo = 500
    if saldo >= valor:
        print("Valor sacado!")

sacar(500)

"""Estruturas condicionais permite o desvio de fluxo de controle, 
quando determinadas expressões lógicas são atendidas
"""
#if
saldo = 20000
saque = 100 
if saldo >= saque:
        print("Valor sacado!")
else:
     print("Saldo insuficiente")

#pratica
MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
idade = int(input("Qual sua idade?"))

if idade >= MAIOR_IDADE:
     print("Maior  idade, pode tirar a CNH")

if idade < MAIOR_IDADE: 
     print("Ainda não pode tirar a CNH")

if idade >= MAIOR_IDADE:
     print("Maior  idade, pode tirar a CNH")
else:
     print("Ainda não pode tirar a CNH")


#Elif
if idade >= MAIOR_IDADE:
     print("Maior  idade, pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
     print("Pode fazer as aulas teoricas, mas não pode fazer as aulas práticas")
else:
     print("Ainda não pode tirar a CNH")
