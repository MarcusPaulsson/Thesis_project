import random

class LightsOut:
    """
    A class to represent the Lights Out game.
    """

    def __init__(self, size=5, initial_state=None):
        """
        Initializes the Lights Out game.

        Args:
            size (int): The size of the grid (size x size).  Defaults to 5.
            initial_state (list of lists): The initial state of the grid.
                If None, the grid is initialized randomly.
        """
        self.size = size
        if initial_state is None:
            self.grid = self.random_grid()
        else:
            self.grid = initial_state
            self.size = len(initial_state) # ensure consistency
            # Check if the initial state is valid
            if not all(len(row) == self.size for row in self.grid):
                raise ValueError("Invalid initial state: Grid must be square.")
            if not all(all(cell in [0, 1] for cell in row) for row in self.grid):
                raise ValueError("Invalid initial state: Grid must contain only 0s and 1s.")


    def random_grid(self):
        """
        Generates a random grid for the game.

        Returns:
            list of lists: A 2D list representing the grid.
        """
        return [[random.randint(0, 1) for _ in range(self.size)] for _ in range(self.size)]

    def print_grid(self):
        """
        Prints the current state of the grid to the console.
        """
        for row in self.grid:
            print(" ".join(map(str, row)))

    def toggle(self, row, col):
        """
        Toggles the state of a cell (0 to 1 or 1 to 0).

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            self.grid[row][col] = 1 - self.grid[row][col]

    def press_button(self, row, col):
        """
        Simulates pressing a button at the given row and column.
        This toggles the state of the button and its neighbors.

        Args:
            row (int): The row index of the button.
            col (int): The column index of the button.
        """
        self.toggle(row, col)
        self.toggle(row - 1, col)
        self.toggle(row + 1, col)
        self.toggle(row, col - 1)
        self.toggle(row, col + 1)

    def is_solved(self):
        """
        Checks if the game is solved (all lights are off).

        Returns:
            bool: True if the game is solved, False otherwise.
        """
        return all(all(cell == 0 for cell in row) for row in self.grid)

    def solve(self, initial_grid = None):
        """
        Solves the Lights Out puzzle using brute force (for small grids).

        Returns:
            list of tuples: A list of (row, col) tuples representing the moves to solve the puzzle,
                            or None if the puzzle is unsolvable.
        """

        if initial_grid is None:
            initial_grid = [row[:] for row in self.grid]  # Make a copy to restore later

        n = self.size
        max_moves = 1 << n  # Maximum number of possible moves in the first row

        for i in range(max_moves):
            # Reset the grid to the initial state for each attempt
            self.grid = [row[:] for row in initial_grid]

            moves = []
            # Apply moves to the first row based on the binary representation of i
            for j in range(n):
                if (i >> j) & 1:
                    self.press_button(0, j)
                    moves.append((0, j))

            # Apply moves to the remaining rows to turn off all lights in the previous row
            for row in range(1, n):
                for col in range(n):
                    if self.grid[row - 1][col] == 1:
                        self.press_button(row, col)
                        moves.append((row, col))

            # Check if the puzzle is solved
            if self.is_solved():
                return moves

        return None  # Puzzle is unsolvable

def main():
    """
    Main function to run the Lights Out game in the command line.
    """
    size = 5  # Default grid size
    game = LightsOut(size)

    print("Welcome to Lights Out!")
    print("Initial grid:")
    game.print_grid()

    while not game.is_solved():
        try:
            row = int(input("Enter row (0-{}): ".format(size - 1)))
            col = int(input("Enter column (0-{}): ".format(size - 1)))

            if 0 <= row < size and 0 <= col < size:
                game.press_button(row, col)
                print("Grid after move:")
                game.print_grid()
            else:
                print("Invalid row or column. Try again.")
        except ValueError:
            print("Invalid input. Please enter integers.")

    print("Congratulations! You solved the puzzle.")

if __name__ == "__main__":
    main()