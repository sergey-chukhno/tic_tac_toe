# Import used models
import ttkbootstrap as ttk  # Library to improve the graphical interface of Tkinter
from ttkbootstrap.constants import *  # Constants used for ttkbootstrap
from tkinter import messagebox  # Module to show messageboxes
import time  # Module to handle timing

# Initialise the board and the current player
board = [[' ' for _ in range(3)] for _ in range(3)]  # Empty 3x3 board
current_player = 'X'  # Current player starts with 'X'

# Fonction to check if there is a winner
def check_win(player):
    # Checking rows and columns
    for i in range(3):
        if all(board[i][j] == player for j in range(3)):  # Checking rows
            return [(i, j) for j in range(3)]
        if all(board[j][i] == player for j in range(3)):  # Checking columns
            return [(j, i) for j in range(3)]
    # Check the diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:  # First diagonal
        return [(0, 0), (1, 1), (2, 2)]
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:  # Second diagonal
        return [(0, 2), (1, 1), (2, 0)]
    return []  # No winner

# Fonction to check if the board is full (draw)
def is_board_full():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Fonction to handle button click
def button_click(row, col):
    global current_player
    if board[row][col] == ' ':  # Check if the case is empty
        board[row][col] = current_player  # Fill in the case with player's symbol
        buttons[row][col].config(text=current_player, state=DISABLED)  # Deactive the button clicked

        winning_positions = check_win(current_player)  # Check winning combinations
        if winning_positions:
            highlight_winning_buttons(winning_positions)  # Highlight winning buttons
            app.after(1000, lambda: announce_winner(current_player))  # Delay the message announcing the winner
            return
        elif is_board_full():  # Check if the board is full
            app.after(500, lambda: messagebox.showinfo("Game Over", "C'est un match nul !"))  # Print draw message
            app.after(600, reset_board)  # Reinitializing the board with a delay 
            return

        # Change current player 
        current_player = 'O' if current_player == 'X' else 'X'

        if current_player == 'O':  # If it is AI's turn
            row, col = best_move()  # Find the best move for AI Trouv
            button_click(row, col)  # Simulate the click for AI

# Fonction to highlight winning buttons 
def highlight_winning_buttons(winning_positions):
    for row, col in winning_positions:
        buttons[row][col].config(
            style="Winning.TButton",  # Apply a special style to winning buttons
            state=DISABLED  # Deactive the buttons
        )

# Function to announce the winner 
def announce_winner(player):
    messagebox.showinfo("Game Over", f"Le joueur {player} a gagné !")  # Print the message in opening window
    reset_board()  # Reinitialize the board

# Fonction pour reset the board
def reset_board():
    global board, current_player
    board = [[' ' for _ in range(3)] for _ in range(3)]  # Reinitialize the board
    current_player = 'X'  # Reinitiliaze the current player with X
    for row in range(3):
        for col in range(3):
            buttons[row][col].config(text=' ', state=NORMAL, style="Game.TButton")  # Reactive the buttons

# Fonction Minimax to evaluate the best move 
def minimax(is_maximizing):
    score = evaluate()  # Evaluate the current state of the board
    if score is not None:
        return score  # Return the score if the game is over (there is a winner or a draw)

    if is_maximizing:  # if AI is a MAX player
        best = -float('inf')  # Initialize the best score
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':  # Check if a case is empty
                    board[i][j] = 'O'  # Simulate a move
                    best = max(best, minimax(False))  # Make a recursive call of minimax for minimaztion (move by the other player who is a minimiser, MIN player) 
                    board[i][j] = ' '  # Cancel the move and move back
        return best
    else:  # Minimizing strategy
        best = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    best = min(best, minimax(True))  # Make a recursive call of minimax for maximization
                    board[i][j] = ' '
        return best

# Fonction to evaluate the board 
def evaluate():
    if check_win('X'): return -1  # The opponent (MIN human player) wins
    if check_win('O'): return 1  # AI (MAX player) wins
    if is_board_full(): return 0  # Draw
    return None  # Game continues

# Fonction to define the best move for AI
def best_move():
    best_val = -float('inf')  # Initialize the best value, equal to minus infinity
    move = (-1, -1)  # Initialize the best move
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':  # Check if a case is empty
                board[i][j] = 'O'  # Simulate a move
                move_val = minimax(False)  # Évaluate the move
                board[i][j] = ' '  # Cancel the move and move back
                if move_val > best_val:  # Update the best move by comparing move's value with the best value
                    move = (i, j)
                    best_val = move_val
    return move

# Creating application's window
app = ttk.Window(themename="cyborg")  # Creates a windonw with 'cyborg' styling theme
app.title("Tic Tac Toe - Neon Style")  # Window's title
app.geometry("600x600")  # Window's size

# Creating a frame for heading
top_frame = ttk.Frame(app)  # Frame for heading 
top_frame.pack(side=TOP, pady=10)  # Positioning it on top

title_label = ttk.Label(top_frame, text="Tic Tac Toe", font=("Orbitron", 24), anchor=CENTER, bootstyle="info")
title_label.pack()  # Adding the heading and styling it

# Creating a frame for the game (game grid)
grid_frame = ttk.Frame(app)
grid_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

# Creating personalized style for the buttons
style = ttk.Style()
style.configure("Game.TButton", font=("Orbitron", 36), padding=10, foreground="cyan", background="black", borderwidth=4)
style.map("Game.TButton", foreground=[("active", "lime")], background=[("active", "black")])
style.configure("Winning.TButton", font=("Orbitron", 36), foreground="white", background="#00FFFF", borderwidth=4)

# Creating the buttons 
buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = ttk.Button(grid_frame, text=' ', bootstyle="primary-outline", style="Game.TButton",
                            command=lambda r=i, c=j: button_click(r, c))  # Defining a button with a command (function button_click()
        button.grid(row=i, column=j, sticky="nsew", padx=5, pady=5)  # Positionning the buttons on the gird on the screen
        row_buttons.append(button)  # Adding a button to a row
    buttons.append(row_buttons)  # Adding a row to the grid

# Adjusting the size of lines and columns
for i in range(3):
    grid_frame.grid_rowconfigure(i, weight=1)  
    grid_frame.grid_columnconfigure(i, weight=1)

# Creating a framework for reset and exit buttons
bottom_frame = ttk.Frame(app)
bottom_frame.pack(side=BOTTOM, pady=20)  # Poisitonned in the bottom

# Fonction to quit the application
def exit_game():
    app.quit()

# Button 'Restart the game'
new_game_button = ttk.Button(bottom_frame, text="Redémarrer", bootstyle="success", command=reset_board)
new_game_button.pack(side=LEFT, padx=10)  # Positionned on the left

# 'Exit' button
exit_button = ttk.Button(bottom_frame, text="Quitter", bootstyle="danger", command=exit_game)
exit_button.pack(side=RIGHT, padx=10)  # Positionned on the right

# Main loop to run the application 
app.mainloop()
