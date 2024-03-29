#aula 2.1 - Data Types
#String
print("Hello"[4])
print("123" + "345")

#Integer
print(123 + 345)

#Float
print(3.15465)

#Boolean
True
False

#aula 2.2 - type function
#type()
#str()
#float()
num_char = len(input("What's your name?"))
print(type(num_char))
new_num_char = str(num_char)
print("Your name has " + new_num_char + " characters.")
print(type(num_char))

#aula 2.3 - Operadores matemáticos
3 + 5
7 - 4
3 * 2
6 / 3
2**3

#Atividade
#Criar IMC

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
BMI = float(weight)/(float(height)**2)

print(round(BMI))

#aula 2.4 - Manipulação de numeros
#round(numero que quero arrendodar, casas depois da vírgula) function 
print(round(8/3, 2))
#Usar scores a point
score = 0 
score += 1
print(score)

#f-String
score = 0
height = 1.8 
isWinning = True
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

#Atividade
#Calcular quanto uma pessoa tem ainda de vida se ela morresse aos 90
age = int(input("What is your current age? "))
left = 90 - age
months = left * 12
weeks = left * 52
days = left * 365
print(f"You have {days} days, {weeks} weeks, and {months} months left")