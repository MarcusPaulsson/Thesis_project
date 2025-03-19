import random

class Minesweeper:
    def __init__(self, width, height, mines):
        self.width = width
        self.height = height
        self.mines = mines
        self.board = [[' ' for _ in range(width)] for _ in range(height)]
        self.revealed = [[' ' for _ in range(width)] for _ in range(height)]
        self.game_over = False
        self.flags = 0
        self.place_mines()
        self.calculate_numbers()

    def place_mines(self):
        mine_locations = random.sample(range(self.width * self.height), self.mines)
        for location in mine_locations:
            row = location // self.width
            col = location % self.width
            self.board[row][col] = 'M'

    def calculate_numbers(self):
        for r in range(self.height):
            for c in range(self.width):
                if self.board[r][c] == 'M':
                    continue
                self.board[r][c] = str(self.count_mines(r, c))

    def count_mines(self, row, col):
        count = 0
        for r in range(max(0, row - 1), min(self.height, row + 2)):
            for c in range(max(0, col - 1), min(self.width, col + 2)):
                if self.board[r][c] == 'M':
                    count += 1
        return count

    def reveal(self, row, col):
        if self.game_over or self.revealed[row][col] != ' ':
            return

        self.revealed[row][col] = self.board[row][col]

        if self.board[row][col] == 'M':
            self.game_over = True
            return

        if self.board[row][col] == '0':
            for r in range(max(0, row - 1), min(self.height, row + 2)):
                for c in range(max(0, col - 1), min(self.width, col + 2)):
                    self.reveal(r, c)

    def flag(self, row, col):
        if self.revealed[row][col] == ' ':
            self.revealed[row][col] = 'F'
            self.flags += 1
        elif self.revealed[row][col] == 'F':
            self.revealed[row][col] = ' '
            self.flags -= 1

    def print_board(self):
        print(' ' + ' '.join(str(i) for i in range(self.width)))
        for r in range(self.height):
            print(r, ' '.join(self.revealed[r]))

    def check_win(self):
        for r in range(self.height):
            for c in range(self.width):
                if self.board[r][c] != 'M' and self.revealed[r][c] == ' ':
                    return False
        return True

    def play(self):
        while not self.game_over:
            self.print_board()
            command = input("Enter command (reveal/flag) and coordinates (row col): ").split()
            if len(command) != 3:
                print("Invalid input. Please enter a command followed by row and column.")
                continue

            cmd, row, col = command[0], int(command[1]), int(command[2])

            if cmd == 'reveal':
                self.reveal(row, col)
            elif cmd == 'flag':
                self.flag(row, col)
            else:
                print("Invalid command. Use 'reveal' or 'flag'.")

            if self.check_win():
                print("Congratulations! You've won!")
                break

        if self.game_over:
            self.revealed = self.board
            self.print_board()
            print("Game over! You hit a mine.")

if __name__ == "__main__":
    game = Minesweeper(width=10, height=10, mines=10)
    game.play()