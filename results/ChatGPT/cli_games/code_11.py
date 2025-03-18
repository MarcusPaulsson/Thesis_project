import random

class LightsOut:
    def __init__(self, size=5):
        self.size = size
        self.board = self.generate_board()

    def generate_board(self):
        return [[random.choice([0, 1]) for _ in range(self.size)] for _ in range(self.size)]

    def display_board(self):
        for row in self.board:
            print(" ".join(['O' if cell == 1 else '.' for cell in row]))
        print()

    def toggle(self, x, y):
        if 0 <= x < self.size and 0 <= y < self.size:
            self.board[x][y] ^= 1  # Toggle the light
            # Toggle adjacent lights
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                self.toggle(x + dx, y + dy)

    def is_solved(self):
        return all(cell == 0 for row in self.board for cell in row)

    def play(self):
        while not self.is_solved():
            self.display_board()
            try:
                x, y = map(int, input("Enter row and column to toggle (e.g., '1 2'): ").split())
                self.toggle(x, y)
            except (ValueError, IndexError):
                print("Invalid input, please enter valid row and column numbers.")
        print("Congratulations! You solved the puzzle!")

if __name__ == "__main__":
    game = LightsOut()
    game.play()