# Adding two parameters in function decleration

userName = input("What is your Name?\n").title()
userLocation = input("Where are you from?\n").title()

def greet(userName, userLocation):
    print(f"Hello, {userName}.")
    print(f"How is teh weather in {userLocation}.")
    print("Have a GoodDay!!!")

greet(userName = userName, userLocation = userLocation)