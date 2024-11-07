#Aula de Loop
fruits = ["Apple", "Peach", "Pear"]

for fruit in fruits:
    print(fruit)
    print (fruit + " pie")


student_scors = [150, 142, 184, 120, 171, 24, 59, 68, 89, 78, 215]

total_exam_score = sum(student_scors)
#replicando o que função sum()
sum = 0 
for score in student_scors:
    sum += score 

print(sum)

print(max(student_scors))
#Exercicios para replicar o que função max() faz
max_score = 0
for score in student_scors:
    if score > max_score:
        max_score = score
        
    
print(max_score)

#Usando for loop e a função range()
#A função range() é para gerar um extensão de numeros para percorrer
#range (a, b, c)  a e b são o intervalo de numeros que quero e o c é de quanto vai ser esse intervalo 
for number in range(1, 10, 3): #range (a, b) não inclui o numero 10
    print(number)

#####################   The Gauss Challenge   ############################
total = 0
for number in range(1, 101):
    total += number 

for number in range(1, 101):
    portres = number%3
    porcinco = number%5
    if portres == 0 and porcinco ==0:
        print("FizzBuzz")
    elif portres == 0:
        print("Fizz")
    elif porcinco == 0:
        print("Buzz")
    
    else:
        print(number)