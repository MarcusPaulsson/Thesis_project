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
        self.calculate_numbers()

    def populate_mines(self):
        placed_mines = 0
        while placed_mines < self.mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] != '*':
                self.board[y][x] = '*'
                placed_mines += 1

    def calculate_numbers(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == '*':
                    continue
                self.board[y][x] = str(self.count_adjacent_mines(x, y))

    def count_adjacent_mines(self, x, y):
        count = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dy == 0 and dx == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.board[ny][nx] == '*':
                    count += 1
        return count

    def reveal(self, x, y):
        if self.game_over or self.visible[y][x] != ' ':
            return
        self.visible[y][x] = self.board[y][x]
        if self.board[y][x] == '*':
            self.game_over = True
            return
        if self.board[y][x] == '0':
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if 0 <= x + dx < self.width and 0 <= y + dy < self.height:
                        self.reveal(x + dx, y + dy)

    def display(self):
        print("Current Board:")
        for y in range(self.height):
            for x in range(self.width):
                print(self.visible[y][x], end=' ')
            print()
        print()

    def play(self):
        while not self.game_over:
            self.display()
            try:
                x, y = map(int, input("Enter coordinates to reveal (x y): ").split())
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.reveal(x, y)
                else:
                    print("Coordinates out of bounds. Try again.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")
        print("Game Over! You hit a mine.")
        self.display()

if __name__ == "__main__":
    width = int(input("Enter board width: "))
    height = int(input("Enter board height: "))
    mines = int(input("Enter number of mines: "))
    game = Minesweeper(width, height, mines)
    game.play()