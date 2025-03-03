import random

class Board:
    def __init__(self, size=5):
        self.size = size
        self.board = [['~' for _ in range(size)] for _ in range(size)]
        self.ships = []

    def place_ship(self, length):
        placed = False
        while not placed:
            orientation = random.choice(['H', 'V'])
            if orientation == 'H':
                row = random.randint(0, self.size - 1)
                col = random.randint(0, self.size - length)
                if all(self.board[row][col + i] == '~' for i in range(length)):
                    for i in range(length):
                        self.board[row][col + i] = 'S'
                    self.ships.append((row, col, orientation, length))
                    placed = True
            else:
                row = random.randint(0, self.size - length)
                col = random.randint(0, self.size - 1)
                if all(self.board[row + i][col] == '~' for i in range(length)):
                    for i in range(length):
                        self.board[row + i][col] = 'S'
                    self.ships.append((row, col, orientation, length))
                    placed = True

    def display_board(self, reveal=False):
        for row in self.board:
            print(' '.join(row if reveal else ['~' if cell == 'S' else cell for cell in row]))

    def make_guess(self, row, col):
        if self.board[row][col] == 'S':
            self.board[row][col] = 'X'  # Hit
            return True
        elif self.board[row][col] == '~':
            self.board[row][col] = 'O'  # Miss
            return False
        return None  # Already guessed

    def all_ships_sunk(self):
        return all(self.board[row][col] != 'S' for row, col, orientation, length in self.ships)

class BattleshipGame:
    def __init__(self):
        self.board = Board()
        self.setup_game()
        self.turns = 0

    def setup_game(self):
        ship_lengths = [2, 3, 3, 4, 5]
        for length in ship_lengths:
            self.board.place_ship(length)

    def play(self):
        print("Welcome to Battleship!")
        while True:
            self.board.display_board()
            try:
                row = int(input("Enter row (0-4): "))
                col = int(input("Enter column (0-4): "))
                if row < 0 or row >= self.board.size or col < 0 or col >= self.board.size:
                    print("Invalid input. Try again.")
                    continue
                result = self.board.make_guess(row, col)
                self.turns += 1
                if result is True:
                    print("Hit!")
                elif result is False:
                    print("Miss!")
                else:
                    print("You already guessed that!")
                
                if self.board.all_ships_sunk():
                    print(f"Congratulations! You've sunk all the ships in {self.turns} turns.")
                    break
            except ValueError:
                print("Please enter valid integers for row and column.")

if __name__ == '__main__':
    game = BattleshipGame()
    game.play()