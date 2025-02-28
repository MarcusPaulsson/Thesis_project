import random

class Minesweeper:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.visible = [[' ' for _ in range(width)] for _ in range(height)]
        self.game_over = False
        self.populate_mines()

    def populate_mines(self):
        mine_positions = set()
        while len(mine_positions) < self.mines:
            position = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
            mine_positions.add(position)
        for (y, x) in mine_positions:
            self.board[y][x] = '*'
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if 0 <= y + dy < self.height and 0 <= x + dx < self.width:
                        if self.board[y + dy][x + dx] != '*':
                            self.board[y + dy][x + dx] = str(int(self.board[y + dy][x + dx]) + 1) if self.board[y + dy][x + dx] != ' ' else '1'

    def display_board(self):
        print("   " + " ".join(str(x) for x in range(self.width)))
        for y in range(self.height):
            print(f"{y} | " + " ".join(self.visible[y]))

    def reveal(self, y, x):
        if self.board[y][x] == '*':
            self.game_over = True
            return
        self._reveal(y, x)

    def _reveal(self, y, x):
        if self.visible[y][x] == ' ':
            self.visible[y][x] = self.board[y][x]
            if self.board[y][x] == '0':
                for dy in range(-1, 2):
                    for dx in range(-1, 2):
                        if 0 <= y + dy < self.height and 0 <= x + dx < self.width:
                            self._reveal(y + dy, x + dx)

    def play(self):
        while not self.game_over:
            self.display_board()
            try:
                y, x = map(int, input("Enter row and column to reveal (e.g., '1 2'): ").split())
                if 0 <= y < self.height and 0 <= x < self.width:
                    self.reveal(y, x)
                else:
                    print("Invalid coordinates. Please try again.")
            except ValueError:
                print("Invalid input. Please enter two numbers separated by a space.")

        print("Game Over! You hit a mine.")
        self.display_board()

if __name__ == "__main__":
    width = 10
    height = 10
    mines = 10
    game = Minesweeper(width, height, mines)
    game.play()