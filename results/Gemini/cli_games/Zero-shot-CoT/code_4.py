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
        self.first_move = True
        self.mine_positions = [] # Keep track of mine positions

    def print_board(self, show_mines=False):
        """Prints the current state of the board."""
        col_labels = "   " + " ".join([str(i % 10) for i in range(self.cols)])  # Handles columns > 9
        print(col_labels)
        print("  " + "-" * (2 * self.cols + 1))
        for i in range(self.rows):
            row_str = str(i % 10) + "| " # Handles rows > 9
            for j in range(self.cols):
                if self.flags[i][j]:
                    row_str += "F "
                elif self.revealed[i][j]:
                    row_str += str(self.board[i][j]) + " "
                elif show_mines and (i,j) in self.mine_positions:
                    row_str += "* "
                else:
                    row_str += ". "
            print(row_str + "|" + str(i % 10))
        print("  " + "-" * (2 * self.cols + 1))
        print(col_labels)

    def place_mines(self, safe_row, safe_col):
        """Places mines randomly on the board, avoiding the initial click."""
        possible_positions = [(r, c) for r in range(self.rows) for c in range(self.cols) if (r, c) != (safe_row, safe_col)]
        self.mine_positions = random.sample(possible_positions, self.mines)

        for r, c in self.mine_positions:
            self.board[r][c] = '*'

    def calculate_neighbor_counts(self):
        """Calculates the number of neighboring mines for each cell."""
        for r in range(self.rows):
            for c in range(self.cols):
                if self.board[r][c] != '*':
                    count = 0
                    for i in range(max(0, r - 1), min(self.rows, r + 2)):
                        for j in range(max(0, c - 1), min(self.cols, c + 2)):
                            if self.board[i][j] == '*':
                                count += 1
                    self.board[r][c] = count if count > 0 else ' '

    def reveal(self, row, col):
        """Reveals a cell and recursively reveals neighboring empty cells."""
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

    def toggle_flag(self, row, col):
        """Toggles a flag on a cell."""
        if self.revealed[row][col]:
            print("Cannot flag a revealed cell.")
            return

        self.flags[row][col] = not self.flags[row][col]

    def check_win(self):
        """Checks if the player has won the game."""
        revealed_count = 0
        for r in range(self.rows):
            for c in range(self.cols):
                if self.revealed[r][c]:
                    revealed_count += 1

        return revealed_count == self.rows * self.cols - self.mines

    def play(self):
        """Main game loop."""
        while not self.game_over:
            self.print_board()
            action = input("Enter action (r=reveal, f=flag, q=quit) and coordinates (e.g., r 0 0): ").split()

            if not action:
                print("Invalid input. Please enter an action and coordinates.")
                continue

            if action[0].lower() == 'q':
                print("Quitting game.")
                return

            try:
                row = int(action[1])
                col = int(action[2])
            except (IndexError, ValueError):
                print("Invalid coordinates. Please enter row and column numbers.")
                continue

            if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
                print("Coordinates are out of bounds.")
                continue

            if action[0].lower() == 'r':
                if self.first_move:
                    self.place_mines(row, col)
                    self.calculate_neighbor_counts()
                    self.first_move = False
                self.reveal(row, col)
                if self.game_over:
                    self.print_board(show_mines=True)
                    print("Game Over! You hit a mine.")
                    return
            elif action[0].lower() == 'f':
                self.toggle_flag(row, col)
            else:
                print("Invalid action. Use 'r' to reveal, 'f' to flag, or 'q' to quit.")

            if self.check_win():
                self.print_board()
                print("Congratulations! You won!")
                return

if __name__ == '__main__':
    rows = 10
    cols = 10
    mines = 15
    game = Minesweeper(rows, cols, mines)
    game.play()