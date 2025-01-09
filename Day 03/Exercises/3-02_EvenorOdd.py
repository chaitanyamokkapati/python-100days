print("Even or Odd !!!")

number = int(input("Enter your Number : "))

# Logic

if number % 2 == 0:
    print(f"Number {number} is a Even.")
elif number % 2 != 0:
    print(f"Number {number} is a Odd.")
else:
    print("...INPUT INVAID...")