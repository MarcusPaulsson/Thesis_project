import random

class Battleship:
    def __init__(self, size=5, ships=3):
        self.size = size
        self.ships = ships
        self.board = [['~'] * size for _ in range(size)]
        self.ship_positions = set()
        self.hits = 0
        self.place_ships()

    def place_ships(self):
        while len(self.ship_positions) < self.ships:
            x = random.randint(0, self.size - 1)
            y = random.randint(0, self.size - 1)
            self.ship_positions.add((x, y))

    def print_board(self):
        print("  " + " ".join(str(i) for i in range(self.size)))
        for idx, row in enumerate(self.board):
            print(idx, " ".join(row))

    def make_guess(self, x, y):
        if (x, y) in self.ship_positions:
            self.board[x][y] = 'X'
            self.ship_positions.remove((x, y))
            self.hits += 1
            print("Hit!")
        else:
            self.board[x][y] = 'O'
            print("Miss!")

    def is_game_over(self):
        return self.hits == self.ships

    def play(self):
        print("Welcome to Battleship!")
        while not self.is_game_over():
            self.print_board()
            try:
                guess = input("Enter your guess (row col): ")
                x, y = map(int, guess.split())
                if 0 <= x < self.size and 0 <= y < self.size:
                    self.make_guess(x, y)
                else:
                    print("Please enter valid coordinates.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column numbers.")

        print("Congratulations! You've sunk all the ships!")

if __name__ == "__main__":
    game = Battleship()
    game.play()