'''
You are going to write a program which will mark a spot with an X.
The map is made of 3 rows of blank squares.

    1       2      3
1  ['⬜', '⬜', '⬜']
2  ['⬜', '⬜', '⬜']
3  ['⬜', '⬜', '⬜']
'''

row1 = ['⬜', '⬜', '⬜']
row2 = ['⬜', '⬜', '⬜']
row3 = ['⬜', '⬜', '⬜']

map = [row1, row2, row3] # List inside Lists (Nested Lists)

print(f"{row1},\n{row2},\n{row3}")

position = input("Where do you wnat to put treasure? ")

horizontal = int(position[0])
vertical = int(position[1]) # To get hold of vertical position map [0], map [1], map [2]

selcted_row = map[vertical - 1]
selcted_row[horizontal -1] = "X"

print(horizontal)
print(vertical)
print(f"{row1},\n{row2},\n{row3}")