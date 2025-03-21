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
        mine_positions = random.sample(range(self.width * self.height), self.mines)
        for pos in mine_positions:
            x = pos % self.width
            y = pos // self.width
            self.board[y][x] = '*'
            self.update_numbers(x, y)

    def update_numbers(self, x, y):
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < self.width and 0 <= y + j < self.height and self.board[y + j][x + i] != '*':
                    if self.board[y + j][x + i] == ' ':
                        self.board[y + j][x + i] = 1
                    else:
                        self.board[y + j][x + i] += 1

    def reveal(self, x, y):
        if self.board[y][x] == '*':
            self.game_over = True
            return
        
        if self.visible[y][x] == ' ':
            self.visible[y][x] = self.board[y][x]
            if self.board[y][x] == 0:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= x + i < self.width and 0 <= y + j < self.height:
                            self.reveal(x + i, y + j)

    def display(self):
        print("Current Board:")
        for row in self.visible:
            print(' '.join(str(cell) for cell in row))
        if self.game_over:
            print("Game Over! You hit a mine.")

    def play(self):
        while not self.game_over:
            self.display()
            try:
                x, y = map(int, input("Enter coordinates (x y): ").split())
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.reveal(x, y)
                else:
                    print("Coordinates out of bounds.")
            except ValueError:
                print("Invalid input. Please enter two integers.")

if __name__ == "__main__":
    width = 10
    height = 10
    mines = 10
    game = Minesweeper(width, height, mines)
    game.play()