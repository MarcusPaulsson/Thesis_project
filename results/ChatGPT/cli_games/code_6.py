import random

class Battleship:
    def __init__(self, size=5, ships=3):
        self.size = size
        self.ships = ships
        self.board = [['~' for _ in range(size)] for _ in range(size)]
        self.ships_coords = set()
        self.guesses = set()
        self.place_ships()

    def place_ships(self):
        while len(self.ships_coords) < self.ships:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            self.ships_coords.add((x, y))

    def print_board(self, show_ships=False):
        print("  " + " ".join(str(i) for i in range(self.size)))
        for i in range(self.size):
            row = " ".join(self.board[i][j] if (i, j) not in self.ships_coords or show_ships else "~" for j in range(self.size))
            print(f"{i} {row}")

    def make_guess(self, x, y):
        if (x, y) in self.guesses:
            print("You already guessed that!")
            return False
        self.guesses.add((x, y))
        if (x, y) in self.ships_coords:
            self.board[x][y] = 'X'
            print("Hit!")
            return True
        else:
            self.board[x][y] = 'O'
            print("Miss!")
            return False

    def play(self):
        print("Welcome to Battleship!")
        while len(self.guesses) < self.size * self.size and len(self.ships_coords) > 0:
            self.print_board()
            try:
                x = int(input("Enter row (0-indexed): "))
                y = int(input("Enter column (0-indexed): "))
                if x < 0 or x >= self.size or y < 0 or y >= self.size:
                    print("Invalid coordinates. Try again.")
                    continue
                hit = self.make_guess(x, y)
                if hit and (x, y) in self.ships_coords:
                    self.ships_coords.remove((x, y))
                    if len(self.ships_coords) == 0:
                        print("You've sunk all the ships! You win!")
                        self.print_board(show_ships=True)
                        return
            except ValueError:
                print("Invalid input. Please enter numbers.")

        print("Game Over! You ran out of guesses.")
        self.print_board(show_ships=True)

if __name__ == "__main__":
    game = Battleship()
    game.play()