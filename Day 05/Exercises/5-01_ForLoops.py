# ForLoop
fruits = ["Strawberries", "Grapes", "Peaches", 
          "Pears", "Nectarines", "Apples", 
          "Cherries", "Blueberries"]

# a cam be any Variable Name
print("----" * 6) # Outside of For Loop
count = 1
for a in fruits:
    print(f"{count}. Fruit : {a}")
    count +=1 # Inside of For Loop
print("----" * 6) # Outside of For Loop