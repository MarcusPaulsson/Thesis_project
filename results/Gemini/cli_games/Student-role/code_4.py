import random

class Minesweeper:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.revealed = [[False for _ in range(cols)] for _range(rows)]
        self.flags = [[False for _ in range(cols)] for _ in range(rows)]
        self.game_over = False
        self.game_won = False
        self.mine_positions = []
        self.first_move = True  # Track if it's the first move

    def print_board(self):
        """Prints the current state of the board."""
        print("   " + " ".join(str(i) for i in range(self.cols)))
        print("  " + "-" * (2 * self.cols + 1))
        for i in range(self.rows):
            row_str = str(i) + "| "
            for j in range(self.cols):
                if self.flags[i][j]:
                    row_str += "F "  # Flag
                elif self.revealed[i][j]:
                    row_str += str(self.board[i][j]) + " "
                else:
                    row_str += ". "  # Hidden
            print(row_str)

    def place_mines(self, safe_row, safe_col):
        """Places mines randomly on the board, excluding the safe cell."""
        count = 0
        while count < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if (row, col) != (safe_row, safe_col) and (row, col) not in self.mine_positions:
                self.board[row][col] = '*'  # Mark as mine
                self.mine_positions.append((row, col))
                count += 1

    def calculate_neighboring_mines(self):
        """Calculates the number of mines adjacent to each cell."""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != '*':
                    count = 0
                    for i in range(max(0, row - 1), min(self.rows, row + 2)):
                        for j in range(max(0, col - 1), min(self.cols, col + 2)):
                            if self.board[i][j] == '*':
                                count += 1
                    self.board[row][col] = count if count > 0 else ' ' # ' ' for empty cells

    def reveal(self, row, col):
        """Reveals a cell and recursively reveals adjacent empty cells."""
        if self.revealed[row][col]:
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
        """Toggles a flag on a cell."""
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

        if revealed_count == self.rows * self.cols - self.mines:
            self.game_won = True

    def play(self):
        """Main game loop."""
        while not self.game_over and not self.game_won:
            self.print_board()
            print("\nOptions: (r)ow (c)ol (a)ction (reveal/flag). Example: 0 0 r")
            user_input = input("Enter your move: ").split()

            if len(user_input) != 3:
                print("Invalid input. Please enter row, column, and action.")
                continue

            try:
                row = int(user_input[0])
                col = int(user_input[1])
                action = user_input[2].lower()
            except ValueError:
                print("Invalid input. Row and column must be integers.")
                continue

            if not (0 <= row < self.rows and 0 <= col < self.cols):
                print("Invalid input. Row and column must be within the board's bounds.")
                continue

            if self.first_move:
                self.place_mines(row, col)
                self.calculate_neighboring_mines()
                self.first_move = False

            if action == 'r':
                self.reveal(row, col)
            elif action == 'f':
                self.flag(row, col)
            else:
                print("Invalid action. Use 'r' to reveal or 'f' to flag.")
                continue

            self.check_win()

        if self.game_over:
            print("\nGame Over! You hit a mine.")
            # Reveal the whole board
            for row in range(self.rows):
                for col in range(self.cols):
                    self.revealed[row][col] = True
            self.print_board()
        elif self.game_won:
            print("\nCongratulations! You won!")
            # Reveal the whole board
            for row in range(self.rows):
                for col in range(self.cols):
                    self.revealed[row][col] = True
            self.print_board()

# Example usage:
if __name__ == "__main__":
    rows = 8
    cols = 8
    mines = 10
    game = Minesweeper(rows, cols, mines)
    game.play()