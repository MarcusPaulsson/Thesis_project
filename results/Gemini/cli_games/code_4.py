import random

class Minesweeper:
    def __init__(self, rows, cols, mines):
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.hidden_board = [[' ' for _ in range(cols)] for _ in range(rows)]
        self.mines_positions = []
        self.game_over = False
        self.game_won = False
        self.first_move = True

    def print_board(self):
        """Prints the current state of the board."""
        print("   " + "  ".join(str(i) for i in range(self.cols)))
        print("  " + "-" * (self.cols * 3))
        for i in range(self.rows):
            print(f"{i} | {'  '.join(self.board[i])} |")
        print("  " + "-" * (self.cols * 3))

    def generate_mines(self, first_row, first_col):
        """Generates mine positions, avoiding the first move."""
        self.mines_positions = []
        while len(self.mines_positions) < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            if (row, col) not in self.mines_positions and (row, col) != (first_row, first_col):
                self.mines_positions.append((row, col))
                self.hidden_board[row][col] = '*'

    def calculate_adjacent_mines(self):
        """Calculates the number of mines adjacent to each cell."""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.hidden_board[row][col] != '*':
                    count = 0
                    for i in range(max(0, row - 1), min(self.rows, row + 2)):
                        for j in range(max(0, col - 1), min(self.cols, col + 2)):
                            if self.hidden_board[i][j] == '*':
                                count += 1
                    if count > 0:
                        self.hidden_board[row][col] = str(count)
                    else:
                        self.hidden_board[row][col] = '0'

    def reveal_cell(self, row, col):
        """Reveals a cell and recursively reveals adjacent empty cells."""
        if self.board[row][col] != ' ':
            return  # Cell already revealed

        self.board[row][col] = self.hidden_board[row][col]

        if self.hidden_board[row][col] == '0':
            for i in range(max(0, row - 1), min(self.rows, row + 2)):
                for j in range(max(0, col - 1), min(self.cols, col + 2)):
                    if self.board[i][j] == ' ':
                        self.reveal_cell(i, j)

    def flag_cell(self, row, col):
        """Flags or unflags a cell."""
        if self.board[row][col] == ' ':
            self.board[row][col] = 'F'
        elif self.board[row][col] == 'F':
            self.board[row][col] = ' '

    def check_win(self):
        """Checks if the player has won the game."""
        revealed_cells = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] != ' ':
                    revealed_cells += 1
        if revealed_cells == self.rows * self.cols - self.mines:
            self.game_won = True

    def play(self):
        """Main game loop."""
        while not self.game_over and not self.game_won:
            self.print_board()

            try:
                action, row, col = input("Enter action (reveal/flag), row, and column (e.g., reveal 0 0): ").split()
                row = int(row)
                col = int(col)
            except ValueError:
                print("Invalid input. Please enter action, row, and column separated by spaces.")
                continue

            if not (0 <= row < self.rows and 0 <= col < self.cols):
                print("Invalid row or column. Please enter values within the board dimensions.")
                continue

            if self.first_move:
                self.generate_mines(row, col)
                self.calculate_adjacent_mines()
                self.first_move = False

            if action.lower() == 'reveal':
                if self.hidden_board[row][col] == '*':
                    self.game_over = True
                    self.board = [row[:] for row in self.hidden_board]
                    self.print_board()
                    print("Game Over! You hit a mine.")
                else:
                    self.reveal_cell(row, col)
                    self.check_win()
            elif action.lower() == 'flag':
                self.flag_cell(row, col)
            else:
                print("Invalid action. Please enter 'reveal' or 'flag'.")

        if self.game_won:
            self.print_board()
            print("Congratulations! You won the game!")


if __name__ == "__main__":
    rows = 10
    cols = 10
    mines = 15
    game = Minesweeper(rows, cols, mines)
    game.play()