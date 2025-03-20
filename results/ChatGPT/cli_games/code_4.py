import random

class Minesweeper:
    def __init__(self, width=10, height=10, mines=10):
        self.width = width
        self.height = height
        self.mines = mines
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.visible = [[' ' for _ in range(width)] for _ in range(height)]
        self.game_over = False
        self.populate_mines()
        self.calculate_numbers()

    def populate_mines(self):
        mine_positions = set()
        while len(mine_positions) < self.mines:
            pos = (random.randint(0, self.height - 1), random.randint(0, self.width - 1))
            mine_positions.add(pos)
        for (y, x) in mine_positions:
            self.board[y][x] = '*'

    def calculate_numbers(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == '*':
                    continue
                count = sum((ny, nx) in self.board for ny in range(max(0, y - 1), min(self.height, y + 2))
                             for nx in range(max(0, x - 1), min(self.width, x + 2)) if self.board[ny][nx] == '*')
                if count > 0:
                    self.board[y][x] = str(count)

    def reveal(self, y, x):
        if self.game_over or self.visible[y][x] != ' ':
            return
        self.visible[y][x] = self.board[y][x]
        if self.board[y][x] == '*':
            self.game_over = True
            return
        if self.board[y][x] == ' ':
            for ny in range(max(0, y - 1), min(self.height, y + 2)):
                for nx in range(max(0, x - 1), min(self.width, x + 2)):
                    self.reveal(ny, nx)

    def print_board(self):
        print("   " + " ".join(str(x) for x in range(self.width)))
        for y in range(self.height):
            print(f"{y} |", end=" ")
            for x in range(self.width):
                print(self.visible[y][x], end=" ")
            print()

    def play(self):
        while not self.game_over:
            self.print_board()
            try:
                y, x = map(int, input("Enter row and column (y x): ").split())
                if 0 <= y < self.height and 0 <= x < self.width:
                    self.reveal(y, x)
                else:
                    print("Invalid coordinates. Try again.")
            except ValueError:
                print("Invalid input. Please enter two numbers.")

        print("Game Over!")
        self.print_board()


if __name__ == "__main__":
    game = Minesweeper()
    game.play()