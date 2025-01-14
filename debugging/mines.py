#!/usr/bin/python3
import random
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        # Création des mines de manière aléatoire
        self.mines = set(random.sample(range(width * height), mines))
        # Création du tableau de jeu
        self.field = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[False for _ in range(width)] for _ in range(height)]

    def print_board(self, reveal=False):
        clear_screen()
        print('  ' + ' '.join(str(i) for i in range(self.width)))
        for y in range(self.height):
            print(y, end=' ')
            for x in range(self.width):
                if reveal or self.revealed[y][x]:
                    if (y * self.width + x) in self.mines:
                        print('*', end=' ')  # Affiche la mine
                    else:
                        count = self.count_mines_nearby(x, y)
                        print(count if count > 0 else ' ', end=' ')  # Affiche le nombre de mines voisines
                else:
                    print('.', end=' ')  # Affiche un point pour les cases non révélées
            print()

    def count_mines_nearby(self, x, y):
        count = 0
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height:
                    if (ny * self.width + nx) in self.mines:
                        count += 1
        return count

    def reveal(self, x, y):
        # Si la case est une mine, on retourne False (jeu perdu)
        if (y * self.width + x) in self.mines:
            return False
        # Révéler la case
        self.revealed[y][x] = True
        # Si la case ne contient pas de mine, on révèle aussi ses voisines si elles sont vides
        if self.count_mines_nearby(x, y) == 0:
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                        self.reveal(nx, ny)
        return True

    def is_victory(self):
        # Vérifie si toutes les cases non-minées ont été révélées
        for y in range(self.height):
            for x in range(self.width):
                if (y * self.width + x) not in self.mines and not self.revealed[y][x]:
                    return False
        return True

    def play(self):
        while True:
            self.print_board()
            try:
                # Demander à l'utilisateur de saisir les coordonnées x et y
                x = int(input("Enter x coordinate: "))
                y = int(input("Enter y coordinate: "))
                
                # Si on touche une mine, afficher la grille révélée et terminer le jeu
                if not self.reveal(x, y):
                    self.print_board(reveal=True)
                    print("Game Over! You hit a mine.")
                    break

                # Vérifier si toutes les cases non-minées ont été révélées
                if self.is_victory():
                    self.print_board(reveal=True)
                    print("Congratulations! You've won the game.")
                    break
            except ValueError:
                print("Invalid input. Please enter numbers only.")

if __name__ == "__main__":
    game = Minesweeper()
    game.play()

