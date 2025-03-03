import random

class Battleship:
    def __init__(self):
        self.board_size = 5
        self.board = [['~' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.ships = []
        self.is_game_over = False

    def place_ships(self):
        for _ in range(3):  # Place 3 ships
            while True:
                ship_row = random.randint(0, self.board_size - 1)
                ship_col = random.randint(0, self.board_size - 1)
                if (ship_row, ship_col) not in self.ships:
                    self.ships.append((ship_row, ship_col))
                    break

    def print_board(self):
        print("  " + " ".join(str(i) for i in range(self.board_size)))
        for idx, row in enumerate(self.board):
            print(idx, " ".join(row))

    def make_guess(self, row, col):
        if (row, col) in self.ships:
            self.board[row][col] = 'X'
            self.ships.remove((row, col))
            print("Hit!")
        else:
            self.board[row][col] = 'O'
            print("Miss!")

        if not self.ships:
            self.is_game_over = True
            print("Congratulations! You've sunk all the ships!")

    def get_guess(self):
        while True:
            try:
                guess = input("Enter your guess (row and column): ")
                row, col = map(int, guess.split())
                if 0 <= row < self.board_size and 0 <= col < self.board_size:
                    return row, col
                else:
                    print("Invalid input. Please enter numbers between 0 and 4.")
            except ValueError:
                print("Invalid input. Please enter row and column as two integers separated by a space.")

    def play(self):
        self.place_ships()
        print("Welcome to Battleship!")
        while not self.is_game_over:
            self.print_board()
            row, col = self.get_guess()
            self.make_guess(row, col)
        self.print_board()
        print("Game Over!")

if __name__ == "__main__":
    game = Battleship()
    game.play()