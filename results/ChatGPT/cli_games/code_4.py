import random

class Minesweeper:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.board = self.create_board()
        self.revealed = [[False] * width for _ in range(height)]
        self.game_over = False

    def create_board(self):
        board = [['0'] * self.width for _ in range(self.height)]
        mine_positions = random.sample(range(self.width * self.height), self.mines)

        for pos in mine_positions:
            row, col = divmod(pos, self.width)
            board[row][col] = '*'
            for r in range(max(0, row - 1), min(self.height, row + 2)):
                for c in range(max(0, col - 1), min(self.width, col + 2)):
                    if board[r][c] != '*':
                        board[r][c] = str(int(board[r][c]) + 1)

        return board

    def reveal(self, row, col):
        if self.revealed[row][col]:
            return
        self.revealed[row][col] = True

        if self.board[row][col] == '*':
            self.game_over = True
            return
        elif self.board[row][col] == '0':
            for r in range(max(0, row - 1), min(self.height, row + 2)):
                for c in range(max(0, col - 1), min(self.width, col + 2)):
                    if not self.revealed[r][c]:
                        self.reveal(r, c)

    def print_board(self):
        for r in range(self.height):
            for c in range(self.width):
                if self.revealed[r][c]:
                    print(self.board[r][c], end=' ')
                else:
                    print('.', end=' ')
            print()
        print()

    def play(self):
        while not self.game_over:
            self.print_board()
            try:
                row, col = map(int, input("Enter row and column to reveal (e.g., 0 1): ").split())
                if 0 <= row < self.height and 0 <= col < self.width:
                    self.reveal(row, col)
                else:
                    print("Invalid input. Please enter valid coordinates.")
            except ValueError:
                print("Invalid input. Please enter two integers.")

        print("Game Over! You hit a mine.")
        self.print_board()

if __name__ == "__main__":
    width = 10
    height = 10
    mines = 10
    game = Minesweeper(width, height, mines)
    game.play()