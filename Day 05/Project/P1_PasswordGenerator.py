import random

# Mixed lowercase and uppercase letters
mixed_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
                 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Digits (numbers)
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Symbols (punctuation)
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

print("Welcome to Password Generator!!!")

no_letters = int(input("How many no of letters your Password should contain:\n "))
no_symbols= int(input("How many no of symbols your Password should contain:\n "))
no_digits= int(input("How many no of numbers your Password should contain:\n "))


# Easy Level
password = ""

for character in range(1, no_letters + 1):
    # or
    # password += random.choice(mixed_letters)
    ran_char = random.choice(mixed_letters)
    password += ran_char

for character in range(1, no_symbols + 1):
    # or
    # password += random.choice(symbols)
    ran_char = random.choice(symbols)
    password += ran_char
    
for character in range(1, no_digits + 1):
    ran_char = random.choice(digits)
    password += ran_char
    # or
    # password += random.choice(digits)

print(f"Easy Level : {password}")


# Hard Level

password_hard = []

for character in range(1, no_letters + 1):
    # or
    # password += random.choice(mixed_letters)
    ran_char = random.choice(mixed_letters)
    password_hard += ran_char

for character in range(1, no_symbols + 1):
    # or
    # password += random.choice(symbols)
    ran_char = random.choice(symbols)
    password_hard += ran_char
    
for character in range(1, no_digits + 1):
    # or
    # password += random.choice(digits)
    ran_char = random.choice(digits)
    password_hard += ran_char

# Randomise lists
random.shuffle(password_hard)

# For loop lists to string
pass_loop = ""
for character in password_hard:
    pass_loop += character

print(f"Hard Password : {pass_loop}")
