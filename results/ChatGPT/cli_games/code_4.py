import random

class Minesweeper:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.visible = [[' ' for _ in range(width)] for _ in range(height)]
        self.mines = set()
        self.game_over = False
        self.populate_mines()

    def populate_mines(self):
        while len(self.mines) < self.num_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if (x, y) not in self.mines:
                self.mines.add((x, y))
                self.board[y][x] = '*'
                self.increment_adjacent_cells(x, y)

    def increment_adjacent_cells(self, x, y):
        for i in range(max(0, y - 1), min(self.height, y + 2)):
            for j in range(max(0, x - 1), min(self.width, x + 2)):
                if (j, i) != (x, y) and self.board[i][j] != '*':
                    if self.board[i][j] == ' ':
                        self.board[i][j] = '1'
                    else:
                        self.board[i][j] = str(int(self.board[i][j]) + 1)

    def print_board(self):
        print("   " + " ".join(str(i) for i in range(self.width)))
        for i in range(self.height):
            print(f"{i} | " + " ".join(self.visible[i]))

    def reveal(self, x, y):
        if self.game_over or self.visible[y][x] != ' ':
            return

        if (x, y) in self.mines:
            self.visible[y][x] = '*'
            self.game_over = True
            return

        self.visible[y][x] = self.board[y][x]

        if self.board[y][x] == ' ':
            for i in range(max(0, y - 1), min(self.height, y + 2)):
                for j in range(max(0, x - 1), min(self.width, x + 2)):
                    if (j, i) != (x, y):
                        self.reveal(j, i)

    def play(self):
        while not self.game_over:
            self.print_board()
            try:
                x, y = map(int, input("Enter x and y coordinates (e.g., 0 1): ").split())
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.reveal(x, y)
                else:
                    print("Coordinates out of bounds. Try again.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by space.")

        self.print_board()
        print("Game Over! You hit a mine!")


if __name__ == "__main__":
    width = 10
    height = 10
    num_mines = 10
    game = Minesweeper(width, height, num_mines)
    game.play()