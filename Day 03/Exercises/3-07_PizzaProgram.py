'''
Small Pizza: $15
Medium Pizza: $20
Large Pizza: $25

Pepperoni for Small Pizza: +$2
pepperoni for Medium or Large pizza: +$3

Extra cheese for any size pizza: + $1
'''
print("Welcome to Pizza Deliveries! 🍕")

# Taking input from the user
size = input("What size Pizza do you want? S, M, L :: ")
addPepperoni = input("Do you want Pepperoni? Y or N = ")
extraCheese = input("Do you want Extra Cheese? Y or N = ")

bill = 0

print("----" * 5)
# Checking the pizza size and calculating the initial bill
if size.lower() == "s":
    bill += 15
    print(f"Your Small Pizza bill is $ {bill}.")
elif size.lower() == "m":
    bill += 20
    print(f"Your Medium Pizza bill is $ {bill}.")
elif size.lower() == "l":
    bill += 25
    print(f"Your Large Pizza bill is $ {bill}.")
else:
    print("Invalid size input.")
    exit()  # Exit the program if the size is invalid

# Checking if the user wants Pepperoni and updating the bill
if addPepperoni.lower() == "y":
    if size.lower() == "s":
        bill += 2
        print(f"Your bill with Pepperoni added is $ {bill}.")
    else:
        bill += 3
        print(f"Your bill with Pepperoni added is $ {bill}.")
elif addPepperoni.lower() == "n":
    print(f"Your bill without Pepperoni is $ {bill}.")
else:
    print("Invalid input for Pepperoni.")
    exit()  # Exit if pepperoni input is invalid

# Checking if the user wants Extra Cheese and updating the bill
if extraCheese.lower() == "y":
    bill += 1
    print(f"Your bill with Extra Cheese added is $ {bill}.")
elif extraCheese.lower() == "n":
    print(f"Your bill without Extra Cheese is $ {bill}.")
else:
    print("Invalid input for Extra Cheese.")
    exit()  # Exit if extra cheese input is invalid
print("----" * 5)
# Final Bill
print(f"Your final bill is $ {bill}.")
