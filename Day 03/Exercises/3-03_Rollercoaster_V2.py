# Nested if and else statements

# Add age to the program: 
#   1.  charge $12 if the age is over 18, and $7 if the age is under 18.
#   2.  If age is less than 12, charge $5; for ages 12 to 18, charge $7; and for ages over 18, charge $12.

print("Welcome to the Rollercoaster!")

height = int(input("What is your Height (in cm) ? "))
age = int(input("What is Your age? "))

if height >= 120:
    print("You are Eligible for Ride.")
    if age < 12:
        print("Ticket price is $5.")
    elif age >= 18:
        print("Ticket price is $12.")
    elif age > 12 and age < 18:
        print("Ticket Price is $7.")
else:
    print("You are Not Eligible.")