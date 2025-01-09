'''
Write a program that calculates the Body Mass Index (BMI) from a
user's weight and height.
It should tell them the interpretation of their BMI based on the BMI value.
   • Under 18.5: They are underweight.
   • Over 18.5 but below 25: They have a normal weight.
   • Over 25 but below 30: They are overweight.
   • Over 30 but below 35: They are obese.
   • Above 35: They are clinically obese.
'''
userHeight = float(input("What is height (in m): "))
userWeight = float(input("Weight in Kg : "))

BMI = round(userWeight / userHeight ** 2)

if BMI < 18.5:
    print(f"Your BMI Value is {BMI:.1f}. You are Underweight.")
elif BMI < 25:
    print(f"Your BMI Value is {BMI:.1f}. You are Normalweight.")
elif BMI < 30:
    print(f"Your BMI Value is {BMI:.1f}. You are Overweight.")
elif BMI < 35:
    print(f"Your BMI Value is {BMI:.1f}. You are obese.")
else:
    print(f"Your BMI Value is {BMI:.1f}. You are clinically obese.")
