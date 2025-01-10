# Don't use len() or sum() Fumctions. Use only For loops.
'''
156 178 165 171 187
'''

studentHeights = input("Input List of Students Heights:\n").split()

for n in range(0, len(studentHeights)):
    studentHeights[n] = int(studentHeights[n])
print(studentHeights)

# Method 1
# totalSum = sum(studentHeights)
# noOfStudents = len(studentHeights)
# Average = round(totalSum / noOfStudents)
# print(f"Avg Height of Class = {Average}")

SumOfTotalHeight = 0
count = 0
for TotHeight in studentHeights:
    SumOfTotalHeight += TotHeight
    count += 1

avg = round(SumOfTotalHeight / count)
print(f"Avg Height of Class = {avg}")