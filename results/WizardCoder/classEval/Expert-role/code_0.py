
import random

class Battleship:
    def __init__(self):
        self.board = self.make_board()
        self.ships = self.locate_ships()

    @staticmethod
    def make_board():
        return [["."]*10 for _ in range(10)]

    def locate_ships(self):
        ship_list = []
        for _ in range(5):
            while True:
                x = random.randint(0, 9)
                y = random.randint(0, 9)
                if (x, y) not in ship_list:
                    ship_list.append((x, y))
                    break
        return ship_list

    def print_board(self):
        for row in self.board:
            print(" ".join(row))

    def guess(self, x, y):
        if (x, y) in self.ships:
            self.board[x][y] = "X"
            print("Hit")
            self.ships.remove((x, y))
            if not self.ships:
                print("You win")
        else:
            self.board[x][y] = "O"
            print("Miss")

game = Battleship()
game.print_board()

while True:
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    game.guess(x, y)
    game.print_board()


