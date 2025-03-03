import random

class LightsOut:
    def __init__(self, size=5):
        self.size = size
        self.board = self.generate_board()
    
    def generate_board(self):
        return [[random.choice([0, 1]) for _ in range(self.size)] for _ in range(self.size)]

    def display_board(self):
        for row in self.board:
            print(" ".join(['☼' if cell else '◯' for cell in row]))
        print()

    def toggle(self, row, col):
        self.board[row][col] ^= 1  # Toggle the selected cell
        # Toggle adjacent cells
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            r, c = row + dr, col + dc
            if 0 <= r < self.size and 0 <= c < self.size:
                self.board[r][c] ^= 1

    def is_solved(self):
        return all(cell == 0 for row in self.board for cell in row)

    def play(self):
        while not self.is_solved():
            self.display_board()
            try:
                row, col = map(int, input(f"Enter row and column (0-{self.size-1}): ").split())
                if 0 <= row < self.size and 0 <= col < self.size:
                    self.toggle(row, col)
                else:
                    print(f"Please enter values between 0 and {self.size-1}.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by space.")
        
        self.display_board()
        print("Congratulations! You've solved the puzzle.")

if __name__ == "__main__":
    game = LightsOut(size=5)
    game.play()