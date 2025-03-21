import random

class LightsOut:
    def __init__(self, size=5):
        self.size = size
        self.board = [[random.choice([True, False]) for _ in range(size)] for _ in range(size)]
        self.is_solved = False

    def display_board(self):
        for row in self.board:
            print(" ".join(['O' if cell else 'X' for cell in row]))
        print()

    def toggle(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            self.board[row][col] = not self.board[row][col]
            if row > 0: self.board[row - 1][col] = not self.board[row - 1][col]
            if row < self.size - 1: self.board[row + 1][col] = not self.board[row + 1][col]
            if col > 0: self.board[row][col - 1] = not self.board[row][col - 1]
            if col < self.size - 1: self.board[row][col + 1] = not self.board[row][col + 1]

    def check_solved(self):
        self.is_solved = all(not cell for row in self.board for cell in row)

    def play(self):
        while not self.is_solved:
            self.display_board()
            try:
                move = input(f"Enter your move (row col) or 'quit' to exit: ")
                if move.lower() == 'quit':
                    print("Thanks for playing!")
                    break
                row, col = map(int, move.split())
                self.toggle(row, col)
                self.check_solved()
            except (ValueError, IndexError):
                print("Invalid move. Please enter valid row and column numbers.")

        if self.is_solved:
            print("Congratulations! You've turned off all the lights!")

if __name__ == "__main__":
    game = LightsOut()
    game.play()