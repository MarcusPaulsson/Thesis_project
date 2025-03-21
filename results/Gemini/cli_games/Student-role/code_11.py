import random

class LightsOut:
    """
    A class representing the Lights Out game.
    """

    def __init__(self, size=5, initial_state=None):
        """
        Initializes the Lights Out game.

        Args:
            size (int): The size of the grid (size x size). Default is 5.
            initial_state (list): A 2D list representing the initial state of the board.
                                  If None, a random initial state is generated.
        """
        self.size = size
        if initial_state is None:
            self.board = self.generate_random_board()
        else:
            self.board = [row[:] for row in initial_state]  # Create a copy to avoid modifying the original
            self.size = len(self.board) # Adjust size if initial state provided
        self.moves = 0

    def generate_random_board(self):
        """
        Generates a random initial state for the board.
        """
        board = [[random.randint(0, 1) for _ in range(self.size)] for _ in range(self.size)]
        return board


    def print_board(self):
        """
        Prints the current state of the board to the console.
        """
        for row in self.board:
            print(" ".join(['*' if cell else '.' for cell in row]))  # Use * for 'on' and . for 'off'

    def toggle_cell(self, row, col):
        """
        Toggles the state of a cell (0 -> 1 or 1 -> 0).
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            self.board[row][col] = 1 - self.board[row][col]

    def press_button(self, row, col):
        """
        Simulates pressing a button at the given row and column, toggling the cell and its neighbors.
        """
        self.toggle_cell(row, col)  # Toggle the cell itself
        self.toggle_cell(row - 1, col)  # Toggle the cell above
        self.toggle_cell(row + 1, col)  # Toggle the cell below
        self.toggle_cell(row, col - 1)  # Toggle the cell to the left
        self.toggle_cell(row, col + 1)  # Toggle the cell to the right
        self.moves += 1

    def is_solved(self):
        """
        Checks if the game is solved (all cells are off).
        """
        for row in self.board:
            for cell in row:
                if cell == 1:  # If any cell is on, the game is not solved
                    return False
        return True

    def play(self):
        """
        Plays the Lights Out game in the command line.
        """
        print("Welcome to Lights Out!")
        self.print_board()

        while not self.is_solved():
            try:
                row = int(input("Enter the row to press (0 to {}): ".format(self.size - 1)))
                col = int(input("Enter the column to press (0 to {}): ".format(self.size - 1)))

                if 0 <= row < self.size and 0 <= col < self.size:
                    self.press_button(row, col)
                    self.print_board()
                    print(f"Moves: {self.moves}")
                else:
                    print("Invalid row or column. Please try again.")
            except ValueError:
                print("Invalid input. Please enter integers.")

        print("Congratulations! You solved the puzzle in {} moves.".format(self.moves))


if __name__ == "__main__":
    game = LightsOut()
    game.play()