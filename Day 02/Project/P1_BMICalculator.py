'''
Write a program that calculates the Body Mass Index (BMI) from a
user's weight and height.
'''
userHeight = float(input("What is height (in m): "))
userWeight = float(input("Weight in Kg : "))

BMI = userWeight / userHeight ** 2

print("User BMI is:", int(BMI))