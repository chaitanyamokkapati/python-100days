# random is a python module
'''
What is a Module?
In Python, a module is simply a file that 
contains code (like functions or variables) 
that you can use in other programs.

'''
import random

# To generate Random Integer
randomInteger = random.randint(1, 10)
randomInteger2 = random.randint(1, 10)
print(randomInteger)
print(randomInteger2)

print("-----" * 4)

# To generate Random Float
randomFloat = random.random() # 0.000 to 0.9999
print(randomFloat)

print("-----" * 4)