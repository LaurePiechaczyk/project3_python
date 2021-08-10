import random
import numpy as np

num_column = 5
num_rows = 2
available_points = num_column * num_rows
number_boats = 3

class Board:
    """
    It will print the board.
    """
    def __init__(self, type):
        self.type = type
        self.board = [["." for x in range(num_column)] for y in range(num_rows)]
        self.boats_position = random.sample(range(1, available_points), number_boats)
        
    def print_board(self,touched_boats_position,missed_boats_position): 

        def place_data_in_board (what_to_place, what_to_write):
            for j in range(len(what_to_place)):
                for i in range(num_rows):
                    if what_to_place[j] > (num_column*(i)) and what_to_place[j] <= (num_column*(i+1)):
                        self.board[i][what_to_place[j]-num_column * i -1] = what_to_write

        #Show boats only for players
        if self.type == "player":
            place_data_in_board (self.boats_position, "B")
        #display touched boats on all boards    
        place_data_in_board (touched_boats_position, "T")
        #display missed on all boards
        place_data_in_board (missed_boats_position, "m")

        #print
        #print("this is the" + self.type + "Board:")
        #print("this is the" + self.type + "boat position:")
        print( self.boats_position )
        print ('\n'.join(' '.join(row) for row in self.board))     

def make_guess():
    player_row_choice = int(input("type your row: "))
    player_column_choice = int(input("type your colum: "))
    player_choice = player_column_choice + (num_column * (player_row_choice-1))
    return player_choice

def computer_guess():
    computer_choice = random.randint(1, available_points)
    print("computer choice:")
    print (computer_choice)
    return computer_choice

def check_guess(choice,boats_position,xx_touched_boats_position,xx_missed_boats_position):
    if choice in boats_position:
        print("Touche")
        return xx_touched_boats_position.append(choice) 
    else:
        print("A l eau")
        return xx_missed_boats_position.append(choice)

################

computer_touched_boats_position = []
player_touched_boats_position = []
computer_missed_boats_position = []
player_missed_boats_position = []

playerboard = Board("player")
computerboard = Board("computer") 

# first time to show the grids
print(playerboard.print_board(player_touched_boats_position  , player_missed_boats_position))
print(computerboard.print_board(computer_touched_boats_position , computer_missed_boats_position))

#start the game and allow to guess
def one_run():
    check_guess(make_guess(),computerboard.boats_position,computer_touched_boats_position,computer_missed_boats_position)
    check_guess(computer_guess(),playerboard.boats_position,player_touched_boats_position,player_missed_boats_position)

    print(playerboard.print_board(player_touched_boats_position  , player_missed_boats_position))
    print(computerboard.print_board(computer_touched_boats_position , computer_missed_boats_position))

while number_boats > len(computer_touched_boats_position) and number_boats > len(player_touched_boats_position):
    one_run()

if len(computer_touched_boats_position) > len(player_touched_boats_position):
    print("You won")
else:
    print("Computer won")
"""
one_run()
one_run()
one_run()
print(computer_touched_boats_position)
print(player_touched_boats_position)
print(computer_missed_boats_position)
print(player_missed_boats_position)

dd=[1,2,3]
ee=[2,1,3]
ff= np.sort(ee)
print(ff)
print(np.array_equal(ee,ee))
print(np.array_equal(np.sort(ee),dd))


"""






