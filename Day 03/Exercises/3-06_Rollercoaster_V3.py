# Multiple if Statements

# Add ticket price based on Photo selection: 
#   1.  charge $3 extra for photo.


print("Welcome to the Rollercoaster!")

height = int(input("What is your Height (in cm) ? "))
age = int(input("What is Your age? "))
bill = 0
if height >= 120:
    print("You are Eligible for Ride.")
    if age < 12:
        bill = 5
        print("Ticket price is $5.")
    elif age >= 18:
        bill = 12
        print("Ticket price is $12.")
    elif age > 12 and age < 18:
        bill = 7
        print("Ticket Price is $7.")
    photo = input("Do you want photo taken? Y or N ")
    if photo == "Y" or "y" or "yes" or "YES":
        bill += 3
    
    print(f"Your final bill is $ {bill}.")
        
else:
    print("You are Not Eligible.")