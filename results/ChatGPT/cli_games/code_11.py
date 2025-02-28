import random

class LightsOut:
    def __init__(self, size=5):
        self.size = size
        self.board = [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]

    def toggle(self, x, y):
        if 0 <= x < self.size and 0 <= y < self.size:
            self.board[x][y] ^= 1  # Toggle the light
            # Toggle the adjacent lights
            if x > 0: self.board[x - 1][y] ^= 1
            if x < self.size - 1: self.board[x + 1][y] ^= 1
            if y > 0: self.board[x][y - 1] ^= 1
            if y < self.size - 1: self.board[x][y + 1] ^= 1

    def print_board(self):
        for row in self.board:
            print(" ".join("O" if cell else "X" for cell in row))
        print()

    def is_solved(self):
        return all(cell == 0 for row in self.board for cell in row)

    def play(self):
        print("Welcome to Lights Out!")
        while not self.is_solved():
            self.print_board()
            try:
                x, y = map(int, input("Enter row and column to toggle (0-indexed, separated by space): ").split())
                self.toggle(x, y)
            except (ValueError, IndexError):
                print("Invalid input, please enter valid coordinates.")
        print("Congratulations! You've turned off all the lights!")

if __name__ == "__main__":
    game = LightsOut()
    game.play()