import random

num_column = 3
num_rows = 4
available_points = num_column * num_rows
number_boats = 7


class Board:
    """
    It will print the board.
    """
    def __init__(self, type):
        self.type = type
        self.board = [["." for x in range(num_column)] for y in range(num_rows)]
        self.boats_position = random.sample(range(1, available_points), number_boats)
        
    def print_board(self,touched_boats_position,missed_boats_position): 

        #Show boats only for players
        if self.type == "player":
            for j in range(number_boats):
                for i in range(num_rows):
                    if self.boats_position[j] > (num_column*(i)) and self.boats_position[j] <= (num_column*(i+1)):
                        self.board[i][self.boats_position[j]-num_column * i -1] = "B"
            
        #display Touched boat on all boards 
        for j in range(len(touched_boats_position)):
            for i in range(num_rows):
                if touched_boats_position[j] > (num_column*(i)) and touched_boats_position[j] <= (num_column*(i+1)):
                    self.board[i][touched_boats_position[j]-num_column * i -1] = "T"   
        
        #display missed on all boards
        for j in range(len(missed_boats_position)):
           for i in range(num_rows):
                if missed_boats_position[j] > (num_column*(i)) and missed_boats_position[j] <= (num_column*(i+1)):
                     self.board[i][missed_boats_position[j]-num_column * i -1] = "m"   

        print("this is the" + self.type + "Board:")
        print("this is the" + self.type + "boat position:")
        print( self.boats_position )
        print ('\n'.join(' '.join(row) for row in self.board))
       

def make_guess():
    player_row_choice = int(input("type your row: "))
    player_column_choice = int(input("type your colum: "))
    player_choice = player_column_choice + (num_column * (player_row_choice-1))
    print("player choice:")
    print(player_choice)
    return player_choice


def computer_guess():
    computer_choice = random.randint(1, available_points)
    print (computer_choice)
    return computer_choice


def check_guess(choice,boats_position):
    if choice in boats_position:
        print("Touche")
        return choice
     
    else:
        print("A l'eau")
        return 0


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

#this will have to be looped (while loop) until somebody won
computer_touched_boats_position.append(check_guess (make_guess(),computerboard.boats_position))
print(playerboard.print_board(player_touched_boats_position  , player_missed_boats_position))

player_touched_boats_position.append(check_guess (computer_guess(),playerboard.boats_position))
print(computerboard.print_board(computer_touched_boats_position , computer_missed_boats_position))


"""
computer_touched_boats_position.append(check_guess (make_guess(),computerboard.boats_position))
print(playerboard.print_board(player_touched_boats_position  , player_missed_boats_position))

player_touched_boats_position.append(check_guess (computer_guess(),playerboard.boats_position))
print(computerboard.print_board(computer_touched_boats_position , computer_missed_boats_position))

"""






