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
        self.won = False
        self.mine_locations = []
        self.place_mines()
        self.calculate_neighboring_mines()

    def place_mines(self):
        """Places mines randomly on the board."""
        mine_count = 0
        while mine_count < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if (row, col) not in self.mine_locations:
                self.mine_locations.append((row, col))
                mine_count += 1

    def calculate_neighboring_mines(self):
        """Calculates the number of mines adjacent to each cell."""
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) not in self.mine_locations:
                    count = 0
                    for i in range(max(0, row - 1), min(self.rows, row + 2)):
                        for j in range(max(0, col - 1), min(self.cols, col + 2)):
                            if (i, j) in self.mine_locations:
                                count += 1
                    self.board[row][col] = str(count) if count > 0 else ' '

    def print_board(self, reveal_all=False):
        """Prints the board to the console."""
        header = "   " + " ".join(str(i) for i in range(self.cols))
        print(header)
        print("  " + "-" * (2 * self.cols + 1))
        for i in range(self.rows):
            row_str = str(i) + "| "
            for j in range(self.cols):
                if reveal_all:
                    if (i, j) in self.mine_locations:
                        row_str += "* "
                    else:
                        row_str += self.board[i][j] + " "
                else:
                    if self.revealed[i][j]:
                        row_str += self.board[i][j] + " "
                    elif self.flags[i][j]:
                        row_str += "F "
                    else:
                        row_str += ". "
            print(row_str)

    def reveal_cell(self, row, col):
        """Reveals a cell and its adjacent cells if it's empty."""
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return

        if self.revealed[row][col] or self.flags[row][col]:
            return

        self.revealed[row][col] = True

        if (row, col) in self.mine_locations:
            self.game_over = True
            return

        if self.board[row][col] == ' ':
            for i in range(max(0, row - 1), min(self.rows, row + 2)):
                for j in range(max(0, col - 1), min(self.cols, col + 2)):
                    self.reveal_cell(i, j)

    def flag_cell(self, row, col):
        """Flags a cell as a mine."""
        if not (0 <= row < self.rows and 0 <= col < self.cols):
            return

        if self.revealed[row][col]:
            return

        self.flags[row][col] = not self.flags[row][col]

    def check_win(self):
        """Checks if the player has won the game."""
        revealed_count = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.revealed[row][col]:
                    revealed_count += 1

        if revealed_count == self.rows * self.cols - self.mines:
            self.won = True
            self.game_over = True

    def play(self):
        """Plays the game."""
        while not self.game_over:
            self.print_board()
            action = input("Enter action (reveal r, flag f, quit q) and coordinates (row col): ").split()

            if not action:
                print("Invalid input.")
                continue

            if action[0].lower() == 'q':
                print("Quitting the game.")
                self.game_over = True
                break

            if len(action) != 3:
                print("Invalid input.  Please provide action, row, and column.")
                continue

            try:
                row = int(action[1])
                col = int(action[2])
            except ValueError:
                print("Invalid row or column.  Please enter numbers.")
                continue

            if not (0 <= row < self.rows and 0 <= col < self.cols):
                print("Invalid row or column.  Out of bounds.")
                continue

            if action[0].lower() == 'r':
                self.reveal_cell(row, col)
            elif action[0].lower() == 'f':
                self.flag_cell(row, col)
            else:
                print("Invalid action.  Use 'r' to reveal, 'f' to flag, or 'q' to quit.")
                continue

            self.check_win()

            if self.game_over:
                self.print_board(reveal_all=True)
                if self.won:
                    print("Congratulations! You won!")
                else:
                    print("Game over! You hit a mine.")


if __name__ == "__main__":
    rows = 10
    cols = 10
    mines = 12
    game = Minesweeper(rows, cols, mines)
    game.play()