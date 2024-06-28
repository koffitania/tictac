import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
                # Initialisation du joueur actuel à 'X' et du plateau de jeu vide (3x3)
        self.current_player = 'X'
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
            # Création de la fenêtre principale avec Tkinter
        self.root = tk.Tk()
        self.root.title("Tic Tac Toe")
           # Initialisation des boutons pour chaque case du plateau
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                  # Création des boutons et association des actions pour chaque bouton
                self.buttons[i][j] = tk.Button(self.root, text=' ', font=('Arial', 20), width=6, height=3,
                                               command=lambda row=i, col=j: self.make_move(row, col))
                   # Placement des boutons dans la grille
                self.buttons[i][j].grid(row=i, column=j)

    def make_move(self, row, col):
           # Vérifie si la case est vide avant de faire un mouvement
        if self.board[row][col] == ' ':
             # Met à jour le plateau de jeu et le texte du bouton
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player)
              # Vérifie si le joueur actuel a gagné
            if self.check_winner():
                messagebox.showinfo("Game Over", f"Player {self.current_player} wins!")
                self.root.quit()
                    # Vérifie si la partie est un match nul
            elif self.check_draw():
                messagebox.showinfo("Game Over", "match nul!")
                
                self.root.quit()
            else:
                 # Change de joueur
                self.current_player = 'O' if self.current_player == 'X' else 'X'

    def check_winner(self):
         # Vérifie les lignes pour un gagnant
        for row in self.board:
            if row[0] == row[1] == row[2] != ' ':
                return True
              # Vérifie les colonnes pour un gagnant
        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != ' ':
                return True
                 # Vérifie les diagonales pour un gagnant
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False
  
    def check_draw(self):
          # Vérifie si toutes les cases sont remplies et qu'il n'y a pas de gagnant
        for row in self.board:
            if ' ' in row:
                return False
        return True

    def play(self):
          # Lance la boucle principale de l'application Tkinter
        self.root.mainloop()
# Création d'une instance du jeu et lancement du jeu
game = TicTacToe()
game.play()
