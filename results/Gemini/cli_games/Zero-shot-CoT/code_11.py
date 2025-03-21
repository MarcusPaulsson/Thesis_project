import random

class LightsOut:
    """
    A class representing the Lights Out game.
    """

    def __init__(self, size=5, board=None):
        """
        Initializes the Lights Out game.

        Args:
            size (int): The size of the board (size x size). Default is 5.
            board (list of lists): An optional initial board state. If None, a random board is generated.
        """
        self.size = size
        if board is None:
            self.board = self.generate_random_board()
        else:
            self.board = board

    def generate_random_board(self):
        """
        Generates a random board for the game.

        Returns:
            list of lists: A 2D list representing the board, with each cell being either 0 (off) or 1 (on).
        """
        board = [[random.randint(0, 1) for _ in range(self.size)] for _ in range(self.size)]
        return board

    def print_board(self):
        """
        Prints the current state of the board to the console.
        """
        for row in self.board:
            print(" ".join(map(str, row)))
        print()

    def toggle_cell(self, row, col):
        """
        Toggles the state of a cell (0 to 1 or 1 to 0).

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            self.board[row][col] = 1 - self.board[row][col]

    def make_move(self, row, col):
        """
        Makes a move by toggling the selected cell and its adjacent cells.

        Args:
            row (int): The row index of the selected cell.
            col (int): The column index of the selected cell.
        """
        self.toggle_cell(row, col)
        self.toggle_cell(row - 1, col)  # Up
        self.toggle_cell(row + 1, col)  # Down
        self.toggle_cell(row, col - 1)  # Left
        self.toggle_cell(row, col + 1)  # Right

    def is_solved(self):
        """
        Checks if the game is solved (all cells are off).

        Returns:
            bool: True if the game is solved, False otherwise.
        """
        for row in self.board:
            if any(row):  # Check if any cell in the row is on (1)
                return False
        return True

    def play(self):
        """
        Plays the game in a command-line interface.
        """
        print("Welcome to Lights Out!")
        self.print_board()

        while not self.is_solved():
            try:
                row, col = map(int, input("Enter row and column (e.g., 0 0): ").split())
                if 0 <= row < self.size and 0 <= col < self.size:
                    self.make_move(row, col)
                    self.print_board()
                else:
                    print("Invalid row or column. Try again.")
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")

        print("Congratulations! You solved the puzzle!")


if __name__ == "__main__":
    game = LightsOut(5)  # You can change the size here (e.g., LightsOut(7))
    game.play()