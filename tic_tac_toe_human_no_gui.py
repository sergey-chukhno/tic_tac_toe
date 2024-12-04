
# Defining the board as a list containing lists, 3x3 
board = [[' ' for _ in range(3)] for _ in range(3)] # We create a list containing other lists, we use list comprehension

# Fonction to print the board on the screen
def print_board():
    for row in board:  # Looping through each line of the board
        print('|'.join(row))  # Print the cases of each line separated by vertical bars
        print('-' * 5)  # Print lines separating rows

# Fonction to check if a player has won (game conditions)
def check_win(player):
    for i in range(3):  # Check for lines and columns using built-in all function 
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True  # Return true if a line or a column is filled in with player's symbol
        
    # Checking diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True  # First diagonal
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True  # Second diagonal
    return False  # No winner

# Fonction to check if the board is not full (condition for draw)
def is_board_full():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))  # Check if all the cases are not taken

# Fonction to allow a player to make a move
def make_move(player):
    while True:  # A loop to get a valid move
        try:
            row = int(input(f"Joueur {player}, entrez la ligne (0-2) : "))  # Ask a player to choose a line
            col = int(input(f"Joueur {player}, entrez la colonne (0-2) : "))  # Ask a player to choose a column
            if board[row][col] == ' ':  # Check if the case is empty
                board[row][col] = player  # Placing player's symbol, X or O 
                break  # Get out of loop if the move is valid
            else:
                print("Case déjà occupée, veuillez choisir une autre case.")  # Message to print of the case is taken
        except (ValueError, IndexError):  # Handling errors
            print("Entrée incorrecte, veuillez entrer un nombre compris entre 0 et 2.")  # Error message if the entered number is not an integer between 0 and 2. 

# Main Game Loop
def play_game():
    current_player = 'X'  #  Player X starts
    while True: # Loop running until the game end conditions (victory or draw) are not met
        print_board()  # Print the board
        make_move(current_player)  # Ask the player to make a move

        # Check if there is a winner (end condition)
        if check_win(current_player):
            print_board()  # Show the final outlook of the board
            print(f"Le joueur {current_player} gagne !")  # Announce the winner
            break  # End the loop

        # Check if the board is full (end condition for draw)
        if is_board_full():
            print_board()  # Print the board
            print("C'est un match nul !")  # Announce the draw
            break  # End the loop

        # Switch player
        current_player = 'O' if current_player == 'X' else 'X'  # Alterner entre X et O

# Launch the game
play_game()