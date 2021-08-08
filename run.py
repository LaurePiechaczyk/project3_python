import random

num_column = 7
num_rows = 4
available_points = num_column * num_rows
number_boats = 7


class Board:
    """
    """
    def __init__(self,type):
        self.type = type
        self.board = [["." for x in range(num_column)] for y in range(num_rows)]
        self.boats_position = random.sample(range(1, available_points), number_boats)

    def print_board(self): 
        if self.type == "player":
            for j in range(number_boats):
                for i in range(num_rows):
                    if self.boats_position[j] > (num_column*(i)) and self.boats_position[j] <= (num_column*(i+1)):
                        self.board[i][self.boats_position[j]-num_column * i -1] = "B"
            print ('\n'.join(' '.join(row) for row in self.board))
        else:
            print ('\n'.join(' '.join(row) for row in self.board))

playerboard = Board("player")
print(playerboard.print_board())
print(playerboard.boats_position)

computerboard = Board("computer")
print(computerboard.print_board())
print(computerboard.boats_position)









