'''
You are going to write a program that calculates the highest score from a List of
scores.
e.g. studeht_scores = [78, 65, 89, 86, 55, 91, 64, 89]

Important you are not allowed to use the max or min functions. The output words
must match the example. i.e

'''
studentScores = input("Input a List of Student Scores : ") . split()

for n in range(0, len(studentScores)):
    studentScores[n] = int(studentScores[n])
    
# max function
#print(max(studentScores))

# Using For loop
highest = 0
for score in studentScores:
    if score > highest:
        highest = score
        
print(f"Highest score : {highest}.")
    
