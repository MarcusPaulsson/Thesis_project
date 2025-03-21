import random

class Battleship:
    def __init__(self, size=5, ships=3):
        self.size = size
        self.ships = ships
        self.board = [['~' for _ in range(size)] for _ in range(size)]
        self.ship_positions = set()
        self.hits = 0
        self.place_ships()

    def place_ships(self):
        while len(self.ship_positions) < self.ships:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            self.ship_positions.add((x, y))

    def print_board(self):
        print("  " + " ".join(str(i) for i in range(self.size)))
        for idx, row in enumerate(self.board):
            print(str(idx) + " " + " ".join(row))

    def take_turn(self, x, y):
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
                x, y = map(int, input("Enter coordinates (row and column) to attack: ").split())
                if 0 <= x < self.size and 0 <= y < self.size:
                    self.take_turn(x, y)
                else:
                    print("Coordinates out of bounds. Try again.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")
        print("Congratulations! You've sunk all the ships.")

if __name__ == "__main__":
    game = Battleship(size=5, ships=3)
    game.play()