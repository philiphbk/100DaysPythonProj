#Tip calculator
#if the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 22.6
#Round the result to 2 Decimal places = 33.6

print("Welcome to the Tip calculator")
price = float(input("What was the total bill? "))
dividend = int(input("What percentage tip would you like to give?: 10, 12, or 15 "))
people = int(input("How many people to split the bill: "))
bill_with_tip = dividend / 100 * price + price
bill_per_person = bill_with_tip / people
bill_per_person = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: £{bill_per_person}")