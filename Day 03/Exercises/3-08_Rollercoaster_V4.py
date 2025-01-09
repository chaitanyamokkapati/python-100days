
# if age is greater than 45 and Lessthan 55 they can ride free


print("Welcome to the Rollercoaster!")

height = int(input("What is your Height (in cm) ? "))
age = int(input("What is Your age? "))
bill = 0
if height >= 120:
    print("You are Eligible for Ride.")
    if age < 12:
        bill = 5
        print("Ticket price is $5.")
    elif age >= 12 and age <= 18:
        bill = 7
        print("Ticket Price is $7.")
    elif age >= 18 and age < 45:
        bill = 12
        print("Ticket price is $12.")

    elif age <= 45 and age <= 55:
        bill = 0
        print(" ")
        print("-----" * 5)
        print("Your ride is F R E E .")
        print("-----" * 5)
        
    photo = input("Do you want photo taken? Y or N ")
    if photo == "Y" or photo == "y" or photo == "yes" or photo == "YES":
        bill += 3
    print("-----" * 5)
    print(f"Your final bill is $ {bill}.")
        
else:
    print("You are Not Eligible.")