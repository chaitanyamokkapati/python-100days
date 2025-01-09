'''
For Love Scores less than 10 or greater than 90, the message should be:
"Your score is x, you go together like coke and mentos. "
---
For Love Scores between 40 and 50, the message should be:
"Your score is y, you are alright together.
---
Otherwise, the message will just be their score. e.g.:
"Your score is z."

'''
name1 = input("Wahat is your Name: \n").upper()
name2 = input("What is their Name: \n").upper()

combined_name = name1 + name2

T = combined_name.count("T")
R = combined_name.count("R")
U = combined_name.count("U")
E = combined_name.count("E")

TRUE =  T + R + U + E

L = combined_name.count("L")
O = combined_name.count("O")
V = combined_name.count("V")
E = combined_name.count("E")

LOVE = L + O + V + E

loveScore = str(TRUE) + str(LOVE)
loveScore = int(loveScore)

if loveScore < 10 or loveScore > 90:
    print(f"Your score is {loveScore}, you go together like coke and mentos.")
elif loveScore >= 40 and loveScore <= 50:
    print(f"Your score is {loveScore}, you are alright together.")
else:
    print(f"Your score is {loveScore}.")