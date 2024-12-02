
# Définir le plateau de Tic Tac Toe comme une grille 3x3
board = [[' ' for _ in range(3)] for _ in range(3)] # On crée une liste qui contenant un autre liste

# Fonction pour afficher le plateau
def print_board():
    for row in board:  # Parcourir chaque rangée du plateau
        print('|'.join(row))  # Afficher les cases de la rangée séparées par des barres verticales
        print('-' * 5)  # Afficher une ligne de séparation entre les rangées

# Fonction pour vérifier si un joueur a gagné
def check_win(player):
    for i in range(3):  # Vérifier les lignes et colonnes
        if all([board[i][j] == player for j in range(3)]) or \
           all([board[j][i] == player for j in range(3)]):
            return True  # Retourner vrai si une ligne ou colonne est complète
        
    # Vérifier les diagonales
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True  # Diagonale principale complète
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True  # Diagonale secondaire complète
    return False  # Aucun gagnant

# Fonction pour vérifier si toutes les cases sont occupées
def is_board_full():
    return all(board[i][j] != ' ' for i in range(3) for j in range(3))  # Vérifie si toutes les cases sont occupées

# Fonction pour permettre à un joueur de faire un mouvement
def make_move(player):
    while True:  # Boucle pour saisir un coup valide
        try:
            row = int(input(f"Joueur {player}, entrez la ligne (0-2) : "))  # Demander la ligne
            col = int(input(f"Joueur {player}, entrez la colonne (0-2) : "))  # Demander la colonne
            if board[row][col] == ' ':  # Vérifier si la case est libre
                board[row][col] = player  # Placer le symbole du joueur sur le plateau
                break  # Sortir de la boucle si le coup est valide
            else:
                print("Case déjà occupée, veuillez choisir une autre case.")  # Message pour case occupée
        except (ValueError, IndexError):  # Gérer les erreurs d'entrée
            print("Entrée incorrecte, veuillez entrer un nombre compris entre 0 et 2.")  # Message d'erreur si l'input n'est pas un nombre compris entre 0 et 2. 

# Boucle principale du jeu
def play_game():
    current_player = 'X'  # Le joueur X commence
    while True:
        print_board()  # Afficher le plateau
        make_move(current_player)  # Demander un mouvement au joueur actuel

        # Vérifier si le joueur actuel a gagné
        if check_win(current_player):
            print_board()  # Afficher le plateau final
            print(f"Le joueur {current_player} gagne !")  # Annoncer le gagnant
            break  # Fin du jeu

        # Vérifier si le jeu est un match nul
        if is_board_full():
            print_board()  # Afficher le plateau final
            print("Match nul !")  # Annoncer le match nul
            break  # Fin du jeu

        # Changer de joueur
        current_player = 'O' if current_player == 'X' else 'X'  # Alterner entre X et O

# Lancer le jeu
play_game()