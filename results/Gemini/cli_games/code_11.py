import random

class LightsOut:
    """
    A class representing the Lights Out game.
    """

    def __init__(self, size=5, initial_state=None):
        """
        Initializes the game board.

        Args:
            size (int): The size of the board (size x size).  Defaults to 5.
            initial_state (list of lists):  An optional initial state for the board.
                                          If None, generates a random initial state.
        """
        self.size = size
        if initial_state is None:
            self.board = self.generate_random_board()
        else:
            if len(initial_state) != size or any(len(row) != size for row in initial_state):
                raise ValueError("Initial state must be a square matrix of the specified size.")
            self.board = initial_state

    def generate_random_board(self):
        """
        Generates a random board state.

        Returns:
            list of lists: A 2D list representing the board.
        """
        board = [[random.randint(0, 1) for _ in range(self.size)] for _ in range(self.size)]
        return board

    def print_board(self):
        """
        Prints the current state of the board to the console.
        """
        for row in self.board:
            print(" ".join(map(str, row)))

    def toggle_light(self, row, col):
        """
        Toggles the light at the given row and column.

        Args:
            row (int): The row of the light to toggle.
            col (int): The column of the light to toggle.
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            self.board[row][col] = 1 - self.board[row][col]  # Flip 0 to 1 and 1 to 0

    def make_move(self, row, col):
        """
        Makes a move by toggling the selected light and its neighbors.

        Args:
            row (int): The row of the light to toggle.
            col (int): The column of the light to toggle.
        """
        self.toggle_light(row, col)  # Toggle the selected light
        self.toggle_light(row - 1, col)  # Toggle the light above
        self.toggle_light(row + 1, col)  # Toggle the light below
        self.toggle_light(row, col - 1)  # Toggle the light to the left
        self.toggle_light(row, col + 1)  # Toggle the light to the right

    def is_solved(self):
        """
        Checks if the game is solved (all lights are off).

        Returns:
            bool: True if the game is solved, False otherwise.
        """
        return all(all(light == 0 for light in row) for row in self.board)

    def play(self):
        """
        Plays the game through the command line.
        """
        print("Welcome to Lights Out!")
        self.print_board()

        while not self.is_solved():
            try:
                move = input(f"Enter your move (row, col) [0-{self.size-1}]: ").split(",")
                row = int(move[0].strip())
                col = int(move[1].strip())

                if 0 <= row < self.size and 0 <= col < self.size:
                    self.make_move(row, col)
                    self.print_board()
                else:
                    print("Invalid move. Row and column must be within the board boundaries.")
            except (ValueError, IndexError):
                print("Invalid input.  Please enter row and column as integers separated by a comma.")

        print("Congratulations! You solved the puzzle!")


if __name__ == "__main__":
    game = LightsOut(size=5)  # You can change the size of the board here
    game.play()