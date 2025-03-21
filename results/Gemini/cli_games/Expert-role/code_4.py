import random

class Minesweeper:
    """
    A command-line Minesweeper game.
    """

    def __init__(self, rows, cols, mines):
        """
        Initializes a new Minesweeper game.

        Args:
            rows (int): The number of rows in the grid.
            cols (int): The number of columns in the grid.
            mines (int): The number of mines to place.
        """
        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.grid = [[' ' for _ in range(cols)] for _ in range(rows)]  # Hidden grid
        self.visible_grid = [['-' for _ in range(cols)] for _ in range(rows)]  # User view
        self.mine_positions = set()
        self.game_over = False
        self.flags_placed = 0
        self.first_move = True # Flag to ensure first move is never a mine

        if mines >= rows * cols:
            raise ValueError("Too many mines for the given grid size.")

        self.place_mines()
        self.calculate_neighboring_mines()

    def place_mines(self):
        """
        Randomly places mines on the grid.  Ensures the number of mines is correct.
        """
        while len(self.mine_positions) < self.mines:
            row = random.randint(0, self.rows - 1)
            col = random.randint(0, self.cols - 1)
            self.mine_positions.add((row, col))


    def calculate_neighboring_mines(self):
        """
        Calculates the number of neighboring mines for each cell.
        """
        for row in range(self.rows):
            for col in range(self.cols):
                if (row, col) not in self.mine_positions:
                    count = 0
                    for r in range(max(0, row - 1), min(self.rows, row + 2)):
                        for c in range(max(0, col - 1), min(self.cols, col + 2)):
                            if (r, c) in self.mine_positions:
                                count += 1
                    self.grid[row][col] = str(count) if count > 0 else '0'

    def print_grid(self):
        """
        Prints the visible grid to the console.
        """
        print("   " + " ".join(str(i) for i in range(self.cols)))
        print("  " + "-" * (2 * self.cols + 1))
        for i, row in enumerate(self.visible_grid):
            print(f"{i}| {' '.join(row)} |")
        print("  " + "-" * (2 * self.cols + 1))
        print(f"Mines: {self.mines}, Flags placed: {self.flags_placed}")

    def is_valid_move(self, row, col):
        """
        Checks if a move is valid (within the grid boundaries).

        Args:
            row (int): The row index.
            col (int): The column index.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return 0 <= row < self.rows and 0 <= col < self.cols

    def reveal_cell(self, row, col):
        """
        Reveals a cell and its neighboring empty cells recursively.

        Args:
            row (int): The row index.
            col (int): The column index.
        """

        if not self.is_valid_move(row, col) or self.visible_grid[row][col] != '-':
            return

        if self.first_move:
            # Ensure first move is not a mine by moving the mine if necessary
            if (row, col) in self.mine_positions:
                self.move_mine(row, col)
            self.first_move = False
            self.calculate_neighboring_mines() # Recalculate neighbor counts after moving mine.


        if (row, col) in self.mine_positions:
            self.visible_grid[row][col] = 'X'
            self.game_over = True
            return

        self.visible_grid[row][col] = self.grid[row][col]

        if self.grid[row][col] == '0':
            for r in range(max(0, row - 1), min(self.rows, row + 2)):
                for c in range(max(0, col - 1), min(self.cols, col + 2)):
                    self.reveal_cell(r, c)

    def move_mine(self, row, col):
        """Moves a mine from the given location to a new random location.

        Args:
            row (int): The row index of the mine to move.
            col (int): The column index of the mine to move.
        """
        self.mine_positions.remove((row, col))
        while True:
            new_row = random.randint(0, self.rows - 1)
            new_col = random.randint(0, self.cols - 1)
            if (new_row, new_col) not in self.mine_positions and (new_row, new_col) != (row, col):
                self.mine_positions.add((new_row, new_col))
                break


    def place_flag(self, row, col):
        """
        Places a flag on a cell.

        Args:
            row (int): The row index.
            col (int): The column index.
        """
        if not self.is_valid_move(row, col):
            print("Invalid move.")
            return

        if self.visible_grid[row][col] == '-':
            self.visible_grid[row][col] = 'F'
            self.flags_placed += 1
        elif self.visible_grid[row][col] == 'F':
            self.visible_grid[row][col] = '-'
            self.flags_placed -= 1
        else:
            print("Cannot place a flag on a revealed cell.")

    def check_win(self):
        """
        Checks if the player has won the game.

        Returns:
            bool: True if the player has won, False otherwise.
        """
        revealed_cells = 0
        for row in range(self.rows):
            for col in range(self.cols):
                if self.visible_grid[row][col] != '-':
                    revealed_cells += 1

        return revealed_cells == self.rows * self.cols - self.mines

    def play_turn(self):
        """
        Plays a single turn of the game.
        """
        self.print_grid()

        while True:
            action = input("Enter your move (r = reveal, f = flag, q = quit), followed by row and column (e.g., r 0 0): ").split()
            if len(action) != 3:
                print("Invalid input. Please enter action, row, and column.")
                continue

            try:
                move, row, col = action[0].lower(), int(action[1]), int(action[2])
            except ValueError:
                print("Invalid input. Row and column must be integers.")
                continue

            if move == 'q':
                self.game_over = True
                return

            if not self.is_valid_move(row, col):
                print("Invalid move. Row and column must be within the grid boundaries.")
                continue

            if move == 'r':
                self.reveal_cell(row, col)
                break  # Exit the loop after a valid reveal
            elif move == 'f':
                self.place_flag(row, col)
                break  # Exit the loop after a valid flag
            else:
                print("Invalid action. Use 'r' to reveal or 'f' to flag.")

    def play(self):
        """
        Starts the Minesweeper game.
        """
        print("Welcome to Minesweeper!")
        while not self.game_over:
            self.play_turn()
            if self.game_over:
                self.print_grid()
                print("Game Over! You hit a mine.")
                break
            if self.check_win():
                self.print_grid()
                print("Congratulations! You win!")
                self.game_over = True


if __name__ == '__main__':
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        mines = int(input("Enter the number of mines: "))
        game = Minesweeper(rows, cols, mines)
        game.play()
    except ValueError as e:
        print(f"Invalid input: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")