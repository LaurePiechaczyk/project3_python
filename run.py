import random

num_column = 5
num_rows = 3
available_points = num_column * num_rows
number_boats = 4

# Create a board with .
board = [["." for x in range(num_column)] for y in range(num_rows)]

# Get random place for boats
boats_position = random.sample(range(1, available_points), number_boats)

print (boats_position)

# Place the boats on the board
for j in range(number_boats):
    for i in range(num_rows):
        if boats_position[j] > (num_column*(i)) and boats_position[j] <= (num_column*(i+1)):
            board[i][boats_position[j]-num_column * i -1] = "U"

#Visualize the board
print ('\n'.join(' '.join(row) for row in board))

#username = input("Type in your name and press return: ")
row_choice = int(input("type your row: "))
column_choice = int(input("type your colum: "))

choice = column_choice + (num_column * (row_choice-1))

if choice in boats_position:
    print("Touche")
    board[row_choice-1][column_choice - 1] = "T"
    print ('\n'.join(' '.join(row) for row in board))

else:
    print("A l'eau")
    board[row_choice-1][column_choice - 1] = "E"
    print ('\n'.join(' '.join(row) for row in board))