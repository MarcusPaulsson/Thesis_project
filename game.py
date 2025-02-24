import random

class Board:
    def __init__(self, size):
        self.size = size
        self.board = [['~' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def place_ship(self, ship):
        self.ships.append(ship)
        for (x, y) in ship.coordinates:
            self.board[x][y] = 'S'

    def display(self):
        print(""  "" + "" "".join(str(i) for i in range(self.size)))
        for idx, row in enumerate(self.board):
            print(idx, "" "".join(row))

    def attack(self, x, y):
        if self.board[x][y] == 'S':
            self.board[x][y] = 'X'
            return True
        elif self.board[x][y] == '~':
            self.board[x][y] = 'O'
            return False
        return None

class Ship:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.coordinates = []

    def set_coordinates(self, coords):
        self.coordinates = coords

class Game:
    def __init__(self, size, ships):
        self.board = Board(size)
        self.ships = ships
        self.setup_game()

    def setup_game(self):
        for ship in self.ships:
            while True:
                direction = random.choice(['H', 'V'])
                if direction == 'H':
                    x = random.randint(0, self.board.size - 1)
                    y = random.randint(0, self.board.size - ship.size)
                    coords = [(x, y + i) for i in range(ship.size)]
                else:
                    x = random.randint(0, self.board.size - ship.size)
                    y = random.randint(0, self.board.size - 1)
                    coords = [(x + i, y) for i in range(ship.size)]

                if all((c[0] < self.board.size and c[1] < self.board.size and 
                        self.board.board[c[0]][c[1]] == '~') for c in coords):
                    ship.set_coordinates(coords)
                    self.board.place_ship(ship)
                    break

    def play(self):
        turns = 0
        while True:
            self.board.display()
            x = int(input("Enter the row (0 to {}): ".format(self.board.size - 1)))
            y = int(input("Enter the column (0 to {}): ".format(self.board.size - 1)))

            if x < 0 or x >= self.board.size or y < 0 or y >= self.board.size:
                print("Invalid coordinates, try again.")
                continue

            result = self.board.attack(x, y)
            turns += 1

            if result is None:
                print("You already attacked this position.")
            elif result:
                print("Hit!")
            else:
                print("Miss!")

            if all(cell == 'X' for ship in self.ships for cell in ship.coordinates):
                print("Congratulations! You've sunk all the ships in {} turns.".format(turns))
                break

def main():
    size = 5
    ships = [Ship("Destroyer", 2), Ship("Submarine", 3), Ship("Battleship", 4)]
    game = Game(size, ships)
    game.play()

if __name__ == "__main__":
    main()