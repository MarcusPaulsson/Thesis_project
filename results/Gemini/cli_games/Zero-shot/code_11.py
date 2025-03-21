import random

class LightsOut:
    """
    A class representing the Lights Out game.
    """

    def __init__(self, size=5, initial_state=None):
        """
        Initializes the Lights Out game.

        Args:
            size (int): The size of the board (size x size). Default is 5.
            initial_state (list): A list of lists representing the initial state of the board.
                                  If None, a random initial state is generated.
        """
        self.size = size
        if initial_state is None:
            self.board = self.generate_random_board()
        else:
            if len(initial_state) != size or any(len(row) != size for row in initial_state):
                raise ValueError("Initial state must be a size x size matrix.")
            self.board = initial_state

    def generate_random_board(self):
        """
        Generates a random initial board state.

        Returns:
            list: A list of lists representing the board.
        """
        board = []
        for _ in range(self.size):
            row = [random.randint(0, 1) for _ in range(self.size)]
            board.append(row)
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
            row (int): The row index (0-based).
            col (int): The column index (0-based).
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            self.board[row][col] = 1 - self.board[row][col]  # Flip 0 to 1 and 1 to 0

    def press_button(self, row, col):
        """
        Simulates pressing the button at the given row and column, toggling the light
        and its adjacent lights (up, down, left, right).

        Args:
            row (int): The row index (0-based).
            col (int): The column index (0-based).
        """
        self.toggle_light(row, col)  # Toggle the button itself
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
        Plays the Lights Out game through the command line interface.
        """
        print("Welcome to Lights Out!")
        print("The goal is to turn off all the lights.")
        print("Enter the row and column of the button you want to press (e.g., '0 0').")
        print("Enter 'q' to quit.")

        while True:
            self.print_board()
            if self.is_solved():
                print("Congratulations! You solved the puzzle!")
                break

            move = input("Enter your move (row col): ").strip().lower()

            if move == 'q':
                print("Quitting the game.")
                break

            try:
                row, col = map(int, move.split())
                if 0 <= row < self.size and 0 <= col < self.size:
                    self.press_button(row, col)
                else:
                    print("Invalid move. Row and column must be between 0 and", self.size - 1)
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")

if __name__ == '__main__':
    game = LightsOut(size=5)  # You can change the size here
    game.play()