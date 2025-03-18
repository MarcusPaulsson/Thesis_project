import random

class LightsOut:
    def __init__(self, size=5, initial_state=None):
        """
        Initializes the Lights Out game.

        Args:
            size (int): The size of the grid (size x size). Default is 5.
            initial_state (list of lists, optional): An initial grid state. If None, a random state is generated.
        """
        self.size = size
        if initial_state is None:
            self.grid = self.generate_random_grid()
        else:
            if len(initial_state) != size or any(len(row) != size for row in initial_state):
                raise ValueError("Initial state must be a square grid of the specified size.")
            self.grid = [list(row) for row in initial_state]  # Create a copy to avoid modifying the original
        self.moves = 0

    def generate_random_grid(self):
        """
        Generates a random grid for the game.

        Returns:
            list of lists: A random grid of 0s and 1s.
        """
        return [[random.randint(0, 1) for _ in range(self.size)] for _ in range(self.size)]

    def __str__(self):
        """
        Returns a string representation of the game grid.

        Returns:
            str: A string representation of the grid.
        """
        grid_str = ""
        for row in self.grid:
            grid_str += " ".join(map(str, row)) + "\n"
        return grid_str

    def toggle(self, row, col):
        """
        Toggles the state of a cell (0 to 1, or 1 to 0).

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.
        """
        if 0 <= row < self.size and 0 <= col < self.size:
            self.grid[row][col] = 1 - self.grid[row][col]

    def press_button(self, row, col):
        """
        Presses a button at the given coordinates, toggling the cell and its neighbors.

        Args:
            row (int): The row index of the button.
            col (int): The column index of the button.
        """
        self.toggle(row, col)
        self.toggle(row - 1, col)  # Toggle above
        self.toggle(row + 1, col)  # Toggle below
        self.toggle(row, col - 1)  # Toggle left
        self.toggle(row, col + 1)  # Toggle right
        self.moves += 1

    def is_solved(self):
        """
        Checks if the game is solved (all cells are 0).

        Returns:
            bool: True if the game is solved, False otherwise.
        """
        return all(cell == 0 for row in self.grid for cell in row)

    def solve(self):
        """
        Solves the game using Gaussian elimination (advanced).  This is optional, but useful for generating solvable puzzles.
        """
        # Create a matrix representing the game's equations.
        matrix = []
        for i in range(self.size):
            for j in range(self.size):
                row = [0] * (self.size * self.size)
                row[i * self.size + j] = 1  # The cell itself

                # Neighbors
                if i > 0:
                    row[(i - 1) * self.size + j] = 1
                if i < self.size - 1:
                    row[(i + 1) * self.size + j] = 1
                if j > 0:
                    row[i * self.size + (j - 1)] = 1
                if j < self.size - 1:
                    row[i * self.size + (j + 1)] = 1

                matrix.append(row)

        # Augment the matrix with the initial state.
        b = [self.grid[i // self.size][i % self.size] for i in range(self.size * self.size)]
        augmented_matrix = [row + [b[i]] for i, row in enumerate(matrix)]

        # Gaussian elimination (mod 2).
        for i in range(self.size * self.size):
            # Find pivot
            pivot_row = i
            for k in range(i + 1, self.size * self.size):
                if augmented_matrix[k][i] == 1:
                    pivot_row = k
                    break

            if augmented_matrix[pivot_row][i] == 0:
                continue  # No pivot in this column

            # Swap rows if necessary
            if pivot_row != i:
                augmented_matrix[i], augmented_matrix[pivot_row] = augmented_matrix[pivot_row], augmented_matrix[i]

            # Eliminate other rows
            for k in range(self.size * self.size):
                if k != i and augmented_matrix[k][i] == 1:
                    for j in range(i, self.size * self.size + 1):
                        augmented_matrix[k][j] = (augmented_matrix[k][j] - augmented_matrix[i][j]) % 2

        # Back substitution
        solution = [0] * (self.size * self.size)
        for i in range(self.size * self.size - 1, -1, -1):
            if augmented_matrix[i][i] == 1:
                solution[i] = augmented_matrix[i][-1]

        # Apply the solution to the grid
        for i in range(self.size):
            for j in range(self.size):
                if solution[i * self.size + j] == 1:
                    self.press_button(i, j)

def play_game():
    """
    Plays the Lights Out game in the command line.
    """
    size = 5
    while True:
        try:
            size = int(input("Enter the size of the grid (default is 5): ") or 5)
            if size < 2:
                print("Grid size must be at least 2.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter an integer.")

    game = LightsOut(size)
    print("Initial grid:")
    print(game)

    while not game.is_solved():
        try:
            row, col = map(int, input("Enter the row and column to press (e.g., 0 0), or 'q' to quit: ").split())
            game.press_button(row, col)
            print(game)
            print(f"Moves: {game.moves}")
        except ValueError:
            user_input = input("Enter the row and column to press (e.g., 0 0), or 'q' to quit: ")
            if user_input.lower() == 'q':
                print("Quitting the game.")
                return
            else:
                print("Invalid input. Please enter two integers separated by a space or 'q'.")
        except IndexError:
            print("Invalid input. Please enter two integers separated by a space.")


    print("Congratulations! You solved the puzzle.")
    print(f"Total moves: {game.moves}")


if __name__ == "__main__":
    play_game()