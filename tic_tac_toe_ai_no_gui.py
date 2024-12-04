# Definining the empty 3x3 board 
board = [[' ' for _ in range(3)] for _ in range(3)]

# Fonction to print the board 
def print_board():
    for row in board:  # Looping through each line of the board
        print('|'.join(row))  # Showing cases separated by "|"
        print('-' * 5)  # Showing horizontal lines separating rows

# Fonction to check if a player has won 
def check_win(player):
    for i in range(3):  # Checking for lines and columns 
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True
        
    # Checking for diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True # there is a winner 
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True # there is a winner 
    return False  # there is no winner

# Fonction to check if there are no empty cases (=board is full, so it is a draw)
def is_board_full():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Fonction to evaluate the actual state of the board. It assings a numeric value to the actual state of the board.
def evaluate():
    if check_win('X'):  # If the player X wins. The player X is  minimizer.
        return -1
    elif check_win('O'):  # If AI wins. AI is a maximizer.
        return 1
    elif is_board_full():  # If all cases are filled in, there is a draw, so each player scores zero. 
        return 0
    return None  # If there is no winner and no draw, the game continues. 

# Implementation of Minimax algorithme
def minimax(depth, is_maximizing): # Depth parameter represents the level of the game tree (0 for the current level, +1 for each next level).
    score = evaluate()  # Evaluate the actual state of the board.
    if score is not None:  # If the game is over (there is a winner or a draw) 
        return score

    if is_maximizing:  # Maximization for the AI, AI is a MAX player
        best = -float('inf') # We intiliazie 'best' with the smallest possible number (-infinity).
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':  # If the case is empty Si la case
                    board[i][j] = 'O'  # AI makes a move
                    best = max(best, minimax(depth + 1, False))  # It calculates the score recursively using minimax function, and compare it to the current value of the 'best' variable. 
                    board[i][j] = ' '  # It cancels the move and moves back. 
        return best
    else:  # Minimizing for human player
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':  # If condition to check if the case is empty
                    board[i][j] = 'X'  # The player makes its move
                    best = min(best, minimax(depth + 1, True))  # Calculating the best score
                    board[i][j] = ' '  # Cancel the move and move back
        return best

# Fonction to find the best move for AI
def best_move():
    best_val = -float('inf')  # Initializing the best value
    move = (-1, -1)  # Initializing the best move

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':  # if the case is empty
                board[i][j] = 'O'  # AI makes its move
                move_val = minimax(0, False)  # Calculate the value corresponding to this move
                board[i][j] = ' '  # Cancel the move so that the case is empty again
                if move_val > best_val:  # Comparing the value of the move with the best value
                    move = (i, j)  # Updating best move
                    best_val = move_val #Making best value equal move's value
    return move  # Return best move

# Fonction for a player to make a move
def make_move(player):
    if player == 'X':  # If it is human player's turn, human player playing with X
        while True:
            try:
                row = int(input(f"Joueur {player}, entrez la ligne (0-2): "))
                col = int(input(f"Joueur {player}, entrez la colonne (0-2): "))
                if board[row][col] == ' ':  # If the case is empty
                    board[row][col] = player  # Place player's symbol in it
                    break
                else:
                    print("Case occupée, essayez encore.")
            except (ValueError, IndexError):
                print("Entrée invalide, entrez un nombre entre 0 et 2.")
    else:  # If it is AI's turn
        print("L'IA joue son tour...")
        row, col = best_move()  # AI uses best move calculated in best_move function
        board[row][col] = 'O'

# Game's main loop
def play_game():
    current_player = 'X'  # Human player starts
    while True: # While loop determining that the game goes on while game end conditions (victory or draw) are not met
        print_board()  # Print the board
        make_move(current_player)  # Current player makes his move

        # Check if there is a winner
        if check_win(current_player):
            print_board()
            print(f"Joueur {current_player} gagne!")
            break

        # Check if there is a draw
        if is_board_full():
            print_board()
            print("C'est un match nul!")
            break

        # Changing player
        current_player = 'O' if current_player == 'X' else 'X'

# Launch the game
play_game()
