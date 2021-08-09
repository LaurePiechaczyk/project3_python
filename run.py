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



def make_guess():
    player_row_choice = int(input("type your row: "))
    player_column_choice = int(input("type your colum: "))
    player_choice = player_column_choice + (num_column * (player_row_choice-1))
    return player_choice


def computer_guess():
    computer_choice = random.randint(1, available_points)
    print (computer_choice)
    return computer_choice

def check_guess(choice,boats_position,board):
    if choice in boats_position:
        print("Touche")
        for i in range(num_rows):
            if choice > (num_column*(i)) and choice <= (num_column*(i+1)):
                    board[i][choice-num_column * i -1] = "T"
        print ('\n'.join(' '.join(row) for row in board))
    
    else:
        print("A l'eau")
        for i in range(num_rows):
            if choice > (num_column*(i)) and choice <= (num_column*(i+1)):
                    board[i][choice-num_column * i -1] = "m"
        print ('\n'.join(' '.join(row) for row in board))


def run_game():
    """
    run the game
    """

    playerboard = Board("player")
    print(playerboard.print_board())
    print(playerboard.boats_position)

    computerboard = Board("computer")   
    print(computerboard.print_board())
    print(computerboard.boats_position)

    player_choice = make_guess()
    player_go = check_guess (player_choice,computerboard.boats_position,computerboard.board)
    computer_go = check_guess (computer_guess(),playerboard.boats_position,playerboard.board)

    player_go = check_guess (player_choice,computerboard.boats_position,computerboard.board)
    computer_go = check_guess (computer_guess(),playerboard.boats_position,playerboard.board)


run_game()








