import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

# Initialize board and current player
board = [[' ' for _ in range(3)] for _ in range(3)]
current_player = 'X'

# Function to check for a win
def check_win(player):
    for i in range(3):
        # Check rows and columns
        if all(board[i][j] == player for j in range(3)):
            return [(i, j) for j in range(3)]
        if all(board[j][i] == player for j in range(3)):
            return [(j, i) for j in range(3)]
    # Check diagonals
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return [(0, 0), (1, 1), (2, 2)]
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return [(0, 2), (1, 1), (2, 0)]
    return []

# Function to check if the board is full
def is_board_full():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))

# Function to handle button click
def button_click(row, col):
    global current_player
    if board[row][col] == ' ':  # Valid move
        board[row][col] = current_player
        buttons[row][col].config(text=current_player, state=DISABLED)

        winning_positions = check_win(current_player)
        if winning_positions:
            highlight_winning_buttons(winning_positions)
            app.after(1000, lambda: announce_winner(current_player))
            return
        elif is_board_full():
            app.after(500, lambda: messagebox.showinfo("Game Over", "C'est un match nul !"))
            app.after(600, reset_board)
            return

        # Switch players
        current_player = 'O' if current_player == 'X' else 'X'

# Highlight winning buttons
def highlight_winning_buttons(winning_positions):
    for row, col in winning_positions:
        buttons[row][col].config(style="Winning.TButton", state=DISABLED)

# Announce winner
def announce_winner(player):
    messagebox.showinfo("Game Over", f"Le joueur {player} a gagné !")
    reset_board()

# Reset the board
def reset_board():
    global board, current_player
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'
    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text=' ', state=NORMAL, style="Game.TButton")

# Create the main window
app = ttk.Window(themename="cyborg")
app.title("Tic Tac Toe")
app.geometry("600x600")

# Top title
top_frame = ttk.Frame(app)
top_frame.pack(side=TOP, pady=10)
title_label = ttk.Label(top_frame, text="Tic Tac Toe", font=("Orbitron", 24), anchor=CENTER, bootstyle="info")
title_label.pack()

# Game grid
grid_frame = ttk.Frame(app)
grid_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

# Button styles
style = ttk.Style()
style.configure("Game.TButton", font=("Orbitron", 36), padding=10, foreground="cyan", background="black", borderwidth=4)
style.map("Game.TButton", foreground=[("active", "lime")], background=[("active", "black")])
style.configure("Winning.TButton", font=("Orbitron", 36), foreground="white", background="#00FFFF", borderwidth=4)

# Create grid buttons
buttons = []
for i in range(3):
    row_buttons = []
    for j in range(3):
        button = ttk.Button(grid_frame, text=' ', bootstyle="primary-outline", style="Game.TButton",
                            command=lambda r=i, c=j: button_click(r, c))
        button.grid(row=i, column=j, sticky="nsew", padx=5, pady=5)
        row_buttons.append(button)
    buttons.append(row_buttons)

# Configure grid weights
for i in range(3):
    grid_frame.grid_rowconfigure(i, weight=1)
    grid_frame.grid_columnconfigure(i, weight=1)

# Cadre inférieur pour les boutons supplémentaires
bottom_frame = ttk.Frame(app)
bottom_frame.pack(side=BOTTOM, pady=20)  # Cadre en bas

# Fonction pour quitter l'application
def exit_game():
    app.quit()

# Bouton "Nouvelle Partie"
new_game_button = ttk.Button(bottom_frame, text="Redémarrer", bootstyle="success", command=reset_board)
new_game_button.pack(side=LEFT, padx=10)  # Bouton à gauche

# Bouton "Quitter"
exit_button = ttk.Button(bottom_frame, text="Quitter", bootstyle="danger", command=exit_game)
exit_button.pack(side=RIGHT, padx=10)  # Bouton à droite

# Run the application
app.mainloop()
