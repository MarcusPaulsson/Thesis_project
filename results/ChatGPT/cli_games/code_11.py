import random

class LightsOut:
    def __init__(self, size=5):
        self.size = size
        self.board = self.generate_board()
    
    def generate_board(self):
        return [[random.choice([0, 1]) for _ in range(self.size)] for _ in range(self.size)]

    def toggle(self, row, col):
        self.board[row][col] ^= 1  # Toggle the selected light
        if row > 0:
            self.board[row - 1][col] ^= 1  # Toggle above
        if row < self.size - 1:
            self.board[row + 1][col] ^= 1  # Toggle below
        if col > 0:
            self.board[row][col - 1] ^= 1  # Toggle left
        if col < self.size - 1:
            self.board[row][col + 1] ^= 1  # Toggle right

    def display(self):
        for row in self.board:
            print(" ".join("O" if light else "." for light in row))
        print()

    def is_solved(self):
        return all(all(light == 0 for light in row) for row in self.board)

    def play(self):
        while not self.is_solved():
            self.display()
            try:
                row, col = map(int, input("Enter row and column to toggle (0-indexed): ").split())
                if 0 <= row < self.size and 0 <= col < self.size:
                    self.toggle(row, col)
                else:
                    print("Invalid input. Please enter numbers within the range.")
            except ValueError:
                print("Invalid input. Please enter two integers.")

        print("Congratulations! You've solved the puzzle.")

if __name__ == "__main__":
    game = LightsOut()
    game.play()