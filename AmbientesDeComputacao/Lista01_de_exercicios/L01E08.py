"""
   Desenvolva um programa que um valor em segundos e, em seguida, imprima quantas horas,
minutos e segundos esse valor representa. Teste com o valor 300
   Autor:Caique Manochio
   Data:01/04/2024

"""
#Recebendo o valor do usuario
valor_recebido = int(input("Digite um valor: "))

#Convertendo  o valor recebido em minutos considerando que o valor é os sengundos  
minutos = valor_recebido/60
#Convertendo o valor de minutos em hora
horas = minutos/60
#Coniderando o valor recebido como segundo
segundos = valor_recebido

print (f"O valor {valor_recebido} equilave\n Em horas: {horas}\n Em minutos {minutos}\n Em segundos {segundos}")