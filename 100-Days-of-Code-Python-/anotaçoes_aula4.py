#Aula 4.1 - Gerando números aleatório 
import random 

#int
random_integer = random.randint(1, 10)
print(random_integer)

#float
random_float = random.random()
print(random_float)


import my_module
random_integer = random.randint(1, 10)

print(random_integer)

print(my_module.my_favourite_number)

#Criando randam float number 
#função randam usada para gerar o numeros, inclui o numero que começa e não inclui o numero que termina
random_number_0_to_1 = random.random() *10 #posso multiplicar os dois numeros 

print(random_number_0_to_1)

random_float = random.uniform(1, 10)
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
#Opção 1
import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
x = len(names)
number = random.randint(0, x - 1)
names_salve = names[number]
print(f"{names_salve} is going to buy the meal today!")

#Opção 2
friends  = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

print(friends[random.randint(0,4)])



#Opção 3
print(random.choice(friends))

#Exercicios ...
fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
fruits[-1] = "Melons"
print(fruits)


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])

