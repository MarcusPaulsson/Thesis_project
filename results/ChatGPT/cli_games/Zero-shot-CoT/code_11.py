import random

class LightsOut:
    def __init__(self, size=5):
        self.size = size
        self.board = self.generate_board()
        self.is_solved = False

    def generate_board(self):
        return [[random.choice([0, 1]) for _ in range(self.size)] for _ in range(self.size)]

    def display_board(self):
        for row in self.board:
            print(' '.join(['O' if col == 1 else '.' for col in row]))
        print()

    def toggle(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            self.board[row][col] ^= 1  # Toggle the light
            if row > 0:  # Toggle the light above
                self.board[row - 1][col] ^= 1
            if row < self.size - 1:  # Toggle the light below
                self.board[row + 1][col] ^= 1
            if col > 0:  # Toggle the light to the left
                self.board[row][col - 1] ^= 1
            if col < self.size - 1:  # Toggle the light to the right
                self.board[row][col + 1] ^= 1

    def check_solved(self):
        self.is_solved = all(col == 0 for row in self.board for col in row)

    def play(self):
        print("Welcome to Lights Out!")
        while not self.is_solved:
            self.display_board()
            try:
                move = input("Enter your move as 'row col' (or 'quit' to exit): ")
                if move.lower() == 'quit':
                    print("Thanks for playing!")
                    break
                row, col = map(int, move.split())
                self.toggle(row, col)
                self.check_solved()
                if self.is_solved:
                    self.display_board()
                    print("Congratulations! You've solved the puzzle!")
            except (ValueError, IndexError):
                print("Invalid input. Please enter a valid row and column.")

if __name__ == "__main__":
    game = LightsOut()
    game.play()