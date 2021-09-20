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
        if self.type == "player":
            place_data_in_board (self.array, self.boats_position, "@")
        place_data_in_board (self.array, self.touched_boats_position, "T")
        place_data_in_board (self.array, self.missed_boats_position, "m") 

        self.board = np.reshape(self.array, (num_rows, num_column)) #reshape the array into a matrix
        print(f'\n{self.name} board')
        print ('\n'.join(' '.join(row) for row in self.board))  


class GameParticipant(Board):
    """
    GameParticipant Class 
    """
    def __init__(self, name, type):
        self.name = name
        self.type = type
        Board.__init__(self,type)


def player_game_customisation (num_rows, num_column, number_boats):
    while True:   
        try:
            num_rows = int(input("type your number of rows:\n"))
            while  num_rows > 13 or num_rows < 1 :
                print("Please use a value between 1 and 13")
                num_rows = int(input("type your number of rows:\n"))
  
            num_column = int(input("type your number of columns:\n"))
            while num_column > 13 or num_column < 1:
                print("Please use a value between 1 and 13")
                num_column = int(input("type your number of column:\n"))

            number_boats = int(input("type your number of boats:\n"))
            while number_boats > (num_rows * num_column) or number_boats < 1:
                print("You might have a bit too much boats (or no boat)")
                number_boats = int(input("type your number of boats:\n"))
            
            return (num_rows, num_column, number_boats )

            if type(num_rows, num_column, number_boats) == int :
                break
        except ValueError:
            print("Values have to be integers.")


def place_data_in_board (array_to_populate, data_to_place, data_Character):
    for i in range(len(data_to_place)):
        array_to_populate[data_to_place[i]-1] = data_Character


def show_game_settings():
    print("-" * 55)
    print(f"The settingds are: \nNumber of rows = {num_rows} \nNumber of columns = {num_column} \nNumber of ships: {number_boats}")
    print("Top left corner is row: 1, col: 1")
    print("-" * 55)


def show_scores():
    print("-" * 55)
    player_score = len(computer.touched_boats_position)
    computer_score = len(player.touched_boats_position)
    print(f'The score is:\n{name}:{player_score} \nComputer:{computer_score} ')
    print("-" * 55)


def let_player_guess_row_column():
    while True:   
        try:
            player_row_choice = int(input("Enter a row number:\n"))
            player_column_choice = int(input("Enter a column number:\n"))
            if player_row_choice in range(1,num_rows+1) and player_column_choice in range(1,num_column+1):
                break
            else:
                print("\nPlease enter correct values")
                show_game_settings()

        except ValueError:
            print("\nPlease enter correct values")
            show_game_settings()
    return player_row_choice, player_column_choice


def player_guess():
    print("\nYour turn to play")
    player_row_choice, player_column_choice = let_player_guess_row_column()
    player_choice_in_array = player_column_choice + (num_column * (player_row_choice-1))
    player_previous_trials = computer.touched_boats_position + computer.missed_boats_position


    while player_choice_in_array in player_previous_trials:
        print("You have already tried this coordinates")
        player_row_choice, player_column_choice = let_player_guess_row_column()
        player_choice_in_array = player_column_choice + (num_column * (player_row_choice-1))

    print(f'{name} guessed: ({player_row_choice };{player_column_choice})')
    return player_choice_in_array


def computer_guess():
    print("\nComputer turn to play")
    computer_choice_in_array = random.randint(1, available_points) #with random.randint we don't add +1 at available_points as for random.sample because with random.randint the last number can be choosen
    computer_previous_trials = player.touched_boats_position + player.missed_boats_position

    while computer_choice_in_array in computer_previous_trials:
        computer_choice_in_array = random.randint(1, available_points) #with random.randint we don't add +1 at available_points as for random.sample because with random.randint the last number can be choosen

    #get the corresponding row and column in matrix to display in the board
    computer_row_choice = np.where(matrix_game == computer_choice_in_array)[0][0]+1
    computer_column_choice = np.where(matrix_game == computer_choice_in_array)[1][0]+1
    print(f'Computer guessed: ({computer_row_choice};{computer_column_choice})')
    return computer_choice_in_array

def check_if_winner():
    player_score = len(computer.touched_boats_position)
    computer_score = len(player.touched_boats_position)
    if player_score == number_boats or computer_score == number_boats:
        if player_score > computer_score:
            show_scores()
            print("\nYou won")
            quit()
        else:
            show_scores()
            print("\nComputer won")
            quit()

def check_if_ship_touched_missed(guess,boats_position,touched_boats_position,missed_boats_position):
    if guess in boats_position:
        print("A ship has been touched")
        return touched_boats_position.append(guess)
    else:
        print("ships have been missed this time")
        return missed_boats_position.append(guess)

def run_game():
    check_if_ship_touched_missed(player_guess(),computer.boats_position,computer.touched_boats_position,computer.missed_boats_position)
    check_if_winner()

    check_if_ship_touched_missed(computer_guess(),player.boats_position,player.touched_boats_position,player.missed_boats_position)
    check_if_winner()

    show_scores()

    next_round_start = (input("Do you want to continue? \nClick on ANY KEY to continue \nto quit click n + Enter \n"))
    if next_round_start in ["N", "n","No", "no"]:
        quit()
    player.print_board()
    computer.print_board()
    run_game()

# --------------------- Game Start here 

# present the game and welcome the player
print("-" * 55)
print("Welcome to ULTIMATE BATTLESHIPS!!")
print("-" * 55)

name = input("Please enter your name:\n")

# Set default values for board size and number of ships
num_column = 5
num_rows = 4
number_boats = 6

# If player wants, let him/her choose values for board size and number of ships
constumisation = input (f'Hello {name}, do you want to choose your number of ships and grid size? \nClick Y + Enter \nOtherwise click Enter to play with the default\n' )
if constumisation in ["Y", "y","Yes", "yes"]:
    num_rows, num_column, number_boats = player_game_customisation(num_rows, num_column , number_boats)

# Show the player the settings so he/her can understand that row and column start at 1, number of ships
show_game_settings()

# Setting some variables. 
# The available points are then in and array and also in a matrix in order to show the board
available_points = num_column * num_rows
array_game = np.arange(1,available_points+1) 
matrix_game = np.reshape(array_game, (num_rows, num_column))


# Using the classes to set a player and a computer
player = GameParticipant(name,"player")
computer = GameParticipant("computer","computer") 


# first time to show the grids
print("-" * 55)
print("Your boats are represented by @.\nT = touched ships \nm = missed.\nGood luck and have fun :)")
print("-" * 55)
player.print_board()
computer.print_board()

run_game()


