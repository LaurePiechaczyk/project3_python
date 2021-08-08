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
    print(j)
    for i in range(num_rows):
        if boats_position[j] > (num_column*(i)) and boats_position[j] <= (num_column*(i+1)):
            board[i][boats_position[j]-num_column * i -1] = "U"

#Visualize the board
print ('\n'.join(' '.join(row) for row in board))