'''
You are going to write a program that calculates the sum of all the even numbers from 1 to 100,
including 1 and 100
'''

total_sum = 0

for number in range (1, 101):
    
    if number % 2 == 0:
        total_sum += number
    
print("----" * 13)

print("The sum of all even numbers from 1 to 100 is:", total_sum)

print("----" * 13)