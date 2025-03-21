import random

class Minesweeper:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.visible = [[' ' for _ in range(width)] for _ in range(height)]
        self.game_over = False
        self.revealed_count = 0
        self._place_mines()
        self._calculate_adjacent_mines()

    def _place_mines(self):
        positions = random.sample(range(self.width * self.height), self.mines)
        for pos in positions:
            row = pos // self.width
            col = pos % self.width
            self.board[row][col] = '*'

    def _calculate_adjacent_mines(self):
        for row in range(self.height):
            for col in range(self.width):
                if self.board[row][col] == '*':
                    continue
                mine_count = self._count_adjacent_mines(row, col)
                if mine_count > 0:
                    self.board[row][col] = str(mine_count)

    def _count_adjacent_mines(self, row, col):
        count = 0
        for r in range(max(0, row - 1), min(self.height, row + 2)):
            for c in range(max(0, col - 1), min(self.width, col + 2)):
                if self.board[r][c] == '*':
                    count += 1
        return count

    def reveal(self, row, col):
        if self.board[row][col] == '*':
            self.game_over = True
            return
        if self.visible[row][col] == ' ':
            self.visible[row][col] = self.board[row][col]
            self.revealed_count += 1
            if self.board[row][col] == '0':
                for r in range(max(0, row - 1), min(self.height, row + 2)):
                    for c in range(max(0, col - 1), min(self.width, col + 2)):
                        if (r, c) != (row, col):
                            self.reveal(r, c)

    def print_board(self):
        print("   " + " ".join(str(i) for i in range(self.width)))
        for r in range(self.height):
            print(f"{r} | " + " ".join(self.visible[r]))

    def play(self):
        while not self.game_over and self.revealed_count < self.width * self.height - self.mines:
            self.print_board()
            try:
                row, col = map(int, input("Enter row and column to reveal (e.g., '1 2'): ").strip().split())
                if 0 <= row < self.height and 0 <= col < self.width:
                    self.reveal(row, col)
                else:
                    print("Invalid coordinates. Please try again.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")

        if self.game_over:
            print("Game Over! You hit a mine.")
            self.reveal_all()
            self.print_board()
        else:
            print("Congratulations! You've cleared the minefield.")
            self.print_board()

    def reveal_all(self):
        for r in range(self.height):
            for c in range(self.width):
                if self.board[r][c] == '*':
                    self.visible[r][c] = '*'
                elif self.visible[r][c] == ' ':
                    self.visible[r][c] = self.board[r][c]

if __name__ == "__main__":
    game = Minesweeper(width=10, height=10, mines=10)
    game.play()