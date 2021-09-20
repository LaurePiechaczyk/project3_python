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


class Player(Board):
    """
    """
    def __init__(self, name, type):
        self.name = name
        self.type = type
        Board.__init__(self,type)