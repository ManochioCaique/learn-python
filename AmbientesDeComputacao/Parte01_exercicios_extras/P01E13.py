"""João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento
diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo
regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo
excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule
o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor
da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

Autor: Caique Manochio
    Data: 24/04/2024_
"""
#Armazendo o valor de quilos de peixes
quilo_de_peixe_pescado =  int(input("Quantos quilos de peixe pescado? "))
#Calculando o valor de quilos a mais
excesso = quilo_de_peixe_pescado - 50 
#calculando a multa  pelo execco de pixe
multa = 4 * excesso

#printando na tela 
print(f"Você pescou {quilo_de_peixe_pescado} kg de peixes. Você exedeu {excesso} kg permitidos e por isso deve pagar {multa} reais")

