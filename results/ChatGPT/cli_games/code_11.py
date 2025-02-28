import random

class LightsOut:
    def __init__(self, size=5):
        self.size = size
        self.board = self.create_board()
        self.is_game_over = False

    def create_board(self):
        board = [[random.choice([0, 1]) for _ in range(self.size)] for _ in range(self.size)]
        return board

    def toggle_light(self, row, col):
        if 0 <= row < self.size and 0 <= col < self.size:
            self.board[row][col] ^= 1  # Toggle the light
            # Toggle adjacent lights
            if row > 0:
                self.board[row - 1][col] ^= 1
            if row < self.size - 1:
                self.board[row + 1][col] ^= 1
            if col > 0:
                self.board[row][col - 1] ^= 1
            if col < self.size - 1:
                self.board[row][col + 1] ^= 1

    def print_board(self):
        for row in self.board:
            print(' '.join(['O' if light == 1 else 'X' for light in row]))
        print()

    def check_win(self):
        return all(light == 0 for row in self.board for light in row)

    def play(self):
        print("Welcome to Lights Out!")
        while not self.is_game_over:
            self.print_board()
            row = int(input(f"Enter row (0-{self.size-1}): "))
            col = int(input(f"Enter column (0-{self.size-1}): "))
            self.toggle_light(row, col)
            if self.check_win():
                self.is_game_over = True
                print("Congratulations! You've turned off all the lights!")
        self.print_board()

if __name__ == "__main__":
    game = LightsOut()
    game.play()