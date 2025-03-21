import random

class Minesweeper:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.flags = [[False for _ in range(cols)] for _ in range(rows)]
        self.game_over = False
        self.mine_positions = self.place_mines()
        self.calculate_neighbors()

    def place_mines(self):
        mine_positions = []
        count = 0
        while count < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if (row, col) not in mine_positions:
                mine_positions.append((row, col))
                count += 1
        return mine_positions

    def calculate_neighbors(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) not in self.mine_positions:
                    count = 0
                    for i in range(max(0, row - 1), min(self.rows, row + 2)):
                        for j in range(max(0, col - 1), min(self.cols, col + 2)):
                            if (i, j) in self.mine_positions:
                                count += 1
                    if count > 0:
                        self.board[row][col] = str(count)

    def print_board(self):
        print("   " + " ".join(str(i) for i in range(self.cols)))
        print("  " + "-" * (2 * self.cols + 1))
        for i in range(self.rows):
            row_str = str(i) + " |"
            for j in range(self.cols):
                if self.flags[i][j]:
                    row_str += "F "
                elif self.revealed[i][j]:
                    row_str += self.board[i][j] + " "
                else:
                    row_str += ". "
            print(row_str)

    def reveal(self, row, col):
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return

        if self.revealed[row][col]:
            return

        self.revealed[row][col] = True

        if (row, col) in self.mine_positions:
            self.game_over = True
            return

        if self.board[row][col] == ' ':
            for i in range(max(0, row - 1), min(self.rows, row + 2)):
                for j in range(max(0, col - 1), min(self.cols, col + 2)):
                    self.reveal(i, j)

    def flag(self, row, col):
        if not self.revealed[row][col]:
            self.flags[row][col] = not self.flags[row][col]

    def check_win(self):
        revealed_count = 0
        for i in range(self.rows):
            for j in range(self.cols):
                if self.revealed[i][j]:
                    revealed_count += 1
        return revealed_count == self.rows * self.cols - self.mines

    def play(self):
        while not self.game_over:
            self.print_board()
            action = input("Enter action (reveal/flag), row, col (e.g., reveal 0 0): ").split()
            if len(action) != 3:
                print("Invalid input. Please enter: reveal/flag, row, col")
                continue

            try:
                act, row, col = action[0].lower(), int(action[1]), int(action[2])
            except ValueError:
                print("Invalid input. Row and col must be integers.")
                continue

            if not (0 <= row < self.rows and 0 <= col < self.cols):
                print("Invalid row or column.  Must be between 0 and {}".format(max(self.rows, self.cols) -1))
                continue

            if act == "reveal":
                self.reveal(row, col)
                if self.game_over:
                    print("Game Over! You hit a mine.")
                    for r, c in self.mine_positions:
                        self.revealed[r][c] = True
                    self.print_board()
                    break
                if self.check_win():
                    print("Congratulations! You won!")
                    self.print_board()
                    self.game_over = True
                    break

            elif act == "flag":
                self.flag(row, col)
            else:
                print("Invalid action.  Choose 'reveal' or 'flag'.")

if __name__ == "__main__":
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    mines = int(input("Enter the number of mines: "))

    game = Minesweeper(rows, cols, mines)
    game.play()