print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Welcome to Treasure Island./nYoor mission is to find the treasure.")
choice1 = str(
    input(
        "You are at a cross road. Wherer do you want to go? Type 'left', 'right' or 'center'"
    ).lower())

if (choice1 == "left"):
  print(
      "You have came to a lake. There is an island in the middle of the lake.")
  choice2 = str(
      input("Type 'wait' to wait for a boat. Type 'swim' to swim across."))
  if (choice2 == "wait"):
    print(
        "You arrive at the island unharmed. There is 3 doors. One red, one yellow ans on blue."
    )
    choice3 = str(input("Which colour do you chosse?"))
    if choice3 == "red":
      print(
          "you found a book that tell the LGBTQIA+ story. Go be a happy Queer")
    elif choice3 == "blue":
      print("you arrive in a straight party. You can cry now")
    else:
      print(
          "you found a magic portal to QUEER WORLD!!! YOU WON!!!! RAINBOW KISS"
      )
  else:
    print("You is find by a shark and he eat you. Game Over!")
elif choice1 == "right":
  print("You fell into a hole. Game over!")
else:
  print("You arrive in a house. Do you want open the door? Type 'Yes' or 'No'")

choice4 = str(input("Type 'yes' or 'no'"))

if choice4 == "yes":
  print("You are save!! You can start again and try to find the treasure!")
else:
  print(
      "You found a straight house and now you have to live with them, sorry. Game over"
  )
