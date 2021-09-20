def choose_grid(num_rows, num_column, number_boats ):
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

def place_data_in_board (array_to_populate, what_to_place, what_to_write):
    for i in range(len(what_to_place)):
        array_to_populate[what_to_place[i]-1] = what_to_write

def show_games_settings():
    print("-" * 55)
    print(f"The settings are: \nNumber of rows = {num_rows} \nNumber of columns = {num_column} \nNumber of ships: {number_boats}")
    print("Top left corner is row: 1, col: 1")
    print("-" * 55)

def show_score():
    print("-" * 55)
    print(f'The score is:\n{name}:{len(player_score)} \nComputer:{len(computer_score)} ')
    print("-" * 55)

def input_player_guess():
    while True:   
        try:
            player_row_choice = int(input("Enter a row number:\n"))
            player_column_choice = int(input("Enter a column number:\n"))
            if player_row_choice in range(1,num_rows+1)  and player_column_choice in range(1,num_column+1):
                break
            else:
                print("\nPlease enter correct values")
                show_games_settings()

        except ValueError:
            print("\nPlease enter correct values")
            show_games_settings()
    return player_row_choice,player_column_choice

def make_guess():
    print("\nYour turn to play")
    player_row_choice, player_column_choice = input_player_guess()
    player_choice = player_column_choice + (num_column * (player_row_choice-1))
    
    while player_choice in player_score or player_choice in computer.missed_boats_position :
        print("You have already tried this coordinates")
        player_row_choice, player_column_choice = input_player_guess()
        player_choice = player_column_choice + (num_column * (player_row_choice-1))

    print(f'{name} guessed: ({player_row_choice };{player_column_choice})')
    return player_choice

def computer_guess():
    print("\nComputer turn to play")
    computer_choice = random.randint(1, available_points) # with random.randint we don't add +1 at available_points as for random.sample because with random.randint the last number can be choosen
    all_trials = computer_score + player.missed_boats_position
    while computer_choice in previous_trials:
        computer_choice = random.randint(1, available_points) # with random.randint we don't add +1 at available_points as for random.sample because with random.randint the last number can be choosen

    #get the corresponding row and column
    computer_row_choice = np.where(matrix_game == computer_choice)[0][0]+1
    computer_column_choice = np.where(matrix_game == computer_choice)[1][0]+1
    print(f'Computer guessed: ({computer_row_choice};{computer_column_choice})')
    return computer_choice

def check_if_winner():
    if len(player_score) == number_boats or len(computer_score) == number_boats:
        if len(player_score) > len(computer_score):
            show_score()
            print("\nYou won")
            quit()
        else:
            show_score()
            print("\nComputer won")
            quit()

def check_guess(choice,boats_position,touched_boats_position,missed_boats_position):
    if choice in boats_position:
        print("A ship has been touched")
        return touched_boats_position.append(choice)
    else:
        print("ships have been missed this time")
        return missed_boats_position.append(choice)

def one_run():
    check_guess(make_guess(),computer.boats_position,player_score,computer.missed_boats_position)
    check_if_winner()

    check_guess(computer_guess(),player.boats_position,computer_score,player.missed_boats_position)
    check_if_winner()

    show_score()

    next_round_start = (input("Click Enter to continue or n + Enter to quit\n"))
    if next_round_start in ["N", "n","No", "no"]:
        quit()
    player.print_board()
    computer.print_board()