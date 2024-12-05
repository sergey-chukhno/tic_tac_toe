from tkinter import messagebox
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import subprocess  # Module to launch external scripts

# Function to run the selected game
def run_game(file_name):
    try:
        subprocess.run(["python", file_name], check=True)  # Launch game
    except FileNotFoundError:
        messagebox.showerror("Erreur", f"Le fichier '{file_name}' est introuvable.")
    except Exception as e:
        messagebox.showerror("Erreur", f"Une erreur s'est produite : {str(e)}")

# Creating main window
app = ttk.Window(themename="cyborg")
app.title("Tic Tac Toe: Choisissez votre jeu")
app.geometry("700x500")

# Top title
title_label = ttk.Label(
    app,
    text="Tic Tac Toe: Choisissez votre jeu",
    font=("Orbitron", 28),
    anchor=CENTER,
    bootstyle="info"
)
title_label.pack(pady=20)

# Style for buttons
style = ttk.Style()
style.configure('TButton.primary-outline', font=('Roboto', 24))

# Frame for buttons
button_frame = ttk.Frame(app)
button_frame.pack(expand=True, fill=BOTH, padx=20, pady=20)

# Define game options
games = [
    ("Jouer à deux sans interface graphique", "tic_tac_toe_human_no_gui.py"),
    ("Jouer à deux avec interface graphique", "tic_tac_toe_human_gui.py"),
    ("Jouer avec l'IA sans interface graphique", "tic_tac_toe_ai_no_gui.py"),
    ("Jouer avec l'IA avec interface graphique", "tic_tac_toe_ai_gui.py")
]

# Create buttons for the game
for idx, (label, file_name) in enumerate(games):
    button = ttk.Button(
        button_frame,
        text=label,
        #style ='Custom.TButton',
        bootstyle="primary-outline",
        command=lambda f=file_name: run_game(f)
    )
    button.grid(row=idx // 2, column=idx % 2, padx=10, pady=10, sticky="nsew")

# Configuring grid appearance
for i in range(2):  # deux lignes
    button_frame.rowconfigure(i, weight=1)
for j in range(2):  # deux colonnes
    button_frame.columnconfigure(j, weight=1)

# Launch application
app.mainloop()
