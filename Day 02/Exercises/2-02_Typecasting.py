numChar = len(input("What is your Name? "))
# print("Your Name has " + numChar + " Characters.") # TypeError
print(type(numChar))
# Method 1
print("---" * 5)
num_char_2 = str(numChar)
print("Your Name has " + num_char_2 + " Characters.")
print("---" * 5)
