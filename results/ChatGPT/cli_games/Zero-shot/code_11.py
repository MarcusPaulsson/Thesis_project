import random

class LightsOut:
    def __init__(self, size=5):
        self.size = size
        self.board = self.generate_board()
        self.is_solved = False

    def generate_board(self):
        return [[random.choice([0, 1]) for _ in range(self.size)] for _ in range(self.size)]

    def toggle_light(self, x, y):
        if 0 <= x < self.size and 0 <= y < self.size:
            self.board[x][y] ^= 1
            if x > 0: self.board[x-1][y] ^= 1
            if x < self.size - 1: self.board[x+1][y] ^= 1
            if y > 0: self.board[x][y-1] ^= 1
            if y < self.size - 1: self.board[x][y+1] ^= 1

    def check_solved(self):
        self.is_solved = all(light == 0 for row in self.board for light in row)

    def display_board(self):
        for row in self.board:
            print(' '.join(['O' if light else '.' for light in row]))
        print()

    def play(self):
        while not self.is_solved:
            self.display_board()
            try:
                x, y = map(int, input(f"Enter coordinates to toggle (row col) [0-{self.size-1}]: ").split())
                self.toggle_light(x, y)
                self.check_solved()
            except (ValueError, IndexError):
                print("Invalid input. Please enter valid coordinates.")

        print("Congratulations! You've solved the puzzle!")

if __name__ == "__main__":
    game = LightsOut()
    game.play()