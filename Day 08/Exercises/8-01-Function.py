# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

userName = input("What is your Name?\n").title()

# Basic Greet

def greet():
    print("----" * 4)
    print("Hello")
    print("How do you do?")
    print("isn't the weather nice today?")
    print("----" * 4)

# def with Parameter and Arguments.
# Parameter : The name of the data that passed in.
# Arguments : The actual value of data.

def greet_with_parameter(userName):
    print(f"Hello, {userName}") 
    print(f"{userName}, How do you do?")
    print("isn't the weather nice today?")
    print("----" * 4)
    
greet()
greet_with_parameter(userName=userName)