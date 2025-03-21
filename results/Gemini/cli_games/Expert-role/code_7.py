import argparse
import time
import os
import random
from typing import List


class GameOfLife:
    """
    Implements Conway's Game of Life.
    """

    ALIVE = '#'
    DEAD = ' '

    def __init__(self, width: int, height: int, initial_state: List[List[int]] = None,
                 random_fill_probability: float = 0.3):
        """
        Initializes the Game of Life.

        Args:
            width: The width of the grid.
            height: The height of the grid.
            initial_state: An optional initial state for the grid.  If None, the grid is initialized randomly.
            random_fill_probability: The probability that a cell is alive when initialized randomly (default 0.3).
        """
        self.width = width
        self.height = height

        if initial_state:
            self.grid = initial_state
            self.height = len(initial_state)
            self.width = len(initial_state[0]) if initial_state else 0  # Handle empty initial state
        else:
            self.grid = self._create_random_grid(random_fill_probability)

    def _create_random_grid(self, fill_probability: float) -> List[List[int]]:
        """
        Creates a random grid with alive cells based on the fill probability.

        Args:
            fill_probability: The probability that a cell is alive.

        Returns:
            A 2D list representing the grid.
        """
        return [[(1 if random.random() < fill_probability else 0) for _ in range(self.width)] for _ in range(self.height)]

    def _get_neighbors(self, row: int, col: int) -> List[int]:
        """
        Gets the neighbors of a cell. Handles edge cases by wrapping around.

        Args:
            row: The row index of the cell.
            col: The column index of the cell.

        Returns:
            A list of the cell's neighbors (0 or 1).
        """
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:  # Skip the cell itself
                    continue
                neighbor_row = (row + i) % self.height
                neighbor_col = (col + j) % self.width
                neighbors.append(self.grid[neighbor_row][neighbor_col])
        return neighbors

    def _get_next_state(self, row: int, col: int) -> int:
        """
        Determines the next state of a cell based on Conway's rules.

        Args:
            row: The row index of the cell.
            col: The column index of the cell.

        Returns:
            The next state of the cell (0 or 1).
        """
        alive_neighbors = sum(self._get_neighbors(row, col))
        if self.grid[row][col] == 1:  # Alive cell
            if alive_neighbors < 2 or alive_neighbors > 3:
                return 0  # Dies of underpopulation or overpopulation
            else:
                return 1  # Survives
        else:  # Dead cell
            if alive_neighbors == 3:
                return 1  # Becomes alive through reproduction
            else:
                return 0  # Remains dead

    def update(self) -> None:
        """
        Updates the grid to the next generation.
        """
        next_grid = [[self._get_next_state(row, col) for col in range(self.width)] for row in range(self.height)]
        self.grid = next_grid

    def display(self) -> None:
        """
        Displays the current state of the grid in the console.
        """
        for row in self.grid:
            print(''.join([self.ALIVE if cell == 1 else self.DEAD for cell in row]))

    def run(self, generations: int, delay: float = 0.1) -> None:
        """
        Runs the Game of Life for a specified number of generations.

        Args:
            generations: The number of generations to run.
            delay: The delay between generations in seconds.
        """
        try:
            for _ in range(generations):
                os.system('cls' if os.name == 'nt' else 'clear')  # Clear the console
                self.display()
                self.update()
                time.sleep(delay)
        except KeyboardInterrupt:
            print("\nGame interrupted by user.")


def main():
    """
    Main function to parse arguments and run the Game of Life.
    """
    parser = argparse.ArgumentParser(description="Conway's Game of Life")
    parser.add_argument('--width', type=int, default=60, help='Width of the grid')
    parser.add_argument('--height', type=int, default=30, help='Height of the grid')
    parser.add_argument('--generations', type=int, default=100, help='Number of generations to run')
    parser.add_argument('--delay', type=float, default=0.1, help='Delay between generations in seconds')
    parser.add_argument('--fill_probability', type=float, default=0.3, help='Probability of a cell being alive at start')
    parser.add_argument('--initial_state_file', type=str, help='Path to a file containing the initial state')

    args = parser.parse_args()

    initial_state = None
    if args.initial_state_file:
        try:
            with open(args.initial_state_file, 'r') as f:
                initial_state = []
                for line in f:
                    row = [1 if char == '#' else 0 for char in line.strip()]
                    initial_state.append(row)
        except FileNotFoundError:
            print(f"Error: Initial state file not found: {args.initial_state_file}")
            return
        except Exception as e:
            print(f"Error reading initial state file: {e}")
            return


    game = GameOfLife(args.width, args.height, initial_state=initial_state, random_fill_probability=args.fill_probability)
    game.run(args.generations, args.delay)


if __name__ == "__main__":
    main()