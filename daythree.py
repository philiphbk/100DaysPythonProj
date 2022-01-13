"""
# Control Flow with if else and Conditional Overflow

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7.")
    elif 45 <= age <= 55:
        print("Everything is going to be ok. Have a free ride on us!")
    else:
        bill = 12
        print("Adult tickets are $12.")
    wants_photo = input("Do you want a photo taken? Y or N.")
    if wants_photo == "Y":
        # Add $3 to their Bill
        bill += 3

    print(f"Your final bill is {bill}")
else:
    print("Sorry, you have to grow taller before you can ride!")
"""
"""
number = int(input("Which number do you want to check? "))
if number % 2 == 0:
    print("The number is EVEN number!")
else:
    print("The number is ODD number!")
"""

"""
# BMI CALCULATOR
print("Welcome to your BMI Calculator!")
weight = float(input("What is your weight? "))
height = float(input("what is height? "))
bmi = weight / (pow(height, 2))
bmi = round(bmi, 2)

if bmi < 18.5:
    print(f'Your BMI is {bmi}, you are underweight')
elif bmi < 22:
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 28:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 33:
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clinically obese.")
"""

"""
# Leap Year
year = int(input("Which Year do you want to check? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"Year {year} is a leap year")
        else:
            print("Not leap year")
    else:
        print("Not a leap year")
else:
    print(f"Year {year} is not a leap year")
"""

"""
# Pizza Deliveries
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want Pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "L":
    bill += 25
elif size == "M":
    bill += 20
elif size == "S":
    bill += 15

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is $: {bill}")
"""
"""
# Love Calculator
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()

true_love1 = str(name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") + name1.count("l") +
                 name1.count("o") + name1.count("v") + name1.count("e"))
true_love2 = str(name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e") + name2.count("l") +
                 name2.count("o") + name2.count("v") + name2.count("e"))

both = true_love1 + true_love2
both = int(both)

if both < 10 or both > 90:
    print(f"Your score is **{both}**, you go together like coke and mentos.")
          
elif 40 <= both <= 50:
    print(f"Your score is **{both}**, you are alright together.")
else:
    print(f"Your score is **{both}**.")
"""

# Treasure Island
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
     _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ _________________|_______
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
print("Welcome to Treasure Island")
print("Your mission is to find the treasure")
street_walk = input("You're walking down the street, getting to a cross road where do you want to go? Type 'left' or "
                    "'right' \n ").lower()
if street_walk == "left":
    haunted_house = input("You've come to a haunted house. Type 'enter' to enter house or 'run' to leave \n").lower()
    if haunted_house == "enter":
        room = input("You've arrived into a room with three doors. One red, one yellow, and blue. Which do you "
                     "choose? \n").lower()
        if room == "yellow":
            print("You Win!")
        elif room == "red":
            print("There are snakes in there. Game Over!")
        elif room == "blue":
            print("There are bombs in there. Game Over!")
        else:
            print("Game Over")
    else:
        print("Game Over")
else:
    print("Game Over")
