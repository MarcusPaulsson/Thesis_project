import argparse
import time
import os
import random


class GameOfLife:
    """
    A class representing the Game of Life.
    """

    def __init__(self, width, height, density=0.3, initial_state=None):
        """
        Initializes the Game of Life.

        Args:
            width (int): The width of the grid.
            height (int): The height of the grid.
            density (float): The initial density of live cells (0 to 1).
            initial_state (list[list[int]]): An optional initial state.  Must be a 2D list of 0s and 1s.
        """
        self.width = width
        self.height = height
        self.grid = self.create_grid(density, initial_state)

    def create_grid(self, density, initial_state):
        """
        Creates the initial grid with a random distribution of live cells.

        Returns:
            list[list[int]]: The grid representing the game state.
        """
        if initial_state:
            if len(initial_state) != self.height or any(len(row) != self.width for row in initial_state):
                raise ValueError("Initial state dimensions do not match specified width and height.")
            return [row[:] for row in initial_state]  # Create a copy to avoid modifying the original

        grid = []
        for _ in range(self.height):
            row = [1 if random.random() < density else 0 for _ in range(self.width)]
            grid.append(row)
        return grid

    def get_neighbors(self, row, col):
        """
        Gets the number of live neighbors for a given cell.

        Args:
            row (int): The row index of the cell.
            col (int): The column index of the cell.

        Returns:
            int: The number of live neighbors.
        """
        neighbors = 0
        for i in range(max(0, row - 1), min(self.height, row + 2)):
            for j in range(max(0, col - 1), min(self.width, col + 2)):
                if (i, j) != (row, col):
                    neighbors += self.grid[i][j]
        return neighbors

    def update_grid(self):
        """
        Updates the grid to the next generation based on the Game of Life rules.
        """
        new_grid = []
        for row in range(self.height):
            new_row = []
            for col in range(self.width):
                neighbors = self.get_neighbors(row, col)
                if self.grid[row][col] == 1:  # Live cell
                    if neighbors < 2 or neighbors > 3:
                        new_row.append(0)  # Dies
                    else:
                        new_row.append(1)  # Stays alive
                else:  # Dead cell
                    if neighbors == 3:
                        new_row.append(1)  # Becomes alive
                    else:
                        new_row.append(0)  # Stays dead
            new_grid.append(new_row)
        self.grid = new_grid

    def display_grid(self):
        """
        Displays the grid in the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        for row in self.grid:
            print("".join(['#' if cell == 1 else ' ' for cell in row]))

    def run_simulation(self, generations, delay=0.1):
        """
        Runs the Game of Life simulation for a specified number of generations.

        Args:
            generations (int): The number of generations to simulate.
            delay (float): The delay between generations in seconds.
        """
        for _ in range(generations):
            self.display_grid()
            self.update_grid()
            time.sleep(delay)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Conway\'s Game of Life')
    parser.add_argument('--width', type=int, default=60, help='Width of the grid')
    parser.add_argument('--height', type=int, default=30, help='Height of the grid')
    parser.add_argument('--generations', type=int, default=100, help='Number of generations to simulate')
    parser.add_argument('--delay', type=float, default=0.1, help='Delay between generations (seconds)')
    parser.add_argument('--density', type=float, default=0.3, help='Initial density of live cells (0 to 1)')

    args = parser.parse_args()

    game = GameOfLife(args.width, args.height, args.density)
    game.run_simulation(args.generations, args.delay)