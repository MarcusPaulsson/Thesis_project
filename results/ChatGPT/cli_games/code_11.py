import random

class LightsOut:
    def __init__(self, size=5):
        self.size = size
        self.board = self.generate_board()

    def generate_board(self):
        return [[random.choice([0, 1]) for _ in range(self.size)] for _ in range(self.size)]

    def display_board(self):
        for row in self.board:
            print(" ".join("■" if cell == 1 else "□" for cell in row))
        print()

    def toggle(self, x, y):
        self.board[x][y] ^= 1  # Toggle the current light
        # Toggle adjacent lights
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                self.board[nx][ny] ^= 1

    def is_solved(self):
        return all(cell == 0 for row in self.board for cell in row)

    def play(self):
        while not self.is_solved():
            self.display_board()
            try:
                move = input(f"Enter your move (row and column) or 'q' to quit: ")
                if move.lower() == 'q':
                    print("Thanks for playing!")
                    break
                x, y = map(int, move.split())
                if 0 <= x < self.size and 0 <= y < self.size:
                    self.toggle(x, y)
                else:
                    print("Invalid move. Please enter valid row and column numbers.")
            except (ValueError, IndexError):
                print("Invalid input. Please enter two integers separated by space.")

        if self.is_solved():
            print("Congratulations! You've turned off all the lights!")

if __name__ == "__main__":
    game = LightsOut()
    game.play()