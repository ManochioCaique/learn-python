#Calculara para calcular um gorjeta
print("Welcome to the tip calculator.")
total_bill = float(input("What was  the total bill? $"))
percentage = int(input("What percentage tip would you loke to give?10, 12, or 15?"))
people = int(input("How many people to split the bill?"))
pay = (total_bill/people) * ((100 + percentage)/100)
pay_two = round(pay, 2)

print(f"Each person should pay: ${pay_two}")