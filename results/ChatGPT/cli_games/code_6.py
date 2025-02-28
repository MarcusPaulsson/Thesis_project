import random

class Board:
    def __init__(self):
        self.size = 5
        self.board = [['~' for _ in range(self.size)] for _ in range(self.size)]
        self.ships = []

    def place_ship(self, ship_size):
        placed = False
        while not placed:
            orientation = random.choice(['H', 'V'])
            if orientation == 'H':
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - ship_size)
                if all(self.board[row][col + i] == '~' for i in range(ship_size)):
                    for i in range(ship_size):
                        self.board[row][col + i] = 'S'
                    self.ships.append((row, col, orientation, ship_size))
                    placed = True
            else:
                row = random.randint(0, self.size - ship_size)
                col = random.randint(0, self.size - 1)
                if all(self.board[row + i][col] == '~' for i in range(ship_size)):
                    for i in range(ship_size):
                        self.board[row + i][col] = 'S'
                    self.ships.append((row, col, orientation, ship_size))
                    placed = True

    def display(self):
        print("  " + " ".join(str(i) for i in range(self.size)))
        for i, row in enumerate(self.board):
            print(i, " ".join(row))

    def attack(self, row, col):
        if self.board[row][col] == 'S':
            self.board[row][col] = 'X'
            return True
        elif self.board[row][col] == '~':
            self.board[row][col] = 'O'
            return False
        return None

    def all_ships_sunk(self):
        return all(self.board[i][j] != 'S' for i in range(self.size) for j in range(self.size))


class Game:
    def __init__(self):
        self.board = Board()
        self.ships_sizes = [2, 3]
        for size in self.ships_sizes:
            self.board.place_ship(size)

    def play(self):
        while not self.board.all_ships_sunk():
            self.board.display()
            try:
                guess = input("Enter your attack coordinates (row col): ")
                row, col = map(int, guess.split())
                if row < 0 or row >= self.board.size or col < 0 or col >= self.board.size:
                    print("Coordinates out of bounds! Try again.")
                    continue
                result = self.board.attack(row, col)
                if result is True:
                    print("Hit!")
                elif result is False:
                    print("Miss!")
                else:
                    print("Already attacked this position!")
            except (ValueError, IndexError):
                print("Invalid input! Please enter valid coordinates.")

        print("Congratulations! You've sunk all the ships!")


if __name__ == "__main__":
    game = Game()
    game.play()