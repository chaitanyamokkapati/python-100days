# Operations
'''
+  -> Addition
-  -> Subtraction
*  -> Multiplication
/  -> Division
** -> Exponentiation
'''

# Addition
print("Addition 2 + 2 = ", 2 + 2)


# Subtraction
print("Subtraction 5 - 3 = ", 5 - 3)

# Multiplication
print("Multiplication 3 * 4 = ", 3 * 4)

# Division
print("Division 10 / 2 = ", 10 / 2) # Float

# Exponentiation
print("Exponentiation 2 ** 3 = ", 2 ** 3)

print("----- Priority - PEMDAS -----")

# Priority - PEMDAS
'''
P -> Parentheses
E -> Exponents
MD -> Multiplication and Division (left to right)
AS -> Addition and Subtraction (left to right)
'''

# Parentheses first
print("Parentheses: (2 + 3) * 2 = ", (2 + 3) * 2)

# Exponents (Exponentiation)
print("Exponents: 2 ** 3 + 4 = ", 2 ** 3 + 4)

# Multiplication and Division (left to right)
print("Multiplication & Division: 4 + 6 / 2 = ", 4 + 6 / 2)  # Division happens before addition

# Addition and Subtraction (left to right)
print("Addition & Subtraction: 4 + 6 - 2 = ", 4 + 6 - 2)  # Addition happens before subtraction
