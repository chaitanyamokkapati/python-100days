import random

# can also use ramdom.choice do not use in this code.

names = input("Give me names seperated with ', ' : ").upper()
namesSplit = names.split(", ")

# print(namesSplit)
length = len(namesSplit)

randNum = random.randint(0, length-1)

print(f"{namesSplit[randNum]} Pays the Bill.")