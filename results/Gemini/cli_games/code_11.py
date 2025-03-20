import random

class LightsOut:
    """
    A class representing the Lights Out game.
    """

    def __init__(self, size=5, initial_state=None):
        """
        Initializes the game board.

        Args:
            size (int): The size of the board (size x size). Default is 5.
            initial_state (list[list[bool]]): An optional initial state for the board.
                                               If None, a random initial state is generated.
        """
        self.size = size
        if initial_state:
            if len(initial_state) != size or any(len(row) != size for row in initial_state):
                raise ValueError("Initial state must be a size x size grid.")
            self.board = [row[:] for row in initial_state]  # Deep copy
        else:
            self.board = self.generate_random_board()

    def generate_random_board(self):
        """
        Generates a random initial board state.

        Returns:
            list[list[bool]]: A randomly generated board.
        """
        board = [[random.choice([True, False]) for _ in range(self.size)] for _ in range(self.size)]
        return board

    def print_board(self):
        """
        Prints the current state of the board to the console.
        """
        for row in self.board:
            print(" ".join(["X" if cell else "O" for cell in row]))

    def toggle_cell(self, row, col):
        """
        Toggles the state of a cell on the board.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            self.board[row][col] = not self.board[row][col]

    def make_move(self, row, col):
        """
        Makes a move by toggling the selected cell and its neighbors.

        Args:
            row (int): The row index of the selected cell.
            col (int): The column index of the selected cell.
        """
        self.toggle_cell(row, col)  # Toggle the selected cell
        self.toggle_cell(row - 1, col)  # Toggle the cell above
        self.toggle_cell(row + 1, col)  # Toggle the cell below
        self.toggle_cell(row, col - 1)  # Toggle the cell to the left
        self.toggle_cell(row, col + 1)  # Toggle the cell to the right

    def is_solved(self):
        """
        Checks if the game is solved (all lights are off).

        Returns:
            bool: True if the game is solved, False otherwise.
        """
        return all(not cell for row in self.board for cell in row)

    def play_game(self):
        """
        Plays the Lights Out game with a command-line interface.
        """
        print("Welcome to Lights Out!")
        self.print_board()

        while not self.is_solved():
            try:
                move = input("Enter your move (row,col): ").split(",")
                row = int(move[0].strip())
                col = int(move[1].strip())

                if not (0 <= row < self.size and 0 <= col < self.size):
                    print("Invalid move. Row and column must be between 0 and", self.size - 1)
                    continue

                self.make_move(row, col)
                self.print_board()

            except (ValueError, IndexError):
                print("Invalid input. Please enter row and column separated by a comma (e.g., 1,2).")

        print("Congratulations! You solved the puzzle.")


if __name__ == "__main__":
    game = LightsOut(size=5)  # You can change the size here
    game.play_game()