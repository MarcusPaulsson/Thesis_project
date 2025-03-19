import random
import sys

class Minesweeper:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _ in range(rows)]
        self.flags = [[False for _ in range(cols)] for _ in range(rows)]
        self.game_over = False
        self.first_move = True
        self.mine_locations = []

    def print_board(self):
        """Prints the current state of the board."""
        print("   " + "  ".join(str(i) for i in range(self.cols)))
        print("  " + "-" * (self.cols * 3))
        for i in range(self.rows):
            row_str = str(i) + " |"
            for j in range(self.cols):
                if self.flags[i][j]:
                    row_str += " F "
                elif self.revealed[i][j]:
                    row_str += " " + self.board[i][j] + " "
                else:
                    row_str += " . "
            row_str += "|"
            print(row_str)
        print("  " + "-" * (self.cols * 3))
        print(f"Mines: {self.mines}")


    def place_mines(self, start_row, start_col):
        """Places mines randomly on the board, avoiding the starting cell."""
        mines_placed = 0
        while mines_placed < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if (row, col) != (start_row, start_col) and (row, col) not in self.mine_locations:
                self.mine_locations.append((row, col))
                self.board[row][col] = '*'
                mines_placed += 1

    def calculate_neighboring_mines(self):
        """Calculates the number of neighboring mines for each cell."""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != '*':
                    count = 0
                    for i in range(max(0, row - 1), min(self.rows, row + 2)):
                        for j in range(max(0, col - 1), min(self.cols, col + 2)):
                            if self.board[i][j] == '*':
                                count += 1
                    self.board[row][col] = str(count) if count > 0 else ' '

    def reveal(self, row, col):
        """Reveals a cell and recursively reveals neighboring cells if they are empty."""

        if row < 0 or row >= self.rows or col < 0 or col >= self.cols or self.revealed[row][col]:
            return

        self.revealed[row][col] = True

        if self.board[row][col] == '*':
            self.game_over = True
            return

        if self.board[row][col] == ' ':
            for i in range(max(0, row - 1), min(self.rows, row + 2)):
                for j in range(max(0, col - 1), min(self.cols, col + 2)):
                    self.reveal(i, j)


    def flag(self, row, col):
         """Flags or unflags a cell."""
         if self.revealed[row][col]:
             print("Cannot flag a revealed cell.")
             return

         self.flags[row][col] = not self.flags[row][col]

    def check_win(self):
        """Checks if the player has won the game."""
        revealed_count = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.revealed[row][col]:
                    revealed_count += 1

        return revealed_count == self.rows * self.cols - self.mines

    def play(self):
        """Main game loop."""
        while not self.game_over:
            self.print_board()
            action = input("Enter action (reveal r, flag f, quit q), row, col (e.g., r 0 0): ").split()

            if not action:
                print("Invalid input. Please try again.")
                continue

            if action[0].lower() == 'q':
                print("Quitting the game.")
                sys.exit()

            try:
                operation = action[0].lower()
                row = int(action[1])
                col = int(action[2])

                if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                    print("Invalid row or column. Please try again.")
                    continue

            except (IndexError, ValueError):
                print("Invalid input. Please try again.")
                continue

            if operation == 'r':
                if self.first_move:
                    self.place_mines(row, col)
                    self.calculate_neighboring_mines()
                    self.first_move = False

                self.reveal(row, col)

                if self.game_over:
                    self.print_board()
                    print("Game Over! You hit a mine.")
                    return

                if self.check_win():
                    self.print_board()
                    print("Congratulations! You won!")
                    return

            elif operation == 'f':
                self.flag(row, col)
            else:
                print("Invalid action. Please enter 'reveal' or 'flag'.")

        print("Game Over!")


if __name__ == "__main__":
    rows = 10
    cols = 10
    mines = 15
    game = Minesweeper(rows, cols, mines)
    game.play()