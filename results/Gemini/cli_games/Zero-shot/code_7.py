import argparse
import time
import random
import os

class GameOfLife:
    """
    Implementation of Conway's Game of Life.
    """

    def __init__(self, width, height, initial_state=None, seed=None):
        """
        Initializes the Game of Life.

        Args:
            width (int): Width of the grid.
            height (int): Height of the grid.
            initial_state (list, optional): Initial state of the grid. 
                                            Defaults to None (random).
            seed (int, optional): Seed for random number generation. Defaults to None.
        """
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

        if seed is not None:
            random.seed(seed)

        if initial_state is None:
            self.randomize_grid()
        else:
            self.grid = initial_state

    def randomize_grid(self):
        """
        Randomly populates the grid with live cells (1) and dead cells (0).
        """
        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j] = random.randint(0, 1)

    def clear_grid(self):
        """
        Clears the grid, setting all cells to dead.
        """
        for i in range(self.height):
            for j in range(self.width):
                self.grid[i][j] = 0

    def get_cell(self, row, col):
        """
        Gets the state of a cell at the given row and column.
        Handles wrapping around the edges of the grid.

        Args:
            row (int): Row index.
            col (int): Column index.

        Returns:
            int: 1 if the cell is alive, 0 if dead.
        """
        row = row % self.height
        col = col % self.width
        return self.grid[row][col]

    def count_neighbors(self, row, col):
        """
        Counts the number of live neighbors for a given cell.

        Args:
            row (int): Row index of the cell.
            col (int): Column index of the cell.

        Returns:
            int: Number of live neighbors.
        """
        count = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                count += self.get_cell(row + i, col + j)
        return count

    def next_generation(self):
        """
        Calculates the next generation of the Game of Life based on the current state.
        """
        next_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]

        for i in range(self.height):
            for j in range(self.width):
                alive_neighbors = self.count_neighbors(i, j)
                if self.grid[i][j] == 1:  # Alive cell
                    if alive_neighbors < 2 or alive_neighbors > 3:
                        next_grid[i][j] = 0  # Dies
                    else:
                        next_grid[i][j] = 1  # Survives
                else:  # Dead cell
                    if alive_neighbors == 3:
                        next_grid[i][j] = 1  # Becomes alive

        self.grid = next_grid

    def print_grid(self):
        """
        Prints the current state of the grid to the console.
        """
        os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
        for row in self.grid:
            print(''.join(['#' if cell else ' ' for cell in row])) # Use # for live, space for dead

    def run(self, generations, delay=0.1):
        """
        Runs the Game of Life for a specified number of generations.

        Args:
            generations (int): Number of generations to run.
            delay (float): Delay (in seconds) between each generation.
        """
        for _ in range(generations):
            self.print_grid()
            time.sleep(delay)
            self.next_generation()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument('--width', type=int, default=60, help='Width of the grid')
    parser.add_argument('--height', type=int, default=30, help='Height of the grid')
    parser.add_argument('--generations', type=int, default=100, help='Number of generations to run')
    parser.add_argument('--delay', type=float, default=0.1, help='Delay between generations (in seconds)')
    parser.add_argument('--seed', type=int, help='Seed for random number generation')
    parser.add_argument('--initial', type=str, help='Path to initial state file')


    args = parser.parse_args()

    initial_state = None
    if args.initial:
        try:
            with open(args.initial, 'r') as f:
                initial_state = []
                for line in f:
                    row = [1 if char == '#' else 0 for char in line.strip()]
                    initial_state.append(row)

                # Validate initial state dimensions
                if len(initial_state) != args.height or any(len(row) != args.width for row in initial_state):
                    raise ValueError("Initial state dimensions do not match specified width and height.")

        except FileNotFoundError:
            print(f"Error: Initial state file not found: {args.initial}")
            exit(1)
        except ValueError as e:
            print(f"Error: Invalid initial state: {e}")
            exit(1)
        except Exception as e:
            print(f"Error reading initial state file: {e}")
            exit(1)

    game = GameOfLife(args.width, args.height, initial_state=initial_state, seed=args.seed)
    game.run(args.generations, args.delay)