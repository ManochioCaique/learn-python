#aula3.1 - if/else

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
else:
  print("Sorry, you have to grow taller before you can ride")

#operadores 
# == igual
# > maior
# >= maior que
# < menor 
# <= menor que 
# != não igual

#Atividade 
number = int(input("Which number do you want to check? "))
remainder = number % 2 

if remainder == 0:
    print("This is an even number.")
else: 
    print("This is an odd number.")



# aula 3.2 - Nested if/else
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("Whta is your age?"))
  if age < 12:
    print("Please pay $5.")
  elif age <= 18:
    print("Please pay $7.")
  else:
    print("Please pay $12.")
else:
  print("Sorry, you have to grow taller before you can ride")

#Atividade de fazer IMC mais completa 

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI1 = float(weight)/(float(height)**2)
BMI = round(BMI1, 0)
BMI = int(BMI)
if BMI < 18.5:
    print(f"Your BMI is {BMI}, you are underweight.")
elif BMI >= 18.5 and BMI < 25:
    print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI >= 25 and BMI < 30:
    print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI >= 30 and BMI < 35:
    print(f"Your BMI is {BMI}, you are obese.")
else:
    print(f"Your BMI is {BMI}, you are clinically obese.")

#Atividade desconbrindo se um ano é bissexto
year = int(input("Which year do you want to check? "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")    
    else:
        print("Leap year.")
else:
    print("Not leap year.")

# aula 3.3 - Multiplos if

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("Whta is your age?"))
  if age < 12:
    bill = 5
    print("Child tickets $5.")   
  elif age <= 18:
    bill = 7
    print("Youth  tickets $7.")
  else:
    bill = 12
    print("Adult tickets $12.")

  wants_photo = input("Do you want a photo taken? Y or N.")
  if wants_photo == "Y":
    bill += 3
  print(f"Your final bill are ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride")

#Atividade - Programa que recebe pedidos de uma pizzaria 

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}")

# aula 3.4 - Operadores logicos 
#and
#or
#not

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
  print("You can ride the rollercoaster!")
  age = int(input("Whta is your age?"))
  if age < 12:
    bill = 5
    print("Child tickets $5.")   
  elif age <= 18:
    bill = 7
    print("Youth  tickets $7.")
  elif age >= 45 and age <= 55:
    bill = 0
    print("Everything is going to be ok. Have a free ride on us!")
  else:
    bill = 12
    print("Adult tickets $12.")
  
   

  wants_photo = input("Do you want a photo taken? Y or N.")
  if wants_photo == "Y":
    bill += 3
  print(f"Your final bill are ${bill}")
else:
  print("Sorry, you have to grow taller before you can ride")

#Atividade criar uma programa que calcular score para o amor
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

combined_names = name1.lower() + name2.lower()

letter_T = combined_names.count('t')
letter_R = combined_names.count('r')
letter_U = combined_names.count('u')
letter_E = combined_names.count('e')
soma_true = letter_T + letter_R + letter_U + letter_E

letter_L = combined_names.count('l')
letter_O = combined_names.count('o')
letter_V = combined_names.count('v')
letter_e = combined_names.count('e')
soma_love = letter_L + letter_O + letter_V + letter_e

love_score = str(soma_true) + str(soma_love)

if int(love_score) < 10 or int(love_score) > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif int(love_score) > 40 and int(love_score) < 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")