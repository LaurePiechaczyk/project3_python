import random
import numpy as np

class Board:
    """
    It will print the board.
    """
    def __init__(self, type):
        self.type = type
        self.array = ["." for x in range(1,available_points+1)]
        self.boats_position = random.sample(range(1, available_points+1), number_boats)
        self.touched_boats_position = [] #it comes when the other is playing because the adversaire ids trying to touch the boats
        self.missed_boats_position = [] #it comes when the other is playing because the adversaire ids trying to touch the boats
  
    def print_board(self): 
        def place_data_in_board (what_to_place, what_to_write):
            for i in range(len(what_to_place)):
                self.array[what_to_place[i]-1] = what_to_write

        if self.type == "player":
            place_data_in_board (self.boats_position, "@")
        place_data_in_board (self.touched_boats_position, "T")
        place_data_in_board (self.missed_boats_position, "m")

        self.board = np.reshape(self.array, (num_rows, num_column)) #reshape the array into a matrix
        print(f'\n{self.name} board')
        print ('\n'.join(' '.join(row) for row in self.board))  

class Player(Board):
    """
    """
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.score = 0
        Board.__init__(self,type)

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
            while number_boats > (num_rows * num_column) or number_boats < 1:
                print("I think you have a bit toomuch boats (or no boat)")
                number_boats = int(input("type your number of boats: "))
            
            return (num_rows, num_column, number_boats )

            if type(num_rows, num_column, number_boats) == int :
                break
        except ValueError:
            print("Both values have to be integers.")

def make_guess():
    print("\nYour turn to play")
    player_row_choice = int(input("Enter a row number: "))
    player_column_choice = int(input("Enter a your colum: "))
    player_choice = player_column_choice + (num_column * (player_row_choice-1))
    print(f'Player guessed: ({player_row_choice };{player_column_choice})')
    return player_choice

def computer_guess():
    print("\nComputer turn to play")
    computer_choice = random.randint(1, available_points)

    while computer_choice in player.touched_boats_position or computer_choice in player.missed_boats_position :
        computer_choice = random.randint(1, available_points)
    #get the corresponding row and column
    computer_row_choice = np.where(matrix_game == computer_choice)[0][0]+1
    computer_column_choice = np.where(matrix_game == computer_choice)[1][0]+1
    print(computer_choice)
    print(available_points)
    print(f'computer guessed: ({computer_row_choice};{computer_column_choice}) ')
    return computer_choice

def check_guess(choice,boats_position,touched_boats_position,missed_boats_position):
    if choice in boats_position:
        print("A ship has been touched")
        return touched_boats_position.append(choice) 
    else:
        print("ships have been missed this time")
        return missed_boats_position.append(choice)

def one_run():
    check_guess(make_guess(),computer.boats_position,computer.touched_boats_position,computer.missed_boats_position)
    check_guess(computer_guess(),player.boats_position,player.touched_boats_position,player.missed_boats_position)

    print("-" * 35)
    print("after this round the score is: ")
    print("-" * 35)
    print(input("enter any key to continue or n to quit"))

    player.print_board()
    computer.print_board()


# present the game and welcome the player
print("-" * 35)
print("Welcome to ULTIMATE BATTLESHIPS!!")
print("-" * 35)

name = input("Please enter your name: \n")

######start with customization
num_column = 2
num_rows = 2
number_boats = 3

constumisation = input (f'Hello {name}, do you want to choose your number of ships and grid size? Y/N \n' )

if constumisation in ["Y", "y","Yes", "yes"]:
    num_rows, num_column, number_boats = choose_grid(num_rows, num_column , number_boats)

print("-" * 35)
print(f"Board size: number rows = {num_rows}, number columns = {num_column}, Number of ships: {number_boats}")
print("top left corner is row: 1, col:1")
print("-" * 35)

available_points = num_column * num_rows
print(available_points)
array_game = np.arange(1,available_points+1) 
print (array_game)
matrix_game = np.reshape(array_game, (num_rows, num_column))
print (matrix_game)

player = Player(name,"player")
computer = Player("computer","computer") 

# first time to show the grids
#print("\nhere is an overview of your bord. Your boats are represented by @.\nWhen you play, T = touched and m = missed.\nGood luck and have fun :)")
player.print_board()
computer.print_board()

while number_boats > len(computer.touched_boats_position) and number_boats > len(player.touched_boats_position):
    one_run()

if len(computer.touched_boats_position) > len(player.touched_boats_position):
    print("\nYou won")
else:
    print("\nComputer won")
 


