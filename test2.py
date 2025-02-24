import random

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [['~' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def place_ship(self, x, y):
        self.board[x][y] = 'S'
        self.ships.append((x, y))

    def attack(self, x, y):
        if self.board[x][y] == 'S':
            self.board[x][y] = 'X'
            return True
        elif self.board[x][y] == '~':
            self.board[x][y] = 'O'
            return False
        return None

    def print_board(self):
        print("  " + " ".join([str(i) for i in range(self.size)]))
        for idx, row in enumerate(self.board):
            print(str(idx) + " " + " ".join(row))

    def all_ships_sunk(self):
        return all(self.board[x][y] == 'X' for x, y in self.ships)


class Game:
    def __init__(self, size=5, num_ships=3):
        self.board = Board(size)
        self.size = size
        self.num_ships = num_ships
        self.place_ships()

    def place_ships(self):
        while len(self.board.ships) < self.num_ships:
            x, y = random.randint(0, self.size - 1), random.randint(0, self.size - 1)
            if (x, y) not in self.board.ships:
                self.board.place_ship(x, y)

    def play(self):
        while not self.board.all_ships_sunk():
            self.board.print_board()
            try:
                x, y = map(int, input("Enter coordinates to attack (row col): ").split())
                if x < 0 or x >= self.size or y < 0 or y >= self.size:
                    print("Coordinates out of bounds. Try again.")
                    continue
            except ValueError:
                print("Invalid input. Please enter two numbers.")
                continue

            result = self.board.attack(x, y)
            if result is True:
                print("Hit!")
            elif result is False:
                print("Miss!")
            else:
                print("Already attacked that position.")

        print("Congratulations! Youve sunk all the ships!")
        self.board.print_board()


if __name__ == "__main__":
    game = Game(size=5, num_ships=3)
    game.play()