import random

word_list = ["aardvark", "baboon", "camel"]

random_choosen = random.choice(word_list) # The Random word choosen by computer

print(f"The Random word choosen was: {random_choosen}")

# Find how many underscores need depended on word_list

# disply_underscore = []
# for _ in random_choosen:
#     disply_underscore += "_"

# print(disply_underscore)

type2 = len(random_choosen) * ["_"]

print(type2)

# Add repeativeness add win or loose

endOfGame = False

while not endOfGame:
# Add user input

    user_choice = input("What is your Guess:\n").lower()

# based on user input letter raplace "_" with word list contained letters

    for position in range(len(random_choosen)):
        letter = random_choosen[position]
        if letter == user_choice:
            type2[position] = letter
            
    print(type2)
    
    if "_" not in type2:
        endOfGame = True
        print("You Win")


# Add repeativeness add win or loose
