#Aula 4.1 - Gerando números aleatório 
import random 

#int
random_integer = random.randint(1, 10)
print(random_integer)

#float
random_float = random.random()
print(random_float)
#Ativdade gerar aleatóriamente cara ou coroa
import random
H = "Heads"
T = "Tails"
number_random = random.randint(1,3)
if number_random == 1:
    print(T)
elif number_random == 2:
    print(H)

# aula 4.2 - Listas
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

print(states_of_america[2])
#Adicionando um item no final da lista.
states_of_america.append("ESTADO NOVO ")

#Atividade de selecionar um elemento da lista de forma aleatória 
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
x = len(names)
number = random.randint(0, x - 1)
names_salve = names[number]
print(f"{names_salve} is going to buy the meal today!")