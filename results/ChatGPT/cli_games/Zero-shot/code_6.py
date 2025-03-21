import random

class Battleship:
    def __init__(self, size=5, ships=3):
        self.size = size
        self.ships = ships
        self.board = [['~' for _ in range(size)] for _ in range(size)]
        self.ships_locations = []
        self.hits = 0
        self.place_ships()

    def place_ships(self):
        while len(self.ships_locations) < self.ships:
            ship_location = (random.randint(0, self.size-1), random.randint(0, self.size-1))
            if ship_location not in self.ships_locations:
                self.ships_locations.append(ship_location)

    def print_board(self):
        print("  " + " ".join(str(i) for i in range(self.size)))
        for i, row in enumerate(self.board):
            print(str(i) + " " + " ".join(row))

    def make_guess(self, x, y):
        if (x, y) in self.ships_locations:
            self.board[x][y] = 'X'
            self.ships_locations.remove((x, y))
            self.hits += 1
            print("Hit!")
            return True
        elif self.board[x][y] == '~':
            self.board[x][y] = 'O'
            print("Miss!")
            return False
        else:
            print("You already guessed that!")
            return False

    def is_game_over(self):
        return self.hits == self.ships

    def play(self):
        print("Welcome to Battleship!")
        while not self.is_game_over():
            self.print_board()
            try:
                x, y = map(int, input("Enter your guess (row and column): ").split())
                if x < 0 or x >= self.size or y < 0 or y >= self.size:
                    print("Out of bounds! Please try again.")
                    continue
                self.make_guess(x, y)
            except ValueError:
                print("Invalid input! Please enter row and column as two integers.")

        print("Congratulations! You've sunk all the ships!")

if __name__ == "__main__":
    game = Battleship()
    game.play()