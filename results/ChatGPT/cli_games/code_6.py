import random

class Ship:
    def __init__(self, size):
        self.size = size
        self.hits = 0

    def hit(self):
        self.hits += 1

    def is_sunk(self):
        return self.hits >= self.size


class Board:
    def __init__(self, size):
        self.size = size
        self.board = [[' ' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def place_ship(self, ship, x, y, orientation):
        if orientation == 'H':
            for i in range(ship.size):
                self.board[x][y + i] = 'S'
        else:
            for i in range(ship.size):
                self.board[x + i][y] = 'S'
        self.ships.append(ship)

    def display(self, show_ships=False):
        print("  " + " ".join(str(i) for i in range(self.size)))
        for i in range(self.size):
            row = str(i) + " "
            for j in range(self.size):
                cell = self.board[i][j]
                if cell == 'S' and not show_ships:
                    row += '. '
                else:
                    row += cell + ' '
            print(row)

    def attack(self, x, y):
        if self.board[x][y] == 'S':
            self.board[x][y] = 'H'
            for ship in self.ships:
                if ship.size > 0:
                    ship.hit()
                    return True
        else:
            self.board[x][y] = 'M'
        return False

    def all_sunk(self):
        return all(ship.is_sunk() for ship in self.ships)


class Game:
    def __init__(self, size=5):
        self.board = Board(size)
        self.setup()

    def setup(self):
        ship_sizes = [2, 3]
        for size in ship_sizes:
            placed = False
            while not placed:
                x = random.randint(0, self.board.size - 1)
                y = random.randint(0, self.board.size - 1)
                orientation = random.choice(['H', 'V'])
                if self.can_place_ship(x, y, size, orientation):
                    self.board.place_ship(Ship(size), x, y, orientation)
                    placed = True

    def can_place_ship(self, x, y, size, orientation):
        if orientation == 'H':
            if y + size > self.board.size:
                return False
            return all(self.board.board[x][y + i] == ' ' for i in range(size))
        else:
            if x + size > self.board.size:
                return False
            return all(self.board.board[x + i][y] == ' ' for i in range(size))

    def play(self):
        while True:
            self.board.display()
            try:
                x = int(input("Enter row (0-{}): ".format(self.board.size - 1)))
                y = int(input("Enter column (0-{}): ".format(self.board.size - 1)))
                if self.board.attack(x, y):
                    print("Hit!")
                else:
                    print("Miss!")
            except (ValueError, IndexError):
                print("Invalid input. Please try again.")
                continue

            if self.board.all_sunk():
                print("All ships sunk! You win!")
                self.board.display(show_ships=True)
                break


if __name__ == '__main__':
    game = Game(size=5)
    game.play()