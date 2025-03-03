import random

class LightsOut:
    """
    A class to represent the Lights Out game.
    """

    def __init__(self, size=5, initial_state=None):
        """
        Initializes the game with a given size and optional initial state.

        Args:
            size (int): The size of the game board (size x size). Defaults to 5.
            initial_state (list): A list of lists representing the initial state of the board.
                                  If None, a random initial state is generated.
        """
        self.size = size
        if initial_state:
            if len(initial_state) != size or any(len(row) != size for row in initial_state):
                raise ValueError("Initial state must be a {0}x{0} matrix".format(size))
            self.board = [list(row) for row in initial_state] # Create a deep copy
        else:
            self.board = self._generate_random_board()

    def _generate_random_board(self):
        """
        Generates a random initial state for the board.

        Returns:
            list: A list of lists representing the randomly generated board.
        """
        board = [[random.choice([0, 1]) for _ in range(self.size)] for _ in range(self.size)]
        return board

    def print_board(self):
        """
        Prints the current state of the board to the console.
        """
        for row in self.board:
            print(" ".join(map(str, row)))

    def toggle(self, row, col):
        """
        Toggles the state of a cell at the given row and column.

        Args:
            row (int): The row index of the cell to toggle.
            col (int): The column index of the cell to toggle.
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            self.board[row][col] = 1 - self.board[row][col]

    def make_move(self, row, col):
        """
        Makes a move by toggling the state of the cell at (row, col) and its neighbors.

        Args:
            row (int): The row index of the cell to click.
            col (int): The column index of the cell to click.
        """
        self.toggle(row, col)       # Toggle the cell itself
        self.toggle(row - 1, col)   # Toggle the cell above
        self.toggle(row + 1, col)   # Toggle the cell below
        self.toggle(row, col - 1)   # Toggle the cell to the left
        self.toggle(row, col + 1)   # Toggle the cell to the right

    def is_solved(self):
        """
        Checks if the game is solved (all lights are off).

        Returns:
            bool: True if the game is solved, False otherwise.
        """
        return all(all(cell == 0 for cell in row) for row in self.board)

    def play(self):
        """
        Plays the game with the user via command line interface.
        """
        print("Welcome to Lights Out!")
        self.print_board()

        while not self.is_solved():
            try:
                move = input("Enter your move (row, col) or 'q' to quit: ").lower()
                if move == 'q':
                    print("Quitting the game.")
                    return

                row, col = map(int, move.split(','))

                if not (0 <= row < self.size and 0 <= col < self.size):
                    print("Invalid move. Row and column must be between 0 and {}.".format(self.size - 1))
                    continue

                self.make_move(row, col)
                self.print_board()

            except ValueError:
                print("Invalid input. Please enter row and column separated by a comma (e.g., 0,1).")
            except Exception as e:
                print(f"An error occurred: {e}")

        print("Congratulations! You solved the puzzle!")


if __name__ == "__main__":
    game = LightsOut()  # You can specify the size: LightsOut(size=7)
    game.play()