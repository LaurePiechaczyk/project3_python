import random

# present the game and welcome the player
name = input("What is your name player? ")
print(f'Welcome: {name}')

######start with customization
num_column = 2
num_rows = 2
number_boats = 3

constumisation = input ("do you want to choose your number of boats and grid size? Y/N \n" )

def choose_grid(num_rows, num_column, number_boats ):
    while True:   
        try:
            num_rows = int(input("type your number of rows: "))
            while  num_rows > 13 or num_rows < 1 :
                print("Please use a value between 1 and 12")
                num_rows = int(input("type your number of rows: "))
  
            num_column = int(input("type your number of columns: "))
            while num_column > 13 or num_column < 1:
                print("Please use a value between 1 and 12")
                num_column = int(input("type your number of column: "))

            number_boats = int(input("type your number of boats: "))
            while number_boats >= (num_rows * num_column) or number_boats < 1:
                print("I think you have a bit toomuch boats (or no boat)")
                number_boats = int(input("type your number of boats: "))
            
            return (num_rows, num_column, number_boats )

            if type(num_rows, num_column, number_boats) == int :
                break
        except ValueError:
            print("Both values have to be integers.")

if constumisation in ["Y", "y","Yes", "yes"]:
    num_rows, num_column, number_boats = choose_grid(num_rows, num_column , number_boats)
else:
     print("Fair enough, you will play with the default. Your boats are shown with @ and the computer had 5 hidden boats.")
#print("this is the" + self.type + "Board:")

available_points = num_column * num_rows


##################

class Board:
    """
    It will print the board.
    """
    def __init__(self, type, name):
        self.type = type
        self.name = name

        self.board = [["." for x in range(num_column)] for y in range(num_rows)]
        self.boats_position = random.sample(range(1, available_points), number_boats)

        self.touched_boats_position = [] #it comes when the other is playing because the adversaire ids trying to touch the boats
        self.missed_boats_position = [] #it comes when the other is playing because the adversaire ids trying to touch the boats
        
    def print_board(self): 

        def place_data_in_board (what_to_place, what_to_write):
            for j in range(len(what_to_place)):
                for i in range(num_rows):
                    if what_to_place[j] > (num_column*(i)) and what_to_place[j] <= (num_column*(i+1)):
                        self.board[i][what_to_place[j]-num_column * i -1] = what_to_write

        #Show boats only for players
        if self.type == "player":
            place_data_in_board (self.boats_position, "@")
        #display touched boats on all boards    
        place_data_in_board (self.touched_boats_position, "T")
        #display missed on all boards
        place_data_in_board (self.missed_boats_position, "m")

        print(f'\n{self.name} board')
        print ('\n'.join(' '.join(row) for row in self.board))     


def make_guess():
    print("\nyour turn to play. Just try to hit the computer boats")
    player_row_choice = int(input("type your row: "))
    player_column_choice = int(input("type your colum: "))
    player_choice = player_column_choice + (num_column * (player_row_choice-1))
    return player_choice

def computer_guess():
    print("\nComputer turn to play")
    computer_choice = random.randint(1, available_points)

    while computer_choice in playerboard.touched_boats_position or computer_choice in playerboard.missed_boats_position :
        computer_choice = random.randint(1, available_points)
    #print("computer choice:")
    #print (computer_choice)
    return computer_choice

def check_guess(choice,boats_position,touched_boats_position,missed_boats_position):
    if choice in boats_position:
        print("Touche")
        return touched_boats_position.append(choice) 
    else:
        print("A l eau")
        return missed_boats_position.append(choice)

################


playerboard = Board("player",name)
computerboard = Board("computer","computer") 

# first time to show the grids
print("\nhere is an overview of your bord. Your boats are represented by @.\nWhen you play, T = touched and m = missed.\nGood luck and have fun :)")
playerboard.print_board()

def one_run():
    check_guess(make_guess(),computerboard.boats_position,computerboard.touched_boats_position,computerboard.missed_boats_position)
    computerboard.print_board()

    check_guess(computer_guess(),playerboard.boats_position,playerboard.touched_boats_position,playerboard.missed_boats_position)
    playerboard.print_board()

while number_boats > len(computerboard.touched_boats_position) and number_boats > len(playerboard.touched_boats_position):
    one_run()

if len(computerboard.touched_boats_position) > len(playerboard.touched_boats_position):
    print("\nComputer won")
else:
    print("\nYou won")







