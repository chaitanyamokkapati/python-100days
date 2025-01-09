print("Welcome to the Rollercoaster!")

height = int(input("What is your Height (in cm) ? "))

# Conditional Statements
'''
# ==  (Equality) : Checks if two values are equal. Returns True if equal, False otherwise.
# Example: 5 == 5  # returns True

# >=  (Greater than or equal to) : Checks if the left operand is greater than or equal to the right operand. 
# Returns True if left operand is greater than or equal to right operand, False otherwise.
# Example: 5 >= 3  # returns True

# <=  (Less than or equal to) : Checks if the left operand is less than or equal to the right operand. 
# Returns True if left operand is less than or equal to right operand, False otherwise.
# Example: 3 <= 5  # returns True

# !=  (Not equal to) : Checks if two values are not equal. Returns True if not equal, False otherwise.
# Example: 5 != 3  # returns True

'''
if height >= 120:
    print("You are Eligible for Ride.")
else:
    print("You are Not Eligible.")