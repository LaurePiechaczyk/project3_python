import random
import numpy as np
from classes import *
from functions import *


# present the game and welcome the player
print("-" * 55)
print("Welcome to ULTIMATE BATTLESHIPS!!")
print("-" * 55)

name = input("Please enter your name:\n")

######start with customization
num_column = 5
num_rows = 4
number_boats = 6

constumisation = input (f'Hello {name}, do you want to choose your number of ships and grid size? \nClick Y + Enter \nOtherwise click Enter to play with the default\n' )

if constumisation in ["Y", "y","Yes", "yes"]:
    num_rows, num_column, number_boats = choose_grid(num_rows, num_column , number_boats)

show_games_settings()

available_points = num_column * num_rows
array_game = np.arange(1,available_points+1) 
matrix_game = np.reshape(array_game, (num_rows, num_column))

player = Player(name,"player")
computer = Player("computer","computer") 

# first time to show the grids
print("-" * 55)
print("Your boats are represented by @.\nT = touched ships \nm = missed.\nGood luck and have fun :)")
print("-" * 55)
player.print_board()
computer.print_board()

while number_boats > len(computer.touched_boats_position) and number_boats > len(player.touched_boats_position):
    one_run()

 
