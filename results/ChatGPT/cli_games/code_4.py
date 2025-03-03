import random

class Minesweeper:
    def __init__(self, width, height, num_mines):
        self.width = width
        self.height = height
        self.num_mines = num_mines
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[' ' for _ in range(width)] for _ in range(height)]
        self.game_over = False
        self.populate_mines()
        self.calculate_numbers()

    def populate_mines(self):
        mines_placed = 0
        while mines_placed < self.num_mines:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.board[y][x] != '*':
                self.board[y][x] = '*'
                mines_placed += 1

    def calculate_numbers(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.board[y][x] == '*':
                    continue
                count = self.count_adjacent_mines(x, y)
                if count > 0:
                    self.board[y][x] = str(count)

    def count_adjacent_mines(self, x, y):
        count = 0
        for dy in range(-1, 2):
            for dx in range(-1, 2):
                if dx == 0 and dy == 0:
                    continue
                nx, ny = x + dx, y + dy
                if 0 <= nx < self.width and 0 <= ny < self.height and self.board[ny][nx] == '*':
                    count += 1
        return count

    def reveal(self, x, y):
        if self.game_over or self.revealed[y][x] != ' ':
            return
        self.revealed[y][x] = self.board[y][x]
        if self.board[y][x] == '*':
            self.game_over = True
            return
        if self.board[y][x] == '0':
            for dy in range(-1, 2):
                for dx in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        self.reveal(nx, ny)

    def display_board(self):
        print("  " + " ".join(str(x) for x in range(self.width)))
        for y in range(self.height):
            row = ' '.join(self.revealed[y][x] if self.revealed[y][x] != ' ' else '.' for x in range(self.width))
            print(f"{y} {row}")

    def play(self):
        while not self.game_over:
            self.display_board()
            try:
                x, y = map(int, input("Enter coordinates (x y): ").split())
                if 0 <= x < self.width and 0 <= y < self.height:
                    self.reveal(x, y)
                else:
                    print("Coordinates out of bounds. Try again.")
            except ValueError:
                print("Invalid input. Please enter two integers.")

        print("Game Over! Here's the final board:")
        self.reveal_all()
        self.display_board()

    def reveal_all(self):
        for y in range(self.height):
            for x in range(self.width):
                self.revealed[y][x] = self.board[y][x]


if __name__ == "__main__":
    width, height, num_mines = 10, 10, 10
    game = Minesweeper(width, height, num_mines)
    game.play()